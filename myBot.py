import discord, time, random
import os
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
		def vhgka(s):
			return s in m
		def rkxek(s):
			return s == m
		def tlwkr(s):
			return m.startswith(s)
		def tlfgod(n):
			with open("명령어", "r") as f:
				lines = f.read()
				start = lines.find("#" + str(n))
				end = lines.find("#" + str(n + 1))
				last = lines[start:end]
				exec(last)
		if message.embeds:
			tlfgod(1)
		elif vhgka("띵킹") or vhgka("Eldzld") or vhgka("띤킹") or vhgka("Elszld") or vhgka("흠터") or vhgka("gmaxj") or vhgka(":소ㅑㅜㅏㅑㅜㅎ:"):
			tlfgod(2)
			tlfgod(3)
		elif vhgka(Eldzld) and not rkxek(Eldzld):
			tlfgod(2)
			tlfgod(3)
		elif rkxek(Eldzld):
			tlfgod(3)
		if vhgka("똥킹") or vhgka("Ehdzld") or vhgka("똔킹") or vhgka("Ehszld") or vhgka("ㅁㄴㅇㄹ") or vhgka("asdf") or vhgka("??") or vhgka(":쇄ㅜㅏㅑㅜㅎ:"):
			tlfgod(4)
			tlfgod(5)
		elif vhgka(Ehdzld) and not rkxek(Ehdzld):
			tlfgod(4)
			tlfgod(5)
		elif rkxek(Ehdzld):
			tlfgod(5)
		if vhgka("ㅘ!") or vhgka("와!"):
			tlfgod(6)
		if tlwkr(","):
			m = m[1:]
			if tlwkr("도움") or tlwkr("ehdna"):
				tlfgod(7)
			elif tlwkr("핑") or tlwkr("vld"):
				tlfgod(8)
			elif tlwkr("계산") or tlwkr("rPtks"):
				tlfgod(9)
			elif tlwkr("에블핑") or tlwkr("dpqmfvld"):
				tlfgod(10)
			elif tlwkr("히어핑") or tlwkr("gldjvld"):
				tlfgod(11)
			elif tlwkr("가위바위보") or tlwkr("rkdnlqkdnlqh"):
				tlfgod(12)
			elif tlwkr("폭8") or tlwkr("vhf8"):
				tlfgod(13)
			elif tlwkr("테스트"):
				await message.channel.send("테스트성공!")
	except Exception as e:
		if str(e) != "404 Not Found (error code: 10008): Unknown Message":
			print("오류:", e)




access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
