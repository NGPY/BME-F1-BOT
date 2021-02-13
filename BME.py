import discord
import random #needed for 8 ball
import time 
import ffmpy
with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0]
ball8 = ["It is certain","It is decidedly so.","Without a doubt","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Beetter not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it","My sources say no.","Outlook not so good.","Very doubtful."]
# random number chooses random phrase to say
total = 0                # jsut totals for all the teams so i can += in a for loop to get totals
mertotal = 0
bultotal = 0
mcltotal = 0
ractotal = 0
alptotal = 0
fertotal = 0
tautotal = 0
romtotal = 0
hastotal = 0
wiltotal = 0
mertotal1 = 0
bultotal1 = 0
mcltotal1 = 0
ractotal1 = 0
alptotal1 = 0
fertotal1 = 0
tautotal1 = 0
romtotal1 = 0
hastotal1 = 0
wiltotal1 = 0

standings = [                  #standings drivers only used to make the team totals as well
	["nod1",0,"mer"],
	["niffle",2,"mer"],
	["paradox",10,"bul"],
	["uhlicek",0,"bul"],
	["emil",0,"mcl"],
	["goot",4,"mcl"],
	["eliax",0,"rac"],
	["jmlima44",0,"rac"],
	["majortom",0,"alp"],
	["hintero",25,"alp"],
	["fredrik",0,"fer"],
	["luuk",0,"fer"],
	["temperr",1,"tau"],
	["immigration",0,"tau"],
	["alfie",12,"rom"],
	["ngpy",8,"rom"],
	["maikki",18,"has"],
	["bean",15,"has"],
	["dawid",6,"wil"],
	["mango",0,"wil"],
]
standingssort = sorted(standings,key=lambda l:l[1], reverse=True)     #sorts all drivers by points

driverstands = ""   # needed for += to work in for loop 
for i in range(0,20):
	a = str(standingssort[i][0]) # setting the name of driver in standing sort
	b = str(standingssort[i][1]) # setting the points
	c = str(standingssort[i][2]) # setting the team
	abc = ("\nDriver: "+a+"  Points: "+b+"  Team: "+c+"") # adding all of these into one string
	driverstands += str(abc) # adding it into the final message used in the main events

for i in range(0,20):
	a = standings[i][1]
	b = standings[i][2]
	if b == "mer":
		mertotal += a
	elif b == "bul":
		bultotal += a
	elif b == "mcl":
		mcltotal += a	
	elif b == "rac":
		ractotal += a
	elif b == "alp":
		alptotal += a
	elif b == "fer":
		fertotal += a
	elif b == "tau":
		tautotal += a
	elif b == "rom":
		romtotal += a
	elif b == "has":
		hastotal += a
	elif b == "wil":
		wiltotal += a   # used to get all the teams points by getting the team of a player and getting his score

constructor = [
	["Mercedes",mertotal],     #standings for teams so i can sort them 
	["Red Bull",bultotal],
	["McLaren",mcltotal],
	["Racing Point",ractotal],
	["Alpine",alptotal],
	["Ferrari",fertotal],
	["Alpha Tauri",tautotal],
	["Alfa Romeo",romtotal],
	["Haas",hastotal],
	["Williams",wiltotal],
]

constructorssort = sorted(constructor,key=lambda l:l[1], reverse=True) # sorts the teams in point order
constructorstands = ""   # needed for += in for loop

for i in range(0,10):                 
	a = str(constructorssort[i][0])   # setting the name of in the sorted list
	b = str(constructorssort[i][1])   # setting the points in the sorted list 
	ab = str("\nTeam: "+a+"  Points: "+b)    # adding points and name into string
	constructorstands += ab #addint it to the final message
#-----------------------------------------------------------
standings2 = [
	["leonardo",0,"mer"],
    ["?",0,"mer"],
    ["screpper",0,"bul"],
    ["lumpy",0,"bul"],
    ["bruna",12,"mcl"],
    ["ngpy",6,"mcl"],
    ["luka",0,"rac"],
    ["ghaz",26,"rac"],
    ["wesley",2,"alp"],
    ["websisson",0,"alp"],
    ["water",8,"fer"],
    ["para",1,"fer"],
    ["eddie",18,"tau"],
    ["bunaseara",4,"tau"],
    ["hintero",0,"rom"],
    ["stan",0,"rom"],
    ["pedro",15,"has"],
    ["niffle",0,"has"],
    ["?",0,"wil"],
    ["yann",10,"wil"],
]

standingssort2 = sorted(standings2,key=lambda l:l[1], reverse=True)
driverstands2 = ""   # needed for += to work in for loop 
for i in range(0,20):
	a = str(standingssort2[i][0]) # setting the name of driver in standing sort
	b = str(standingssort2[i][1]) # setting the points
	c = str(standingssort2[i][2]) # setting the team
	abc = ("\nDriver: "+a+"  Points: "+b+"  Team: "+c+"") # adding all of these into one string
	driverstands2 += str(abc) # adding it into the final message used in the main events

for i in range(0,20):
	a = standings2[i][1]
	b = standings2[i][2]
	if b == "mer":
		mertotal1 += a
	elif b == "bul":
		bultotal1 += a
	elif b == "mcl":
		mcltotal1 += a	
	elif b == "rac":
		ractotal1 += a
	elif b == "alp":
		alptotal1 += a
	elif b == "fer":
		fertotal1 += a
	elif b == "tau":
		tautotal1 += a
	elif b == "rom":
		romtotal1 += a
	elif b == "has":
		hastotal1 += a
	elif b == "wil":
		wiltotal1 += a

constructor2 = [
	["Mercedes",mertotal1],     #standings for teams so i can sort them 
	["Red Bull",bultotal1],
	["McLaren",mcltotal1],
	["Racing Point",ractotal1],
	["Alpine",alptotal1],
	["Ferrari",fertotal1],
	["Alpha Tauri",tautotal1],  
	["Alfa Romeo",romtotal1],
	["Haas",hastotal1],
	["Williams",wiltotal1],
]
constructorssort2 = sorted(constructor2,key=lambda l:l[1], reverse=True) # sorts the teams in point order
constructorstands2 = ""

for i in range(0,10):                 
	a = str(constructorssort2[i][0])   # setting the name of in the sorted list
	b = str(constructorssort2[i][1])   # setting the points in the sorted list 
	ab = str("\nTeam: "+a+"  Points: "+b)    # adding points and name into string
	constructorstands2 += ab #addint it to the final message
client = discord.Client() # client 

@client.event
async def on_ready(): # when the bot is on and ready after all the processes before it happen
	print('We have logged in as {0.user}'.format(client))	 # types into cmd we have logged in and bot name
	await client.change_presence(activity=discord.Game(name=".help for commands")) # adds the status which says .help for commands
@client.event
async def on_message(message): # when a message is received
	print(message.author.id,': Message from {0.author}: {0.content}'.format(message))          # prints the message into the console
	if message.author == client.user:
		return            # if the message is the coming from the bot do not do any of the commands
	if message.content.startswith('.8ball'):    # simple 8 ball system
		num = random.randint(0,len(ball8))
		reply = ball8[num]
		await message.channel.send(reply)
	if message.content.startswith('.help'):   #if the message starts with .help messages that channel with the commands
		await message.channel.send('.8ball : 8ball response to anything\n.driverstands1 : shows div 1 driver standings\n.driverstands2 : shows div 2 driver standings\n.constructorstands1 : shows div 1 constructor standings\n.constructorstands2 : shows div 2 constructor standings\n.coin : coinflip\n.racetime : shows at what times races start')
	if message.content.startswith('.driverstands1'): # just sends a message with the sorted driver standings in pretty print
		await message.channel.send(driverstands)
	if message.content.startswith('.constructorstands1'):  # just sends the constructor standings in pretty print
		await message.channel.send(constructorstands)
	if message.content.startswith('.coin'):
		coin = random.randint(0,1)
		if coin == 0:
			await message.channel.send('Heads')
		elif coin == 1:
			await message.channel.send('Tails')
	if message.content.startswith('.join'):
		channel = message.author.voice.channel
		vc = await channel.connect()
		player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/Users/bened/OneDrive/Desktop/cock.mp3"))
		time.sleep(7)
		await vc.disconnect()
	if message.content.startswith('.driverstands2'):
		await message.channel.send(driverstands2)
	if message.content.startswith('.constructorstands2'):
		await message.channel.send(constructorstands2)
	if message.content.startswith('.racetime'):
		await message.channel.send('DIV 1:\nEvery Sunday 4pm **UTC**\nExceptions: NONE\nDIV 2:\nEvery Friday 7pm **UTC**\nExceptions: NONE')
	if message.content.startswith('.picofday'):
		await message.channel.send('https://cdn.discordapp.com/attachments/809005623899324419/809939640382521364/unknown.png')
client.run(token)      # runs the client with my bot key