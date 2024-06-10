import asyncio
import telegram
import os


def send_telegram():
    async def send_audio(audio_path):
        TOKEN = ""
        CHAT_ID = ""

        bot = telegram.Bot(TOKEN)

        async with bot:
            with open(audio_path, 'rb') as audio:
                await bot.send_audio(chat_id=CHAT_ID, audio=audio)

    def send_telegram_audio(audio_path):
        asyncio.run(send_audio(audio_path))

    audio_path = 'PATH_TO_MP3\\GM.mp3'
    send_telegram_audio(audio_path)


if __name__ == "__main__":
    send_telegram()
