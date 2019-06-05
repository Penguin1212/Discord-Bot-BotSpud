import discord
from discord.ext import commands

class Mod (commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# custome help command

    @commands.command(pass_context=True)
    async def vhelp(self, ctx):
        print("Sent Voice Command Help")
        author = ctx.message.author

        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="Voice Command Help")
        embed.add_field(name='join', value='When in a voice channel use this to have the bot join said voice channel',
                        inline=False)
        embed.add_field(name='leave', value='When you want the bot to leave the voice channel '
                                            '(Must be in the channel with the bot for this to work)',
                        inline=False)
        embed.add_field(name='play', value='Used to play audio from a link(Youtube, Spotify, SoundCloud) | play [url]',
                        inline=False)
        embed.add_field(name='queue', value='This is the same as the play command, but only queues the music to be '
                                            'played after the song being played(Must be used after the play command) | '
                                            'queue [url]',
                        inline=False)
        embed.add_field(name='next', value='If audio is queued this will stop the currently playing audio and start '
                                           'the next',
                        inline=False)
        embed.add_field(name='pause', value='This will pause the playing audio',
                        inline=False)
        embed.add_field(name='resume', value='This will resume paused music',
                        inline=False)
        embed.add_field(name='stop', value='This is a full stop. If something is not working correctly use this '
                                           'command as a reset of the system',
                        inline=False)

        await author.send(embed=embed)


def setup(bot):
    bot.add_cog(Mod(bot))
