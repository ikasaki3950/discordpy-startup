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
  

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよー"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = " + message.author.name + "さんおっはー！！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = " + message.author.name + "さんおっはー！！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

    
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
