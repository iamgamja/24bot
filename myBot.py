import discord, time, datetime, random, os, math
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
종코 = 1
맥코 = 55203
초성 = ('ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
중성 = ('ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ')
종성 = ('', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
한글 = ('ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ', '')
영어 = ('r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'E', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'Q', 'qt', 't', 'T', 'd', 'w', 'W', 'c', 'z', 'x', 'v', 'g', 'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l', '')
한영 = dict(zip(한글, 영어))
영한 = dict(zip(영어, 한글))
겹글 = "rsfqhnm"
빈공 = '​'
폭팔 = "https://cdn.discordapp.com/attachments/740144542753357845/740145588594540604/100.gif"
구분 = "https://cdn.discordapp.com/attachments/740144542753357845/740161182136139806/131.gif"
똥달 = "https://cdn.discordapp.com/attachments/740144542753357845/740161338218905600/117_20200804190557.png"
반복 = [0, ""] # ,반복 명령어에 사용
출력 = ""      # ,계산 명령어에 사용
기억 = {}      # ,기억 명령어에 사용
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
지뢰 = (
	"<:0z:762919979388502027>", #0
	"<:z1:750200417836859472>", #1
	"<:z2:750200417564229673>", #2
	"<:z3:750200417304051795>", #3
	"<:z4:750200417782202429>", #4
	"<:z5:750200417421623448>", #5
	"<:z6:750200417740390442>", #6
	"<:z7:750200417748516965>", #7
	"<:z8:750200417748779059>", #8
	"<:z9:750200417417166879>", #9
	"<:z_:750200417287274529>") #10

def 시간():

	utcnow   = datetime.datetime.utcnow()
	time_gap = datetime.timedelta(hours=9)
	kor_time = utcnow + time_gap
	n        = kor_time.strftime('%Y-%m-%d %p %I:%M:%S')
	return n
	# return (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime('%Y-%m-%d %p %I:%M:%S')
	
@client.event
async def on_ready():
	# print('시작')
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))
	startmsg = await client.get_channel(762916201654386701).send(f"{시간()}, 시작")

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

		def 관맂(): # 관리자(감자#9400)인지 확인
			return message.author.id == 526889025894875158

		def 체크(m): # 같은 사람이 같은 채널에서 보낸 메시지인지 확인
			return m.channel.id == message.channel.id and m.author == message.author
		
		if message.author.id == 688978156535021599: # 자신이 보낸 메시지 무시
			return

		if message.channel.id == 762916201654386701: # 로그채널의 메시지일경우
			await message.channel.send(f"""
			m: `{m}`
			id: `{message.id}`
			authorId: `{message.author.id}`
			channelId: `{message.channel.id}`
			""")
			return

		if 반복[0]:
			반복[0] -= 1
			await message.channel.send(str(eval(반복[1]))+f"\n(앞으로 {반복[0]}번 반복)")
			return

		if 시작("!청소 ") or 포함("건 중에 ") and 포함("건의 메시지를 삭제했습니다.") or 포함("응답 대기 중입니다.") or 포함(", 메시지 개수는 `2 ~ 99`로 입력하세요."):
			await message.add_reaction(청소)
			time.sleep(1)
			await message.delete()
			return

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

		if 시작(","):
			m = m[1:]
			if 시작("도움"):
				# **`도움`**
				
				# ":GWchadMEGATHINK:"
				# ":GWchadThonkery:"
				# ":GWchadThinkeyes:"
				# ":GWchadThink:"
				# ":GWoicZenThink:"
				# ":GWoicFidgetThinker:"
				# ":GWmythicalThonkCool:"
				
				
				embed = discord.Embed(title=킹똥+"도움말"+똥킹, color=0xffccff)
				embed.add_field(name=빈공, value="**`도움`**", inline=False)
				embed.add_field(name=",도움", value="이 메시지를 출력합니다.", inline=True)
				embed.add_field(name=빈공, value="**`재미`**", inline=False)
				embed.add_field(name=",핑", value="으악 핑", inline=True)
				embed.add_field(name=",에블핑", value="으악 핑", inline=True)
				embed.add_field(name=",히어핑", value="으악 핑", inline=True)
				embed.add_field(name=",폭8", value="폭☆8", inline=True)
				embed.add_field(name=",지뢰찾기 <x> <y> <지뢰 수>", value="지뢰찾기를 할수", inline=True)
				embed.add_field(name=빈공, value=빈공, inline=True)
				embed.add_field(name=빈공, value="**`기능`**", inline=False)
				embed.add_field(name=",프사", value="프사를 출력합니다.", inline=True)
				embed.add_field(name=",말 <할말>", value="<할말>을 출력합니다.", inline=True)
				embed.add_field(name=",계산 <식>", value="<식>을 계산합니다.", inline=True)
				embed.add_field(name=",청소 <수>", value="<수>만큼의 메시지를 지웁니다.", inline=True)
				embed.add_field(name=",임베드", value="임베드를 만듭니다.", inline=True)
				embed.add_field(name=빈공, value=빈공, inline=True)
				embed.add_field(name=",한영 <한글>", value="<한글>을 영타로 번역합니다.", inline=True)
				embed.add_field(name=",영한 <영어>", value="<영어>을 한타로 번역합니다.", inline=True)
				embed.add_field(name=빈공, value=빈공, inline=True)
				embed.add_field(name=빈공, value="**`기타`**", inline=False)
				embed.add_field(name=",기억", value="기억된 목록을 확인합니다", inline=True)
				embed.add_field(name=",기억 <단어>", value="<단어>를 찾습니다", inline=True)
				embed.add_field(name=",기억 <단어> <뜻>", value="<단어>에 <뜻>을 등록합니다", inline=True)
				embed.set_footer(text= f'{message.author.name} | {시간()}')
				await message.channel.send(embed=embed)
				
			elif 시작("핑"):
				await message.channel.send("으악 핑")
				
			elif 시작("에블핑"):
				msg = await message.channel.send("||@everyone||")
				time.sleep(1)
				await msg.edit(content="으악 핑")
				
			elif 시작("히어핑"):
				msg = await message.channel.send("||@here||")
				time.sleep(1)
				await msg.edit(content="으악 핑")
				
			elif 시작("폭8"):
				await message.channel.send(폭팔)
				
			elif 시작("프사"):
				await message.channel.send(embed=discord.Embed(title=킹똥+"프사"+똥킹, color=0xffccff).set_image(url=message.author.avatar_url))
				
			elif 시작("말"):
				await message.channel.send(m[2:])
				
			elif 시작("반복"):
				if 반복[0]:
					await message.channel.send(f"아직 {반복[0]}번 남음")
				반복[0], 반복[1] = int(m.split()[1]), m.split()[2]
				await message.channel.send(f"앞으로 {반복[0]}번 반복")
				
			elif 시작("임베드"):
				inputdict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
				look_dict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
				mymsg = await message.channel.send("준비중...")
				for i in range(len(list(inputdict.keys()))):
					await mymsg.delete()
					mymsg = await message.channel.send(str(i) + ". " + str(list(inputdict.keys())[i]) + "을(를) 입력해주세요.\n```yaml\n" + str(str(look_dict)[1:-1].replace(', ', ',\n').replace(땀표[0], 땀표[1])) + 땀표[0])
					inputmsg = await client.wait_for('message', timeout=30.0, check=체크)
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
					await message.channel.send(str(기억.keys())[10:-1].replace(', ', ',\n'))
				elif len(q) == 1: # 찾기
					await message.channel.send(f"{기억[q[0]][0]} - `{기억[q[0]][1]}`" if q[0] in 기억 else "없음")
				elif len(q) == 2: # 등록
					if q[0] in list(기억.keys()):
						기억[q[0]] = [q[1], str(message.author)]
						await message.channel.send(q[0] + " 을(를) 덮음")
					else:
						기억[q[0]] = [q[1], str(message.author)]
						await message.channel.send(q[0] + " 을(를) 기억")
				else:
					await message.channel.send("ㅏ 띄어쓰기 안됨")
				
			elif 시작("지뢰찾기"):
				#제대로 input 했는지 확인
				mine_input = m[5:].split()
				if len(mine_input) != 3:
					await message.channel.send("```yaml\nx : 1~17\ny : 1~50\n지뢰 수 : 1~x*y```") ; return
				mine_x = int(mine_input[0])
				mine_y = int(mine_input[1])
				mine_z = int(mine_input[2])
				if (mine_x < 1) or (mine_y < 1) or (mine_z < 1) or (mine_x > 17) or (mine_y > 50) or (mine_z > mine_x * mine_y):
					await message.channel.send("```yaml\nx : 1~17\ny : 1~50\n지뢰 수 : 1~x*y```") ; return
				#확인 끝, 틀 만들기
				mine_map = []
				for i in range(mine_y):
					mine_map.append([])
					for j in range(mine_x):
						mine_map[i].append(지뢰[0])
				#틀 만들기 끝, 지뢰 넣기
				i=0
				while i < mine_z:
					i1 = random.randrange(mine_y)
					i2 = random.randrange(mine_x)
					if mine_map[i1][i2] == 지뢰[10]:
						continue
					else:
						mine_map[i1][i2] = 지뢰[10]
						i+=1
				#지뢰 넣기 끝, 숫자 넣기
				for i1 in range(mine_y):
					for i2 in range(mine_x):
						if mine_map[i1][i2] == 지뢰[10]:
							continue
						else:
							i=0

							try:
								i += 1 if mine_map[i1-1 if i1>0 else 0/0][i2-1 if i2>0 else 0/0] == 지뢰[10] else 0
							except:
								pass

							try:
								i += 1 if mine_map[i1-1 if i1>0 else 0/0][i2] == 지뢰[10] else 0
							except:
								pass

							try:
								i += 1 if mine_map[i1-1 if i1>0 else 0/0][i2+1] == 지뢰[10] else 0
							except:
								pass

							try:
								i += 1 if mine_map[i1][i2-1 if i2>0 else 0/0] == 지뢰[10] else 0
							except:
								pass

							#try:
								#i += 1 if mine_map[i1][i2] == 지뢰[10] else 0
							#except:
								#pass

							try:
								i += 1 if mine_map[i1][i2+1] == 지뢰[10] else 0
							except:
								pass

							try:
								i += 1 if mine_map[i1+1][i2-1 if i2>0 else 0/0] == 지뢰[10] else 0
							except:
								pass

							try:
								i += 1 if mine_map[i1+1][i2] == 지뢰[10] else 0
							except:
								pass

							try:
								i += 1 if mine_map[i1+1][i2+1] == 지뢰[10] else 0
							except:
								pass

							mine_map[i1][i2] = 지뢰[i]
				mine_map_lookver = ''
				for i in mine_map:
					for j in i:
						mine_map_lookver += f"||{j}||"
					mine_map_lookver += '\n'

				for j in mine_map_lookver.split():
					time.sleep(1)
					await message.channel.send(j)
				
			elif 시작("청소"):
				await message.channel.purge(limit=int(m[3:])+1)
				msg = await message.channel.send(f"{m[3:]}개의 메시지를 지움")
				time.sleep(2)
				await msg.delete()
				
			elif 시작("계산"):
				m = m[3:]
				if '\n' in m:
					exec('global 출력\n' + '\n'.join(m.split('\n')[:-1]) + '\n출력=' + m.split('\n')[-1])
					outputmsg = str(출력)
				else:
					outputmsg = str(eval(m))

				await message.channel.send(outputmsg[:2000-3]+'...' if len(outputmsg) > 2000 else outputmsg)
			
			elif 시작("한영"):
				f=''
				for i in m[3:]:
					c=ord(i)
					if 배코<=c<=맥코:
						c-=배코 ; f+=한영[초성[c//초코]]
						c%=초코 ; f+=한영[중성[c//중코]]
						c%=중코 ; f+=한영[종성[c//종코]]
					else:
						try:
							f += 한영[i]
						except:
							f += i
				await message.channel.send(f)

			elif 시작("영한"):
				f=''
				m=m[3:]
				w=''
				임시 = "NaN"
				#한글로 바꾸기
				for i in range(len(m)):
					if m[i] in 겹글 and len(m)>=i+2 and 임시 == "NaN":
						임시 = m[i]
					elif 임시+m[i] in 영한:
						w+=영한[임시+m[i]] ; 임시 = "NaN"
					elif 임시 != "NaN":
						w+=영한[임시] ; 임시 = "NaN"
						if m[i] in 겹글 and len(m)>=i+2 and 임시 == "NaN":
							임시 = m[i]
						else:
							w+=영한[m[i]] if m[i] in 영한 else m[i]
					else:
						w+=영한[m[i]] if m[i] in 영한 else m[i]
				#한글을 합치기
				w=list(w)
				임시 = []
				for i in range(len(w)):
					if len(임시) == 0:
						if w[i] in 초성:
							임시.append(w[i])
						else:
							f+=w[i]
					elif len(임시) == 1:
						if w[i] in 중성:
							임시.append(w[i])
						else:
							f+=임시[0] ; del 임시[0]
							if w[i] in 초성:
								임시.append(w[i])
							else:
								f+=w[i]
					else:
						if w[i] in 종성:
							if w[i] in 초성 and ((w[i+1] in 중성) if len(w)>=i+2 else False):
								f+=chr(배코+초성.index(임시[0])*초코+중성.index(임시[1])*중코)
								del 임시[1]
								del 임시[0]
								임시.append(w[i])
							else:
								f += chr(배코 + 초성.index(임시[0])*초코 + 중성.index(임시[1])*중코 + 종성.index(w[i]))
								del 임시[1]
								del 임시[0]
						else:
							f+=chr(배코 + 초성.index(임시[0])*초코 + 중성.index(임시[1])*중코)
							del 임시[1]
							del 임시[0]
							if w[i] in 초성:
								임시.append(w[i])
							else:
								f+=w[i]
				for i in 임시:
					f+=i
				await message.channel.send(f)
				
		elif 시작('```'):
			m = m[3:-3]
			if '\n' in m:
				exec('global 출력\n' + '\n'.join(m.split('\n')[:-1]) + '\n출력=' + m.split('\n')[-1])
				outputmsg = str(출력)
			else:
				outputmsg = str(eval(m))

			await message.channel.send(outputmsg[:2000-3]+'...' if len(outputmsg) > 2000 else outputmsg)

	except Exception as e:
		await message.add_reaction(엑스)
		await message.channel.send(f"오류: {e}\n위치: {message.jump_url}")

access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
