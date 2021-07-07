import discord

from discord.ext import commands

import os

import random


bot = commands.Bot(command_prefix='!')
dotax = '?svc=popular'

gos = { 1 : '<:11:857452587343020032>', 2 : '<:12:857452649082912768>', 3 : '<:21:857452701150740492>', 4 : '<:22:857452738002288690>'
, 5 : '<:31:857452773692014622>', 6 : '<:32:857452807732199434>', 7 : '<:41:857452844444286996>', 8 : '<:42:857452878233993247>'
, 9 : '<:51:857452914000134155>', 10 : '<:52:857452943960047646>', 11 : '<:61:857452983569743912>', 12 : '<:62:857453024431177759>'
, 13 : '<:71:857453058241069106>', 14 : '<:72:857453092336042004>', 15 : '<:81:857453128366686238>', 16 : '<:82:857453235996327958>'
, 17 : '<:91:857453273392349244>', 18 : '<:92:857453308980756480>', 19 : '<:101:857453337623396352>', 20 : '<:102:857453354639818762>'}

rule1 = { 1 : 1 , 2 : 1 , 3 : 2 , 4 : 2 , 5 : 3 , 6 : 3 , 7 : 4, 8 : 4, 9 : 5, 10 : 5, 11 : 6, 12 : 6 , 13 : 7, 14 : 7 , 15 : 8 ,16 : 8 ,17 : 9 , 18 : 9 , 19 : 10 ,20 : 10}


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot)) #봇이 실행되면 콘솔창에 표시
    await bot.change_presence(status=discord.Status.online,activity=discord.Game('야옹 '))

@bot.event
async def on_message(ctx):

    if ctx.author == bot.user: # 봇 자신이 보내는 메세지는 무시
        return

    if ctx.content.startswith('!'):
        await bot.process_commands(ctx) 

    if ctx.content.startswith('http'):
        url = ctx.content.find('dotax')
        if url >= 0 : 

            await ctx.channel.send(ctx.content + dotax)
            await ctx.delete()

    if '개추' in ctx.content:
        await ctx.add_reaction('👍')
 
    if '몰?루' in ctx.content:
        await ctx.add_reaction('❓')



@bot.command()
async def 하윙(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} 님, 하윙하윙',reference=ctx.message)

@bot.command()
async def 골라(ctx):

    myMsg = ctx.message.content[4:].split(' ',maxsplit=5)
    rd = random.randrange(1,len(myMsg)+1)
    if rd == 1:
        await ctx.channel.send(myMsg[0]+'!!')
    elif rd ==2:
        await ctx.channel.send(myMsg[1]+'!!')
    elif rd ==3:
        await ctx.channel.send(myMsg[2]+'!!')
    elif rd ==4:
        await ctx.channel.send(myMsg[3]+'!!')
    elif rd ==5:
        await ctx.channel.send(myMsg[4]+'!!')
    elif rd ==6:
        await ctx.channel.send(myMsg[5]+'!!')

@bot.command()
async def 섯다(ctx):
    print('섯다')
    global gos
    global rule1
    rd = random.randrange(1,21)
    sd = []
    
    user1 = ''

    while(len(sd) <2):
        rd = random.randrange(1,21)
        if rd in sd :
            print('rd' + str(rd))
        else :
            sd.append(rd)
            print(sd)
    
    user1h = [rule1[sd[0]],rule1[sd[1]]]
    user1c = [sd[0],sd[1]]

    if 5 in user1c and 15 in user1c:
        user1 = '3 8 광땡'
    elif 1 in user1c and 5 in user1c:
        user1 = '1 3 광땡'
    elif 1 in user1c and 15 in user1c:
        user1 = '1 8 광땡'
    elif rule1[sd[0]] == rule1[sd[1]] :
        user1 = f'{rule1[sd[0]]} 땡'
    else : 

        if (rule1[sd[0]]+rule1[sd[1]])%10 == 9 :
            user1 = '갑오'
        elif 4 in user1h and 6 in user1h:
            user1 = '세륙'
        elif 4 in user1h and 10 in user1h:
            user1 = '장사'
        elif 1 in user1h and 10 in user1h:
            user1 = '장삥'
        elif 1 in user1h and 9 in user1h:
            user1 = '구삥'
        elif 1 in user1h and 4 in user1h :
            user1 = '독사'
        elif 1 in user1h and 2 in user1h: 
            user1 = '알리'
        elif (rule1[sd[0]]+rule1[sd[1]])%10 == 0 :
            user1 = '망통'
        else :       
            user1 = f'{(rule1[sd[0]]+rule1[sd[1]])%10} 끗'
            print(rule1[sd[0]] , rule1[sd[1]])
#    await ctx.message.delete()
    await ctx.channel.send(f'{gos[sd[0]]}{gos[sd[1]]}  {user1}',reference=ctx.message)


@bot.command()
async def 섯다2(ctx):
    print('섯다')
    global gos
    global rule1
    rd = random.randrange(1,21)
    sd = []
    
    user1 = ''
    user2 = ''

    while(len(sd) <4):
        rd = random.randrange(1,21)
        if rd in sd :
            print('rd' + str(rd))
        else :
            sd.append(rd)
            print(sd)
    
    user1h = [rule1[sd[0]],rule1[sd[1]]]
    user1c = [sd[0],sd[1]]
    user2h = [rule1[sd[2]],rule1[sd[3]]]
    user2c = [sd[2],sd[3]]

    if 5 in user1c and 15 in user1c:
        user1 = '3 8 광땡'
    elif 1 in user1c and 5 in user1c:
        user1 = '1 3 광땡'
    elif 1 in user1c and 15 in user1c:
        user1 = '1 8 광땡'
    elif rule1[sd[0]] == rule1[sd[1]] :
        user1 = f'{rule1[sd[0]]} 땡'
    else : 
        if (rule1[sd[0]]+rule1[sd[1]])%10 == 0 :
            user1 = '망통'
        elif (rule1[sd[0]]+rule1[sd[1]])%10 == 9 :
            user1 = '갑오'
        elif 4 in user1h and 6 in user1h:
            user1 = '세륙'
        elif 4 in user1h and 10 in user1h:
            user1 = '장사'
        elif 1 in user1h and 10 in user1h:
            user1 = '장삥'
        elif 1 in user1h and 9 in user1h:
            user1 = '구삥'
        elif 1 in user1h and 4 in user1h :
            user1 = '독사'
        elif 1 in user1h and 2 in user1h: 
            user1 = '알리'
        else :       
            user1 = f'{(rule1[sd[0]]+rule1[sd[1]])%10} 끗'
            print(rule1[sd[0]] , rule1[sd[1]])

    if 5 in user2c and 15 in user2c:
        user2 = '3 8 광땡'
    elif 1 in user2c and 5 in user2c:
        user2 = '1 3 광땡'
    elif 1 in user2c and 15 in user2c:
        user2 = '1 8 광땡'
    elif rule1[sd[2]] == rule1[sd[3]] :
        user2 = f'{rule1[sd[2]]} 땡'
    else : 
        if (rule1[sd[2]]+rule1[sd[3]])%10 == 0 :
            user2 = '망통'
        elif (rule1[sd[2]]+rule1[sd[3]])%10 == 9 :
            user2 = '갑오'
        elif 4 in user2h and 6 in user2h:
            user2 = '세륙'
        elif 4 in user2h and 10 in user2h:
            user2 = '장사'
        elif 1 in user2h and 10 in user2h:
            user2 = '장삥'
        elif 1 in user2h and 9 in user2h:
            user2 = '구삥'
        elif 1 in user2h and 4 in user1h :
            user2 = '독사'
        elif 1 in user2h and 2 in user2h: 
            user2 = '알리'
        else :   
            user2 = f'{(rule1[sd[2]]+rule1[sd[3]])%10} 끗'
            print(rule1[sd[2]] , rule1[sd[3]])
#    await ctx.message.delete()
    await ctx.channel.send(f'{gos[sd[0]]}{gos[sd[1]]}  {user1} ||  {user2}  {gos[sd[2]]}{gos[sd[3]]}',reference=ctx.message)

token = os.environ["token"]
bot.run(token)
