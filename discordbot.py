from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def ping(ctx):
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
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

@client.event
async def on_message(message):
    if "#iおみくじ" in message.content:
        word_list = ["大吉","中吉","小吉"]
        await message.channel.send(random.choice(word_list))

client.run("TOKEN")
