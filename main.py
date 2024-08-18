# This example requires the 'message_content' intent.

import discord
import os

from dotenv import load_dotenv

load_dotenv()  # これにより .env ファイルが読み込まれる



# アクセストークンを設定
TOKEN = os.getenv("TOKEN") 

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == '/neko':
            await message.channel.send('にゃーん')

        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)

