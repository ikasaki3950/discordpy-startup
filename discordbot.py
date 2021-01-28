from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def にゃーん(ctx):
    await ctx.send('にゃーん')

    
import random

def generate_num():
   """ランダムな3桁の数字をタプルに入れて生成"""
   while True:
       first_num = random.randint(1, 9)
       second_num = random.randint(0, 9)
       third_num = random.randint(0, 9)
       num = (first_num, second_num, third_num)
       if check_duplication(num) is True:
           return num
       else:
           pass
def check_duplication(num):
   """すべての桁で数字が重複していないか判定"""
   if len(num) == len(set(num)) and len(num) == 3:
       return True
len(num) == len(set(num)) and len(num) == 3
async def numer0n(self, ctx):
    gen_num_tuple = generate_num()

    def check(m):
        return m.author == ctx.author

    est_num = await self.bot.wait_for("message", check=check, timeout=None)
    est_num_list = []
        for num in est_num.content:
            est_num_list.append(int(num))
def check_num(est_num, gen_num):
   """位置が一致のときにEATに加算、数字が一致の時にBYTEに加算"""
   EAT = 0
   BYTE = 0
   i = 0
   while i < 3:
       if est_num[i] == gen_num[i]:
           EAT += 1
       elif est_num[i] in gen_num:
           BYTE += 1
       else:
           pass
       i += 1
   return EAT, BYTE
if est_num[0] == gen_num[0]: #インデックスは0から始まる事に注意
    EAT += 1
elif est_num[0] in gen_num:
    BYTE += 1
else:
    pass
async def numer0n(self, ctx):
    gen_num_tuple = generate_num()

    def check(m):
        return m.author == ctx.author

    est_num = await self.bot.wait_for("message", check=check, timeout=None)
    est_num_list = []
        for num in est_num.content:
            est_num_list.append(int(num))
    eat_byte = check_num(gen_num_tuple, est_num_list)
    await ctx.send(f'{eat_byte[0]}EAT, {eat_byte[1]}BYTE')
async def numer0n(self, ctx):
    gen_num_tuple = generate_num()

    def check(m):
        return m.author == ctx.author

　　 i = 0
    while True:
        est_num = await self.bot.wait_for("message", check=check, timeout=None)
        est_num_list = []
            for num in est_num.content:
                est_num_list.append(int(num))
        eat_byte = check_num(gen_num_tuple, est_num_list)
        i += 1

        if eat_byte[0] == 3:
            await ctx.send('ゲームクリア！')
　　　　　　　 break #クリアしたのでwhileループを抜ける

　　　　　elif i >= 10:
　　　　　    await ctx.send('ゲームオーバー！10回以内に当てることができませんでした！')
            break #ゲームオーバーなのでwhileループを抜ける
　　　　　

        await ctx.send(f'{i}回目: {est_num.content} | {eat_byte[0]}EAT, {eat_byte[1]}BYTE')    
bot.run(token)

