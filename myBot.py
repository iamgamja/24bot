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
		def 포함(s):
			return s in m
		def 같다(s):
			return s == m
		if message.embeds:
			await message.add_reaction("<:thonking:732864307196592199>")
			time.sleep(0.5)
			await message.clear_reaction("<:thonking:732864307196592199>")
		elif 포함("띵킹") or 포함("Eldzld") or\
		포함("띤킹") or 포함("Elszld") or\
		포함("흠터") or 포함("gmaxj") or\
		포함(":소ㅑㅜㅏㅑㅜㅎ:"):
			await message.channel.send("🤔")
			await message.add_reaction("🤔")
		elif 포함("🤔") and not 같다("🤔"):
			await message.channel.send("🤔")
			await message.add_reaction("🤔")
		elif 같다("🤔"):
			await message.add_reaction("🤔")

		if 포함("똥킹") or 포함("Ehdzld") or\
		포함("똔킹") or 포함("Ehszld") or\
		포함("ㅁㄴㅇㄹ") or 포함("asdf") or\
		포함("??") or 포함(":쇄ㅜㅏㅑㅜㅎ:"):
			await message.channel.send("<:thonking:732864307196592199>")
			await message.add_reaction("<:thonking:732864307196592199>")
		elif 포함("<:thonking:732864307196592199>") and not 같다("<:thonking:732864307196592199>"):
			await message.channel.send("<:thonking:732864307196592199>")
			await message.add_reaction("<:thonking:732864307196592199>")
		elif 같다("<:thonking:732864307196592199>"):
			await message.add_reaction("<:thonking:732864307196592199>")
			
		if 포함("ㅘ!") or 포함("와!"):
			await message.channel.send("샌즈!")

		if m.startswith(","):
			m = m[1:]
			if m.startswith("도움") or m.startswith("ehdna"):
				embed = discord.Embed(title="<:gniknoht:733977049743753247>기타 도움말<:thonking:732864307196592199>", color=0x62c1cc)
				embed.add_field(name=",핑", value="으악 핑", inline=True)
				embed.add_field(name=",에블핑", value="으악 핑", inline=True)
				embed.add_field(name=",히어핑", value="으악 핑", inline=True)
				embed.add_field(name=",폭8", value="폭☆8", inline=True)
				embed.add_field(name=",계산 <식>", value="식을 계산합니다.", inline=False)
				embed.add_field(name=",가위바위보 <가위|바위|보>", value="가위바위보를 합니다", inline=False)
				await message.channel.send(embed=embed)
			
			elif m.startswith("핑") or m.startswith("vld"):
				firstTime = time.time()
				msg = await message.channel.send("으악 핑")
				lastTime = time.time()
				subTime = lastTime - firstTime
				await msg.delete()
				await message.channel.send(subTime)
			elif m.startswith("계산"):
				try:
					q = m[3:]
					w = str(eval(q))
					await message.channel.send(w)
				except Exception as e:
					await message.channel.send("오류: " + str(e))
			elif m.startswith("rPtks"):
				try:
					q = m[6:]
					w = str(eval(q))
					await message.channel.send(w)
				except Exception as e:
					await message.channel.send("오류: " + str(e))
			elif m.startswith("에블핑") or m.startswith("dpqmfvld"):
				await message.channel.send("@everyone")
			elif m.startswith("히어핑") or m.startswith("gldjvld"):
				await message.channel.send("@here")
			elif m.startswith("가위바위보"):
				w = m[6:]
				
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
			elif m.startswith("rkdnlqkdnlqh"):
				w = m[13:]
				
				if w == "rkdnl":
					e = 0
				elif w == "qkdnl":
					e = 1
				elif w == "qh":
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
			elif m.startswith("폭8") or m.startswith("vhf8"):
				await message.channel.send("https://cdn.discordapp.com/attachments/732870251351376033/737457954189738014/100.gif")
	except Exception as e:
		if str(e) != "404 Not Found (error code: 10008): Unknown Message":
			print("오류:", e)




access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
