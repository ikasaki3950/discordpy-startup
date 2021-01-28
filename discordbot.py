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
    await ctx.send('おっはー！！')
    
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

#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

CHANNEL_ID = 804500361812770816 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '09:00':
        channel = client.get_channel(804500361812770816)
        await channel.send('おはよー')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
