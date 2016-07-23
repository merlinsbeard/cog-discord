import discord
from random import randint, choice
from discord.ext import commands

class Mycog:
	""" hehe """

	def __init__(self, bot):
		self.bot = bot
		self.punch_gif = [
			"https://gfycat.com/WaterloggedDiligentDarklingbeetle",
			"https://gfycat.com/OffensiveAnyGemsbuck",
			"https://gfycat.com/ChubbyEarlyCalf",
				]
		self.dungeons = {
		"AC": ["Ascalonian Catacombs Story",
			"Ascalonian Catacombs Path 1",
			"Ascalonian Catacombs Path 2",
			"Ascalonian Catacombs Path 3"
		],
		"CM": [
			"Caudecus's Manor Story",
			"Caudecus's Manor Path 1",
			"Caudecus's Manor Path 2",
			"Caudecus's Manor Path 3"
		],

		"TA": [
			"Twilight Arbor Story",
			"Twilight Arbor Aetherpath",
			"Twilight Arbor Forward",
			"Twilight Arbor Up"
		],
		"SE": [
			"Sorrow's Embrace Story",
			"Sorrow's Embrace Path 1",
			"Sorrow's Embrace Path 2",
			"Sorrow's Embrace Path 3"
		],
		"COF": ["Citadel of Flame Story",
			"Citadel of Flame Path 1",
			"Citadel of Flame Path 2",
			"Citadel of Flame Path 3"
		],
		"HOTW": ["Honor of the Waves Story",
			"Honor of the Waves Path 1",
			"Honor of the Waves Path 2",
			"Honor of the Waves Path 3"
		],
		"COE": ["Crucible of Eternity Story",
			"Crucible of Eternity Path 1",
			"Crucible of Eternity Path 2",
			"Crucible of Eternity Path 3"
		],
		"ARAH": ["Arah Path 1",
			"Arah Path 2",
			"Arah Path 3",
			"Arah Path 4"
		]
	} 



	@commands.command()
	async def mycom(self):
		"""This does stuff!"""

		# code foes here"
		await self.bot.say("Heres you coffee!")

	@commands.command()
	async def coffee(self,  user : discord.Member):
		"""This does stuff!"""

		# code foes here"
		reply = "{} heres your coffee!".format(user.mention)
#		await self.bot.say(reply)
		await self.bot.send_message(user, reply)	

	@commands.command()
	async def punch_old(self, user : discord.Member):
		"""This does stuff!"""

		# code foes here"
		reply = "{} somebody punched you! Punch the person back with !punch @<username>".format(user.mention)
		await self.bot.say(reply)


	@commands.command()
	async def poke(self, user : discord.Member):
		"""This does stuff!"""

		# code foes here"
		reply = "*pokes* {}".format(user.mention)
		await self.bot.say(reply)
	
	@commands.command()
	async def punch(self, user : discord.Member):
		"""This does stuff!"""

		# code foes here"
		gif = choice(self.punch_gif)
		reply = "{} You just got **PUNCHED!** {}".format(user.mention, gif)


		await self.bot.say(reply)

	@commands.command()
	async def shot(self):
		""" No idea what to do here yet """
	
		reply = "**TAKE A SHOT**"
		await self.bot.say(reply)
	@commands.command()
	async def dungeon(self, text='all'):
		""" Randomly chooses a dungeon"""
		dungeons = self.dungeons
		if text in list(dungeons):
			path = choice(dungeons[text])
		else:
			dun = choice(list(dungeons))
			path = choice(dungeons[dun])
		reply = "Go do **{}**".format(path, text)
		await self.bot.say(reply)

def setup(bot):
	bot.add_cog(Mycog(bot))
