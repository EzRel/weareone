import discord
import time
import os
import config
import random
from config import link, prefix, ownerid
from discord.ext.commands import Bot
from time import sleep
from random import randint

client = Bot(prefix)

#saved as 17.01.2018-17:34!
levelsdex = {'3943' : 1, '70711' : 100, '292684049116430338' : 1020, '295158983982055424' : 385580, '399949104068952064' : 11290, '239748580464656385' : 19020, '342853951353520128' : 10}

@client.event
async def on_ready():
	print("----------------------")
	print("Logged In As")
	print("Username: %s"%client.user.name)
	print("ID: %s"%client.user.id)
	print("----------------------")
	await client.change_presence(game=discord.Game(name='Foloseste w.help!'))
	server = client.get_server('295959610043531264')

@client.event
async def on_message(message):
	levelvalue = -1
	levelkey = 0
	for key, value in levelsdex.items():
		if int(key) == int(message.author.id):
			levelvalue = int(value)
			levelkey = key
			break

	if levelvalue != -1:
		levelvalue += 10 #randint(1, 10)
		#if message.author.display_name == 'EzRel':
		#	levelvalue += 20
		if levelvalue % 1000 == 0 and levelvalue != 0 and message.author.display_name != 'WAO Official':
			await client.send_message(message.channel, "%s, ai mai castigat 1000 de experienta! Acum ai **LEVEL %s**! BRAVO si **GG**!"%(message.author.mention, int(levelvalue / 100)))
		elif levelvalue % 100 == 0 and levelvalue != 0 and message.author.display_name != 'WAO Official':
			await client.send_message(message.channel, "GG %s, ai avansat la **LEVEL %s**!"%(message.author.mention, int(levelvalue / 100)))
		levelsdex[levelkey] = levelvalue
	else:
		levelsdex.update({message.author.id : 0})

	msgc = message.content.lower()
	await client.process_commands(message)
	user_roles = [r.name.lower() for r in message.author.roles]

	if "helpers" not in user_roles:
		canlink = 0
	else:
		canlink = 1
		
	if canlink == 0:
		if "bots" not in user_roles:
			canlink = 0
		else:
			canlink = 1
		
	if "admin" not in user_roles:
		isadm = 0
	else:
		isadm = 1
		
	if isadm == 1:
		if msgc.find("w.tell ") == 0:
			await client.delete_message(message)
	
	if canlink == 0:
		if msgc.find("discord.gg/") != -1:
			await client.send_message(message.channel, "Nu promova alte servere!")
			await client.delete_message(message)
		elif msgc.find("http://") != -1 or msgc.find("https://") != -1:
			await client.send_message(message.channel, "Nu trimite link-uri!")
			await client.delete_message(message)
		elif message.content.upper() != message.content.upper():
			await client.send_message(message.channel, "\"%s\" ~ Nu spama caps lock!"%message.content.lower())
			await client.delete_message(message)
	if msgc.find("fuck") != -1 or msgc.find("shit") != -1 or msgc.find("pula") != -1 or msgc.find("pizda") != -1 or msgc.find("muie") != -1:
		await client.send_message(message.channel, "Nu injura!")
		await client.delete_message(message)

@client.event
async def on_member_join(member):
	channel = discord.utils.get(member.server.channels, name="logs")
	server = member.server
	fmt = '**+** {0.mention} tocmai a intrat in comunitatea **WeAreOne**!'
	await client.send_message(channel, fmt.format(member))

@client.event
async def on_member_remove(member):
	channel = discord.utils.get(member.server.channels, name="logs")
	server = member.server
	fmt = '**-** {0.mention} a parasit comunitatea. :confused:'
	await client.send_message(channel, fmt.format(member, server))

@client.command()
async def ping():
	'''See if The Bot is Working'''
	pingtime = time.time()
	pingms = await client.say("Pinging...")
	ping = time.time() - pingtime
	await client.edit_message(pingms, ":ping_pong:  Pong! A luat `%.01f secunde` !" % ping)
	
@client.command(pass_context=True)
async def levels(ctx, mode = '1'):
	'''See the levels'''
	if mode == '1':
		await client.say("Esti %s | AS FOLLOWING:"%ctx.message.author.id)
		for key, value in levelsdex.items():
			await client.say("%s => %s"%(key, value))
	else:
		lvlmsg = "{'3943' : 1"
		for key, value in levelsdex.items():
			lvlmsg = "%s, '%s' : %s"%(lvlmsg, key, value)
		lvlmsg = "%s}"%lvlmsg
	await client.say(lvlmsg)
	
@client.command()
async def play():
	'''Music!'''
	await client.say(":tools: Lucram la comanda asta!")

@client.command()
async def online():
	'''See if The Bot is online'''
	await client.say("Sunt online! `w.help`")

@client.command()
async def animate():
	'''Animeaza, maai'''
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

"""@client.command(pass_context=True)
async def guild(ctx, subcom = ""):
	if subcom == "" || subcom == "help":
		ms = await client.say("Foloseste `!guild {join|leave|create}`!")
	elif subcom == "create":
		ms = await client.say("Inca lucram la `!guild create` !")
	else:
		ms = await client.say("Foloseste `!guild {join|leave|create}`!")"""

@client.command(pass_context=True)
async def memes(ctx, number = ""):
	'''Iti da memezurile'''

	mxnb = 35

	if number == "":
		rdnb = randint(1, mxnb)
	else:
		rdnb = int(number)

	await client.say("Ni aici un meme.")
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
		x = "https://www.youtube.com/watch?v=Pz68j1pXrLE" #
	elif rdnb == 12:
		x = "https://www.youtube.com/watch?v=X9NruRk3nfk" #
	elif rdnb == 13:
		x = "https://www.youtube.com/watch?v=wsO-Td0hqXo" #
	elif rdnb == 14:
		x = "https://www.youtube.com/watch?v=Vra0Qq0HYsg" #
	elif rdnb == 15:
		x = "https://www.youtube.com/watch?v=eFajTI4lOHM" #
	elif rdnb == 16:
		x = "https://www.youtube.com/watch?v=OxDSXasDF0w" #
	elif rdnb == 17:
		x = "https://www.youtube.com/watch?v=EBy3y3iCy2A" #
	elif rdnb == 18:
		x = "https://www.youtube.com/watch?v=-g2fiGwGto4" #
	elif rdnb == 19:
		x = "https://www.youtube.com/watch?v=uOFk60NRxCo" #
	elif rdnb == 20:
		x = "https://www.youtube.com/watch?v=kZSfPPJ4Fk8" #
	elif rdnb == 21:
		x = "https://www.youtube.com/watch?v=2JxaNWdspjY" #
	elif rdnb == 22:
		x = "https://www.youtube.com/watch?v=H5d42w4ZcY4" #
	elif rdnb == 23:
		x = "https://www.youtube.com/watch?v=TFlqWou57iQ" #
	elif rdnb == 24:
		x = "No memez for da streamz." #https://cdn.discordapp.com/attachments/397456576631537664/401065897420259348/aq79Lnj_460s.png
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
async def havefun(ctx, number = ""):
	'''Comenzi simple si distractive!'''
	for x in range(1, 100 * int(number)):
		await client.say("SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM")
			#SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM
@client.command(pass_context=True)   
async def dice(ctx, number = ""):
	'''Exact ca un zar normal!'''
	dicemsg = await client.say("Ruleaza...")
	if number == "":
		number = randint(1, 6)
	else:
		number = int(number)
	for x in range(1, 5):
		await client.edit_message(dicemsg, randint(1, 6))
		sleep(0.1 * x)
	await client.edit_message(dicemsg, "A picat %s!"%number)

@client.command(pass_context=True)   
async def tellthenews(ctx, timestosay = "", interval = ""):
	'''Informatii date o data la x secunde :)'''

	timestosay = int(timestosay)
	interval = int(interval)
	messages = ['Urmareste-ne pe paginile tale preferate de social media! Twitter / Instagram: *@waodiscord*', 'Avem si un website! **http://waodiscord.000webhostapp.com** este deschis pentru cosmetice, guild shop si multe altele in curand!', 'Poti sa dai `w.suntnou` daca esti nou sau vrei sa citesti regulile!', 'Ai nevoie de ajutor? Da `w.help`!']

	for x in range(1, timestosay):
		currmesg = random.choice(messages)
		await client.say("**ANUNT >>** %s"%currmesg)
		sleep(interval)

"""@client.command()
async def botinvite():
	'''A Link To Invite This Bot To Your Server!'''
	await client.say("Uite-te in dm's :wink:")
	await client.whisper(link)"""

@client.command()
async def suntnou():
	'''Esti nou? w.suntnou!'''
	await client.say("Salut! Bine ai venit pe WeAreOne. Ti-am trimis pe privat toate informatiile de care ai nevoie!")
	await client.whisper("Bine ai venit in comunitatea WeAreOne! Eu sunt @WAOGuilds#9280 , un bot special facut pentru server.")
	await client.whisper("Regulile serverului se gasesc in INFO-SERVER > #rules !")
	await client.whisper("Avem si un website, http://waodiscord.000webhostapp.com !")
	await client.whisper("Daca ai nevoie de ajutorul meu, striga-ma cu `w.help` (Prefixul este `w.`) !")
	await client.whisper("Distreaza-te!")

#gets a server invite and pms it to the user who requested it  

@client.command(pass_context=True)
async def serverinvite(context):
	"""Pm's A Invite Code (To The Server) To The User"""
	invite = await client.create_invite(context.message.channel, max_uses = 0, max_age = 0)
	await client.send_message(context.message.author,"Link-ul la server este {}! [NE]".format(invite.url))
	await client.say("Uite-te in dm's :wink:")

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
		roles.append('>>>> Primele [50/%s] roluri'%len(roles))

	roles = ', '.join(roles);
	channelz = len(server.channels);
	time = str(server.created_at); time = time.split(' '); time= time[0];

	join = discord.Embed(description= '%s '%(str(server)),title = 'Numele serverului', colour = 0xFFFF);
	join.set_thumbnail(url = server.icon_url);
	join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
	join.add_field(name = '__ID__', value = str(server.id))
	join.add_field(name = '__Nr membrii__', value = str(server.member_count));
	join.add_field(name = '__Channel-uri text/voice__', value = str(channelz));
	join.add_field(name = '__Roluri (%s)__'%str(role_length), value = roles);
	join.set_footer(text ='Creat in: %s'%time);

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

@client.command(pass_context=True)   
async def tell(ctx, type, *, tmsg):
	'''Spune lumii mesajele tale prin mine ;)'''

	user_roles = [r.name.lower() for r in ctx.message.author.roles]

	if "admin" not in user_roles:
		return await client.say("Ca sa spun ceva, trebuie sa ma fac auzit! Cred ca rank-ul de admin ma va ajuta...")
	pass
	tmsg = tmsg.replace("%20", " ");
	if type == 'n':
		await client.say("%s"%tmsg)
	else:
		embed = discord.Embed(title = type.replace("%20", " "), description = tmsg, color = 0xFFFFF)
		await client.send_message(ctx.message.channel, embed = embed)

@client.command(pass_context = True)
async def poll(ctx, opt1 = "👍", opt2 = "👎", *, pmsg):
	await client.delete_message(ctx.message)
	await client.say("*Voteaza!*")
	rmsg = await client.say("%s"%pmsg)
	await client.add_reaction(rmsg, opt1)
	await client.add_reaction(rmsg, opt2)
	print("Un nou w.poll!")

@client.command(pass_context = True)   
async def rankcolor(ctx, colour):
	'''Configureaza culoarea rank-ului tau! (MEMBERS ONLY)'''
	server = ctx.message.server
	roles = server.roles
	members = server.members
	member = None
	for mem in members:
		if mem.id == ctx.message.author.id:
			member = mem
			break
	for role in roles:
		if role.name == "color--%s"%colour:
			await client.add_roles(member, role)
			break

	await client.say("Ai primit **color::%s**!"%colour)

@client.command(pass_context = True)   
async def guild(ctx, option, guildname = "", user: discord.Member = ""):
	'''Configureaza guild-ul in care esti'''
	if option == 'create':
		user_roles = [r.name.lower() for r in ctx.message.author.roles]

		if "guildmaker" not in user_roles:
			return await client.say("Ai nevoie de rolul de **Guild Maker** pentru a putea crea un guild!")
		pass
		await client.say("Ai creat guild-ul %s!"%guildname)
		#await ctx.guild.create_category("----%s----"%guildname)
		await client.create_role(client.get_server('295959610043531264'), name = "%sGUILDw"%guildname, colour = discord.Colour.purple())
		grole = await client.create_role(client.get_server('295959610043531264'), name = "%sGUILD"%guildname, colour = discord.Colour.purple())
		server = ctx.message.server
		roles = server.roles
		members = server.members
		member = None
		for mem in members:
			if mem.id == ctx.message.author.id:
				member = mem
				await client.add_roles(member, grole)
				break
		#await client.create_channel(client.get_server('295959610043531264'), "> %s-GUILD"%guildname, type=discord.ChannelType.category)
		await client.create_channel(client.get_server('295959610043531264'), "%s_voice"%guildname, type=discord.ChannelType.voice)
		gchatchannel = await client.create_channel(client.get_server('295959610043531264'), "%s_chat"%guildname, type=discord.ChannelType.text)  #"%s [%s]"%(discord.User.name, guildname)
		await client.send_message(gchatchannel, "Bine ai venit pe guild-ul %s! Daca este primul tau guild, te invitam sa tragi un ochi si pe la #guild_info si #guild_shop ."%guildname)
	elif option == 'join':
		#ctx.message.author.display_name.find('[') == -1
		if 1 == 1:
			server = ctx.message.server
			roles = server.roles
			members = server.members
			member = None
			for mem in members:
				if mem.id == ctx.message.author.id:
					member = mem
					break
			for role in roles:
				if role.name == "%sGUILDw"%guildname:
					await client.add_roles(member, role)
					break

			channels = server.channels
			gchatchannel = None
			for chn in channels:
				if chn.name == "%s_chat"%guildname.lower():
					gchatchannel = chn
					break
			x = "%s vrea sa intre in guild! Da `w.guild accept %s @%s#----` ca sa intre!"%(ctx.message.author.display_name, guildname, ctx.message.author.name)
			embed = discord.Embed(title = "Membru nou", description = x, color = 0x2ecc71)
			nmemmsg = await client.send_message(gchatchannel, embed = embed)
			#await client.pin_message(nmemmsg)
			await client.say("Ai cerut sa intri in %s!"%guildname)
		else:
			await client.say("Esti deja intr-un guild!")
	elif option == 'accept':
		user_roles = [r.name for r in user.roles]

		if "%sGUILDw"%guildname not in user_roles:
			await client.say("Acest membru nu a cerut sa fie in %s!"%guildname)
		else:
			server = ctx.message.server
			roles = server.roles
			members = server.members
			member = None
			for mem in members:
				if mem.id == user.id:
					member = mem
					break
			for role in roles:
				if role.name == "%sGUILD"%guildname:
					await client.add_roles(member, role)
				if role.name == "%sGUILDw"%guildname:
					await client.remove_roles(member, role)

			channels = server.channels
			gchatchannel = None
			for chn in channels:
				if chn.name == "%s_chat"%guildname.lower():
					gchatchannel = chn
					break
			x = "Bine ai venit in guild, %s!"%user.display_name
			embed = discord.Embed(title = "Membru nou", description = x, color = 0x2ecc71)
			nmemmsg = await client.send_message(gchatchannel, embed = embed)
			#await client.pin_message(nmemmsg)
			await client.say("Ai intrat in guild-ul %s!"%guildname)
	elif option == 'leave':
		server = ctx.message.server
		channels = server.channels
		gchatchannel = None
		for chn in channels:
			if chn.name == "%s_chat"%guildname.lower():
				gchatchannel = chn
				break
		roles = server.roles
		members = server.members
		member = None
		for mem in members:
			if mem.id == ctx.message.author.id:
				member = mem
				break
		for role in roles:
			if role.name == "%sGUILD"%guildname:
				await client.remove_roles(member, role)
				break

		x = "Din pacate, %s a iesit din guild."%ctx.message.author.display_name
		embed = discord.Embed(title = "Membru iesit", description = x, color = 0xFFFFF)
		#await client.send_message(gchatchannel, embed = embed)
		#print(gchatchannel.name)
		await client.say("Ai iesit din guild-ul %s!"%guildname)
	elif option == 'delete':
		user_roles = [r.name.lower() for r in ctx.message.author.roles]

		if "guildmaker" not in user_roles:
			return await client.say("Nu tu ai creat %s!"%guildname)

		
	else:
		await client.say("`w.guild %s` nu este o comanda recunoscuta!"%option)
		await client.say("Incearca `w.guild {create|join|leave}`!")

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
