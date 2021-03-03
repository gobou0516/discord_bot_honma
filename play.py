import discord

class Play:
    async def on_message(self, message, music):
        if message.author.voice.channel is not None:
            vcc = message.author.voice.channel
            await vcc.connect()

            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio("music/" + music)
            voice_client.play(source)