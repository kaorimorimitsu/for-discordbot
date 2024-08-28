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
import discord 
import random

# 画像で現在時刻
import discord
import io
import datetime

# "test"の画像検索
import discord
import requests



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

            # Discordクライアントの作成
            intents = discord.Intents.default()
            intents.message_content = True
            client = discord.Client(intents=intents)

            # ランダムな画像URLのリスト
            image_urls = [
                "https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixta.jp%2Ftags%2F%25E9%2581%25A9%25E5%25BD%2593%3Fsearch_type%3D2&psig=AOvVaw07YefohidI8qTFVlIBdRNt&ust=1724803749821000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNiBgJHzk4gDFQAAAAAdAAAAABAE",
                "https://www.google.com/url?sa=i&url=https%3A%2F%2Fnote.com%2Ftwentynine%2Fn%2Fn3cb88944d77b&psig=AOvVaw07YefohidI8qTFVlIBdRNt&ust=1724803749821000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNiBgJHzk4gDFQAAAAAdAAAAABAJ",
                "https://www.google.com/url?sa=i&url=https%3A%2F%2Ftwicomi.com%2Fsearch%2Fmanga%2F%2523%25E3%2583%25AA%25E3%2583%2597%25E3%2581%2597%25E3%2581%259F%25E4%25BA%25BA%25E3%2581%25AB%25E5%25BE%258C%25E6%2582%2594%25E3%2581%2599%25E3%2582%258B%25E3%2581%25BB%25E3%2581%25A9%25E9%2581%25A9%25E5%25BD%2593%25E3%2581%25AA%25E3%2582%25A4%25E3%2583%25A9%25E3%2582%25B9%25E3%2583%2588%25E3%2582%2592%25E6%258F%258F%25E3%2581%258F%2Fpage%2F1&psig=AOvVaw0D88Qkcb89LBy0pTEY2jSR&ust=1724803819953000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKiyj7Lzk4gDFQAAAAAdAAAAABAE",
                "https://www.google.com/url?sa=i&url=https%3A%2F%2Fpngtree.com%2Fso%2Fapple&psig=AOvVaw24MSa8Wv6RE2D9sTF1lu-3&ust=1724806235793000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNjF1rP8k4gDFQAAAAAdAAAAABAJ"
                # さらに画像のURLを追加
            ]
            
                  

        if message.content.startswith('/image'):
            # ランダムな画像URLを選択
            random_image_url = random.choice(IMAGE_URLS)
            # メッセージを送信
            await message.channel.send(random_image_url)



        # 画像で現在時刻

        from PIL import Image, ImageDraw, ImageFont
        import os
        from dotenv import load_dotenv

        if message.content == '/time-image':
            # 現在時刻を取得
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # 画像を作成
            img = Image.new('RGB', (400, 100), color=(255, 255, 255))
            d = ImageDraw.Draw(img)
            font = ImageFont.load_default()

            # 画像に時刻を描画
            d.text((10, 40), f"Current Time:\n{now}", font=font, fill=(0, 0, 0))

            # 画像をバイナリストリームに保存
            with io.BytesIO() as buf:
                img.save(buf, format='PNG')
                buf.seek(0)
                # 画像を Discord に送信
                await message.channel.send(file=discord.File(fp=buf, filename='time_image.png'))


        # "test"の画像検索
        from bs4 import BeautifulSoup
        import os
        from dotenv import load_dotenv      


        def fetch_image_url(query):
            # Google画像検索のURL
            search_url = f"https://www.google.com/search?hl=ja&tbm=isch&q={query}"
    
            # HTTPリクエストを送信
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(search_url, headers=headers)
    
            # レスポンスのHTMLを解析
            soup = BeautifulSoup(response.text, 'html.parser')
    
            # 画像URLを取得
            try:
                image_tag = soup.find('img', {'class': 'rg_i Q4LuWd'})
                image_url = image_tag['src']
                return image_url
            except (AttributeError, TypeError):
                return None

        

            if message.content.startswith('/search'):
                query = message.content[len('/search '):]
                if query:
                    image_url = fetch_image_url(query)
                    if image_url:
                        await message.channel.send(image_url)
                    else:
                        await message.channel.send("画像が見つかりませんでした。")
                else:
                    await message.channel.send("検索クエリが指定されていません。")



        

            print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)

