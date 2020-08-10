import discord, time, random, os, math
client = discord.Client()

버전 = 44
띵킹 = "🤔"
똥킹 = "<:thonking:732864307196592199>"
킹똥 = "<:gniknoht:733977049743753247>"
이몾 = [띵킹, 똥킹, 킹똥]
엑스 = "❌"
청소 = "🗑️"
BASE_CODE, CHO_CODE, JUNG_CODE, MAX_CODE = 44032, 588, 28, 55203
초성 = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
중성 = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
종성 = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
한글 = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ', '', ' ']
영어 = ['r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'qt', 't', 'T', 'd', 'w', 'c', 'z', 'x', 'v', 'g', 'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l', '', ' ']
한영 = dict(zip(한글, 영어))
영한 = dict(zip(영어, 한글))

@client.event
async def on_ready():
	print('시작')
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))

@client.event
async def on_message(message):
	try:
		m = message.content
		# print(m)
		def 포함(s):
			return m.find(s)+1
		def 시작(s):
			return m.startswith(s)

		if message.embeds:
			await message.add_reaction(똥킹)
			time.sleep(0.5)
			await message.clear_reaction(똥킹)
			return
		if 시작("!청소 ") or 포함("건 중에 ") and 포함("건의 메시지를 삭제했습니다.") or 포함("응답 대기 중입니다.") or 포함(", 메시지 개수는 `2 ~ 99`로 입력하세요."):
			await message.add_reaction(청소)
			time.sleep(0.5)
			await message.delete()
			return
		if (포함("띵킹") or 포함("띤킹") or 포함("흠터") or 포함(":소ㅑㅜㅏㅑㅜㅎ:") or 포함(띵킹)) or(포함("똔킹") or 포함("ㅁㄴㅇㄹ") or 포함("??") or 포함(":쇄ㅜㅏㅑㅜㅎ:") or 포함(똥킹)) or (포함("킹똥") or 포함("킹똔") or 포함(킹똥)):
			q = [[포함("띵킹"), 포함("띤킹"), 포함("흠터"), 포함(":소ㅑㅜㅏㅑㅜㅎ:"), 포함(띵킹)],
			[포함("똔킹"), 포함("ㅁㄴㅇㄹ"), 포함("??"), 포함(":쇄ㅜㅏㅑㅜㅎ:"), 포함(똥킹)],
			[포함("킹똥"), 포함("킹똔"), 포함(킹똥)]]
			for i in range(3):
				while 0 in q[i]:
					q[i].remove(0)
			w = [3000,3000,3000]
			for i in range(3):
				if q[i]:
					w[i] = min(q[i])
			e = sorted(w)
			await message.add_reaction(이몾[w.index(e[0])])
			del e[0]
			if e != [3000, 3000]:
				await message.add_reaction(이몾[w.index(e[0])])
				del e[0]
				if e != [3000]:
					await message.add_reaction(이몾[w.index(e[0])])
					del e[0]
		if 포함("ㅘ") or 포함("와"):
			await message.channel.send("샌즈!")
		if 시작(","):
			m = m[1:]
			if 시작("도움"):
				embed = discord.Embed(title=킹똥+"도움말"+똥킹, color=0xffccff)
				embed.add_field(name=",도움", value="이 메시지를 볼수 있습니다", inline=False)
				embed.add_field(name=",핑", value="으악 핑", inline=True)
				embed.add_field(name=",에블핑", value="으악 핑", inline=True)
				embed.add_field(name=",히어핑", value="으악 핑", inline=True)
				embed.add_field(name=",폭8", value="폭☆8", inline=False)
				embed.add_field(name=",계산 <식>", value="식을 계산합니다.", inline=False)
				embed.add_field(name=",버전", value="버전을 확인합니다.", inline=False)
				embed.set_footer(text=str(message.author)[:-5])
				await message.channel.send(embed=embed)
			if 시작("핑"):
				await message.channel.send("으악 핑")
			if 시작("에블핑"):
				await message.channel.send("||@everyone||")
				time.sleep(0.5)
				await message.channel.send("으악 핑")
			if 시작("히어핑"):
				await message.channel.send("||@here||")
				time.sleep(0.5)
				await message.channel.send("으악 핑")
			if 시작("폭8"):
				await message.channel.send("https://cdn.discordapp.com/attachments/740144542753357845/740145588594540604/100.gif")
			if 시작("버전"):
				await message.channel.send(버전)
			if 시작("계산"):
				q = m[3:] # 원래 식
				w = q[:] # 바뀔 식
				while True:
					if '^' in w:
						w = w.replace('^', '**')
					elif '√(' in w:
						w = w.replace('√(', 'math.sqrt(')
					elif '×' in w:
						w = w.replace('×', '*')
					elif '÷' in w:
						w = w.replace('÷', '/')
					else:
						break
				e = str(eval(w))
				embed = discord.Embed(title=킹똥+"계산 결과"+똥킹, color=0xffccff)
				embed.add_field(name=q + "\n" + w, value=e)
				embed.set_footer(text=str(message.author)[:-5])
				await message.channel.send(embed=embed)

	except Exception as e:
		await message.add_reaction(엑스)
		await message.channel.send("오류: " + str(e) + '\n' + "위치: " + str(message.jump_url))

access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
