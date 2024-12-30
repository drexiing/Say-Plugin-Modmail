from discord.ext import commands

class Sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sync(self, ctx):
        await bot.tree.sync()
        await ctx.send("Comandos de aplicación sincronziados.")
         
async def setup(bot: commands.Bot):
    await bot.add_cog(Say(bot))