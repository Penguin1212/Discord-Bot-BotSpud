import discord
from discord.ext import commands

class Mod (commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# this is a test command in a cog
# look at other cogs in this folder for more examples

    @commands.command(pass_context=True)
    async def test(self, ctx):
        print("Yes you just used a cog! now make your own")

# copy above to make a new command or just use the above to make a new command
# cogs are used to organize code inside of the discord bot

def setup(bot):
    bot.add_cog(Mod(bot))
