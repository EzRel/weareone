import discord
import time
import os
import config
import random
import urllib.request
from config import link, prefix, ownerid
from discord.ext.commands import Bot
from time import sleep
from random import randint

client = Bot(prefix)

@client.event
async def on_ready():
	print("----------------------")
	print("Logged In As")
	print("Username: %s"%client.user.name)
	print("ID: %s"%client.user.id)
	print("----------------------")
	await client.change_presence(game=discord.Game(name='cloudr, help'))
	server = client.get_server('295959610043531264')

@client.event
async def on_message(message):
	msgc = message.content.lower()
	await client.process_commands(message)

"""@client.event
async def on_member_join(member):
	channel = discord.utils.get(member.server.channels, name="logs")
	server = member.server
	fmt = '**+** {0.mention} just entered the **WeAreOne** community!'
	await client.send_message(channel, fmt.format(member))

@client.event
async def on_member_remove(member):
	channel = discord.utils.get(member.server.channels, name="logs")
	server = member.server
	fmt = '**-** {0.mention} left **WeAreOne**. :confused:'
	await client.send_message(channel, fmt.format(member, server))"""

@client.command()
async def ping():
	'''Ping the bot!'''
	pingtime = time.time()
	pingms = await client.say("Pinging...")
	ping = time.time() - pingtime
	await client.edit_message(pingms, ":ping_pong:  Pong! It took `%.01f seconds` to respond!" % ping)
	
@client.command()
async def azu.ga():
	'''Website'''
	await client.say("**http://gazu.ga**")
	
@client.command()
async def animate():
	'''Animate'''
	animms = await client.say("Animating")
	sleep(.1)
	await client.edit_message(animms, "aNimating")
	sleep(.1)
	await client.edit_message(animms, "anImating")
	sleep(.1)
	await client.edit_message(animms, "aniMating")
	sleep(.1)
	await client.edit_message(animms, "animAting")
	sleep(.1)
	await client.edit_message(animms, "animaTing")
	sleep(.1)
	await client.edit_message(animms, "animatIng")
	sleep(.1)
	await client.edit_message(animms, "animatiNg")
	sleep(.1)
	await client.edit_message(animms, "animatinG")

@client.command(pass_context=True)
async def memes(ctx, number = ""):
	'''Free, old memes ;)'''

	mxnb = 35

	if number == "":
		rdnb = randint(1, mxnb)
	else:
		rdnb = int(number)

	messg = random.choice(["Here you have a meme.", "MEMES = LIFE.", "This is my favorite meme!", "This is a nice meme:"])
	await client.say(messg)
	print("Searching for memes...")

	if rdnb == 1:
		x = "https://www.youtube.com/watch?v=eHzIbzO5QdE" #SOMEBODY TOUCHA MY SPAGHET
	elif rdnb == 2:
		x = "https://www.youtube.com/watch?v=v-RE7RUzjf8" #Cereal - life gives you lemons
	elif rdnb == 3:
		x = "https://www.youtube.com/watch?v=EwAajOtfNT8" #Anthony Padilla "Chillin in the Hot Tub" Vine
	elif rdnb == 4:
		x = "https://www.youtube.com/watch?v=g6cIYDvFS-U" #Is that a WEED?!
	elif rdnb == 5:
		x = "https://www.youtube.com/watch?v=eTMb2UkW4xY" #Attack of the Umbrellas - Run Vine
	elif rdnb == 6:
		x = "https://www.youtube.com/watch?v=NfbQTiW7kDY" #FRE SHA VACA DO!
	elif rdnb == 7:
		x = "https://www.youtube.com/watch?v=JhDIILjlhBQ" #Flamingo
	elif rdnb == 8:
		x = "https://www.youtube.com/watch?v=LzVjuQj8Bsg" #Get out of my room im playing mincraft
	elif rdnb == 9:
		x = "https://www.youtube.com/watch?v=du-TY1GUFGk" #It Is Wednesday My Dudes Vine
	elif rdnb == 10:
		x = "https://www.youtube.com/watch?v=UcRtFYAz2Yo" #DANCE TILL YOU'RE DEAD 10 HOURS
	elif rdnb == 11:
		x = "https://www.youtube.com/watch?v=Pz68j1pXrLE" #The Ting Goes Running In The 90s
	elif rdnb == 12:
		x = "https://www.youtube.com/watch?v=X9NruRk3nfk" #Woah-ing in the 90's
	elif rdnb == 13:
		x = "https://www.youtube.com/watch?v=wsO-Td0hqXo" #DEDOTADED WAM
	elif rdnb == 14:
		x = "https://www.youtube.com/watch?v=Vra0Qq0HYsg" #VINE - Scaring cat with car horn (remix 2)
	elif rdnb == 15:
		x = "https://www.youtube.com/watch?v=eFajTI4lOHM" #Super Mario Head Smash
	elif rdnb == 16:
		x = "https://www.youtube.com/watch?v=OxDSXasDF0w" #Vine - It's summer...
	elif rdnb == 17:
		x = "https://www.youtube.com/watch?v=EBy3y3iCy2A" #I Thought You Said Printer Vine
	elif rdnb == 18:
		x = "https://www.youtube.com/watch?v=-g2fiGwGto4" #Ulala...
	elif rdnb == 19:
		x = "https://www.youtube.com/watch?v=uOFk60NRxCo" #Kid rages over CSGO
	elif rdnb == 20:
		x = "https://www.youtube.com/watch?v=kZSfPPJ4Fk8" #Adam Smoke Fail Vine
	elif rdnb == 21:
		x = "https://www.youtube.com/watch?v=2JxaNWdspjY" #ACTUALLY MEGAN
	elif rdnb == 22:
		x = "https://www.youtube.com/watch?v=H5d42w4ZcY4" #When will you learn
	elif rdnb == 23:
		x = "https://www.youtube.com/watch?v=TFlqWou57iQ" #School got me like... (vine)
	elif rdnb == 24:
		x = "No memez for da streamz." #unlucky :P
	elif rdnb == 25:
		x = "https://cdn.discordapp.com/attachments/397456576631537664/401065897420259348/aq79Lnj_460s.png" #Go to Romania they said
	elif rdnb == 26:
		x = "https://www.youtube.com/watch?v=Udas5_Q6mmo" #Kid falling vine
	elif rdnb == 27:
		x = "https://www.youtube.com/watch?v=wzpux4yh7bQ" #Patricia
	elif rdnb == 28:
		x = "https://www.youtube.com/watch?v=XiP6h9cNyHg" #Who is she (sunglasses girl)
	elif rdnb == 29:
		x = "https://www.youtube.com/watch?v=crv99-LT4j8" #Colorado
	elif rdnb == 30:
		x = "https://www.youtube.com/watch?v=Cv0d_KFuuBk" #OOVOO JAVER
	elif rdnb == 31:
		x = "https://www.youtube.com/watch?v=7doCJbg_XBA" #Is this real life?
	elif rdnb == 32:
		x = "https://www.youtube.com/watch?v=AK-AjJzr2Z4" #Oh boy what flavour
	elif rdnb == 33:
		x = "https://www.youtube.com/watch?v=0DNha94yZa0" #Nailed student shot
	elif rdnb == 34:
		x = "https://www.youtube.com/watch?v=Bs1mG3OOAFM" #KAHOOT Trolling
	else:
		x = "https://www.youtube.com/watch?v=CqCCBohjaqA" #Waddup I'm Jared
	await client.say(x)

@client.command(pass_context=True)   
async def dice(ctx, number = ""):
	'''Roll it!'''
	dicemsg = await client.say("Ruleaza...")
	if number == "":
		number = randint(1, 6)
	else:
		number = int(number)
	for x in range(1, 5):
		await client.edit_message(dicemsg, randint(1, 6))
		sleep(0.1 * x)
	await client.edit_message(dicemsg, "A picat %s!"%number)

#Gets a List of Bans From The Server

@client.command(pass_context = True)
async def gbans(ctx):
	'''Gets A List Of Users Who Are No Longer With us'''
	x = await client.get_bans(ctx.message.server)
	x = '\n'.join([y.name for y in x])
	embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
	return await client.say(embed = embed)

#Lists Info About The server

@client.command(pass_context = True)
async def serverinfo(ctx):
	'''Displays Info About The Server!'''

	server = ctx.message.server
	roles = [x.name for x in server.role_hierarchy]
	role_length = len(roles)

	if role_length > 50: #Just in case there are too many roles...
		roles = roles[:50]
		roles.append('>>>> First [50/%s] roles'%len(roles))

	roles = ', '.join(roles);
	channelz = len(server.channels);
	time = str(server.created_at); time = time.split(' '); time= time[0];

	join = discord.Embed(description= '%s '%(str(server)),title = 'Numele serverului', colour = 0xFFFF);
	join.set_thumbnail(url = server.icon_url);
	join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
	join.add_field(name = '__ID__', value = str(server.id))
	join.add_field(name = '__Members__', value = str(server.member_count));
	join.add_field(name = '__Total number of channels__', value = str(channelz));
	join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
	join.set_footer(text ='Created: %s'%time);

	return await client.say(embed = join);

#a command that sets the bots game

@client.command(pass_context=True)
async def setgame(ctx, *, topresent):
	"""Sets my game (Owner)"""
	if ctx.message.author.id == (ownerid):
		message = ctx.message
		await client.delete_message(message)
		await client.whisper("Game was set to **{}**!".format(topresent))
		await client.change_presence(game=discord.Game(name=topresent))

#Clears The Chat

@client.command(pass_context=True)   
async def clear(ctx, number):
	'''Clears The Chat 1-100'''
	user_roles = [r.name.lower() for r in ctx.message.author.roles]

	if "admin" not in user_roles:
		return await client.say("You do not have the role: Admin")
	pass
	mgs = []
	number = int(number)
	async for x in client.logs_from(ctx.message.channel, limit = number):
		mgs.append(x)
	await client.delete_messages(mgs)
	deletedm = await client.say("Am sters ultimele %s mesaje!"%number)
	sleep(3)
	await client.delete_message(deletedm) 

@client.command(pass_context = True)
async def poll(ctx, opt1 = "👍", opt2 = "👎", *, pmsg):
	await client.delete_message(ctx.message)
	await client.say("*Vote!*")
	rmsg = await client.say("%s"%pmsg)
	await client.add_reaction(rmsg, opt1)
	await client.add_reaction(rmsg, opt2)

@client.command(pass_context=True)
async def warn(ctx, user="", reason="", mod="", n="", channel=""):
	"""Warns a Member"""
	user_roles = [r.name.lower() for r in ctx.message.author.roles]

	if "admin" not in user_roles:
		return await client.say("You do not have the role: Admin")
	pass

	if user == "":
		await client.say(":x: No user Mentioned")
	if reason == "":
		await client.say(":x: No reason entered!")
	if mod == "":
		await client.say(":x: No Mod is Selected!")
	if n == "":
		await client.say(":x: No Warn Number was selected")
	if channel == "":
		await client.say(":x: No Channel entered!")
	channel = client.get_channel(channel)
	em = discord.Embed(color=0x42fc07)
	em.add_field(name='Warning', value=("You Have Been Warned -->"))
	em.add_field(name='User', value=(user))
	em.add_field(name='Reason', value=(reason))
	em.add_field(name='Moderator', value=(mod))
	em.set_footer(text="Warnings had : {}".format(n))
	await client.send_message(channel, embed=em)

@client.command(pass_context=True, hidden = True)
async def report(ctx, user: discord.Member, *, reason):
	"""Reports user and sends report to Bot Admin"""
	user_roles = [r.name.lower() for r in ctx.message.author.roles]

	if "admin" not in user_roles:
		return await client.say("You do not have the role: Admin")
	pass

	author = ctx.message.author
	server = ctx.message.server


	joined_at = user.joined_at
	user_joined = joined_at.strftime("%d %b %Y %H:%M")
	joined_on = "{}".format(user_joined)

	args = ''.join(reason)
	adminlist = []
	check = lambda r: r.name in 'YOUR_ROLE_HERE'

	members = server.members
	for i in members:

		role = bool(discord.utils.find(check, i.roles))

		if role is True:
			adminlist.append(i)
		else:
			pass

	colour = discord.Colour.magenta()

	description = "User Reported"
	data = discord.Embed(description=description, colour=colour)
	data.add_field(name="Report reason", value=reason)
	data.add_field(name="Report by", value=author)
	data.add_field(name="Reported user joinned this server on", value=joined_on)
	data.set_footer(text="User ID:{}"
							"".format(user.id))

	name = str(user)
	name = " ~ ".join((name, user.nick)) if user.nick else name

	if user.avatar_url:
		data.set_author(name=name, url=user.avatar_url)
		data.set_thumbnail(url=user.avatar_url)
	else:
		data.set_author(name=name)

	for i in adminlist:
		await client.send_message(i, embed=data)

@client.command(pass_context = True)
async def ban(ctx, member : discord.Member = None, days = " ", reason = " "):
	"""Bans specified member from the server."""
	user_roles = [r.name.lower() for r in ctx.message.author.roles]

	if "admin" not in user_roles:
		return await client.say("You do not have the role: Admin")
	pass

	try:
		if member == None:
			await client.say(ctx.message.author.mention + ", please specify a member to ban.")
			return

		if member.id == ctx.message.author.id:
			await client.say(ctx.message.author.mention + ", you cannot ban yourself.")
			return
		else:
			await client.ban(member, days)
			if reason == ".":
				await client.say(member.mention + " has been banned from the server.")
			else:
				await client.say(member.mention + " has been banned from the server. Reason: " + reason + ".")
			return
	except Forbidden:
		await client.say("You do not have the necessary permissions to ban someone.")
		return
	except HTTPException:
		await client.say("Something went wrong, please try again.")

#Kick a Member From The Server

@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
	'''Kicks A User From The Server'''
	user_roles = [r.name.lower() for r in ctx.message.author.roles]

	if "admin" not in user_roles:
		return await client.say("You do not have the role: Admin")
	pass

	if not member:
		return await client.say(ctx.message.author.mention + "Specify a user to kick!")
	try:
		await client.kick(member)
	except Exception as e:
		if 'Privilege is too low' in str(e):
			return await client.say(":x: Privilege too low!")
 
	embed = discord.Embed(description = "**%s** has been kicked."%member.name, color = 0xF00000)
	embed.set_footer(text="BasicDiscord Bot v1.0")
	await client.say(embed = embed)

#Mutes a Member From The server

@client.command(pass_context = True)
async def mute(ctx, *, member : discord.Member):
	'''Mutes A Member'''
	user_roles = [r.name.lower() for r in ctx.message.author.roles]

	if "admin" not in user_roles:
		return await client.say("You do not have the role: Admin")
	pass

	overwrite = discord.PermissionOverwrite()
	overwrite.send_messages = False
	await client.edit_channel_permissions(ctx.message.channel, member, overwrite)

	await client.say("**%s** is now Muted! Wait For an Unmute.."%member.mention)

#Unmutes a member

@client.command(pass_context = True)
async def unmute(ctx, *, member : discord.Member):
	'''Unmutes The Muted Memeber'''
	user_roles = [r.name.lower() for r in ctx.message.author.roles]

	if "admin" not in user_roles:
		return await client.say("You do not have the role: Admin")
	pass

	overwrite = discord.PermissionOverwrite()
	overwrite.send_messages = True
	await client.edit_channel_permissions(ctx.message.channel, member, overwrite)

	await client.say("**%s** Times up...You are Unmuted!"%member.mention)


if not os.environ.get('TOKEN'):
	print("no token found!")
client.run(os.environ.get('TOKEN').strip('"'))
