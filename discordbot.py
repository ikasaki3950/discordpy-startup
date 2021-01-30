from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def /ping(ctx):
    await ctx.send('pong')

@bot.command()
async def にゃーん(ctx):
    await ctx.send('にゃーん')
  

@bot.command()
async def おはよー(ctx):
    await ctx.send('おっはー！！！') 

@bot.command()
async def おはよう(ctx):
    await ctx.send('おっはー！！！') 
     
@bot.command()
async def こんちわー(ctx):
    await ctx.send('こんちゃ！！')  
    
@bot.command()
async def こんにちは(ctx):
    await ctx.send('こんちゃ！！')
    
@bot.command()
async def こんばんは(ctx):
    await ctx.send('こんばんわに～')
bot.run(token)
Nzg0OTU3MzQ0NTYzMDY4OTc4.X8w2fg.M6LzmaIc6bDz0E7MUOAr9CB_mag
