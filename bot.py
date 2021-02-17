import discord
import os
from response import Response
from discord.ext import tasks
from datetime import datetime

TOKEN = os.environ.get("DISCORD_TOKEN_HONMA")

client = discord.Client()

response = Response()

# 60秒に1回ループ
#@tasks.loop(seconds = 60)
#async def loop():
    #now_minute = datetime.now().strftime('%M')
    #if now_minute == '00':
        

# 起動時の動作
@client.event
async def on_ready():
    print('本間課長が出社しました')

# メッセージ受信時の処理
@client.event
async def on_message(message):
    global vcc

    # 送信者がBotだったら無視
    if message.author.bot:
        return
    
    # メンションを送られたらランダムに返信
    if client.user in message.mentions:
        await response.on_message(message)

    # 接続 & 再生
    if message.content == '!jikken':
        if message.author.voice.channel is not None:
            vcc = message.author.voice.channel
            await vcc.connect()

            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio("課長と恋の実験室.mp3")
            voice_client.play(source)
    
    # 再度再生
    if message.content == '!again':
        voice_client = message.guild.voice_client
        source = discord.FFmpegPCMAudio("課長と恋の実験室.mp3")
        voice_client.stop()
        voice_client.play(source)

    # 切断
    if message.content == '!bye':
        voice_client = message.guild.voice_client
        await voice_client.disconnect()

#loop.start()
    
client.run(TOKEN)