import discord
from discord.ext import commands
import pyshorteners

bot = commands.Bot(command_prefix=("#"))


@bot.event
async def on_ready():
    print('----------------------------')
    print(f'{bot.user.name} Olarak Giriş Yapıldı')
    print(f'Discord Versiyonu {discord.__version__}')
    print('----------------------------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"#linkkısalt"))
  
# Pycharm git denemesi
@bot.command()
async def linkkısalt(ctx, url):
    description = str(ctx.guild.description)
    s = pyshorteners.Shortener()

    embed = discord.Embed(title="🔗 │ Link Kısaltma", description="Bot, komut sonrasında belirttiğiniz linki kolay bir şekilde kısaltır.", color=0x14ffd8)
    embed.add_field(name=f"🔗 │ Asıl Link", value=f"{url}", inline=True)
    embed.add_field(name=f"🔗 │ Kısaltılmış Link", value=s.tinyurl.short(f'{url}'), inline=True)

    await ctx.send(embed=embed)      

@linkkısalt.error
async def linkkısalt_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen kısaltmak istedğiniz linki komut sonrasında belirtiniz. ') 

bot.run('TOKEN')       
