import asyncio
import random
import re

from pyrogram.types import InlineKeyboardMarkup, Message
from pyrogram.errors import MessageIdInvalid
from pyrogram.raw.types.messages import BotCallbackAnswer

from ._templ_a import TemplateACheckin


class MICUCheckin(TemplateACheckin):
    name = "MICU Cloud Media"
    bot_username = "micu_user_bot"

    bot_question_pat = r"(-?\d+)\s*([+\-*/])\s*(-?\d+)\s*=\s*\?"  # 匹配 "15 + 19 = ?" 形式的算式

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._answered = set()  # 已作答过的题目, 避免消息被编辑时重复作答

    async def send_checkin(self, retry=False):
        self._answered.clear()  # 每轮重试重新发送 /start, 清空上一轮的作答记录
        return await super().send_checkin(retry=retry)

    def get_keys(self, message: Message):
        """获得消息中所有内联按钮的文本."""
        if isinstance(message.reply_markup, InlineKeyboardMarkup):
            return [k.text for r in message.reply_markup.inline_keyboard for k in r]
        return []

    async def message_handler(self, client, message: Message):
        # 点击签到按钮后 Bot 会返回一道数学题, 需在此拦截并作答. 该消息不能进入 on_text,
        # 否则 "请完成下面这道题后签到" 中的 "完成" 会命中默认成功关键词而误判为签到成功.
        text = message.text or message.caption
        if text:
            norm = text.replace("×", "*").replace("✕", "*").replace("÷", "/").replace("−", "-")
            match = re.search(self.bot_question_pat, norm)
            if match:
                return await self.on_question(message, match)

        await super().message_handler(client, message)

    async def on_question(self, message: Message, match: re.Match):
        """解析数学题, 并点击答案对应的按钮."""
        num1, operator, num2 = int(match.group(1)), match.group(2), int(match.group(3))
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        else:
            if not num2 or num1 % num2:
                self.log.warning(f"签到失败: 无法整除的题目 {num1}{operator}{num2}, 正在重试.")
                return await self.retry()
            result = num1 // num2

        keys = self.get_keys(message)
        if not keys:
            self.log.debug(f"[gray50]题目消息尚未附带答案按钮, 等待更新.[/]")
            return

        signature = (message.id, num1, operator, num2)
        if signature in self._answered:
            return
        self._answered.add(signature)

        def digits(key: str):
            match = re.search(r"-?\d+", key)
            return match.group(0) if match else None

        # 优先精确匹配, 再退化为提取按钮中的数字匹配, 以容忍带装饰的选项
        for extract in (str.strip, digits):
            for k in keys:
                if extract(k) == str(result):
                    self.log.info(f"解析数学题答案: {num1}{operator}{num2}={result}.")
                    await asyncio.sleep(random.uniform(1, 3))
                    try:
                        answer: BotCallbackAnswer = await message.click(k)
                    except TimeoutError:
                        self.log.debug(f"[gray50]点击答案无响应, 一般来说不影响签到.[/]")
                    except MessageIdInvalid:
                        pass
                    else:
                        await self.on_button_answer(answer)
                    return

        self.log.warning(f'签到失败: 答案 {result} 不在选项 ({", ".join(keys)}) 中, 正在重试.')
        return await self.retry()
