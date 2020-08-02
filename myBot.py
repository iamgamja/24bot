import discord, time, random
import os
client = discord.Client()
@client.event
async def on_ready():
	print('시작')
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))

@client.event
async def on_m(m):
	try:
		Eldzld = "🤔"
		Ehdzld = "<:thonking:732864307196592199>"
		zldEhd = "<:gniknoht:733977049743753247>"
		m = message
		mt = m.content
		# print(mt)
		def 포함(s):
			return s in mt
		def 같다(s):
			return s == mt
		def 시작(s):
			return mt.startswith(s)
		if m.embeds:
			await m.add_reaction(Ehdzld)
			time.sleep(0.5)
			await m.clear_reaction(Ehdzld)
		elif 포함("띵킹") or 포함("Eldzld") or 포함("띤킹") or 포함("Elszld") or 포함("흠터") or 포함("gmaxj") or 포함(":소ㅑㅜㅏㅑㅜㅎ:"):
			await m.channel.send(Eldzld)
			await m.add_reaction(Eldzld)
		elif 포함(Eldzld) and not 같다(Eldzld):
			await m.channel.send(Eldzld)
			await m.add_reaction(Eldzld)
		elif 같다(Eldzld):
			await m.add_reaction(Eldzld)
		if 포함("똥킹") or 포함("Ehdzld") or 포함("똔킹") or 포함("Ehszld") or 포함("ㅁㄴㅇㄹ") or 포함("asdf") or 포함("??") or 포함(":쇄ㅜㅏㅑㅜㅎ:"):
			await m.channel.send(Ehdzld)
			await m.add_reaction(Ehdzld)
		elif 포함(Ehdzld) and not 같다(Ehdzld):
			await m.channel.send(Ehdzld)
			await m.add_reaction(Ehdzld)
		elif 같다(Ehdzld):
			await m.add_reaction(Ehdzld)
		if 포함("ㅘ!") or 포함("와!"):
			await m.channel.send("샌즈!")
		if 시작(","):
			mt = mt[1:]
			if 시작("도움") or 시작("ehdna"):
				embed = discord.Embed(title=zldEhd + "기타 도움말" + Ehdzld, color=0x62c1cc)
				embed.add_field(name=",핑", value="으악 핑", inline=True)
				embed.add_field(name=",에블핑", value="으악 핑", inline=True)
				embed.add_field(name=",히어핑", value="으악 핑", inline=True)
				embed.add_field(name=",폭8", value="폭☆8", inline=True)
				embed.add_field(name=",계산 <식>", value="식을 계산합니다.", inline=False)
				embed.add_field(name=",가위바위보 <가위|바위|보>", value="가위바위보를 합니다", inline=False)
				await m.channel.send(embed=embed)
			elif 시작("핑") or 시작("vld"):
				firstTime = time.time()
				msg = await m.channel.send("으악 핑")
				lastTime = time.time()
				subTime = lastTime - firstTime
				await msg.delete()
				await m.channel.send(subTime)
			elif 시작("계산"):
				try:
					q = mt[3:]
					w = str(eval(q))
					await m.channel.send(w)
				except Exception as e:
					await m.channel.send("오류: " + str(e))
			elif 시작("rPtks"):
				try:
					q = mt[6:]
					w = str(eval(q))
					await m.channel.send(w)
				except Exception as e:
					await m.channel.send("오류: " + str(e))
			elif 시작("에블핑") or 시작("dpqmfvld"):
				await m.channel.send("@everyone")
			elif 시작("히어핑") or 시작("gldjvld"):
				await m.channel.send("@here")
			elif 시작("가위바위보"):
				w = mt[6:]
				if w == "가위":
					e = 0
				elif w == "바위":
					e = 1
				elif w == "보":
					e = 2
				else:
					await m.channel.send("알수 없는!")
					return
				r = random.choice(["가위", "바위", "보"])
				await m.channel.send(r)
				if r == "가위":
					ee = 0
				elif r == "바위":
					ee = 1
				elif r == "보":
					ee = 2
				if e == 0:
					if ee == 0:
						await m.channel.send("비긴!")
					if ee == 1:
						await m.channel.send("이긴!")
					if ee == 2:
						await m.channel.send("진!")
				if e == 1:
					if ee == 0:
						await m.channel.send("진!")
					if ee == 1:
						await m.channel.send("비긴!")
					if ee == 2:
						await m.channel.send("이긴!")
				if e == 2:
					if ee == 0:
						await m.channel.send("이긴!")
					if ee == 1:
						await m.channel.send("진!")
					if ee == 2:
						await m.channel.send("비긴!")
			elif 시작("rkdnlqkdnlqh"):
				w = mt[13:]
				if w == "rkdnl":
					e = 0
				elif w == "qkdnl":
					e = 1
				elif w == "qh":
					e = 2
				else:
					await m.channel.send("알수 없는!")
					return
				r = random.choice(["가위", "바위", "보"])
				await m.channel.send(r)
				if r == "가위":
					ee = 0
				elif r == "바위":
					ee = 1
				elif r == "보":
					ee = 2
				if e == 0:
					if ee == 0:
						await m.channel.send("비긴!")
					if ee == 1:
						await m.channel.send("이긴!")
					if ee == 2:
						await m.channel.send("진!")
				if e == 1:
					if ee == 0:
						await m.channel.send("진!")
					if ee == 1:
						await m.channel.send("비긴!")
					if ee == 2:
						await m.channel.send("이긴!")
				if e == 2:
					if ee == 0:
						await m.channel.send("이긴!")
					if ee == 1:
						await m.channel.send("진!")
					if ee == 2:
						await m.channel.send("비긴!")
			elif 시작("폭8") or 시작("vhr8"):
				await m.channel.send("https://cdn.discordapp.com/attachments/732870251351376033/737457954189738014/100.gif")
	except Exception as e:
		if str(e) != "404 Not Found (error code: 10008): Unknown m":
			print("오류:", e)




access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
