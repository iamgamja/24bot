import discord, time, datetime, random, os, math, asyncio
client = discord.Client()

# await asyncio.sleep(1.0)
# await message.channel.send()
# eval() 식
# exec() 코드

# 반응
띵킹 = "🤔"
동글 = "⭕"
엑스 = "❌"
청소 = "🗑️"
체크 = "✅"
크체 = "❎"
똥킹 = "<:thonking:792609223099940864>"
킹똥 = "<:gniknoht:792609325562068992>"
똥키 = "<:thonkery:792646930077188096>"
저런 = "<:wjfjs:783226650664894544>"
흠ㅁ = "<:gma:783226674413043733>"
히히 = "<:glgl:783226584575508484>"
헐ㄹ = "<:gjf:783226547515555890>"
아ㅏ = "<:dk:783226610529599488>"
와ㅏ = "<:dhk:783226517655912478>"
# 한영
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
# 기타
빈공 = '​'
땀표 = '```'
# 사진
폭팔 = "https://cdn.discordapp.com/attachments/740144542753357845/740145588594540604/100.gif"
구분 = "https://cdn.discordapp.com/attachments/740144542753357845/740161182136139806/131.gif"
똥달 = "https://cdn.discordapp.com/attachments/740144542753357845/740161338218905600/117_20200804190557.png"
# 기능
출력 = ""      # ,계산 명령어에 사용
기억 = {}      # ,기억 명령어에 사용
피버 = False   # ,피버 명령어에 사용
note = None
note2 = None
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
사달 = {
	"아" : "<:down:793740736583303168>" ,
	"오" : "<:right:793740751904309269>",
	"왼" : "<:left:793743882944118794>" }

슬롯 = ('<a:slotspin:793667557419778069>', '<a:slotseven:793668040712650783>', '<a:slotdia:793668088817123358>', '<a:slotstar:793668066692956160>', '<a:slotspade:793668129350877184>', '<a:slotheart:793668152319016980>', '<a:slotclover:793668174783709194>')

def 시간():
	utcnow   = datetime.datetime.utcnow()
	time_gap = datetime.timedelta(hours=9)
	kor_time = utcnow + time_gap
	n        = kor_time.strftime('%Y-%m-%d %p %I:%M:%S')
	return n

@client.event
async def on_ready():
	print('시작')
	await client.change_presence(status = discord.Status.online, activity = discord.Activity(name=",도움", type=discord.ActivityType.listening))
	await client.get_channel(762916201654386701).send(f"{시간()}, <@526889025894875158>, 시작")

@client.event
async def on_reaction_add(reaction, user):
	await reaction.message.channel.id == 762916201654386701 and str(reaction) == 체크:
		await reaction.message.add_reaction(체크)

@client.event
async def on_message(message):

	if message.guild.id == 798353590040920094:
		global note
		if True:
			if note is None:
				note = await client.get_channel(798358860456001566).fetch_message(798724124188475392)

		if message.content == "!등록":
			if "<@"+str(message.author.id)+">" in note.content:
				await message.channel.send("이미 등록되었습니다")
				return
			else:
				await note.edit(content=f"{note.content}\n<@{message.author.id}> : 0")
				await message.channel.send("완료")
  
		if message.author.id == 646998005643476993:
			if message.content.startswith("!돈"):
				m = message.content
				m = m[5:]
				if m.startswith("!"):
					m = m[1:]
				user = "<@"+m[:18]+">"
				m = m[18:]
				m = m[2:]
				usermoney = int(m)
				if not (user in note.content):
					await message.channel.send("등록되어있지 않은 유저입니다.")
					return
				else:
					notec = note.content
					notec = notec.split("\n")[1:]
					for i in range(len(notec)):
						if notec[i].startswith(user):
							noten = i
					notec[noten] = notec[noten][:24] + str(int(notec[noten][24:])+usermoney)
					notem = "이름 : 돈\n" + "\n".join(notec)
					await note.edit(content = notem)
					await message.channel.send("완료")
			if message.content.startswith("!등록"):
				mm = message.content[4:]
				m = ""
				for i in mm:
					if i in "1234567890":
						m += i
				if len(m) != 16:
					await message.channel.send("잘못된 유저입니다.")
					return
				if m in note.content:
					await message.channel.send("이미 등록되었습니다.")
					return
				else:
					await note.edit(content=f"{note.content}\n{m} : 0")
					await message.channel.send("완료")

	if message.guild.id == 798353590040920094: 
		return

	try:
		global 반복
		m = message.content
		# print(m)

		def 시작(s):
			s = 한영변환(s)
			mm = m
			mmm = 한영변환(mm)
			return mmm.startswith(s)

		def 관리(): # 관리자(감자#9400)인지 확인
			return message.author.id == 526889025894875158

		def 체크1(m): # 같은 사람이 같은 채널에서 보낸 메시지인지 확인 (임베드)
			return m.channel.id == message.channel.id and m.author == message.author

		def 체크2(r,u): # 리엑션이 0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣ 그리고 같은 사람 (실드)
			return str(r.emoji) in "0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣" and u == message.author
		
		def 제목(s):
			return 킹똥 + s + 똥킹
		
		def 코드(s):
			return 땀표 + s + 땀표

		def 한영변환(m):
			m+='.'
			f = ''
			for i in m:
				c=ord(i)
				if 배코<=c<=맥코:
					c%=배코 ; f+=한영[초성[c//초코]]
					c%=초코 ; f+=한영[중성[c//중코]]
					c%=중코 ; f+=한영[종성[c//종코]]
				else:
					try:
						f += 한영[i]
					except:
						f += i
			return f[:-1]

		def 영한변환(m):
			m+='.'
			f=''
			w=''
			임시 = "NaN"
			#한글로 바꾸기
			for i in range(len(m)):
				if m[i] in 겹글 and len(m)>=i+2 and 임시 == "NaN":
					임시 = m[i]
				elif 임시+m[i] in 영한:
					임시 += m[i]
				elif len(임시) == 2 and 영한[m[i]] in 중성:
					w+=영한[임시[0]]
					w+=영한[임시[1]]
					w+=영한[m[i]]
					임시 = "NaN"
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
			return f[:-1]
		
		if message.author.id == 405664776954576896 and message.channel.id in (766932314973929527, 783516524685688842, 784228694940057640, 794146499034480661):
			#랭크업, 시간, 도박장, 도박2 에서의 슷칼봇 메시지 삭제
			await message.delete()
			return
		
		if message.author.bot: # 봇이 보낸 메시지 무시
			return

		if message.channel.id == 762916201654386701: # 로그채널의 메시지일경우
			await message.channel.send(	f"m: `{m}`\n"				+
							f"message_id: `{message.id}`\n"		+
							f"author_id: `{message.author.id}`\n"	+
							f"channel_id: `{message.channel.id}`\n"	+
							f"guild_id: `{message.guild.id}`\n"	)
			return
		
		if '@everyone' in m or '@here' in m:
			# await message.add_reaction(똥키)
			return


		if 시작(",도움"):
			m = ' '.join(m.split(' ')[1:])
			
			help_list = {
				"도움" : {"`,도움`" : "전체 도움말을 출력합니다.", "`,도움 <명령어>`" : "<명령어> 에 대한 세부 도움말을 출력합니다."},
				"핑" : {"`,핑`" : "명령어를 입력한 사람을 핑합니다."},
				"에블핑" : {"`,에블핑`" : "@everyone을 출력합니다."},
				"히어핑" : {"`,히어핑`" : "@here을 출력합니다."},
				"폭8" : {"`,폭8`" : "폭☆8하는 gif를 출력합니다."},
				"지뢰찾기" : {"`,지뢰찾기 <랜덤|최소|최대>`" : "<랜덤|최소|최대> 크기의 지뢰찾기 판을 출력합니다.", "`,지뢰찾기 <x> <y> <지뢰 수>`" : "지뢰찾기 판을 출력합니다."},
				"사다리타기" : {"`,사다리타기 <x> <y>`" : "사다리타기 판을 출력합니다."},
				"슬롯" : {"`,슬롯`" : "슬롯머신을 여러 메시지에서 돌립니다.", "`,ㅅ`" : "슬롯머신을 여러 메시지에서 돌립니다."},
				"롯슬" : {"`,롯슬`" : "슬롯머신을 한 메시지에서 돌립니다.", "`,ㄹ`" : "슬롯머신을 한 메시지에서 돌립니다."},
				"프사" : {"`,프사`" : "명령어를 입력한 사람의 프사를 출력합니다."},
				"말" : {"`,말 <할 말>`" : "<할 말>을 출력합니다."},
				"계산" : {"`,계산 <식>`" : "<식>을 계산합니다."},
				"청소" : {"`,청소 <수>`" : "<수>만큼의 메시지를 지웁니다."},
				"임베드" : {"`,임베드`" : "임베드를 만듭니다."},
				"역할생성" : {"`,역할생성 <이름>`" : "<이름>의 역할을 생성합니다."},
				"역할제거" : {"`,역할제거 <이름>`" : "<이름>의 역할을 제거합니다."},
				"채널생성" : {"`,채널생성 (카테고리) <이름>`" : "(카테고리)에 <이름>의 채널을 생성합니다."},
				"채널제거" : {"`,채널제거 <이름>`" : "<이름>의 채널을 제거합니다."},
				"시간" : {"`,시간`" : "현재시간을 출력합니다."},
				"한영" : {"`,한영 <한글>`" : "<한글>을 영타로 바꿉니다."},
				"영한" : {"`,영한 <영어>`" : "<영어>를 한타로 바꿉니다."},
				"기억" : {"`,기억`" : "기억된 목록을 출력합니다.", "`,기억 <키워드>`" : "<키워드>에 기억된 <대답>을 출력합니다.", "`,기억 <키워드> <대답>`" : "<키워드>에 <대답>을 기억합니다."},
				"초대" : {"`,초대`" : "이 봇의 초대링크를 출력합니다."},
				"정보" : {"`,정보`" : "이 봇을 만든 사람을 핑합니다."},
			}
			embed = discord.Embed(title=제목("도움말"), color=0x825cff)
			
			if m in help_list:
				for i in help_list[m]:
					embed.add_field(name=i, value=help_list[m][i], inline=False)
			else:
				embed.add_field(name="**취소선은 아마도 사용할수 없는 명령어입니다.**", value="`,도움 <명령어>`로 세부 도움말을 확인할수 있습니다", inline=False)
				embed.add_field(name="**`도움`**", value="`도움`", inline=False)
				embed.add_field(name="**`재미`**", value="`핑` ~~`에블핑`~~ ~~`히어핑`~~ `폭8` `지뢰찾기` `사다리타기` `슬롯` `롯슬`", inline=False)
				embed.add_field(name="**`기능`**", value="`프사` `말` `계산` ~~`청소`~~ `임베드` ~~`역할생성`~~ ~~`역할제거`~~ ~~`채널생성`~~ ~~`채널제거`~~ `시간` `한영` `영한` `기억`", inline=False)
				embed.add_field(name="**`기타`**", value="`초대` `정보`", inline=False)
				
			embed.set_footer(text= f'{message.author.name} | {시간()}')
			await message.channel.send(embed=embed)

		elif 시작(",초대"):
			await message.channel.send("https://discord.com/oauth2/authorize?&client_id=688978156535021599&scope=bot&permissions=8")

		elif 시작(",핑"):
			await message.channel.send(f"<@{message.author.id}>")

		elif 시작(",시간"):
			await message.channel.send(시간())

		elif 시작(",정보"):
			await message.channel.send(f"만든사람: <@526889025894875158>")

		elif 시작(",에블핑") and 관리():
			await message.channel.send("@everyone")

		elif 시작(",히어핑") and 관리():
			await message.channel.send("@here")

		elif 시작(",폭8"):
			await message.channel.send(폭팔)

		elif 시작(",프사"):
			await message.channel.send(embed=discord.Embed(title=제목("프사"), color=0xffccff).set_image(url=message.author.avatar_url))

		elif 시작(",말"):
			m = ' '.join(m.split(' ')[1:])
			await message.channel.send(m)

		elif 시작(",임베드"):
			inputdict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
			look_dict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
			mymsg = await message.channel.send("준비중...")
			for i in range(len(list(inputdict.keys()))):
				await mymsg.delete()
				mymsg = await message.channel.send(str(i) + ". " + str(list(inputdict.keys())[i]) + "을(를) 입력해주세요.\n```yaml\n" + str(str(look_dict)[1:-1].replace(', ', ',\n').replace(땀표[0], 땀표[1])) + 땀표[0])
				inputmsg = await client.wait_for('message', timeout=30.0, check=체크1)
				inputmsg = inputmsg.content
				inputdict[list(inputdict.keys())[i]] = inputmsg
				look_dict[list(inputdict.keys())[i]] = str(inputmsg)[:7]+'...' if len(str(inputmsg)) > 10 else str(inputmsg)
			await mymsg.delete()
			try:
				embed = discord.Embed(title=제목(inputdict["제목"]), color=int("0x"+inputdict["색"], 16))
			except:
				embed = discord.Embed(title=제목(inputdict["제목"]), color=0x000000)
			embed.add_field(name=inputdict["소제목"], value=inputdict["내용"], inline=False)
			embed.set_footer(text=inputdict["푸터"])
			await message.channel.send(embed=embed)

		elif 시작(",기억"):
			m = ' '.join(m.split(' ')[1:])
			q = m.split()
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

		elif 시작(",지뢰찾기"):
			m = ' '.join(m.split(' ')[1:])
			#제대로 input 했는지 확인
			if 시작("랜덤"):
				m = str(random.randint(1, 17)) + ' '
				m += str(random.randint(1, 50)) + ' '
				m += str(random.randint(1, int(m.split()[0]) * int(m.split()[1])))
			
			m = '17 50 850' if 시작("최대") else m
			m = '1 1 1' if 시작('최소') else m
			mine_input = m.split()
			
			if len(mine_input) != 3:
				await message.channel.send("```yaml\nx : 1~17\ny : 1~50\n지뢰 수 : 1~x*y\n또는 ,지뢰찾기 <랜덤|최대|최소>```") ; return
			mine_x = int(mine_input[0])
			mine_y = int(mine_input[1])
			mine_z = int(mine_input[2])
			if (mine_x < 1) or (mine_y < 1) or (mine_z < 1) or (mine_x > 17) or (mine_y > 50) or (mine_z > mine_x * mine_y):
				await message.channel.send("```yaml\nx : 1~17\ny : 1~50\n지뢰 수 : 1~x*y\n또는 ,지뢰찾기 <랜덤|최대|최소>```") ; return
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
				await asyncio.sleep(1.0)
				await message.channel.send(j)
			await message.channel.send(f"{mine_x} * {mine_y}, 지뢰 수: {mine_z}")

		elif 시작(",청소") and 관리():
			m = ' '.join(m.split(' ')[1:])
			await message.channel.purge(limit=int(m)+1)
			msg = await message.channel.send(f"{m}개의 메시지를 지움")
			await asyncio.sleep(2.0)
			await msg.delete()

		elif 시작(",한영"):
			m = ' '.join(m.split(' ')[1:])
			await message.channel.send(한영변환(m))

		elif 시작(",영한"):
			m = ' '.join(m.split(' ')[1:])
			await message.channel.send(영한변환(m))

		elif 시작(",역할생성") and 관리():
			m = ' '.join(m.split(' ')[1:])
			try:
				await message.guild.create_role(name = m)
				await message.add_reaction(동글)
			except:
				await message.add_reaction(엑스)

		elif 시작(",역할제거") and 관리():
			m = ' '.join(m.split(' ')[1:])
			try:
				role = discord.utils.get(message.guild.roles, name=m)
				await role.delete()
				await message.add_reaction(동글)
			except:
				await message.add_reaction(엑스)

		elif 시작(",채널생성") and 관리():
			m = ' '.join(m.split(' ')[1:])
			try:
				category = discord.utils.get(message.guild.categories, name=' '.join(m.split(' ')[:-1]))
				await message.guild.create_text_channel(m.split(' ')[-1], category=category)
				await message.add_reaction(동글)
			except:
				await message.add_reaction(엑스)

		elif 시작(",채널제거") and 관리():
			m = ' '.join(m.split(' ')[1:])
			try:
				channel = discord.utils.get(message.guild.channels, name=m)
				await channel.delete()
				await message.add_reaction(동글)
			except:
				await message.add_reaction(엑스)
				
		elif 시작(",사다리타기"):
			m = ' '.join(m.split(' ')[1:])
			if len(m.split()) != 2:
				await message.channel.send("```yaml\nx : 2~17\ny : 1~50```") ; return
			Sx = int(m.split()[0])
			Sy = int(m.split()[1])
			if (Sx < 2) or (Sy < 1) or (Sx > 17) or (Sy > 50):
				await message.channel.send("```yaml\nx : 2~17\ny : 1~50```") ; return
			#틀
			Slist = []
			for i in range(Sy):
				Slist.append([])
				for j in range(Sx):
					Slist[i].append(None)
			#넣
			for i in range(Sy):
				Smix = random.randint(0, Sx-2)
				for j in range(Sx):
					if j == Smix:
						Slist[i][j] = 사달["오"] # 오른쪽
					elif j == Smix + 1:
						Slist[i][j] = 사달["왼"] # 왼쪽
					else:
						Slist[i][j] = 사달["아"] # 아래
			
			#보
			f = ""
			for i in Slist:
				for j in i:
					f += j
				f += '\n'
				
			for i in f.split():
				await asyncio.sleep(1.0)
				await message.channel.send(i+빈공)
			await message.channel.send(f"{Sx} * {Sy}")
				
		elif 시작(",ㅅ"):
			await message.channel.send(message.author)
			ghkrfbf = []
			ghkrfbf += [1]*4930
			ghkrfbf += [2]*8451
			ghkrfbf += [3]*11972
			ghkrfbf += [4]*17606
			ghkrfbf += [5]*22535
			ghkrfbf += [6]*34507
			msg = await message.channel.send(슬롯[0]*3)
			await asyncio.sleep(1.0)
			a = [random.choice(ghkrfbf), random.choice(ghkrfbf), random.choice(ghkrfbf)]
			await msg.edit(content = 슬롯[a[0]] + 슬롯[a[1]] + 슬롯[a[2]])
			
			a.sort()
			a = tuple(a)
			if a in [(1,1,1) , (2,2,2) , (3,3,3)]:
				await message.channel.send("**잭팟!**")
			if a in [(1,1,2) , (1,1,3) , (1,2,2) , (2,2,3) , (1,3,3) , (2,3,3)]:
				await message.channel.send("**빅윈!**")
			if a in [(1,2,3)]:
				await message.channel.send("~~**유사잭팟!**~~")

		
		elif 시작(",ㄹ"):
			msg = await message.channel.send(message.author)
			ghkrfbf = []
			ghkrfbf += [1]*4930
			ghkrfbf += [2]*8451
			ghkrfbf += [3]*11972
			ghkrfbf += [4]*17606
			ghkrfbf += [5]*22535
			ghkrfbf += [6]*34507
			await msg.edit(content = str(message.author) + "\n" + 슬롯[0]*3)
			await asyncio.sleep(1.0)
			a = [random.choice(ghkrfbf), random.choice(ghkrfbf), random.choice(ghkrfbf)]
			await msg.edit(content = str(message.author) + "\n" + 슬롯[a[0]] + 슬롯[a[1]] + 슬롯[a[2]])
			
			a.sort()
			a = tuple(a)
			if a in [(1,1,1) , (2,2,2) , (3,3,3)]:
				await msg.edit(content = msg.content + "\n" + "**잭팟!**")
			if a in [(1,1,2) , (1,1,3) , (1,2,2) , (2,2,3) , (1,3,3) , (2,3,3)]:
				await msg.edit(content = msg.content + "\n" + "**빅윈!**")
			if a in [(1,2,3)]:
				await msg.edit(content = msg.content + "\n" + "~~**유사잭팟!**~~")

		elif 시작(",테스트") and 관리():
			pass

		elif 시작(",코드") and 관리():
			m = ' '.join(m.split(' ')[1:])
			if '\n' in m:
				exec('global 출력\n' + '\n'.join(m.split('\n')[:-1]) + '\n출력=' + m.split('\n')[-1])
				outputmsg = str(출력)
			else:
				outputmsg = str(eval(m))

			await message.channel.send(outputmsg[:2000-3]+'...' if len(outputmsg) > 2000 else outputmsg)
		
		elif 시작(",계산"):
			m = ' '.join(m.split(' ')[1:])
			if m == "목록":
				await message.channel.send("목록:\n```\n1 일 하나 2 이 둘 3 삼 셋 4 사 넷 5 오 다섯 6 육 여섯 7 칠 일곱 8 팔 여덟 9 구 아홉 0 영 . 점 + ＋ 더하기 - － 빼기 * × 곱하기 / ÷ 나누기 ^ 제곱 % 나머지 ( ) π 파이 원주율 √ 루트\n```")
				return
			
			f = ''
			for i in m:
				if i in '1일하나2이둘3삼셋4사넷5오다섯6육여섯7칠일곱8팔여덟9구아홉0영.점+＋더하기-－빼기*×곱하기/÷나누기^제곱%나머지()π파이원주율√루트':
					f += i

			f = f.replace("π", "math.pi")
			f = f.replace("파이", "math.pi")
			f = f.replace("원주율", "math.pi")
			f = f.replace("√", "math.sqrt")
			f = f.replace("루트", "math.sqrt")
			f = f.replace("일", "1")
			f = f.replace("하나", "1")
			f = f.replace("이", "2")
			f = f.replace("둘", "2")
			f = f.replace("삼", "3")
			f = f.replace("셋", "3")
			f = f.replace("사", "4")
			f = f.replace("넷", "4")
			f = f.replace("오", "5")
			f = f.replace("다섯", "5")
			f = f.replace("육", "6")
			f = f.replace("여섯", "6")
			f = f.replace("칠", "7")
			f = f.replace("일곱", "7")
			f = f.replace("팔", "8")
			f = f.replace("여덟", "8")
			f = f.replace("구", "9")
			f = f.replace("아홉", "9")
			f = f.replace("영", "0")
			f = f.replace("더하기", "+")
			f = f.replace("＋", "+")
			f = f.replace("빼기", "-")
			f = f.replace("－", "-")
			f = f.replace("곱하기", "*")
			f = f.replace("×", "*")
			f = f.replace("나누기", "/")
			f = f.replace("÷", "/")
			f = f.replace("제곱", "**")
			f = f.replace("^", "**")
			f = f.replace("나머지", "%")
			
			await message.channel.send(eval(f))










		if message.guild is None:
			return
		if message.guild.id != 766932314973929522:
			return
		m = message.content
		
		Ranks_10 = (766937626862682116, 766937654481780736, 766937674124623882, 766937691643183105, 766937708387631104, 766937752767037440)
		Ranks_01 = (766937776733159424, 766937795330703390, 766937812620017665, 766937834522411028, 766938115112697866, 766938128673144833, 766938145773060096, 766938159208071188, 766938180409753601, 766938192661184522)
		Tears = ('아톰', '몰레큘', '셀', '슈퍼 셀', '하이퍼 셀', '워터', '클린 워터', '아이스', '클린 아이스', '하드 아이스', '소일', '샌드', '우드', '페이퍼', '글래스', '클리어 글래스', '미러', '클리어 미러', '스톤', '하드 스톤', '아이언', '하드 아이언', '브론즈', '클리어 브론즈', '브론즈 메달', '실버', '클리어 실버', '실버 메달', '골드', '클리어 골드', '골드 메달', '아메티스트(자수정)', '크리스탈', '클리어 크리스탈', '블랙 크리스탈', '다이아몬드', '블랙 다이아몬드', '아다만티움', '사파이어', '에메랄드', '루비', '우루', '비브라늄', '클래식', '프리미엄', '딜럭스', '익스트림', '플래티넘', '미스틱', '챌린저', '마스터', '그랜드', '챔피언', '레전드')
		Agains_10 = ('환생 횟수 : 0', '환생 횟수 : 1', '환생 횟수 : 2', '환생 횟수 : 3', '환생 횟수 : 4', '환생 횟수 : 5')
		Agains_01 = ('0회', '1회', '2회', '3회', '4회', '5회', '6회', '7회', '8회', '9회')
		God1 = ('초', '중', '고', '하', '상', '-', '+')
		God2 = ('', '초하-', '초하', '초하+', '초-', '초', '초+', '초상-', '초상', '초상+', '중하-', '중하', '중하+', '중-', '중', '중+', '중상-', '중상', '중상+', '고하-', '고하', '고하+', '고-', '고', '고+', '고상-', '고상', '고상+', '초고-', '초고', '초고+')
		God_Agains_10 = ('신급 환생 횟수 : 0', '신급 환생 횟수 : 1', '신급 환생 횟수 : 2', '신급 환생 횟수 : 3', '신급 환생 횟수 : 4', '신급 환생 횟수 : 5')
		God_Agains_01 = ('0회.', '1회.', '2회.', '3회.', '4회.', '5회.', '6회.', '7회.', '8회.', '9회.')
		
		mentions = {
			'시인': '<@!647001590766632966>',
			'둔늑': '<@!544076137593176120>',
			'민망': '<@!693386027036835912>',
			'감자': '<@!526889025894875158>',
			}
		
		for nickname in mentions:
			if m == nickname:
				ping = await message.channel.send(f"{message.author} : {mentions[nickname]}")
				await asyncio.sleep(1.0)
				await ping.delete()
				await message.delete()
				return
			
		if 시작(",피버") and message.author.id == 647001590766632966: # 생강 피버타임
			global 피버
			피버 = not 피버
			if 피버:
				await message.channel.send("피버타임이 **켜**졌습니다")
			else:
				await message.channel.send("피버타임이 **꺼**졌습니다")

		elif (시작(",+") or 시작(",-")) and message.author.id == 647001590766632966: # 생강 + 또는 -
			q=m.split()
			money = int(q[0][1:])
			users = []
			for i in q[1:]:
				users.append(await message.guild.fetch_member(int(i[-18:] if i[-1] in "1234567890" else i[-19:-1])))
			#유저가 가지고 있는 역할의 이름 찾기
			for user in users:
				userRank = 0
				
				userGod = ''
				for i in God1:
					if i in [i.name for i in user.roles]:
						userGod += i
				try:
					userGod = God2.index(userGod)
				except:
					userGod = 0
				
				for i in range(len(Ranks_10)):
					if Ranks_10[i] in [i.id for i in user.roles]:
						userRank += i*10 ; break
				else:
					await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return
				for i in range(len(Ranks_01)):
					if Ranks_01[i] in [i.id for i in user.roles]:
						userRank += i ; break
				else:
					await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return

				for i in range(len(Tears)):
					if Tears[i] in [i.name for i in user.roles]:
						userTear = i ; break
				else:
					await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return

				userAgain = 0
				for i in range(len(Agains_10)):
					if Agains_10[i] in [i.name for i in user.roles]:
						userAgain += i*10 ; break
				else:
					userAgain += 0*10

				for i in range(len(Agains_01)):
					if Agains_01[i] in [i.name for i in user.roles]:
						userAgain += i ; break
				else:
					userAgain += 0
					
				userGodAgain = 0
				for i in range(len(God_Agains_10)):
					if God_Agains_10[i] in [i.id for i in user.roles]:
						userGodAgain += i*10 ; break
				for i in range(len(God_Agains_01)):
					if God_Agains_01[i] in [i.id for i in user.roles]:
						userGodAgain += i ; break

				#역할제거
				for i in user.roles:
					if i.id in Ranks_10 or \
					   i.id in Ranks_01 or \
					   i.name in Tears or \
					   i.name in Agains_10 or \
					   i.name in Agains_01 or \
					   i.name in God2 or \
					   i.name in God_Agains_10 or \
					   i.name in God_Agains_01:
						await user.remove_roles(i)
				
				#유저랭크 계산
				userTotalRank = 0
				userTotalRank += userRank
				userTotalRank += userTear*50
				userTotalRank += userAgain*2700
				userTotalRank += userGod*81000
				userTotalRank += userGodAgain*4050000
				userTotalRank += money
				
				
				#신급환생적용
				await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_10[(userTotalRank//4050000) // 10]))
				await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_01[(userTotalRank//4050000) %  10]))
				userTotalRank %= 4050000
				#신급적용
				for i in God2[userTotalRank // 81000]:
					await user.add_roles(discord.utils.get(message.guild.roles, name=i))
				userTotalRank %= 81000
				#환생횟수 적용
				await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_10[(userTotalRank//2700) // 10]))
				await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_01[(userTotalRank//2700) %  10]))
				userTotalRank %= 2700
				#티어 적용 (0이어도 0번째(아톰))
				await user.add_roles(discord.utils.get(message.guild.roles, name=Tears[userTotalRank//50]))
				userTotalRank %= 50
				#랭크 적용 (0이어도 0번째(L))
				await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_10[userTotalRank // 10]))
				await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_01[userTotalRank %  10]))
			await message.add_reaction(동글)
		
		elif message.channel.id in (766932314973929527, 783516524685688842): # 랭크업 가능한 채널일경우
			tryRank = False # 기본값

			if 시작("ㅇ"):
				tryRank = [1,1,0,0,0,0,0,0,0,0]
			if 시작("ㄱ"):
				if 시간()[5:7] == "02" and 시간()[8:10] == "14" or\
				   시간()[5:7] == "04" and 시간()[8:10] == "15" or\
				   시간()[5:7] == "05" and 시간()[8:10] == "05" or\
				   시간()[5:7] == "05" and 시간()[8:10] == "08" or\
				   시간()[5:7] == "06" and 시간()[8:10] == "06" or\
				   시간()[5:7] == "09" and 시간()[8:10] == "01" or\
				   시간()[5:7] == "11" and 시간()[8:10] == "15" or\
				   시간()[5:7] == "12" and 시간()[8:10] == "01" or\
				   시간()[5:7] == "12" and 시간()[8:10] == "25":
					tryRank = [1,1,1,0,0,0,0,0,0,0]
			if 시작("ㅅ"):
				if 시간()[5:7] == "03" and 시간()[8:10] == "01" or\
				   시간()[5:7] == "07" and 시간()[8:10] == "17" or\
				   시간()[5:7] == "08" and 시간()[8:10] == "15" or\
				   시간()[5:7] == "10" and 시간()[8:10] == "03" or\
				   시간()[5:7] == "10" and 시간()[8:10] == "09":
					tryRank = [1,1,1,1,0,0,0,0,0,0]
			if 시작("ㅌ"):
				if 시간()[5:7] == "01" and 시간()[8:10] == "01" or\
				   시간()[5:7] == "08" and 시간()[8:10] == "30" or\
				   시간()[5:7] == "10" and 시간()[8:10] == "09" or\
				   시간()[5:7] == "12" and 시간()[8:10] == "04" or\
				   not "아래는 설날" or\
				   시간()[2:4] == "20" and 시간()[5:7] == "01" and 시간()[8:10] == "25" or\
				   시간()[2:4] == "21" and 시간()[5:7] == "02" and 시간()[8:10] == "12" or\
				   시간()[2:4] == "22" and 시간()[5:7] == "02" and 시간()[8:10] == "01" or\
				   시간()[2:4] == "23" and 시간()[5:7] == "01" and 시간()[8:10] == "22" or\
				   시간()[2:4] == "24" and 시간()[5:7] == "02" and 시간()[8:10] == "10" or\
				   시간()[2:4] == "25" and 시간()[5:7] == "01" and 시간()[8:10] == "29" or\
				   시간()[2:4] == "26" and 시간()[5:7] == "02" and 시간()[8:10] == "17" or\
				   시간()[2:4] == "27" and 시간()[5:7] == "02" and 시간()[8:10] == "07" or\
				   시간()[2:4] == "28" and 시간()[5:7] == "01" and 시간()[8:10] == "27" or\
				   시간()[2:4] == "29" and 시간()[5:7] == "02" and 시간()[8:10] == "13" or\
				   시간()[2:4] == "30" and 시간()[5:7] == "02" and 시간()[8:10] == "03" or\
				   not "아래는 추석" or\
				   시간()[2:4] == "20" and 시간()[5:7] == "10" and 시간()[8:10] == "01" or\
				   시간()[2:4] == "21" and 시간()[5:7] == "09" and 시간()[8:10] == "21" or\
				   시간()[2:4] == "22" and 시간()[5:7] == "09" and 시간()[8:10] == "10" or\
				   시간()[2:4] == "23" and 시간()[5:7] == "09" and 시간()[8:10] == "29" or\
				   시간()[2:4] == "24" and 시간()[5:7] == "09" and 시간()[8:10] == "17" or\
				   시간()[2:4] == "25" and 시간()[5:7] == "10" and 시간()[8:10] == "06" or\
				   시간()[2:4] == "26" and 시간()[5:7] == "09" and 시간()[8:10] == "25" or\
				   시간()[2:4] == "27" and 시간()[5:7] == "09" and 시간()[8:10] == "15" or\
				   시간()[2:4] == "28" and 시간()[5:7] == "10" and 시간()[8:10] == "03" or\
				   시간()[2:4] == "29" and 시간()[5:7] == "09" and 시간()[8:10] == "22" or\
				   시간()[2:4] == "30" and 시간()[5:7] == "09" and 시간()[8:10] == "12":
					tryRank = [1,1,1,1,1,0,0,0,0,0]
			if 시작("ㅊ"):
				if 시간()[5:7] == "01" and 시간()[8:10] == "26":
					tryRank = [1,1,1,1,1,1,0,0,0,0]
			if 시작("ㄹ"):
				if discord.utils.get(message.guild.roles, name="랭커") in message.author.roles:
					tryRank = [1,1,1,0,0,0,0,0,0,0]
			if 시작("ㅍ"):
				if discord.utils.get(message.guild.roles, name="SIP") in message.author.roles or\
				   discord.utils.get(message.guild.roles, name="HIP") in message.author.roles or\
				   discord.utils.get(message.guild.roles, name="UIP") in message.author.roles or\
				   discord.utils.get(message.guild.roles, name="MIP") in message.author.roles:
					tryRank = [1,1,1,1,0,0,0,0,0,0]
			if 시작("ㅂ"):
				if 피버:
					tryRank = [1,1,1,0,0,0,0,0,0,0]

			if not tryRank:
				return
			if not random.choice(tryRank):
				await message.channel.send("랭크업에 실패하였습니다...")
				return

			#랭크업했을경우
			money = 1
			user = message.author

			userRank = 0

			userGod = ''
			for i in God1:
				if i in [i.name for i in user.roles]:
					userGod += i
			try:
				userGod = God2.index(userGod)
			except:
				userGod = 0

			for i in range(len(Ranks_10)):
				if Ranks_10[i] in [i.id for i in user.roles]:
					userRank += i*10 ; break
			else:
				await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return
			for i in range(len(Ranks_01)):
				if Ranks_01[i] in [i.id for i in user.roles]:
					userRank += i ; break
			else:
				await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return
			
			for i in range(len(Tears)):
				if Tears[i] in [i.name for i in user.roles]:
					userTear = i ; break
			else:
				await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return
			
			userAgain = 0
			for i in range(len(Agains_10)):
				if Agains_10[i] in [i.name for i in user.roles]:
					userAgain += i*10 ; break
			else:
				userAgain += 0*10
				
			for i in range(len(Agains_01)):
				if Agains_01[i] in [i.name for i in user.roles]:
					userAgain += i ; break
			else:
				userAgain += 0

			userGodAgain = 0
			for i in range(len(God_Agains_10)):
				if God_Agains_10[i] in [i.id for i in user.roles]:
					userGodAgain += i*10 ; break
			for i in range(len(God_Agains_01)):
				if God_Agains_01[i] in [i.id for i in user.roles]:
					userGodAgain += i ; break
			
			#역할제거
			for i in user.roles:
				if i.id in Ranks_10 or \
				   i.id in Ranks_01 or \
				   i.name in Tears or \
				   i.name in Agains_10 or \
				   i.name in Agains_01 or \
				   i.name in God2 or \
				   i.name in God_Agains_10 or \
				   i.name in God_Agains_01:
					await user.remove_roles(i)

			#유저랭크 계산
			userTotalRank = 0
			userTotalRank += userRank
			userTotalRank += userTear*50
			userTotalRank += userAgain*2700
			userTotalRank += userGod*81000
			userTotalRank += userGodAgain*4050000
			userTotalRank += money
			
			#신급환생적용
			await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_10[(userTotalRank//4050000) // 10]))
			await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_01[(userTotalRank//4050000) %  10]))
			userTotalRank %= 4050000
			#신급적용
			for i in God2[userTotalRank // 81000]:
				await user.add_roles(discord.utils.get(message.guild.roles, name=i))
			userTotalRank %= 81000
			#환생횟수 적용
			await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_10[(userTotalRank//2700) // 10]))
			await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_01[(userTotalRank//2700) %  10]))
			userTotalRank %= 2700
			#티어 적용 (0이어도 0번째(아톰))
			await user.add_roles(discord.utils.get(message.guild.roles, name=Tears[userTotalRank//50]))
			userTotalRank %= 50
			#랭크 적용 (0이어도 0번째(L))
			await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_10[userTotalRank // 10]))
			await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_01[userTotalRank %  10]))
			
			await message.channel.send("랭크업에 성공하였습니다!")
			await message.add_reaction(체크)
			
		elif message.channel.id == 783507226983399504: #이벤트채널일경우
			global note2
			if True:
				if note2 is None:
					note2 = await client.get_channel(783502506470146049).fetch_message(806721717551497237)
			if 시작("참가") or 시작("등록"):
				if "<@"+str(message.author.id)+">" in note2.content:
					await message.channel.send("이미 참가(등록)되었습니다")
					return
				else:
					await note2.edit(content=f"{note2.content}\n<@{message.author.id}> : 0")
					await message.channel.send("완료되었습니다")

			elif 시작("ㅇ"):
				user = f"<@{message.author.id}>"
				
				if user not in note2.content:
					await message.channel.send("등록되어있지 않은 유저입니다. `등록` 또는 `참가`를을 입력하여 등록해보세요")
					return
				
				if not random.choice([1,1,0,0,0,0,0,0,0,0]):
					await message.channel.send("랭크업에 실패하였습니다...")
					return

				note2c = note2.content.split("\n")[1:]
				
				for i in range(len(note2c)):
					if note2c[i].startswith(user):
						note2n = i
				note2c[note2n] = note2c[note2n][:24] + str(int(note2c[note2n][24:])+1)
				
				note2m = "유저 : 성공 횟수\n" + "\n".join(note2c)
				await note2.edit(content = note2m)
				
				
				money = 1
				user = message.author

				userRank = 0

				userGod = ''
				for i in God1:
					if i in [i.name for i in user.roles]:
						userGod += i
				try:
					userGod = God2.index(userGod)
				except:
					userGod = 0

				for i in range(len(Ranks_10)):
					if Ranks_10[i] in [i.id for i in user.roles]:
						userRank += i*10 ; break
				else:
					await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return
				for i in range(len(Ranks_01)):
					if Ranks_01[i] in [i.id for i in user.roles]:
						userRank += i ; break
				else:
					await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return

				for i in range(len(Tears)):
					if Tears[i] in [i.name for i in user.roles]:
						userTear = i ; break
				else:
					await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return

				userAgain = 0
				for i in range(len(Agains_10)):
					if Agains_10[i] in [i.name for i in user.roles]:
						userAgain += i*10 ; break
				else:
					userAgain += 0*10

				for i in range(len(Agains_01)):
					if Agains_01[i] in [i.name for i in user.roles]:
						userAgain += i ; break
				else:
					userAgain += 0

				userGodAgain = 0
				for i in range(len(God_Agains_10)):
					if God_Agains_10[i] in [i.id for i in user.roles]:
						userGodAgain += i*10 ; break
				for i in range(len(God_Agains_01)):
					if God_Agains_01[i] in [i.id for i in user.roles]:
						userGodAgain += i ; break

				#역할제거
				for i in user.roles:
					if i.id in Ranks_10 or \
					   i.id in Ranks_01 or \
					   i.name in Tears or \
					   i.name in Agains_10 or \
					   i.name in Agains_01 or \
					   i.name in God2 or \
					   i.name in God_Agains_10 or \
					   i.name in God_Agains_01:
						await user.remove_roles(i)

				#유저랭크 계산
				userTotalRank = 0
				userTotalRank += userRank
				userTotalRank += userTear*50
				userTotalRank += userAgain*2700
				userTotalRank += userGod*81000
				userTotalRank += userGodAgain*4050000
				userTotalRank += money

				#신급환생적용
				await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_10[(userTotalRank//4050000) // 10]))
				await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_01[(userTotalRank//4050000) %  10]))
				userTotalRank %= 4050000
				#신급적용
				for i in God2[userTotalRank // 81000]:
					await user.add_roles(discord.utils.get(message.guild.roles, name=i))
				userTotalRank %= 81000
				#환생횟수 적용
				await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_10[(userTotalRank//2700) // 10]))
				await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_01[(userTotalRank//2700) %  10]))
				userTotalRank %= 2700
				#티어 적용 (0이어도 0번째(아톰))
				await user.add_roles(discord.utils.get(message.guild.roles, name=Tears[userTotalRank//50]))
				userTotalRank %= 50
				#랭크 적용 (0이어도 0번째(L))
				await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_10[userTotalRank // 10]))
				await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_01[userTotalRank %  10]))
				
				await message.channel.send("랭크업에 성공하였습니다!")
				await message.add_reaction(체크)

		elif message.channel.id == 784228694940057640 or message.channel.id == 794146499034480661 or message.channel.id == 787976375301701692: # 도박채널 또는 도박2 채널 또는 ㅇㅇ(테스트채널)일경우
			#도박 아니면 제거
			if 시작("ㄷ"):
				dp = random.choice([2, 2, 1.5, 1.5, 1.5, 1.5, 1, 1, 0.5, 0.5])
			elif 시작("ㅅ"):
				dp = random.choice([2, 2, 2, 1.5, 1.5, 1.5, 1.5, 1, 1, 0.5])
			else:
				return

			#현재 얼마있는지
			user = message.author

			userRank = 0

			userGod = ''
			for i in God1:
				if i in [i.name for i in user.roles]:
					userGod += i
			try:
				userGod = God2.index(userGod)
			except:
				userGod = 0

			for i in range(len(Ranks_10)):
				if Ranks_10[i] in [i.id for i in user.roles]:
					userRank += i*10 ; break
			else:
				await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return
			for i in range(len(Ranks_01)):
				if Ranks_01[i] in [i.id for i in user.roles]:
					userRank += i ; break
			else:
				await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return
			
			for i in range(len(Tears)):
				if Tears[i] in [i.name for i in user.roles]:
					userTear = i ; break
			else:
				await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return
			
			userAgain = 0
			for i in range(len(Agains_10)):
				if Agains_10[i] in [i.name for i in user.roles]:
					userAgain += i*10 ; break
			else:
				userAgain += 0*10
				
			for i in range(len(Agains_01)):
				if Agains_01[i] in [i.name for i in user.roles]:
					userAgain += i ; break
			else:
				userAgain += 0
				
			userGodAgain = 0
			for i in range(len(God_Agains_10)):
				if God_Agains_10[i] in [i.id for i in user.roles]:
					userGodAgain += i*10 ; break
			for i in range(len(God_Agains_01)):
				if God_Agains_01[i] in [i.id for i in user.roles]:
					userGodAgain += i ; break
			
			#유저랭크 계산
			userTotalRank = 0
			userTotalRank += userRank
			userTotalRank += userTear*50
			userTotalRank += userAgain*2700
			userTotalRank += userGod*81000
			userTotalRank += userGodAgain*4050000
			
			#얼마나 걸었는지
			if message.content.split()[1] == "최대" or message.content.split()[1] == "chleo":
				if 시작("ㄷ"):
					dmoney = 100+userAgain*50
				else:
					dmoney = 100+userAgain*100
				await message.channel.send(f"{dmoney}만큼의 돈을 겁니다...")
			else:
				dmoney = int(message.content.split()[1])
			
			#건 돈이 10~(환생횟수+1)*100 아닐경우 제거
			if 시작("ㄷ"):
				if not 10 <= dmoney <= 100+userAgain*50:
					await message.channel.send(f"`10~100+(환생횟수)*50 (10~{100+userAgain*50})` 만 걸수 있습니다.")
					return
			elif 시작("ㅅ"):
				if not 10 <= dmoney <= 100+userAgain*100:
					await message.channel.send(f"`10~100+(환생횟수)*100 (10~{100+userAgain*100})` 만 걸수 있습니다.")
					return

			#가진돈보다 건돈이 많다면 알림
			if dmoney > userTotalRank:
				await message.channel.send("랭크가 부족합니다.")
				return
			if 시작("ㅅ"):
				if userTotalRank < 81000:
					await message.channel.send("초하-급신부터 사용할수 있습니다.")
					return

			#도박을 해봄
			await message.channel.send(f"{dp}배")
			if dp == 0.5 and userTotalRank >= 20:
				mymsg2 = await message.channel.send(f"실드를 구매 및 사용하시겠습니까?\n실드 1개당 20랭크, 20%입니다.\n0️⃣ `100% {round(-dmoney+dmoney*dp)}`\n1️⃣ `20% {round(-20)}, 80% {round(-20-dmoney+dmoney*dp)}`\n2️⃣ `40% {round(-40)}, 60% {round(-40-dmoney+dmoney*dp)}`\n3️⃣ `60% {round(-60)}, 40% {round(-60-dmoney+dmoney*dp)}`\n4️⃣ `80% {round(-80)}, 20% {round(-80-dmoney+dmoney*dp)}`\n5️⃣ `100% {round(-100)}`")
				await mymsg2.add_reaction("0️⃣");time.sleep(0.5)
				await mymsg2.add_reaction("1️⃣");time.sleep(0.5)
				await mymsg2.add_reaction("2️⃣");time.sleep(0.5)
				await mymsg2.add_reaction("3️⃣");time.sleep(0.5)
				await mymsg2.add_reaction("4️⃣");time.sleep(0.5)
				await mymsg2.add_reaction("5️⃣")
				try:
					reaction, temp = await client.wait_for('reaction_add', timeout=60.0, check=체크2)
					reaction = str(reaction.emoji)
				except:
					reaction = "0️⃣"
				if reaction == "0️⃣":
					money = round(-dmoney+dmoney*dp)
				elif reaction == "1️⃣":
					if random.choice([1,0,0,0,0]):
						money = round(-20)
						await message.channel.send(f"실드 사용에 성공함 ({money})")
					else:
						money = round(-20-dmoney+dmoney*dp)
						await message.channel.send(f"실드 사용에 실패함 ({money})")

					await client.get_channel(783513080352079872).send(f"{message.author}님이 실드를 구매함")

				elif reaction == "2️⃣":
					if random.choice([1,1,0,0,0]):
						money = round(-40)
						await message.channel.send(f"실드 사용에 성공함 ({money})")
					else:
						money = round(-40-dmoney+dmoney*dp)
						await message.channel.send(f"실드 사용에 실패함 ({money})")

					await client.get_channel(783513080352079872).send(f"{message.author}님이 실드를 구매함")

				elif reaction == "3️⃣":
					if random.choice([1,1,1,0,0]):
						money = round(-60)
						await message.channel.send(f"실드 사용에 성공함 ({money})")
					else:
						money = round(-60-dmoney+dmoney*dp)
						await message.channel.send(f"실드 사용에 실패함 ({money})")

					await client.get_channel(783513080352079872).send(f"{message.author}님이 실드를 구매함")

				elif reaction == "4️⃣":
					if random.choice([1,1,1,1,0]):
						money = round(-80)
						await message.channel.send(f"실드 사용에 성공함 ({money})")
					else:
						money = round(-80-dmoney+dmoney*dp)
						await message.channel.send(f"실드 사용에 실패함 ({money})")

					await client.get_channel(783513080352079872).send(f"{message.author}님이 실드를 구매함")

				elif reaction == "5️⃣":
					money = round(-100)
					await message.channel.send(f"실드 사용에 성공함 ({money})")

					await client.get_channel(783513080352079872).send(f"{message.author}님이 실드를 구매함")
			else:
				money = round(-dmoney+dmoney*dp)
			await client.get_channel(762916201654386701).send(f"{userRank}, {userTear}, {userAgain}, {userGod}; {userTotalRank}+{money} {message.jump_url}")
			#랭크적용...
			userTotalRank += money
			if userTotalRank < 0:
				await message.channel.send("이런! 랭크가 부족합니다.")
				return
			
			#역할제거
			for i in user.roles:
				if i.id in Ranks_10 or \
				   i.id in Ranks_01 or \
				   i.name in Tears or \
				   i.name in Agains_10 or \
				   i.name in Agains_01 or \
				   i.name in God2 or \
				   i.name in God_Agains_10 or \
				   i.name in God_Agains_01:
					await user.remove_roles(i)
			await client.get_channel(762916201654386701).send("역할을 제거함")
			
			#신급환생적용
			await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_10[(userTotalRank//4050000) // 10]))
			await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_01[(userTotalRank//4050000) %  10]))
			await client.get_channel(762916201654386701).send(f"{userTotalRank}에서 /4050000, 신급을 {userTotalRank//4050000} 로 적용함, -> {userTotalRank%4050000}")
			userTotalRank %= 4050000
			#신급적용
			for i in God2[userTotalRank // 81000]:
				await user.add_roles(discord.utils.get(message.guild.roles, name=i))
			await client.get_channel(762916201654386701).send(f"{userTotalRank}에서 /81000, 신급을 {userTotalRank//81000} 로 적용함, -> {userTotalRank%81000}")
			userTotalRank %= 81000
			#환생횟수 적용
			await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_10[(userTotalRank//2700) // 10]))
			await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_01[(userTotalRank//2700) %  10]))
			await client.get_channel(762916201654386701).send(f"{userTotalRank}에서 /2700, 환생 횟수를 {userTotalRank//2700} 로 적용함, -> {userTotalRank%2700}")
			userTotalRank %= 2700
			#티어 적용 (0이어도 0번째(아톰))
			await user.add_roles(discord.utils.get(message.guild.roles, name=Tears[userTotalRank//50]))
			await client.get_channel(762916201654386701).send(f"{userTotalRank}에서 /50, 티어를 {userTotalRank//50} 로 적용함, -> {userTotalRank%50}")
			userTotalRank %= 50
			#랭크 적용 (0이어도 0번째(L))
			await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_10[userTotalRank // 10]))
			await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_01[userTotalRank %  10]))
			await client.get_channel(762916201654386701).send(f"{userTotalRank}에서 /1, 랭크를 {userTotalRank//1} 로 적용함, -> {userTotalRank%1}")
			
			await message.add_reaction(체크)

		elif 시작(",일급") and message.author.id == 647001590766632966: # 생강
			m = ' '.join(m.split(' ')[1:])
			try:
				a = int(m)
			except:
				a = 1
			users = [
				526889025894875158, #감자
				693386027036835912, #민트망고
				544076137593176120, #둔난늑대
				506786900195934218, #자감
				681403207620100135, #푺으
				]

			ilGup = {
				'인턴'   : 10,
				'과장'   : 20,
				'부장'   : 30,
				'사장'   : 50,
				'부회장' : 100,
				}

			for l in users:
				user = await message.guild.fetch_member(l)

				##
				for i in ilGup:
					if i in [i.name for i in user.roles]:
						money = ilGup[i] ; break
				##
				userRank = 0
				
				userGod = ''
				for i in God1:
					if i in [i.name for i in user.roles]:
						userGod += i
				try:
					userGod = God2.index(userGod)
				except:
					userGod = 0
				
				for i in range(len(Ranks_10)):
					if Ranks_10[i] in [i.id for i in user.roles]:
						userRank += i*10 ; break
				else:
					await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return
				for i in range(len(Ranks_01)):
					if Ranks_01[i] in [i.id for i in user.roles]:
						userRank += i ; break
				else:
					await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return

				for i in range(len(Tears)):
					if Tears[i] in [i.name for i in user.roles]:
						userTear = i ; break
				else:
					await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; return

				userAgain = 0
				for i in range(len(Agains_10)):
					if Agains_10[i] in [i.name for i in user.roles]:
						userAgain += i*10 ; break
				else:
					userAgain += 0*10

				for i in range(len(Agains_01)):
					if Agains_01[i] in [i.name for i in user.roles]:
						userAgain += i ; break
				else:
					userAgain += 0
					
				userGodAgain = 0
				for i in range(len(God_Agains_10)):
					if God_Agains_10[i] in [i.id for i in user.roles]:
						userGodAgain += i*10 ; break
				for i in range(len(God_Agains_01)):
					if God_Agains_01[i] in [i.id for i in user.roles]:
						userGodAgain += i ; break

				#역할제거
				for i in user.roles:
					if i.id in Ranks_10 or \
					   i.id in Ranks_01 or \
					   i.name in Tears or \
					   i.name in Agains_10 or \
					   i.name in Agains_01 or \
					   i.name in God2 or \
					   i.name in God_Agains_10 or \
					   i.name in God_Agains_01:
						await user.remove_roles(i)

				#유저랭크 계산
				userTotalRank = 0
				userTotalRank += userRank
				userTotalRank += userTear*50
				userTotalRank += userAgain*2700
				userTotalRank += userGod*81000
				userTotalRank += userGodAgain*4050000
				userTotalRank += money*a
				
				#신급환생적용
				await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_10[(userTotalRank//4050000) // 10]))
				await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_01[(userTotalRank//4050000) %  10]))
				userTotalRank %= 4050000
				#신급적용
				for i in God2[userTotalRank // 81000]:
					await user.add_roles(discord.utils.get(message.guild.roles, name=i))
				userTotalRank %= 81000
				#환생횟수 적용
				await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_10[(userTotalRank//2700) // 10]))
				await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_01[(userTotalRank//2700) %  10]))
				userTotalRank %= 2700
				#티어 적용 (0이어도 0번째(아톰))
				await user.add_roles(discord.utils.get(message.guild.roles, name=Tears[userTotalRank//50]))
				userTotalRank %= 50
				#랭크 적용 (0이어도 0번째(L))
				await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_10[userTotalRank // 10]))
				await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_01[userTotalRank %  10]))
				
			await message.add_reaction(동글)
			
	except Exception as e:
		await message.add_reaction(엑스)
		await client.get_channel(762916201654386701).send(f"""
-----
{시간()}
<@526889025894875158>
에러
오류: {e}
링크: {message.jump_url}
서버: {message.guild} ({message.guild.id})
채널: {message.channel} ({message.channel.id})
보낸이: {message.author} ({message.author.id})
{message}
-----
""")

try:
	access_token = os.environ["BOR_TOKEN"]
except:
	f = open("token.txt", "r")
	access_token = f.read()
	f.close()
client.run(access_token)
