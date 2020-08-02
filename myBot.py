import discord, time, random
import os
client = discord.Client()
@client.event
async def on_ready():
	print('시작')
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))

@client.event
async def on_message(message):
	await message.channel.send("ㅇㅇ")
	try:
		audfuddj = '''#1
		await message.add_reaction(Ehdzld)
		time.sleep(0.5)
		await message.clear_reaction(Ehdzld)
		#2
		await message.channel.send(Eldzld)
		#3
		await message.add_reaction(Eldzld)
		#4
		await message.channel.send(Ehdzld)
		#5
		await message.add_reaction(Ehdzld)
		#6
		await message.channel.send("샌즈!")
		#7
		embed = discord.Embed(title=zldEhd + "기타 도움말" + Ehdzld, color=0x62c1cc)
		embed.add_field(name=",핑", value="으악 핑", inline=True)
		embed.add_field(name=",에블핑", value="으악 핑", inline=True)
		embed.add_field(name=",히어핑", value="으악 핑", inline=True)
		embed.add_field(name=",폭8", value="폭☆8", inline=True)
		embed.add_field(name=",계산 <식>", value="식을 계산합니다.", inline=False)
		embed.add_field(name=",가위바위보 <가위|바위|보>", value="가위바위보를 합니다", inline=False)
		await message.channel.send(embed=embed)
		#8
		firstTime = time.time()
		msg = await message.channel.send("으악 핑")
		lastTime = time.time()
		subTime = lastTime - firstTime
		await msg.delete()
		await message.channel.send(subTime)
		#9
		if tlwkr("계산"):
		\ti = 3
		else:
		\ti = 6
		try:
		\tq = m[i:]
		\tw = str(eval(q))
		\tawait message.channel.send(w)
		except Exception as e:
		\tawait message.channel.send("오류: " + str(e))
		#10
		await message.channel.send("@everyone")
		#11
		await message.channel.send("@here")
		#12
		if tlwkr("가위바위보"):
		\ti = 6
		else:
		\ti = 13
		w = m[i:]
		if w == "가위":
		\te = 0
		elif w == "바위":
		\te = 1
		elif w == "보":
		\te = 2
		else:
		\tawait message.channel.send("알수 없는!")
		\treturn
		r = random.choice(["가위", "바위", "보"])
		await message.channel.send(r)
		if r == "가위":
		\tee = 0
		elif r == "바위":
		\tee = 1
		elif r == "보":
		\tee = 2
		if e == 0:
		\tif ee == 0:
		\t\tawait message.channel.send("비긴!")
		\tif ee == 1:
		\t\tawait message.channel.send("이긴!")
		\tif ee == 2:
		\t\tawait message.channel.send("진!")
		if e == 1:
		\tif ee == 0:
		\t\tawait message.channel.send("진!")
		\tif ee == 1:
		\t\tawait message.channel.send("비긴!")
		\tif ee == 2:
		\t\tawait message.channel.send("이긴!")
		if e == 2:
		\tif ee == 0:
		\t\tawait message.channel.send("이긴!")
		\tif ee == 1:
		\t\tawait message.channel.send("진!")
		\tif ee == 2:
		\t\tawait message.channel.send("비긴!")
		#13
		await message.channel.send("https://cdn.discordapp.com/attachments/732870251351376033/737457954189738014/100.gif")
		#14
		#15
		#16
		#17
		#18
		#19'''
		Eldzld = "🤔"
		Ehdzld = "<:thonking:732864307196592199>"
		zldEhd = "<:gniknoht:733977049743753247>"
		m = message.content
		# print(m)
		def vhgka(s):
			return s in m
		def rkxek(s):
			return s == m
		def tlwkr(s):
			return m.startswith(s)
		def tlfgod(n):
			start = audfuddj.find("#" + str(n))
			end = lines.find("#" + str(n + 1))
			last = lines[start:end]
			exec(last)
		if message.embeds:
			tlfgod(1)
		elif vhgka("띵킹") or vhgka("Eldzld") or vhgka("띤킹") or vhgka("Elszld") or vhgka("흠터") or vhgka("gmaxj") or vhgka(":소ㅑㅜㅏㅑㅜㅎ:"):
			tlfgod(2)
			tlfgod(3)
		elif vhgka(Eldzld) and not rkxek(Eldzld):
			tlfgod(2)
			tlfgod(3)
		elif rkxek(Eldzld):
			tlfgod(3)
		if vhgka("똥킹") or vhgka("Ehdzld") or vhgka("똔킹") or vhgka("Ehszld") or vhgka("ㅁㄴㅇㄹ") or vhgka("asdf") or vhgka("??") or vhgka(":쇄ㅜㅏㅑㅜㅎ:"):
			tlfgod(4)
			tlfgod(5)
		elif vhgka(Ehdzld) and not rkxek(Ehdzld):
			tlfgod(4)
			tlfgod(5)
		elif rkxek(Ehdzld):
			tlfgod(5)
		if vhgka("ㅘ!") or vhgka("와!"):
			tlfgod(6)
		if tlwkr(","):
			m = m[1:]
			if tlwkr("도움") or tlwkr("ehdna"):
				tlfgod(7)
			elif tlwkr("핑") or tlwkr("vld"):
				tlfgod(8)
			elif tlwkr("계산") or tlwkr("rPtks"):
				tlfgod(9)
			elif tlwkr("에블핑") or tlwkr("dpqmfvld"):
				tlfgod(10)
			elif tlwkr("히어핑") or tlwkr("gldjvld"):
				tlfgod(11)
			elif tlwkr("가위바위보") or tlwkr("rkdnlqkdnlqh"):
				tlfgod(12)
			elif tlwkr("폭8") or tlwkr("vhf8"):
				tlfgod(13)
			elif tlwkr("테스트"):
				await message.channel.send("테스트성공!")
	except Exception as e:
		if str(e) != "404 Not Found (error code: 10008): Unknown Message":
			print("오류:", e)
			await message.channel.send("오류:", e)




access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
