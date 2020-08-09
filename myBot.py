import discord, time, random, os, math
client = discord.Client()

버전 = 34
띵킹 = "🤔"
똥킹 = "<:thonking:732864307196592199>"
킹똥 = "<:gniknoht:733977049743753247>"
엑스 = "❌"
청소 = "🗑️"
BASE_CODE, CHO_CODE, JUNG_CODE, MAX_CODE = 44032, 588, 28, 55203
CHO_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
KORS = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ', '', ' ']
ENGS = ['r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'qt', 't', 'T', 'd', 'w', 'c', 'z', 'x', 'v', 'g', 'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l', '', ' ']
KOR_ENG_TABLE = dict(zip(KORS, ENGS))
ENG_KOR_TABLE = dict(zip(ENGS, KORS))

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
            if 번역(s)[0] in m:
                return 1
            if 번역(s)[1] in m:
                return 2
            return 0
        def 시작(s):
            if m.startswith(번역(s)[0]):
                return 1
            if m.startswith(번역(s)[1]):
                return 2
            return 0
        def 번역(s):
            return [영한(s), 한영(s)]
        def 영한(text):
            q = ''
            while text:
                if text[:2] in ENGS and len(text) > 1:
                    q += ENG_KOR_TABLE[text[:2]]
                    text = text[2:]
                elif text[:1] in ENGS:
                    q += ENG_KOR_TABLE[text[0]]
                    text = text[1:]
                else:
                    q += text[0]
                    text = text[1:]
            # 여기서부터 합치기
            w = ''
            while q:
                if q[0] in CHO_LIST:
                    if len(q) > 1:
                        if q[1] in JUNG_LIST:
                            if len(q) > 2:
                                if q[2] in JONG_LIST:
                                    if len(q) > 3:
                                        if q[2] in CHO_LIST and q[3] in JUNG_LIST:
                                            w += 조합(q[0], q[1], '')
                                            q = q[2:]
                                        else:
                                            w += 조합(q[0], q[1], q[2])
                                            q = q[3:]
                                    else:
                                        w += 조합(q[0], q[1], q[2])
                                        q = q[3:]
                                else:
                                    w += 조합(q[0], q[1], '')
                                    q = q[2:]
                            else:
                                w += 조합(q[0], q[1], '')
                                q = q[2:]
                        else:
                            w += q[0]
                            q = q[1:]
                    else:
                        w += q[0]
                        q = q[1:]
                else:
                    w += q[0]
                    q = q[1:]
            return w
        def 한영(text):
            res = ''
            for ch in text:
                spl = 분리(ch)
                for i in spl:
                    if i in KOR_ENG_TABLE:
                        res += KOR_ENG_TABLE[i]
                    else:
                        res += i
            return res
        def 조합(cho, jung, jong):
            res = BASE_CODE
            res += 0 if cho == '' else CHO_LIST.index(cho)  * CHO_CODE
            res += 0 if jung == '' else JUNG_LIST.index(jung) * JUNG_CODE
            res += 0 if jong == '' else JONG_LIST.index(jong)
            return chr(res)
        def 분리(kor):
            code = ord(kor) - BASE_CODE*2
            if BASE_CODE < code < MAX_CODE:
                q = [CHO_LIST[code // CHO_CODE], JUNG_LIST[(code % CHO_CODE) // JUNG_CODE], JONG_LIST[(code % CHO_CODE) % JUNG_CODE]]
                w = []
                for i in q:
                    if i == ' ':
                        i = ''
                    w += i
                return w
            if kor in CHO_LIST: return kor, '', ''
            if kor in JUNG_LIST: return '', kor, ''
            if kor in JONG_LIST: return '', '', kor
            return kor
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
        if 포함("띵킹") or 포함("띤킹") or 포함("흠터") or 포함(":소ㅑㅜㅏㅑㅜㅎ:") or 포함(띵킹):
            await message.add_reaction(띵킹)
        if 포함("똥킹") or 포함("똔킹") or 포함("ㅁㄴㅇㄹ") or 포함("??") or 포함(":쇄ㅜㅏㅑㅜㅎ:") or 포함(똥킹):
            await message.add_reaction(똥킹)
        if 포함("킹똥") or 포함("킹똔") or 포함(킹똥):
            await message.add_reaction(킹똥)
        if 포함("ㅘ") or 포함("와"):
            await message.channel.send("샌즈!")
        if 시작(","):
            m = m[1:]
            if 시작("도움"):
                embed = discord.Embed(title=킹똥+"도움말"+똥킹, color=0xffccff)
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
                i = 시작("계산")*3 # '계산'으로 시작 => i = 3 / 'rPtks'으로 시작 => i = 6
                q = m[i:] # 원래 식
                w = q[:] # 바뀔 식
                while True:
                    if '^' in w:
                        w = w.replace('^', '**')
                    elif '√(' in w:
                        w = w.replace('√(', 'math.sqrt(')
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
