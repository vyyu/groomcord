# 8bot v3
# written with <3 by eight
#
# read the readme before starting

import json
import extra
import string
import random
import discord
import asyncio
import requests
import rextester_py as rex
from googletrans import Translator

cl = "en"
rc = False
tr = Translator()

bot = discord.Client()
tok = json.loads(open("bot.json").read())['token']

kanye = "https://api.kanye.rest"
price = "https://api.cryptowat.ch/markets/kraken/{}/price"
btcaddr = json.loads(open("bot.json").read())['btcaddr']

def rn():
	return random.choice([0xdead10, 0xcafe00, 0xb00b13, 0x717713, 0x215600, 0xcaca00, 0xd00d00])

#################################################### TRANSLATOR

@bot.event
async def on_message_edit(_, after): # compatibility with other eightbot forks
	if rc:
		try:
			x = tr.detect(after.content).lang
			if x != 'en':
				print("{} -> en | {}#{} => {}".format(x, \
														after.author.name, \
														after.author.discriminator, \
														tr.translate(text = after.content, \
														dest = 'en', \
														src = x).text))
		except:
			pass

@bot.event
async def on_message(message):
	global cl, rc

	if rc:
		try:
			x = tr.detect(message.content).lang
			if x != 'en':
				print("{} -> en | {}#{} => {}".format(x, \
														message.author.name, \
														message.author.discriminator, \
														tr.translate(text = message.content, \
														dest = 'en', \
														src = x).text))
		except:
			pass

	if message.content.startswith("/ "):
		try:
			if message.author == bot.user:
				await message.edit(content = tr.translate(text = message.content[2::], dest = cl).text)
		except:
			await message.channel.send('Error translating!')

	if message.content.startswith("8t"):
		args = message.content.split(" ")
		if len(args) == 2:
			cl = args[1]

		await message.channel.send("Language changed to: {}".format(cl))

	if message.content == "rc":
		rc = not rc
		await message.channel.send("Receiver {}!".format("on" if rc else "off"))


#################################################### REXTESTER

	if message.content.startswith("rexc"):
		try:
			t = await rex.rexec_aio("c (gcc)", message.content.strip("rexc"))
			await message.channel.send("```{}\n{}\n{}```".format(t.errors, t.warnings, t.results))
		except:
			pass

#################################################### OG COMMANDS

	if message.author != bot.user:
		return

	if message.content == "cl":
		try:
			async for m in message.channel.history(limit = 31337):
				if m.is_system():
					pass

				if m.author == bot.user:
					await m.delete()
		except:
			pass

	if message.content == "cc":
		x = ['BTCUSD', 'ETHUSD', 'LTCUSD']

		reqs = ["$" + str(requests.get(price.format(i)).json()['result']['price']) for i in x]

		embed = discord.Embed(color = rn())

		for i in range(len(reqs)):
			embed.add_field(name = x[i], value = reqs[i], inline = False)

		await message.channel.send(embed = embed)

	if message.content == "ck":
		z = requests.get(kanye).json()['quote']

		embed = discord.Embed(color = rn())
		embed.add_field(name = "Kanye Quote", value = z, inline = False)

		await message.channel.send(embed = embed)

	if message.content == "cn":
		embed = discord.Embed(color = rn())
		embed.add_field(name = "Nuclear Quote", value = random.choice(extra.nukequotes), inline = False)

		await message.channel.send(embed = embed)

	if message.content == "dn":
		embed = discord.Embed(color = rn())
		embed.add_field(name = "Bitcoin address", value = btcaddr, inline = False)

		await message.channel.send(embed = embed)

	if message.content == "hl":
		embed = discord.Embed(title = "eightbot v3", description = "written with <3", color = rn())
		embed.add_field(name = "help screen", value = """
cc - check crypto
cl - clear messages
ck - get kanye quote
cn - get nuclear quote
dn - bitcoin address
hl - help screen
rexc <code> - run C code on rextester
8t <lang> - set language for translation
/ <message> - translate message
		""", inline = True)

		await message.channel.send(embed = embed)

# START
print("[e][i][g][h][t][b][o][t] [v][3]\nwritten with <3\nenter 'hl' for details\nread the readme b4 tinkering")
bot.run(tok, bot = False)
