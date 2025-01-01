from discord.ext import commands

class Sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def sync(self, ctx):
        await self.bot.tree.sync()
        await ctx.send("Comandos de aplicación sincronziados.")
         
async def setup(bot: commands.Bot):
    await bot.add_cog(Sync(bot))