import discord, time, random, os, math
client = discord.Client()

띵킹 = "🤔"
똥킹 = "<:thonking:732864307196592199>"
킹똥 = "<:gniknoht:733977049743753247>"
와샍 = "<:aemoji_29:736146757716803605>"
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
출력 = ""
기억 = {}
이몾 = {
	"띵킹":띵킹,
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
지뢰 = [
	"<:z0:750200417664893020>",
	"<:z1:750200417836859472>",
	"<:z2:750200417564229673>",
	"<:z3:750200417304051795>",
	"<:z4:750200417782202429>",
	"<:z5:750200417421623448>",
	"<:z6:750200417740390442>",
	"<:z7:750200417748516965>",
	"<:z8:750200417748779059>",
	"<:z9:750200417417166879>",
	"<:z_:750200417287274529>"]
@client.event
async def on_ready():
	# print('시작')
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))
	await client.get_channel(686743756166135862).send("<@526889025894875158>, 시작")

@client.event
async def on_message(message):
	global 반복
	try:
		m = message.content
		# print(m)
		def 포함(s):
			return m.find(s)+1
		def 시작(s):
			return m.startswith(s)
		def 관맂():
			return message.author.id == 526889025894875158
		def 몯밖(s, *dd):
			l = []
			for i in range(len(dd)//2):
				l.append((dd[i*2],dd[i*2+1]))
			d = dict(l)
			for i in d:
				while i in s:
					s = s.replace(i, d[i])
			return s
		def check(m):
			return m.channel.id == message.channel.id and m.author == message.author
		if message.author.id == 688978156535021599:
			return
# 		if 관맂():
# 			await message.channel.send('`' + m + '`')
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
		if 시작(","):
			m = m[1:]
			if 시작("도움"):
				embed = discord.Embed(title=킹똥+"도움말"+똥킹, color=0xffccff)
				embed.add_field(name=",도움", value="도움", inline=False)
				embed.add_field(name=",핑", value="으악 핑", inline=True)
				embed.add_field(name=",에블핑", value="으악 핑", inline=True)
				embed.add_field(name=",히어핑", value="으악 핑", inline=True)
				embed.add_field(name=",폭8", value="폭☆8", inline=False)
				embed.add_field(name=",프사", value="프사", inline=False)
				embed.add_field(name=",말", value="말", inline=False)
				embed.add_field(name=",계산 <식>", value="계산", inline=False)
				embed.add_field(name=",임베드", value="임베드", inline=False)
				embed.add_field(name=",지뢰찾기 <x> <y> <지뢰 수>", value="지뢰찾기를 할수 ", inline=False)
				embed.add_field(name=",기억", value="기억된 목록을 확인합니다", inline=True)
				embed.add_field(name=",기억 <단어>", value="<단어>를 찾습니다", inline=True)
				embed.add_field(name=",기억 <단어> <뜻>", value="<단어>에 <뜻>을 등록합니다", inline=True)
				embed.set_footer(text=message.author.name)
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
				if '\n' in m:
					qwer = [None, None, None]
					qwer[2] = 'global 출력\n' + '\n'.join(m[3:].split('\n')[:-1]) + '\n출력=' + m[3:].split('\n')[-1]
					exec(qwer[2]) ; qwer[1] = str(출력)
					qwer[0] = m[3:]
				else:
					qwer = [None, None, None]
					qwer[0] = m[3:]
					qwer[1] = str(eval(qwer[0]))
				for i in range(2):
						if len(qwer[i]) > 1900:
							qwer[i] = qwer[i][:1900]+'...'
						await message.channel.send('```yaml\n' + 몯밖(qwer[i], 땀표[0], 땀표[1]) + '```')
						time.sleep(0.3)
			elif 시작("임베드"):
				inputdict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
				look_dict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
				mymsg = await message.channel.send("준비중...")
				for i in range(len(list(inputdict.keys()))):
					await mymsg.delete()
					mymsg = await message.channel.send(str(i) + ". " + str(list(inputdict.keys())[i]) + "을(를) 입력해주세요.\n```yaml\n" + str(몯밖(str(look_dict)[1:-1], ', ', ',\n', 땀표[0], 땀표[1])) + "```")
					inputmsg = await client.wait_for('message', timeout=30.0, check=check)
					inputmsg = inputmsg.content
					inputdict[list(inputdict.keys())[i]] = inputmsg
					look_dict[list(inputdict.keys())[i]] = str(inputmsg)[:7]+'...' if len(str(inputmsg)) > 10 else str(inputmsg)
				await mymsg.delete()
				try:
					embed = discord.Embed(title=킹똥+inputdict["제목"]+똥킹, color=int("0x"+inputdict["색"]))
				except:
					embed = discord.Embed(title=킹똥+inputdict["제목"]+똥킹, color=0x000000)
				embed.add_field(name=inputdict["소제목"], value=inputdict["내용"], inline=False)
				embed.set_footer(text=inputdict["푸터"])
				await message.channel.send(embed=embed)
			elif 시작("기억"):
				q = m[3:].split()
				if len(q) == 0: # 목록
					await message.channel.send(몯밖(str(기억.keys())[10:-1], ", ", ",\n"))
				elif len(q) == 1: # 찾기
					await message.channel.send(기억[q[0]])
				elif len(q) == 2: # 등록
					if q[0] in list(기억.keys()):
						기억[q[0]] = q[1]
						await message.channel.send(q[0] + " 을(를) 덮어씀")
					else:
						기억[q[0]] = q[1]
						await message.channel.send(q[0] + " 을(를) 기억")
			elif 시작("지뢰찾기") and 관맂():
				mine_x = int(m.split()[1]) ; await message.channel.send(mine_x)
				mine_y = int(m.split()[2]) ; await message.channel.send(mine_y)
				mine_z = int(m.split()[3]) ; await message.channel.send(mine_z)
				if mine_x < 1 or mine_y < 1 or mine_z < 1 or mine_x > 9 or mine_y > 9 or mine_z > mine_x * mine_y:
					await message.channel.send("```yaml\nx : 1~9\ny : 1~9\n지뢰 수 : 1~x*y```")
					return
				while True:
					mine_map = []
					for i in range(mine_y):
						mine_map.append([])
						for j in range(mine_x):
							mine_map[i].append(지뢰[0])
					i=0 ; await message.channel.send(f"minemap:{mine_map}")
					while i <= mine_z:
						i1 = random.randrange(mine_y) ; await message.channel.send(f"i1:{i1}")
						i2 = random.randrange(mine_x) ; await message.channel.send(f"i2:{i2}")
						if mine_map[i1][i2] == 지뢰[10]:
							continue
						else:
							mine_map[i1][i2] = 지뢰[10]
							i+=1
					mine_map_lookver = ''
					for i in mine_map:
						for j in i:
							mine_map_lookver += j
						mine_map_lookver += '\n'
					#if mine_map_lookver.count(지뢰[10]) != mine_z:
					#	continue
					else:
						await message.channel.send(mine_map_lookver)
# 	 	 				await message.channel.send(mine_map)
						break

		# 반응달기
		gumsajung = m[:]
		while gumsajung:
			isend = True
			for i in 이몾.keys():
				if gumsajung.startswith(i):
					isend = False
					await message.add_reaction(이몾[i])
					gumsajung = gumsajung[len(i):]
			if isend:
				gumsajung = gumsajung[1:]

	except Exception as e:
		await message.add_reaction(엑스)
		await message.channel.send("오류: " + str(e) + '\n' + "위치: " + str(message.jump_url))

access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
