import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN_HONMA")

client = discord.Client()

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

    if message.content == '!hi':
        await message.channel.send('気づかなかった？')

    # 接続
    if message.content == '!connect':
        if message.author.voice.channel is not None:
            vcc = message.author.voice.channel
            await vcc.connect()

            # 再生
            source = discord.FFmpegPCMAudio("課長と恋の実験室.mp3")
            vcc.play(source)

    # 切断
    if message.content == '!disconnect':
        voice_client = message.guild.voice_client
        await voice_client.disconnect()
    
client.run(TOKEN)