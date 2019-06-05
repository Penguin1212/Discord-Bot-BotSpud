import discord
from discord.ext import commands

class Mod (commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# custome help command

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ahelp(self, ctx):
        print("Sent Admin Command Help")
        author = ctx.message.author

        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="Admin Command Help")
        embed.add_field(name='slog', value='This will DM the Log.txt file to any admin as requested',
                        inline=False)
        embed.add_field(name='log', value='Re-call from the Log.txt file within any text channel | log [Line #]',
                        inline=False)

        await author.send(embed=embed)


# Looks at chat logs

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def log(self, ctx, num: int):
        with open('Other/Log.txt') as log:
            for i, line in enumerate(log, 1):
                if i == num:
                    print("looking at logs\n")
                    break
        print(f"Send log line {num} to discord")
        await ctx.send(line)


# Send the log file to server admins

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def slog(self, ctx):
        author = ctx.message.author
        File = discord.File("Other/Log.txt")
        await author.send("Logs for that discord server: ")
        await author.send(file=File)
        print(f"Sent Log.txt to {author}")


# Test cog

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def test2(self, ctx):
        await ctx.send("This test2 worked")


def setup(bot):
    bot.add_cog(Mod(bot))
