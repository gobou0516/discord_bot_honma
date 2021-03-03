import discord

class Play:
    async def on_message(self, message, music):
        if message.author.voice.channel is not None:
            voice_client = message.guild.voice_client

            if not voice_client:
                vcc = message.author.voice.channel
                await vcc.connect()
            else:
                voice_client.stop()
            
            source = discord.FFmpegPCMAudio("music/" + music)
            voice_client.play(source)