import discord
from discord.ext import commands
import os
import random
import emo
import requests
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='!')
dotax = '?svc=popular'

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

            chatUser = ''
            if ctx.author.nick is not None:
                chatUser = ctx.author.nick
            else:
                chatUser = ctx.author.name 

            embed=discord.Embed(color=0x7FFFD4)
            embed.add_field(name=chatUser,value=ctx.content + dotax,inline=True)
            await ctx.channel.send(embed=embed)
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
async def 날씨(ctx):

    word = ctx.message.content[4:]


    url = requests.get(f'https://search.naver.com/search.naver?query={word} 날씨')
    soup = BeautifulSoup(url.text, 'html.parser')

    data1 = soup.find('div', {'class':'weather_box'})
    today = data1.find('div',{'class':'today_area _mainTabContent'})
    tommorow = data1.find('div',{'class':'tomorrow_area _mainTabContent'})

    location = data1.find('span', {'class':'btn_select'}).text

    temp = today.find('span', {'class':'todaytemp'}).text + '℃'
    temp_cast = today.find('p',{'class':'cast_txt'}).text
    temp_sensible = today.find('span',{'class':'sensible'}).text

    ttemp = tommorow.find('span', {'class':'todaytemp'}).text + '℃'
    ttemp_cast = tommorow.find('p',{'class':'cast_txt'}).text

    ##icon
   
    w_icon = emo.weather_icon(temp_cast)
    wt_icon = emo.weather_icon(ttemp_cast)

    ##embed
    embed=discord.Embed(color=0x7FFFD4)
    embed.add_field(name=f"{word} 날씨 - {w_icon}",value=temp+" | "+temp_cast+" ! "+temp_sensible + " ||",inline=True)
    embed.add_field(name=f"내일 날씨 - {wt_icon}",value=ttemp+" | "+ttemp_cast+" ! ",inline=True)

    await ctx.message.delete()
    await ctx.channel.send(embed=embed)

@bot.command()
async def 운세(ctx):

    word = ctx.message.content[4:]

    url = requests.get(f'https://search.naver.com/search.naver?query={word} 운세')
    soup = BeautifulSoup(url.text, 'html.parser')

    data1 = soup.find('div', {'id':'yearFortune'})

    my_ = data1.find('li',{'class':'first_lst'}).text
    my_icon = emo.fortune_icon(my_)
    fortune = data1.find('p',{'class':'text _cs_fortune_text'}).text
    
    embed=discord.Embed(color=0x7FFFD4)
    embed.add_field(name=f"{my_} {my_icon}",value="^"+fortune,inline=True)
    
    await ctx.message.delete()
    await ctx.channel.send(embed=embed)


token = os.environ["token"]
bot.run(token)
