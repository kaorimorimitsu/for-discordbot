# This example requires the 'message_content' intent.

import discord
import os

from dotenv import load_dotenv

#　単語取得
import random

WORDLIST = ["apple","orange", "love", "hungry", "starve"]



#　時間取得
import datetime


# 天気取得
# -*- coding:utf-8 -*-
import requests
import json





# 画像取得




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
        
        if message.content == '/test':
            await message.channel.send('Hello!')

        if message.content.startswith('/name'):
            name = message.content.split(' ', 1)[1]  # コマンドの後のテキストを取得
            await message.channel.send(f'Hello, {name}!')

        if message.content == '/random-int':
            await message.channel.send(random.randint(0, 100))

        if message.content == 'random-word':
            await message.channel.send(random.choice(WORDLIST))
        
        if message.content == '/time':
            dt_now = datetime.datetime.utcnow()

            DIFF_JST_FROM_UTC = 9
            nowJapan = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)

            DIFF_MYT_FROM_UTC = 8
            nowMalysia = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_MYT_FROM_UTC)

            await message.channel.send(dt_now.strftime('%Y/%m/%d %H:%M:%S'))
            await message.channel.send("Japan " + nowJapan.strftime('%Y/%m/%d %H:%M:%S'))
            await message.channel.send("Malysia " + nowMalysia.strftime('%Y/%m/%d %H:%M:%S'))

        if message.content == '/weather':
            # 気象庁データの取得
            jma_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
            jma_json = requests.get(jma_url).json()

            # 取得したいデータを選ぶ
            jma_date = jma_json[0]["timeSeries"][0]["timeDefines"][0]
            jma_weather = jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][0]
            # 全角スペースの削除
            jma_weather = jma_weather.replace('　', '')

            await message.channel.send(jma_weather)

        if message.content == '/image':
            file = ["パス名","パス名2"]
            file2 = random.choice(file)
            file3 = discord.File(file2, filename=file2)
            await message.channel.send(file=file3)

        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)

