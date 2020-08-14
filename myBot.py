import discord, time, random, os, math
client = discord.Client()

띵킹 = "🤔"
똥킹 = "<:thonking:732864307196592199>"
킹똥 = "<:gniknoht:733977049743753247>"
와샍 = "<:aemoji_29:736146757716803605>"
이몾 = { "띵킹":띵킹,
	"띤킹":띵킹,
	"흠터":띵킹,
	":소ㅑㅜㅏㅑㅜㅎ:":띵킹,
	띵킹:띵킹,
	"똥킹":똥킹,
	"똔킹":똥킹,
	"ㅁㄴㅇㄹ":똥킹,
	"??":똥킹,
	":쇄ㅜㅏㅑㅜㅎ:":똥킹,
	똥킹:똥킹,
	"킹똥":킹똥,
	"킹똔":킹똥,
	킹똥:킹똥,
	"ㅘ":와샍,
	"와":와샍}
엑스 = "❌"
청소 = "🗑️"
배코 = 44032
초코 = 588
중코 = 28
맥코 = 55203
초성 = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
중성 = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
종성 = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
한글 = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ', '', ' ']
영어 = ['r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'qt', 't', 'T', 'd', 'w', 'c', 'z', 'x', 'v', 'g', 'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l', '', ' ']
한영 = dict(zip(한글, 영어))
영한 = dict(zip(영어, 한글))
땀표 = ['```', '​`​`​`​']
폭팔 = "https://cdn.discordapp.com/attachments/740144542753357845/740145588594540604/100.gif"
구분 = "https://cdn.discordapp.com/attachments/740144542753357845/740161182136139806/131.gif"
똥달 = "https://cdn.discordapp.com/attachments/740144542753357845/740161338218905600/117_20200804190557.png"
반복 = [0, ""]

@client.event
async def on_ready():
	# print('시작')
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))
	await client.get_channel(686743756166135862).send("<@526889025894875158>, 시작")

@client.event
async def on_message(message):
	global 반복
	try:
		msg=[]
		m = message.content
		# print(m)
		def 포함(s):
			return m.find(s)+1
		def 시작(s):
			return m.startswith(s)
		def 몯밖(s, *dd):
			l = []
			for i in range(len(dd)//2):
				l.append((dd[i*2],dd[i*2+1]))
			d = dict(l)
			for i in d:
				while i in s:
					s = s.replace(i, d[i])
			return s
		if message.author.bot:
			return
		if 반복[0]:
			반복[0] -= 1
			await message.channel.send(str(eval(반복[1]))+f"\n(앞으로 {반복[0]}번 반복)")
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
		if True: # 들여쓰기를 위한 쓸모없는 코드
			q = m[:]
			while q:
				isend = True
				for i in 이몾.keys():
					if q.startswith(i):
						isend = False
						await message.add_reaction(이몾[i])
						q = q[len(i):]
				if isend:
					q = q[1:]
		if 시작(","):
			m = m[1:]
			if 시작("도움"):
				embed = discord.Embed(title=킹똥+"도움말"+똥킹, color=0xffccff)
				embed.add_field(name=",도움", value="이 메시지를 볼수 있습니다", inline=False)
				embed.add_field(name=",핑", value="으악 핑", inline=True)
				embed.add_field(name=",에블핑", value="으악 핑", inline=True)
				embed.add_field(name=",히어핑", value="으악 핑", inline=True)
				embed.add_field(name=",폭8", value="폭☆8", inline=False)
				embed.add_field(name=",프사", value="프사", inline=False)
				embed.add_field(name=",말", value="따라말합니다.", inline=False)
				embed.add_field(name=",계산 <식>", value="식을 계산합니다.", inline=False)
				embed.set_footer(text=str(message.author)[:-5])
				await message.channel.send(embed=embed)
			elif 시작("핑"):
				await message.channel.send("으악 핑")
			elif 시작("에블핑"):
				await message.channel.send("||@everyone||")
				time.sleep(0.5)
				await message.channel.send("으악 핑")
			elif 시작("히어핑"):
				await message.channel.send("||@here||")
				time.sleep(0.5)
				await message.channel.send("으악 핑")
			elif 시작("폭8"):
				await message.channel.send(폭팔)
			elif 시작("프사"):
				await message.channel.send(embed=discord.Embed(title=킹똥+"프사"+똥킹, color= 0xffccff).set_image(url=message.author.avatar_url))
			elif 시작("말"):
				await message.channel.send(m[2:])
			elif 시작("반복"):
				if 반복[0]:
					await message.channel.send(f"아직 {반복[0]}번 남음")
				반복[0], 반복[1] = int(m[3:].split()[0]), m[3:].split()[1]
				await message.channel.send(f"앞으로 {반복[0]}번 반복")
			elif 시작("계산"):
				q = m[3:] # 원래 식
				w = q[:] # 바뀔 식
				w = 몯밖(w, '(빈공백)', '​', '(공백)', ' ', '(큰공백)', '　', '(탭)', '\t', '^', '**', '√(', 'math.sqrt(', '×', '*', '÷', '/')
				e = str(eval(w))
				qwe = [q,w,e]
				for i in range(3):
					if len(qwe[i]) > 1900:
						qwe[i] = qwe[i][:1900]+'...'
					await message.channel.send('```yaml\n' + 몯밖(qwe[i], 땀표[0], 땀표[1]) + '```')
					time.sleep(0.3)

	except Exception as e:
		await message.add_reaction(엑스)
		await message.channel.send("오류: " + str(e) + '\n' + "위치: " + str(message.jump_url))

access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
