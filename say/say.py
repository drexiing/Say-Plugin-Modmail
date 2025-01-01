from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def say(self, ctx, channel_or_message=None, *, message=None):
        if not (channel_or_message or message):
            await ctx.send(
                content=(
                    'Debes escribir para que el bot lo envíe. También puedes mencionar un canal.'
                )
            )
            return 

        arg_is_channel = False
        channel = ctx.channel

        if channel_or_message:
            if channel_or_message.startswith('<#') and channel_or_message.endswith('>'):
                if channel_or_message[2:-1].isdigit():
                    channel_id = int(channel_or_message[2:-1])
                    channel = self.bot.get_channel(channel_id)
                    if channel:
                        arg_is_channel = True
                    else:
                        channel = ctx.channel
            elif channel_or_message.isdigit():
                channel = self.bot.get_channel(int(channel_or_message))
                if channel: 
                    arg_is_channel = True
                else:
                    channel = ctx.channel

        if arg_is_channel and message:
            content = message
        elif not arg_is_channel:
            content = f'{channel_or_message} {message}' if message else channel_or_message
        else:
            content = None

        if arg_is_channel and not message:
            await ctx.send('Debes escribir un mensaje o subir un archivo para que el bot lo envíe.')
            return

        await channel.send(content)
         
async def setup(bot: commands.Bot):
    await bot.add_cog(Say(bot))