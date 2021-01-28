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

def duplication_check(num):
    if len(num) == len(set(num)) and len(num) == 3:
        return True

def eat_bite_check(self_number,enemy_number):
    global eat
    global bite
    eat = 0
    bite = 0
    if self_number[0] == enemy_number[0]:
        eat += 1
    elif self_number[0] in enemy_number:
        bite += 1
    else:
        pass

    if self_number[1] == enemy_number[1]:
        eat += 1
    elif self_number[1] in enemy_number:
        bite += 1
    else:
        pass

    if self_number[2] == enemy_number[2]:
        eat += 1
    elif self_number[2] in enemy_number:
        bite += 1
    else:
        pass

    return (str(eat)+ 'EAT-'+ str(bite)+ 'BITE')


print('まず始めにあなたの番号を決めます')
while True:
    try:
        given_number = input('３桁の数字を入力：')
        if duplication_check(given_number) and str.isdecimal(given_number):
            player_number = list(given_number)
            break;
    except:
        pass
    print('3桁の数値を重複無しで再入力してください')

while True:
    random_number = str(random.randint(1,1000))
    if len(random_number) == 3:
        computer_number = list(random_number)
        if duplication_check(computer_number):
            break;
        else:
            pass
    elif len(random_number) == 2:
        computer_number = list(random_number)
        computer_number.insert(0, "0")
        if duplication_check(computer_number):
            break;
        else:
            pass

eat = 0
bite = 0

print('---------------------------------------------------')
print('ゲームを開始します')

while True:
    while True:
        players_answer = input('コンピューターの３桁の数字を予想してください：')
        if duplication_check(players_answer) and str.isdecimal(players_answer):
            players_expectation = list(players_answer)
            break;
        else:
            print('3桁の数値を重複無しで再入力してください')

    print('結果は['+ eat_bite_check(players_expectation,computer_number)+ ']でした')
    if eat == 3:
        print('あなたの勝ちです')
        break;

    print('コンピューターがあなたの番号を予想します')

    while True:
        random_number = str(random.randint(1,1000))
        if len(random_number) == 3:
            computer_expectation = list(random_number)
            if duplication_check(computer_number):
                break;
            else:
                pass
        elif len(random_number) == 2:
            computer_expectation = list(random_number)
            computer_expectation.insert(0, "0")
            if duplication_check(computer_expectation):
                break;
            else:
                pass

    print('コンピューターは'+ str(computer_expectation)+ 'と予想しました')
    print('結果は['+ eat_bite_check(computer_expectation,player_number)+ ']でした')
    if eat == 3:
        print('あなたの負けです')
        break;
    print('-----------------------------------------------------')

print('ゲームを終了します')
bot.run(token)

