import discord, time, random, os
client = discord.Client()

버전 = 10
띵킹 = "🤔"
똥킹 = "<:thonking:732864307196592199>"
킹똥 = "<:gniknoht:733977049743753247>"
엑스 = "❌"
		
@client.event
async def on_ready():
	print('시작')
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))

@client.event
async def on_message(message):
	try:
		global 버전
		global 띵킹
		global 똥킹
		global 킹똥
		global 엑스
		m = message.content
		# print(m)
		def 포함(s, b=None):
			if b == None:
				return s in m
			else:
				return s in b
		def 같다(s, b=None):
			if b == None:
				return s == m
			else:
				return s == b
		def 시작(s, b=None):
			if b == None:
				return m.startswith(s)
			else:
				return b.startswith(s)
		if message.embeds:
			await message.add_reaction(똥킹)
			time.sleep(0.5)
			await message.clear_reaction(똥킹)
			return
		if 시작("!청소 ") or 포함("건 중에 ") and 포함("건의 메시지를 삭제했습니다.") or 포함("응답 대기 중입니다.") or 포함(", 메시지 개수는 `2 ~ 99`로 입력하세요."):
			await message.add_reaction(엑스)
			time.sleep(0.5)
			await message.delete()
			return
		if 포함("띵킹") or 포함("Eldzld") or 포함("띤킹") or 포함("Elszld") or 포함("흠터") or 포함("gmaxj") or 포함(":소ㅑㅜㅏㅑㅜㅎ:"):
			await message.channel.send(띵킹)
			await message.add_reaction(띵킹)
		elif 포함(띵킹) and not 같다(띵킹):
			await message.channel.send(띵킹)
			await message.add_reaction(띵킹)
		elif 같다(띵킹):
			await message.add_reaction(띵킹)
		if 포함("똥킹") or 포함("Ehdzld") or 포함("똔킹") or 포함("Ehszld") or 포함("ㅁㄴㅇㄹ") or 포함("asdf") or 포함("??") or 포함(":쇄ㅜㅏㅑㅜㅎ:"):
			await message.channel.send(똥킹)
			await message.add_reaction(똥킹)
		elif 포함(똥킹) and not 같다(똥킹):
			await message.channel.send(똥킹)
			await message.add_reaction(똥킹)
		elif 같다(똥킹):
			await message.add_reaction(똥킹)
		if 포함("킹똥") or 포함("zldEhd") or 포함("킹똔") or 포함("zldEhs"):
			await message.channel.send(킹똥)
			await message.add_reaction(킹똥)
		elif 포함(킹똥) and not 같다(킹똥):
			await message.channel.send(킹똥)
			await message.add_reaction(킹똥)
		elif 같다(킹똥):
			await message.add_reaction(킹똥)
		if 포함("ㅘ!") or 포함("와!"):
			await message.channel.send("샌즈!")
		if 시작(","):
			m = m[1:]
			if 시작("도움") or 시작("ehdna"):
				embed = discord.Embed(title=킹똥 + "도움말" + 똥킹, color=0x62c1cc)
				embed.add_field(name=",핑", value="으악 핑", inline=True)
				embed.add_field(name=",에블핑", value="으악 핑", inline=True)
				embed.add_field(name=",히어핑", value="으악 핑", inline=True)
				embed.add_field(name=",폭8", value="폭☆8", inline=False)
				embed.add_field(name=",계산 <식>", value="식을 계산합니다.", inline=False)
				embed.add_field(name=",가위바위보 <가위|바위|보>", value="가위바위보를 합니다.", inline=False)
				embed.add_field(name=",버전", value="버전을 확인합니다.", inline=False)
				await message.channel.send(embed=embed)
			elif 시작("핑") or 시작("vld"):
				await message.channel.send("으악 핑")
			elif 시작("에블핑") or 시작("dpqmfvld"):
				await message.channel.send("@everyone")
				time.sleep(0.5)
				await message.channel.send("으악 핑")
			elif 시작("히어핑") or 시작("gldjvld"):
				await message.channel.send("@here")
				time.sleep(0.5)
				await message.channel.send("으악 핑")
			elif 시작("계산") or 시작("rPtks"):
				if 시작("계산"):
					i = 3
				else:
					i = 6
				try:
					q = m[i:]
					while True:
						if 포함('^', q):
							q = q.replace('^', "**")
						elif 포함('√(', q):
							inde = q.find('√(')
							q = q.replace(q[q.find(')',inde)],")**0.5")
						else:
							break
					w = str(eval(q))
					await message.channel.send(w)
				except Exception as e:
					await message.channel.send("오류: " + str(e))
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
					await message.channel.send(똥킹)
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
			elif 시작("버전") or 시작("qjwjs"):
				await message.channel.send(버전)
	except Exception as e:
		await message.add_reaction(엑스)
		await client.get_channel(732896130127626261).send("오류: " + str(e))
	
access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
