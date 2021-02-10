import discord
import json
import random

class Response:
    def __init__(self):
        self.tbl = json.load(open("reply.json")) # 読み込み

    async def on_message(self, message):
        reply_message = random.choice(self.tbl)
        await message.channel.send(reply_message)