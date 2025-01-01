import discord
from discord.ext import commands
from urllib.parse import urlparse

class Embed(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def embed(self, ctx, channel: discord.TextChannel = None):
        try:
            colour = commands.ColourConverter
            if channel is None:
                channel = ctx.channel
            menú = await ctx.send("**Menú de creación de embed**\n- Autor del embed")
            def check(message):
                return ctx.message and message.author == ctx.author and message.channel == ctx.channel 
            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            if msg.content != "skip":
                autor = msg.content
                foto = None
                if msg.attachments:
                    parsed_url = urlparse(msg.attachments[0].url)
                    filename = parsed_url.path.split("/")[-1]
                    if filename.endswith(("jpg", "jpeg", "png", "gif", "webp")):
                        foto = msg.attachments[0].url        
                else:
                    pass    
            elif msg.content == "skip":
                autor = None
                foto = None
                pass
            await menú.edit(content="**Menú de creación de embed**\n- ~~Autor del embed~~\n- Título del embed")
            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            if msg.content != "skip":
                titulo = msg.content
            elif msg.content == "skip":
                titulo = None
                pass  
            await menú.edit(content="**Menú de creación de embed**\n- ~~Autor del embed~~\n- ~~Título del embed~~\n- Descripción del embed")
            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            if msg.content != "skip":
                descripción = msg.content
            elif msg.content == "skip":
                descripción = None
                pass
            await menú.edit(content="**Menú de creación de embed**\n- ~~Autor del embed~~\n- ~~Título del embed~~\n- ~~Descripción del embed~~\n- Color del embed")
            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            if msg is not None:
                color = None
                while color is None:
                    try:
                        color = await colour.convert(self, ctx, argument=msg.content)
                    except commands.BadArgument:
                        if msg.content == "skip":
                            color = int("ff921f", 16)
                            pass 
                        else:
                            await ctx.send("Por favor, indica un formato de color válido:\n- `0x<hex>`\n- `#<hex>`\n- `0x#<hex>`\n- `rgb(<número>, <número>, <número>)`")
                            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
                    if color:
                        break
            await menú.edit(content="**Menú de creación de embed**\n- ~~Autor del embed~~\n- ~~Título del embed~~\n- ~~Descripción del embed~~\n- ~~Color del embed~~\n- Imagen del embed")
            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            if msg is not None:
                imagen = None
                while imagen is None:
                    if msg.attachments:
                        parsed_url = urlparse(msg.attachments[0].url)
                        filename = parsed_url.path.split("/")[-1]
                        if filename.endswith(("jpg", "jpeg", "png", "gif", "webp")):
                            imagen = msg.attachments[0].url
                            break
                        else:
                            await ctx.send("Por favor, indica la URL de una imagen o gif válidos.")
                            msg = await self.bot.wait_for("message", check=check, timeout=60.0)         
                    else:
                        if msg.content == "skip":
                            break
                        else:
                            await ctx.send("Por favor, indica la URL de una imagen válida.")
                            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            await menú.edit(content="**Menú de creación de embed**\n- ~~Autor del embed~~\n- ~~Título del embed~~\n- ~~Descripción del embed~~\n- ~~Color del embed~~\n- ~~Imagen del embed~~\n- Thumbnail del embed") 
            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            if msg is not None:
                miniatura = None
                while miniatura is None:
                    if msg.attachments:
                        parsed_url = urlparse(msg.attachments[0].url)
                        filename = parsed_url.path.split("/")[-1]
                        if filename.endswith(("jpg", "jpeg", "png", "gif", "webp")):
                            miniatura = msg.attachments[0].url
                            break
                        else:
                            await ctx.send("Por favor, indica la URL de una imagen o gif válidos.")
                            msg = await self.bot.wait_for("message", check=check, timeout=60.0)         
                    else:
                        if msg.content == "skip":
                            break
                        else:
                            await ctx.send("Por favor, indica la URL de una imagen válida.")
                            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            await menú.edit(content="**Menú de creación de embed**\n- ~~Autor del embed~~\n- ~~Título del embed~~\n- ~~Descripción del embed~~\n- ~~Color del embed~~\n- ~~Imagen del embed~~\n- ~~Thumbnail del embed~~\n- Footer del embed")
            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            if msg.content != "skip":
                pie = msg.content
                icono = None
                if msg.attachments:
                    parsed_url = urlparse(msg.attachments[0].url)
                    filename = parsed_url.path.split("/")[-1]
                    if filename.endswith(("jpg", "jpeg", "png", "gif", "webp")):
                        icono = msg.attachments[0].url        
                else:
                    pass    
            elif msg.content == "skip":
                pie = None
                icono = None
                pass
            await menú.edit(content="**Menú de creación de embed**\n- ~~Autor del embed~~\n- ~~Título del embed~~\n- ~~Descripción del embed~~\n- ~~Color del embed~~\n- ~~Imagen del embed~~\n- ~~Thumbnail del embed~~\n- ~~Footer del embed~~")             
            embed = discord.Embed(
                title=titulo,
                description=descripción,
                colour=color
            )
            if autor:
                embed.set_author(name=autor, icon_url=foto)
            else:
                pass
            embed.set_image(url=imagen)
            embed.set_thumbnail(url=miniatura)
            embed.set_footer(text=pie, icon_url=icono)
            await channel.send(embed=embed)
        except TimeoutError:    
            await menú.edit(content="**Menú de creación de embed expirado**")
                 
    @embed.error
    async def error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Formato inválido de embed, vuelve a intentarlo.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Embed(bot)) 