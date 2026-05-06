from pyrogram.types import Message

from ._templ_a import TemplateACheckin


class DPeakCheckin(TemplateACheckin):
    name = "DPeak"
    bot_username = "emby_dpeak_bot"

    async def message_handler(self, client, message: Message):
        if message.text and "人机验证" in message.text:
            if not await self.gpt_handle_message(message, unexpected=False):
                self.log.info(f"签到失败: 智能解析错误, 正在重试.")
                return await self.retry()
            else:
                return
        await super().message_handler(client, message)
