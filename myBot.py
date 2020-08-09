import discord, time, random, os, math
client = discord.Client()

버전 = 25
띵킹 = "🤔"
똥킹 = "<:thonking:732864307196592199>"
킹똥 = "<:gniknoht:733977049743753247>"
엑스 = "❌"

@client.event
async def on_ready():
	# print('시작')
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))

@client.event
async def on_message(message):
	try:
		m = message.content
		# print(m)
		def 포함(s):
			return s in m
		def 같다(s):
			return s == m
		def 시작(s):
			return m.startswith(s)
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
				embed = discord.Embed(title=킹똥+"도움말"+똥킹, color=0xffccff)
				embed.add_field(name=",핑", value="으악 핑", inline=True)
				embed.add_field(name=",에블핑", value="으악 핑", inline=True)
				embed.add_field(name=",히어핑", value="으악 핑", inline=True)
				embed.add_field(name=",폭8", value="폭☆8", inline=False)
				embed.add_field(name=",계산 <식>", value="식을 계산합니다.", inline=False)
				embed.add_field(name=",버전", value="버전을 확인합니다.", inline=False)
				await message.channel.send(embed=embed)
			if 시작("핑") or 시작("vld"):
				await message.channel.send("으악 핑")
			if 시작("에블핑") or 시작("dpqmfvld"):
				await message.channel.send("||@everyone||")
				time.sleep(0.5)
				await message.channel.send("으악 핑")
			if 시작("히어핑") or 시작("gldjvld"):
				await message.channel.send("||@here||")
				time.sleep(0.5)
				await message.channel.send("으악 핑")
			if 시작("폭8") or 시작("vhr8"):
				await message.channel.send("https://cdn.discordapp.com/attachments/740144542753357845/740145588594540604/100.gif")
			if 시작("버전") or 시작("qjwjs"):
				await message.channel.send(버전)
			if 시작("계산") or 시작("rPtks"):
				if 시작("계산"):
					i = 3
				else:
					i = 6
				q = m[i:]
				while True:
					if '^' in q:
						q = q.replace('^', '**')
					elif '√(' in q:
						q = q.replace('√(', 'math.sqrt(')
					else:
						break
				w = str(eval(q))
				embed = discord.Embed(title=킹똥+"계산 결과"+똥킹, color=0xffccff)
				embed.add_field(name=q, value=w)
				await message.channel.send(embed=embed)
			
	except Exception as e:
		await message.add_reaction(엑스)
		await message.channel.send("오류: " + str(e))
		await client.get_channel(693705236220739594).send("오류: " + str(e))
	
access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
