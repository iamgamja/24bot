import discord, time, random, os
client = discord.Client()
@client.event
async def on_ready():
	print('시작')
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))
@client.event
async def on_message(message):
	try:
		Eldzld = "🤔"
		Ehdzld = "<:thonking:732864307196592199>"
		zldEhd = "<:gniknoht:733977049743753247>"
		m = message.content
		# print(m)
		def 포함(s):
			return s in m
		def 같다(s):
			return s == m
		def 시작(s):
			return m.startswith(s)
		if message.embeds:
			await message.add_reaction(Ehdzld)
			time.sleep(0.5)
			await message.clear_reaction(Ehdzld)
			return
		if 시작("!청소 ") or 포함("건 중에 ") and 포함("건의 메시지를 삭제했습니다.") or 포함("응답 대기 중입니다."):
			await message.delete()
			# await
			return
		if 포함("띵킹") or 포함("Eldzld") or 포함("띤킹") or 포함("Elszld") or 포함("흠터") or 포함("gmaxj") or 포함(":소ㅑㅜㅏㅑㅜㅎ:"):
			await message.channel.send(Eldzld)
			await message.add_reaction(Eldzld)
		elif 포함(Eldzld) and not 같다(Eldzld):
			await message.channel.send(Eldzld)
			await message.add_reaction(Eldzld)
		elif 같다(Eldzld):
			await message.add_reaction(Eldzld)
		if 포함("똥킹") or 포함("Ehdzld") or 포함("똔킹") or 포함("Ehszld") or 포함("ㅁㄴㅇㄹ") or 포함("asdf") or 포함("??") or 포함(":쇄ㅜㅏㅑㅜㅎ:"):
			await message.channel.send(Ehdzld)
			await message.add_reaction(Ehdzld)
		elif 포함(Ehdzld) and not 같다(Ehdzld):
			await message.channel.send(Ehdzld)
			await message.add_reaction(Ehdzld)
		elif 같다(Ehdzld):
			await message.add_reaction(Ehdzld)
		if 포함("킹똥") or 포함("zldEhd") or 포함("킹똔") or 포함("zldEhs"):
			await message.channel.send(zldEhd)
			await message.add_reaction(zldEhd)
		elif 포함(zldEhd) and not 같다(zldEhd):
			await message.channel.send(zldEhd)
			await message.add_reaction(zldEhd)
		elif 같다(zldEhd):
			await message.add_reaction(zldEhd)
		if 포함("ㅘ!") or 포함("와!"):
			await message.channel.send("샌즈!")
		if 시작(","):
			m = m[1:]
			if 시작("도움") or 시작("ehdna"):
				embed = discord.Embed(title=zldEhd + "도움말" + Ehdzld, color=0x62c1cc)
				embed.add_field(name=",핑", value="으악 핑", inline=True)
				embed.add_field(name=",에블핑", value="으악 핑", inline=True)
				embed.add_field(name=",히어핑", value="으악 핑", inline=True)
				embed.add_field(name=",폭8", value="폭☆8", inline=False)
				embed.add_field(name=",계산 <식>", value="식을 계산합니다.", inline=False)
				embed.add_field(name=",가위바위보 <가위|바위|보>", value="가위바위보를 합니다", inline=False)
				await message.channel.send(embed=embed)
			elif 시작("핑") or 시작("vld"):
				await message.channel.send("으2악 핑")
			elif 시작("계산") or 시작("rPtks"):
				if 시작("계산"):
					i = 3
				else:
					i = 6
				try:
					q = m[i:]
					w = str(eval(q))
					await message.channel.send(w)
				except Exception as e:
					await message.channel.send("오류: " + str(e))
			elif 시작("에블핑") or 시작("dpqmfvld"):
				await message.channel.send("@everyone")
				time.sleep(0.5)
				await message.channel.send("으악 핑")
			elif 시작("히어핑") or 시작("gldjvld"):
				await message.channel.send("@here")
				time.sleep(0.5)
				await message.channel.send("으악 핑")
			elif 시작("폭8") or 시작("vhr8"):
				await message.channel.send("https://cdn.discordapp.com/attachments/740144542753357845/740145588594540604/100.gif")
			elif 시작("가위바위보") or 시작("rkdnlqkdnlqh"):
				if 시작("가위바위보"):
					i = 6
				else:
					i = 13
				w = m[i:]
				if w == "가위":
					e = 0
				elif w == "바위":
					e = 1
				elif w == "보":
					e = 2
				else:
					await message.channel.send("알수 없는!")
					return
				r = random.choice(["가위", "바위", "보"])
				await message.channel.send(r)
				if r == "가위":
					ee = 0
				elif r == "바위":
					ee = 1
				elif r == "보":
					ee = 2
				if e == 0:
					if ee == 0:
						await message.channel.send("비긴!")
					if ee == 1:
						await message.channel.send("이긴!")
					if ee == 2:
						await message.channel.send("진!")
				if e == 1:
					if ee == 0:
						await message.channel.send("진!")
					if ee == 1:
						await message.channel.send("비긴!")
					if ee == 2:
						await message.channel.send("이긴!")
				if e == 2:
					if ee == 0:
						await message.channel.send("이긴!")
					if ee == 1:
						await message.channel.send("진!")
					if ee == 2:
						await message.channel.send("비긴!")
	except Exception as e:
		cn = discord.Object(id='732896130127626261')
		await ch.send("<@526889025894875158>\n오류: " + str(e))
		# print("오류:", e)
			
			
access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
