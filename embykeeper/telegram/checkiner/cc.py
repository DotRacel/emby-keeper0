import asyncio
import random

from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid

from . import AnswerBotCheckin


class CCCheckin(AnswerBotCheckin):
    name = "CC公益"
    bot_username = "EmbyCc_bot"
    bot_checkin_cmd = "/start"
    bot_checked_keywords = ["已经签到过了"]
    bot_checkin_caption_pat = "请选择正确验证码"
    max_retries = 1

    async def message_handler(self, client, message: Message):
        if message.caption and "欢迎使用" in message.caption and message.reply_markup:
            keys = [k.text for r in message.reply_markup.inline_keyboard for k in r]
            for k in keys:
                if "签到" in k:
                    await asyncio.sleep(random.uniform(0.5, 1.5))
                    try:
                        await message.click(k)
                    except (TimeoutError, MessageIdInvalid):
                        pass
                    return
            else:
                self.log.warning(f"签到失败: 账户错误.")
                return await self.fail()
        await super().message_handler(client, message)
