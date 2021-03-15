# Created By: Leo Power
# Discord: -{ Power1482 }-#0101
# https://powerthecoder.xyz/

import os
import sys
import time
import random
from random import randrange
import discord
from discord.ext import commands
from discord.ext import tasks
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
from discord.utils import find
from discord.utils import get
import asyncio
import requests
from requests import get
import logging
from datetime import datetime


client = commands.Bot(command_prefix="$")
Token = "TOKEN HERE"
Verison = "1.1"
client.remove_command("help")


# BetzBeyond ID: 210260301696729088
# Powerlt1482 ID: 255876083918831616
# TwilightLogs: 791852159519686666
# Betz Logs: THIS
# General: 529838468063559687

#betzbeyond_console_log = client.get_channel(THIS)

# Bot Events #
@client.event
async def on_ready():
	print()
	print("-"*70)
	print("Bot Online")
	print(f"Logged In As: {client.user.name}")
	print(f"ID: {client.user.id}")
	print(f"Bot Version: 1.0")
	print(f"Discord Version {discord.__version__}")
	print("-"*70)
	print()
	print()
	await client.change_presence(status=discord.Status.online, activity=discord.Game("mixer.com/BetzBeyond"))
	#await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Testing'))

StartTime = datetime.now()

@client.event
async def on_guild_join(guild):										    							 										   
	print(f"Bot Joined {guild} ")
	twilight_console_log = client.get_channel(791852159519686666)
	general = client.get_channel(529838468063559687)
	staff = client.get_channel(664523965871685654)
	await twilight_console_log.send(f"Bot Joined **{guild}**")
	msg = ">>> Thankyou for adding me. My prefix is `$`"
	embed=discord.Embed(title="My prefix is `$", description="here are all of the commands available", color=0xfea730)
	embed.set_author(name="Thankyou For Adding Me")
	embed.add_field(name="I am a bot to assist Betz's Server", value="$about", inline=False)
	embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
	await general.send(embed=embed)
	await staff.send(embed=embed)


@client.event
async def on_guild_remove(guild):									    								   
	print(f"The Bot Has Been Removed From {guild}")
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**BetzBeyond Bot** Has been removed from **{guild}**")

@client.event
async def on_member_join(member):
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{member}** joined **BetzBeyond**")
	print(f"**{member}** joined **BetzBeyond**")
	Viewer = discord.utils.get(member.guild.roles, id=664757537488502804)
	await Member.add_roles(member, Viewer)

@client.event
async def on_member_remove(member):
	print(f"{member} left BetzBeyond")
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{member}** has left a server")

@client.event
async def on_message(message):
	if 'nigga' in message.content.lower():
		print(" PowerBot found bad word")
		await message.channel.purge(limit=1)
		powerbot_console_log = client.get_channel(791852159519686666)
		author = message.author
		await powerbot_console_log.send(f"PowerBot found a bad word from **{author}**")
	if 'rape' in message.content.lower():
		print(" PowerBot found bad word")
		await message.channel.purge(limit=1)
		powerbot_console_log = client.get_channel(791852159519686666)
		author = message.author
		await powerbot_console_log.send(f"PowerBot found a bad word from **{author}**")
	if 'nigger' in message.content.lower():
		print(" PowerBot found bad word")
		await message.channel.purge(limit=1)
		powerbot_console_log = client.get_channel(791852159519686666)
		author = message.author
		await powerbot_console_log.send(f"PowerBot found a bad word from **{author}**")
	if 'niger' in message.content.lower():
		print(" PowerBot found bad word")
		await message.channel.purge(limit=1)
		powerbot_console_log = client.get_channel(791852159519686666)
		author = message.author
		await powerbot_console_log.send(f"PowerBot found a bad word from **{author}**")
	if 'n1gg3r' in message.content.lower():
		print(" PowerBot found bad word")
		await message.channel.purge(limit=1)
		powerbot_console_log = client.get_channel(791852159519686666)
		author = message.author
		await powerbot_console_log.send(f"PowerBot found a bad word from **{author}**")
	if 'nigg3r' in message.content.lower():
		print(" PowerBot found bad word")
		await message.channel.purge(limit=1)
		powerbot_console_log = client.get_channel(791852159519686666)
		author = message.author
		await powerbot_console_log.send(f"PowerBot found a bad word from **{author}**")
	if 'n1gger' in message.content.lower():
		print(" PowerBot found bad word")
		await message.channel.purge(limit=1)
		powerbot_console_log = client.get_channel(791852159519686666)
		author = message.author
		await powerbot_console_log.send(f"PowerBot found a bad word from **{author}**")
	await client.process_commands(message)

#@client.event
#async def betz_advertisement():
#	await client.wait_until_ready()
#	betz_ad = client.get_channel(529838468063559687)
#	while not client.is_closed():
#		await asyncio.sleep(86400) #86400 = 24 hours
#		await betz_ad.send("Come join **Betz Beyond** on Mixer https://mixer.com/BetzBeyond and **Minecraft Server** IP: **45.35.89.195:25582**")
#		powerbot_console_log = client.get_channel(791852159519686666)
#		await powerbot_console_log.send("Advertised Server For **Betz Beyond**")



# Client Commands #
@client.command()
async def help(ctx):
	author = ctx.message.author.id
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{author}** did the **Help** Command")
	print(f"**{author}** did the **Help** Command")
	embed=discord.Embed(title="HELP", description="Help Menu For BetzBeyond", color=0x00ffff)
	embed.add_field(name="$about", value="About The Bot", inline=False)
	embed.add_field(name="$ping", value="Check Ping Status", inline=False)
	embed.add_field(name="$status", value="Check Bot Server Status", inline=False)
	embed.add_field(name="$stream", value="Get the BetzBeyond Stream Link", inline=False)
	embed.add_field(name="$ban", value="Ban Members", inline=False)
	embed.add_field(name="$kick", value="Kick Members", inline=False)
	embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
	await ctx.send(embed=embed)
	
@client.command()
async def ping(ctx):
	author = ctx.message.author.name
	print(f"{author} entered ping command")
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{author}** entered **Ping** Command")
	embed=discord.Embed(title="PING", description=f"Testing Network Latency For **{author}**", color=0xfea730)
	embed.add_field(name=f"Your Ping Is", value=f"**{round(client.latency * 1000)}**", inline=False)
	embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
	await ctx.send(embed=embed)

@client.command()
async def about(ctx):
	author = ctx.message.author.name
	print(f"{author} Entered About Command")
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{author}** Entered **About** Command")
	embed=discord.Embed(title="Created By: -{ Power1482 }-#0101 for BetzBeyond", description="Version: **1.0**", color=0xfea730)
	embed.add_field(name="Website: ", value="https://powerthecoder.xyz", inline=False)
	embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
	await ctx.send(embed=embed)

@client.command()
async def status(ctx):
	author = ctx.message.author.name
	print(f"Status command ran by {author}")
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{author}** ran the **status** command")
	amm_server = 0
	for guild in client.guilds:
		amm_server += 1
	T2 = datetime.now()
	time_total = T2 - StartTime
	embed=discord.Embed(title="Server Status: **online**", color=0xfea730)
	embed.set_author(name="Server Status")
	embed.add_field(name="Ammount Of Servers In ", value=amm_server, inline=False)
	embed.add_field(name="Server Version ", value="0.0", inline=False)
	embed.add_field(name="Uptime", value=time_total, inline=False)
	embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
	await ctx.send(embed=embed)

@client.command()
async def stream(ctx):
	author = ctx.message.author.name
	print(f"{author} ran the stream command")
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{author}** ran the **Stream** command")
	embed=discord.Embed(title="Stream", url="https://mixer.com/BetzBeyond", description="**Mixer Stream Link**", color=0x00ffff)
	embed.set_author(name="Find BetzBeyond On Mixer")
	embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
	await ctx.send(embed=embed)



# ADMIN COMMANDS #
@client.command(pass_context=True)
@has_permissions(ban_members=True)
async def ban(ctx, user_name: discord.Member, *, reason=None):
	author = ctx.message.author.name				
	print(f'The Ban Command Ran by {author}')
	embed=discord.Embed(title="BANNED", discription=f"**{user_name}** got **banned** as they have done something wrong", color=0xff0000)
	embed.add_field(name="Member", value=f"**{user_name}** got **Banned**")
	embed.add_field(name="Opperator", value=f"{author}")
	embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
	await ctx.send(embed=embed)
	await user_name.ban(reason=reason)
	print(f'{user_name} got Banned')
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{user_name}** got **banned**")
@ban.error
async def ban_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed=discord.Embed(title="You are not an Admin", description="Please Contact Administrators If you think this is incorrect", color=0xff0000)
		embed.set_author(name="ERROR Command")
		embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
		await ctx.send(embed=embed)
	else:
		await ctx.send(">>> command is `$ban <client>` Replace `client` with the user you want to ban  ")

@client.command(pass_context=True) 
@has_permissions(kick_members=True)
async def kick(ctx, *, user_name: discord.Member, reason=None): 	
	author = ctx.message.author.name	
	print(f'The Kick Command Ran by {author}')
	embed=discord.Embed(title="KICKED", discription=f"**{user_name}** got **Kicked** as they have done something wrong", color=0xff0000)
	embed.add_field(name="Member", value=f"**{user_name}** got **Kicked**")
	embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
	await ctx.send(embed=embed)
	await user_name.kick()
	asyncio.sleep(2)
	print(f"{user_name} got Kicked")
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{user_name}** got **kicked**")
@kick.error
async def kick_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed=discord.Embed(title="You are not an Admin", description="Please Contact Administrators If you think this is incorrect", color=0xff0000)
		embed.set_author(name="ERROR Command")
		embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
		await ctx.send(embed=embed)
	else:
		await ctx.send(">>> command is `$kick <client>` Replace `client` with the user you want to kick ")

@client.command(pass_context=True)
async def say(ctx, *, args):
	if (ctx.author.id == 255876083918831616) or (ctx.author.id == 210260301696729088):
		await asyncio.sleep(0.5)
		await ctx.channel.purge(limit=1)
		await asyncio.sleep(0.5)
		embed=discord.Embed(title=args, description="\u200b", color=0xfea730)
		embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
		await ctx.send(embed=embed)
		twilight_console_log = client.get_channel(791852159519686666)
		author = ctx.message.author.name
		await twilight_console_log.send(f"**{author}** ran the **Say** command")
	else:
		embed=discord.Embed(title="**-{ Power1482 }-#0101** and **Betz Beyond#2225** are my owner", color=0xff0000)
		embed.set_author(name="You Are Not My Owner")
		embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101 \nhttps://powerthecoder.xyz")
		await ctx.send(embed=embed)
		print(f"{author} tried to use Say command and Failed")

@client.command(pass_context=True)
async def mod(ctx, user_name: discord.Member):
	author = ctx.message.author.id
	mod_role = discord.utils.get(Member.guild.roles, id=0)
	await user_name.add_roles(user_name, mod_role)
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{author}** added **Moderator** to **{user_name}**")
	print(f"**{author}** added **Moderator** to **{user_name}**")

@client.command(pass_context=True)
async def admin(ctx, user_name: discord.Member):
	author = ctx.message.author.id
	mod_role = discord.utils.get(Member.guild.roles, id=0)
	await user_name.add_roles(user_name, mod_role)
	twilight_console_log = client.get_channel(791852159519686666)
	await twilight_console_log.send(f"**{author}** added **Admin** to **{user_name}**")
	print(f"**{author}** added **Admin** to **{user_name}**")

@client.command(pass_context=True)
async def mode(ctx, arg1):
	author = ctx.message.author.id
	if(ctx.author.id == 255876083918831616):
		if(arg1 == "testing".lower()) or (arg1 == "test".lower()) or (arg1 == "dev".lower()):
			await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Testing'))
		else:
			await client.change_presence(status=discord.Status.online, activity=discord.Game("mixer.com/BetzBeyond"))
	else:
		embed=discord.Embed(title="-{ Power1482 }-#0101 is my owner", color=0xff0000)
		embed.set_author(name="You Are Not My Owner")
		embed.set_footer(text="Bot Created By: -{ Power1482 }-#0101")
		await ctx.send(embed=embed)
		print(f"{author} tried to update my Presence and FAILED")
		twilight_console_log = client.get_channel(791852159519686666)
		await twilight_console_log.send(f"**{author}** Tried To Change Status @everyone")



#client.loop.create_task(betz_advertisement())
client.run(Token)
