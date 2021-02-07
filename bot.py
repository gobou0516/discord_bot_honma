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
    # 送信者がBotだったら無視
    if message.author.bot:
        return
    
    if message.content == '!hi':
        await message.channel.send('課長と恋の実験室')

client.run(TOKEN)