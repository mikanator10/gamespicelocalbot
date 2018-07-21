# GSbot by gamespice

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime
import random
import asyncio

bot = commands.Bot(command_prefix='GS')

@bot.event

async def on_ready():
    now = datetime.now()
    print('%s Bot: running' % now)
    print('%s Bot: name = %s' % (now, bot.user.name))
    print('%s Bot: id = %s\n' % (now, bot.user.id))

@bot.command(pass_context=True)
async def hello(ctx):
    now = datetime.now()
    await bot.say("Hello, @" + str(ctx.message.author))
    print('%s %s: GShello' % (now, str(ctx.message.author)))

@bot.event
async def on_member_join(member):
    now = datetime.now()
    channel = member.server.get_channel('469143217670193152')
    await bot.send_message(channel, 'Welcome, ' + str(member))
    role = discord.utils.get(member.server.roles, name='Fan')
    await bot.add_roles(member, role)
    print('%s Bot: Welcome: %s' % (now, str(member)))
    
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    now = datetime.now()
    embed = discord.Embed(title="{}'s info".format(user.name), description="User info", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    print('%s %s: GSuserinfo %s' % (now, str(ctx.message.author), user.name))
    
@bot.command(pass_context=True)
async def serverinfo(ctx):
    now = datetime.now()
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="http://www.gamespice.net/")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    print('%s %s: GSserverinfo' % (now, str(ctx.message.author)))

@bot.command(pass_context=True)
async def website(ctx):
    now = datetime.now()
    await bot.say('http://www.gamespice.net/')
    print('%s %s: GSwebsite' % (now, str(ctx.message.author)))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    now = datetime.now()
    if(ctx.message.author.id == '302400842810523649'):
        await bot.say("{} Got kicked :boot:".format(user.name))
        await bot.kick(user)
        print('%s %s: GSkick %s' % (now, str(ctx.message.author), user.name))
    else:
        now = datetime.now()
        await bot.say('You do not have permission to use that command')
        print('%s %s: GSkick, does not have permission' % (now, str(ctx.message.author)))

@bot.command(pass_context=True)
async def truth(ctx):
    now = datetime.now()
    await bot.say(random.choice(['Absolutly!', ':thumbdown::skin-tone-1:', ':thumbsup::skin-tone-1:', 'No, what are you talking about']))
    print('%s %s: GStruth' % (now, str(ctx.message.author)))
        
@bot.command(pass_context=True)
async def clear(ctx, message, amout=100):
    if(ctx.message.author.id == '302400842810523649'):
        now = datetime.now()
        channel = ctx.message.channel
        messages = []
        async for message in bot.logs_from(channel, limit=int(amout+1)):
            messages.append(message)
        await bot.delete_messages(messages)
        print('%s %s: GSclear' % (now, str(ctx.message.author)))
    else:
        now = datetime.now()
        await bot.say('You do not have permission to use that command')
        print('%s %s: GSclear, does not have permission' % (now, str(ctx.message.author)))

@bot.command(pass_context=True)
async def giverole(ctx, user: discord.Member, arg):
    now = datetime.now()
    if(ctx.message.author.id == '302400842810523649'):
        role = discord.utils.get(user.server.roles, name=arg)
        await bot.add_roles(user, role)
        await bot.say('given %s the role %s' % (user, arg))
        print('%s %s: GSgiverole %s %s' % (now, str(ctx.message.author), user, arg))
    else:
        print('%s %s: GSgiverole, does not have permission' % (now, str(ctx.message.author)))
        await bot.say('You do not have permission to use this command.')   

bot.run('NDY5MTE5MDU3Njk0NTU2MTcw.DjDI0Q.WzyXdH_DLZqT61D3sG7ymIKUhiM')
