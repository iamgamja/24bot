from imports import *

intents = discord.Intents.all()
client = discord.ext.commands.Bot(',', intents=intents)

async def log(*s, channel_id=762916201654386701):
    s = '\n'.join(s)
    
    print(s)
    if len(s) > 2000:
        await client.get_channel(channel_id).send(s[:2000])
        await log(s[2000:])
    else:
        await client.get_channel(channel_id).send(s)
    
@client.event
async def on_error(event, *args, **kwargs):
    await log('=====', '<@526889025894875158>, error!', event, args, kwargs, '=====')

@client.event
async def on_ready():
    print('시작')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))
    await log(f"{시간()}, <@526889025894875158>, 시작")
    #await log(A)
    DiscordComponents(client)
    # [무지개] 색
    def RGB2hex(rgb):
        r, g, b = rgb['R'], rgb['G'], rgb['B']
        
        r = hex(r)[2:]
        g = hex(g)[2:]
        b = hex(b)[2:]
        
        r = r if len(r)!=1 else '0'+r
        g = g if len(g)!=1 else '0'+g
        b = b if len(b)!=1 else '0'+b
        
        f = int(f'{r}{g}{b}', 16)
        # await log(hex(f))
        return f

    RGB = {
        'R': 255,
        'G': 0,
        'B': 0
    }
    rgb_spin = {
        'R': 'B',
        'G': 'R',
        'B': 'G'
    }
    
    nowChange = ['G', +85]

    N_role = client.get_guild(766932314973929522).get_role(855022848224919572)
    N_msg = await client.get_channel(762916201654386701).fetch_message(856802676468875264)

    while not client.is_closed():
        await asyncio.sleep(30)
        try:
            before_color = str(N_role.color)
            await N_role.edit(color=RGB2hex(RGB)) # 나중에 혹시 안되면 여기를 time over 하다
            after_color = str(N_role.color)
            
            if before_color == after_color:
                await log(f'-----<@526889025894875158> 실패!\n{시간()}\n{before_color} → {after_color}\n-----')
            else:
                await N_msg.edit(content = f'-----성공!\n{시간()}\n{before_color} → {after_color}\n-----')
                
            RGB[nowChange[0]] += nowChange[1]
            if RGB[nowChange[0]] == (255 if nowChange[1]>0 else 0):
                nowChange[0] = rgb_spin[nowChange[0]]
                nowChange[1] = -nowChange[1]
            
        except Exception as e:
            #await log(f"-----error: <@526889025894875158>\n```\n{traceback.format_exc()}\n```")
            pass
        else:
            #await log(f"-----not error")
            pass
        
@client.event
async def on_button_click(res):
    #await log('-----dir(res) on_button_click\n' + str(dir(res)))
    await res.respond(
        type=InteractionType.ChannelMessageWithSource, content=f"{res.component.label} pressed"
    )

@client.event
async def on_message(message):
    
    if message.guild.id == 826264040740618301:
        global note2
        note2 = await client.get_channel(833557179821981707).fetch_message(833579939701325854)

        if message.content == ",등록" and not (message.author.id in (647001590766632966, 646998005643476993, 826322347862261760, 725528129648721920)):
            if "<@"+str(message.author.id)+">" in note2.content:
                await message.channel.send("이미 등록되었습니다")
                return
            else:
                await note2.edit(content=f"{note2.content}\n<@{message.author.id}> : 0")
                await message.channel.send("완료")
                
        if message.content == ",탈퇴" and message.author.id != 647001590766632966:
            if not "<@"+str(message.author.id)+">" in note2.content:
                await message.channel.send("이미 탈퇴되었습니다")
                return
            else:
                noteC = note2.content.split('\n')
                f_noteC = ""
                for i in noteC:
                    if not i.startswith(f"<@{message.author.id}> : "):
                        f_noteC += '\n' + i
                        
                await note2.edit(content=f_noteC)
                await message.channel.send("완료")
                
        if message.author.id in (647001590766632966, 646998005643476993, 826322347862261760, 725528129648721920):
            if message.content.startswith(",+") or message.content.startswith(",-"):
                m = message.content
                usermoney = int(m.split()[0][1:])
                
                userid1 = m.split()[1]
                userid2 = ""
                for i in userid1:
                    if i in "1234567890":
                        userid2 += i
                user = f"<@{userid2}>"
                
                if not (user in note2.content):
                    await message.channel.send("등록되어있지 않은 유저입니다.")
                    return
                else:
                    notec = note2.content
                    notec = notec.split("\n")[1:]
                    for i in range(len(notec)):
                        if notec[i].startswith(user):
                            noten = i
                    notec[noten] = notec[noten][:24] + str(int(notec[noten][24:])+usermoney)
                    notem = "이름 : 돈\n" + "\n".join(notec)
                    await note2.edit(content = notem)
                    await message.channel.send("완료")
            if message.content.startswith(",등록"):
                mm = message.content[4:]
                m = ""
                for i in mm:
                    if i in "1234567890":
                        m += i
                if len(m) != 18:
                    await message.channel.send("잘못된 유저입니다.")
                    return
                if m in note2.content:
                    await message.channel.send("이미 등록되었습니다.")
                    return
                else:
                    await note2.edit(content=f"{note2.content}\n<@{m}> : 0")
                    await message.channel.send("완료")
            if message.content.startswith(",탈퇴"):
                mm = message.content[4:]
                m = ""
                for i in mm:
                    if i in "1234567890":
                        m += i
                if len(m) != 18:
                    await message.channel.send("잘못된 유저입니다.")
                    return
                elif not f"<@{m}>" in note2.content:
                    await message.channel.send("이미 탈퇴되었습니다")
                    return
                else:
                    noteC = note2.content.split('\n')
                    f_noteC = ""
                    for i in noteC:
                        if not i.startswith(f"<@{m}> : "):
                            f_noteC += '\n' + i

                    await note2.edit(content=f_noteC)
                    await message.channel.send("완료")
                

    if message.guild.id == 826264040740618301:
        return
    
    if message.guild.id == 857545260816138251:
        if message.author.id == 647001590766632966 or message.author.id == 646998005643476993:
            if message.content.startswith(",+") or message.content.startswith(",-"):
                try:
                    money = int(message.content.split()[0][1:])
                
                    user = message.content.split()[1]
                    userid = ''
                    for i in user:
                        if i in '1234567890':
                            userid += i
                
                    user = await message.guild.fetch_member(int(userid))
                
                    level_10 = [857554305065156608, 857554349126844417, 857554366842929164, 857554378516594730, 857554399891030097, 857554413656342538, 857554426847297556, 857554437030412308, 857554446342160384, 857554456745082890]
                    level_01 = [857554543206596608, 857554613062205490, 857554647773085696, 857554657751859240, 857554667861311488, 857554676484145152, 857554685689987102, 857554702329839616, 857554715008565260, 857554731320868884]
                    exp_100 =  [857555085957922816, 857555101199237121, 857555119193456640, 857555133474406402, 857555150525038643, 857555300885200906, 857555315046350858, 857555325162225665, 857555337242869760, 857555346242928660]
                    exp_010 =  [857555356509929513, 857555372083642439, 857555382003302410, 857555390966530048, 857555402122854400, 857555421791125504, 857555431945273354, 857555444846690324, 857555456221380638, 857555466930094100]
                    exp_001 =  [857555477574189067, 857555489830862848, 857555519845564416, 857555520822575104, 857555572868775946, 857555585699938324, 857555593437904926, 857555606268280833, 857555616376684554, 857555622954663947]
                
                    user_money = ['0', '1', '0', '0', '0']
                    for i in user.roles:
                        if i.id in level_10:
                            user_money[0] = i.name ; await user.remove_roles(i)
                        elif i.id in level_01:
                            user_money[1] = i.name ; await user.remove_roles(i)
                        elif i.id in exp_100:
                            user_money[2] = i.name ; await user.remove_roles(i)
                        elif i.id in exp_010:
                            user_money[3] = i.name ; await user.remove_roles(i)
                        elif i.id in exp_001:
                            user_money[4] = i.name ; await user.remove_roles(i)
                        
                    usermoney = int(''.join(user_money))
                    usermoney += money
                    usermoney = str(usermoney).zfill(5)
                
                    if int(usermoney) >= 100000:
                        await message.channel.send(f"{user}이 100레벨이 되었습니다.") ; return
                    #await log("*"+str(usermoney)+"*")
                    await user.add_roles(message.guild.get_role( level_10[ int( usermoney[0] ) ] ))
                    await user.add_roles(message.guild.get_role( level_01[ int( usermoney[1] ) ] ))
                    await user.add_roles(message.guild.get_role(  exp_100[ int( usermoney[2] ) ] ))
                    await user.add_roles(message.guild.get_role(  exp_010[ int( usermoney[3] ) ] ))
                    await user.add_roles(message.guild.get_role(  exp_001[ int( usermoney[4] ) ] ))
                
                    await message.add_reaction(체크)
                except:
                    await message.add_reaction(엑스)
                    await log(f"=-=-=☆☆```\n{traceback.format_exc()}\n```")
    if message.guild.id == 857545260816138251:
        return
    

    try:
        global 도배
        m = message.content
        # print(m)

        def 시작(s):
            return k2e(m).startswith(k2e(s))

        관리 = (message.author.id == 526889025894875158)
        
        if message.author.id == 405664776954576896 and message.channel.id in (766932314973929527, 783516524685688842, 784228694940057640, 794146499034480661):
            #랭크업, 시간, 도박장, 도박2 에서의 슷칼봇 메시지 삭제
            await message.delete()
            return
        
        #if message.author.bot: # 봇이 보낸 메시지 무시
        #    return

        #if message.channel.id == 762916201654386701: # 로그채널의 메시지일경우
        #    await message.channel.send(    f"m: `{m}`\n"                +
        #                    f"message_id: `{message.id}`\n"        +
        #                    f"author_id: `{message.author.id}`\n"    +
        #                    f"channel_id: `{message.channel.id}`\n"    +
        #                    f"guild_id: `{message.guild.id}`\n"    )
        #    return
        
        if '@everyone' in m or '@here' in m:
            return


        filelist = os.listdir("commands")
        filelist = [f[:-3] for f in filelist if f.endswith(".py")]
        filelist.sort(key=lambda x: len(x), reverse=True)
        for file in filelist:
            if 시작("," + file):
                exec(f"import commands.{file} as c\nglobal C\nC = c.{file}")
                await C(discord=discord,
                        client=client,
                        message=message,
                        시간=시간)
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
                "ㅅ" : {"`,슬롯`" : "슬롯머신을 돌립니다.", "`,ㅅ`" : "슬롯머신을 돌립니다."},
                "슬롯" : {"`,슬롯`" : "슬롯머신을 돌립니다.", "`,ㅅ`" : "슬롯머신을 돌립니다."},
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
                "번역" : {"`,번역 <한글>`" : "<한글>을 영어로 번역합니다.", "`,번역 <영어>`" : "<영어>를 한글로 번역합니다."},
                "썸네일" : {"`,썸네일 <유튜브 영상 url>`" : "<유튜브 영상 url>의 썸네일을 출력합니다."},
                "기억" : {"`,기억`" : "기억된 목록을 출력합니다.", "`,기억 <키워드>`" : "<키워드>에 기억된 <대답>을 출력합니다.", "`,기억 <키워드> <대답>`" : "<키워드>에 <대답>을 기억합니다."},
                "초대" : {"`,초대`" : "이 봇의 초대링크를 출력합니다."},
                "정보" : {"`,정보`" : "이 봇을 만든 사람을 핑합니다."},
            }
            embed = discord.Embed(title="도움말", color=0x825cff)
            
            if m in help_list:
                for i in help_list[m]:
                    embed.add_field(name=i, value=help_list[m][i], inline=False)
            else:
                embed.add_field(name="**취소선은 아마도 사용할수 없는 명령어입니다.**", value="`,도움 <명령어>`로 세부 도움말을 확인할수 있습니다", inline=False)
                embed.add_field(name="**`도움`**", value="`도움`", inline=False)
                embed.add_field(name="**`재미`**", value="`핑` ~~`에블핑`~~ ~~`히어핑`~~ `지뢰찾기` `슬롯`", inline=False)
                embed.add_field(name="**`기능`**", value="`프사` `말` `계산` ~~`청소`~~ `임베드` ~~`역할생성`~~ ~~`역할제거`~~ ~~`채널생성`~~ ~~`채널제거`~~ `시간` `한영` `영한` `번역` `썸네일` `기억`", inline=False)
                embed.add_field(name="**`기타`**", value="`초대` `정보`", inline=False)
                
            embed.set_footer(text= f'{message.author.name} | {시간()}')
            await message.channel.send(embed=embed)

        #elif 시작(",핑"):
        #    await message.channel.send(f"<@{message.author.id}>")

        #elif 시작(",시간"):
        #    await message.channel.send(시간())

        #elif 시작(",정보"):
        #    await message.channel.send(f"만든사람: <@526889025894875158>")

        elif 시작(",에블핑") and 관리:
            await message.channel.send("@everyone")

        elif 시작(",히어핑") and 관리:
            await message.channel.send("@here")

        #elif 시작(",프사"):
        #    await message.channel.send(embed=discord.Embed(title="프사", color=0xffccff).set_image(url=message.author.avatar_url))

        elif 시작(",말"):
            m = ' '.join(m.split(' ')[1:])
            if not 도배: return
            try:
                await message.channel.send(m)
            except:
                await message.channel.send('말을 할수 없는')
        elif 시작(",도배 멈춰!"):
            도배 = False
            await asyncio.sleep(7.0)
            도배 = True
            await message.add_reaction(체크)

        elif 시작(",임베드"):
            inputdict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
            look_dict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
            mymsg = await message.channel.send("준비중...")
            for i in range(len(list(inputdict.keys()))):
                await mymsg.delete()
                mymsg = await message.channel.send(str(i) + ". " + str(list(inputdict.keys())[i]) + "을(를) 입력해주세요.\n```yaml\n" + str(str(look_dict)[1:-1].replace(', ', ',\n').replace(땀표[0], 땀표[1])) + 땀표[0])
                inputmsg = await client.wait_for('message', timeout=30.0, check=lambda m: m.channel.id == message.channel.id and m.author == message.author)
                inputmsg = inputmsg.content
                inputdict[list(inputdict.keys())[i]] = inputmsg
                look_dict[list(inputdict.keys())[i]] = str(inputmsg)[:7]+'...' if len(str(inputmsg)) > 10 else str(inputmsg)
            await mymsg.delete()
            try:
                embed = discord.Embed(title=inputdict["제목"], color=int("0x"+inputdict["색"], 16))
            except:
                embed = discord.Embed(title=inputdict["제목"], color=0x000000)
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

                        i += 1 if i1>0        and i2>0        and mine_map[i1-1][i2-1] == 지뢰[10] else 0
                        i += 1 if i1>0        and                 mine_map[i1-1][i2  ] == 지뢰[10] else 0
                        i += 1 if i1>0        and i2<mine_x-1 and mine_map[i1-1][i2+1] == 지뢰[10] else 0
                        i += 1 if                 i2>0        and mine_map[i1  ][i2-1] == 지뢰[10] else 0
#                       i += 1 if                                 mine_map[i1  ][i2  ] == 지뢰[10] else 0
                        i += 1 if                 i2<mine_x-1 and mine_map[i1  ][i2+1] == 지뢰[10] else 0
                        i += 1 if i1<mine_y-1 and i2>0        and mine_map[i1+1][i2-1] == 지뢰[10] else 0
                        i += 1 if i1<mine_y-1 and                 mine_map[i1+1][i2  ] == 지뢰[10] else 0
                        i += 1 if i1<mine_y-1 and i2<mine_x-1 and mine_map[i1+1][i2+1] == 지뢰[10] else 0

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

        elif 시작(",청소") and 관리:
            m = ' '.join(m.split(' ')[1:])
            await message.channel.purge(limit=int(m)+1)
            msg = await message.channel.send(f"{m}개의 메시지를 지움")
            await asyncio.sleep(2.0)
            await msg.delete()

        elif 시작(",한영"):
            m = ' '.join(m.split(' ')[1:])
            await message.channel.send(k2e(m))

        elif 시작(",영한"):
            m = ' '.join(m.split(' ')[1:])
            await message.channel.send(e2k(m))
            
        elif 시작(",번역"):
            m = ' '.join(m.split(' ')[1:])
            await message.channel.send(translate(m))

        elif 시작(",썸네일"):
            m = ' '.join(m.split(' ')[1:])
            await message.channel.send(get_thumbnail_by_url(m))
            
        elif 시작(",최신영상") and 관리:
            m = ' '.join(m.split(' ')[1:])
            await message.channel.send(get_last_video_by_search(m))

        elif 시작(",역할생성") and 관리:
            m = ' '.join(m.split(' ')[1:])
            try:
                await message.guild.create_role(name=m)
                await message.add_reaction(체크)
            except:
                await message.add_reaction(엑스)

        elif 시작(",역할제거") and 관리:
            m = ' '.join(m.split(' ')[1:])
            try:
                role = discord.utils.get(message.guild.roles, name=m)
                await role.delete()
                await message.add_reaction(체크)
            except:
                await message.add_reaction(엑스)

        elif 시작(",채널생성") and 관리:
            m = ' '.join(m.split(' ')[1:])
            try:
                category = discord.utils.get(message.guild.categories, name=' '.join(m.split(' ')[:-1]))
                await message.guild.create_text_channel(m.split(' ')[-1], category=category)
                await message.add_reaction(체크)
            except:
                await message.add_reaction(엑스)

        elif 시작(",채널제거") and 관리:
            m = ' '.join(m.split(' ')[1:])
            try:
                channel = discord.utils.get(message.guild.channels, name=m)
                await channel.delete()
                await message.add_reaction(체크)
            except:
                await message.add_reaction(엑스)
                
        elif 시작(",슬롯"):
            ghkrfbf = []
            ghkrfbf += [1]*4930
            ghkrfbf += [2]*8451
            ghkrfbf += [3]*11972
            ghkrfbf += [4]*17606
            ghkrfbf += [5]*22535
            ghkrfbf += [6]*34507
            msg = await message.reply(content=슬롯[0]*3, mention_author=False)
            await asyncio.sleep(1.0)
            a = [random.choice(ghkrfbf), random.choice(ghkrfbf), random.choice(ghkrfbf)]
            await msg.edit(content = 슬롯[a[0]] + 슬롯[a[1]] + 슬롯[a[2]], mention_author=False)
            
            a.sort()
            a = tuple(a)
            if a in [(1,1,1) , (2,2,2) , (3,3,3)]:
                await msg.edit(content=msg.content+"\n**잭팟!**")
            if a in [(1,1,2) , (1,1,3) , (1,2,2) , (2,2,3) , (1,3,3) , (2,3,3)]:
                await msg.edit(content=msg.content+"\n**빅윈!**")
            
        elif 시작(",테스트") and 관리:
            m = m.split(' ')[1:]
            number = int(m[0])
            m = m[1:]
            o = m[:number]
            o2 = {}
            for i in o:
                i1, i2 = i.split("=")
                o2[i1] = eval(i2)
            m = ' '.join(m[number:])
            await eval(m)(**o2)
            
        elif 시작(",버튼") and 관리:
            await message.channel.send(
                "와!",
                components=[
                    Button(style=ButtonStyle.random_color(), label="wa!")
                ]
            )

        elif 시작(",초대코드") and 관리:
            m = ' '.join(m.split(' ')[1:])
            try_list = ['', '', '', '', ''] # 10진 아스키, 16진 아스키, 10진 아스키(대문자.), 16진 아스키(대문자.), 알파벳 순서(대문자.숫자,)
            for i in m.split():
                if i.endswith("."): # 대문자
                    i = i[:-1]
                    try:
                        try_list[0] += chr(int(i, 10))
                    except:
                        pass
                    try:
                        try_list[1] += chr(int(i, 16))
                    except:
                        pass
                    try:
                        try_list[2] += dict(zip(string.ascii_lowercase, string.ascii_uppercase))[chr(int(i, 10))]
                    except:
                        pass
                    try:
                        try_list[3] += dict(zip(string.ascii_lowercase, string.ascii_uppercase))[chr(int(i, 16))]
                    except:
                        pass
                    try:
                        try_list[4] += string.ascii_uppercase[int(i)-1]
                    except:
                        pass
                elif i.endswith(","): # 숫자
                    i = i[:-1]
                    try:
                        try_list[0] += chr(int(i, 10))
                    except:
                        pass
                    try:
                        try_list[1] += chr(int(i, 16))
                    except:
                        pass
                    try:
                        try_list[2] += chr(int(i, 10))
                    except:
                        pass
                    try:
                        try_list[3] += chr(int(i, 16))
                    except:
                        pass
                    try:
                        try_list[4] += str(i)
                    except:
                        pass
                else: # 없음
                    try:
                        try_list[0] += chr(int(i, 10))
                    except:
                        pass
                    try:
                        try_list[1] += chr(int(i, 16))
                    except:
                        pass
                    try:
                        try_list[2] += dict(zip(string.ascii_uppercase, string.ascii_lowercase))[chr(int(i, 10))]
                    except:
                        pass
                    try:
                        try_list[3] += dict(zip(string.ascii_uppercase, string.ascii_lowercase))[chr(int(i, 16))]
                    except:
                        pass
                    try:
                        try_list[4] += string.ascii_lowercase[int(i)-1]
                    except:
                        pass
            for i in try_list:
                await message.channel.send(f"discord.gg/{i}")
                
        elif 시작(",초대"):
            await message.channel.send("https://discord.com/oauth2/authorize?&client_id=688978156535021599&scope=bot&permissions=8")
                
        elif 시작(",코드") and 관리:
            m = ' '.join(m.split(' ')[1:])
            if '\n' in m:
                exec('global 출력\n' + '\n'.join(m.split('\n')[:-1]) + '\n출력=' + m.split('\n')[-1])
                outputmsg = str(출력)
            else:
                outputmsg = str(eval(m))

            await message.channel.send(outputmsg[:2000-3]+'...' if len(outputmsg) > 2000 else outputmsg)
            
        elif 시작(",await코드") and 관리:
            m = ' '.join(m.split(' ')[1:])
            
            exec('global awaitFunction\nasync def awaitFunction(message):\n' + '\n'.join(list(map(lambda x: '    '+x, m.split('\n')[:-1]))) + '\n    return ' + m.split('\n')[-1])
            outputmsg = str(await awaitFunction(message))

            await message.channel.send(outputmsg[:2000-3]+'...' if len(outputmsg) > 2000 else outputmsg)
            
        elif 시작(",계산"):
            m = ' '.join(m.split(' ')[1:])
            
            response = W_client.query(m)
            result = list(response.results)[-1]
            f = result.text
            
            await message.channel.send(f)
            
            
        elif 시작(",올려") and message.guild.id == 743101101401964647:
            m = ' '.join(m.split(' ')[1:])
            for i in range(int(m)):
                await message.channel.send("ㅋ올려")
                
        elif 시작("섬바삭보") and message.guild.id == 743101101401964647:
            await message.channel.send("ㄹㅇㅋㅋ 섬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ밬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ삭ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ봌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
            
        elif 시작(",우탐") and message.guild.id == 743101101401964647:
            embed = discord.Embed(title=message.author.display_name, color=0x4849c3)
            channelname = message.channel.name.split('-')[0]
            embed.add_field(name=f"{channelname} 탐험 결과", value=f"탐험 레벨: {str(message.author)[-4:]} 로 증가!", inline=False)
            random_result = random.choice(["돈", "경험치", "레벨"])
            embed.add_field(name="획득한 보상", value=f"{random_result} +0.0000000000000000...", inline=False)
            await message.channel.send(embed=embed)
            
        elif 시작(",잡키") and message.guild.id == 743101101401964647:
            embed = discord.Embed(title="잡초에게 물을 주었다.", color=0x00ff7f)
            embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/3gXDoQqnWaQQKtbS99CR7ViBZY4o7o-epmmsWGgzG4s/https/media.discordapp.net/attachments/783226362856734730/818719628602638387/224_20210125224126.png?width=427&height=427")
            embed.add_field(name="잡초 레벨", value=f"{int(str(message.author)[-4:])-1} -> {str(message.author)[-4:]}", inline=False)
            embed.add_field(name="잡초 성장 진행도", value="ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ", inline=False)
            random_result = random.choice(["돈", "경험치", "레벨"])
            embed.add_field(name="받은 보상", value=f"{random_result} +0.0000000000000000...", inline=False)
            await message.channel.send(embed=embed)

        elif 시작(",커뉴봇") and message.guild.id == 743101101401964647:
            await message.channel.send("ㅋ강화")
            await message.channel.send("ㅋ섭강")
            await message.channel.send("ㅋ잡키") ; await asyncio.sleep(1.0)
            await message.channel.send("ㅋ우탐")
            try:
                mac_msg = await client.wait_for('message', timeout=10.0, check=lambda msg: msg.author.id == 772274871563583499 and msg.channel == message.channel and "매크로" in msg.content)
                await message.channel.send(mac_msg.content[49:54])
            except:
                pass


            
            
            
            
            
        if message.guild is None: # dm
            return
        if message.author.bot:
            return
        
        

        
        
        
        ##### 여기서부터는 ihs 관련 코드임. #####

        if message.guild.id == 768697423446540318:
            m = message.content
            
            tears = ('', '브론즈5', '브론즈4', '브론즈3', '브론즈2', '브론즈1', '실버5', '실버4', '실버3', '실버2', '실버1', '골드5', '골드4', '골드3', '골드2', '골드1', '플래티넘5', '플래티넘4', '플래티넘3', '플래티넘2', '플래티넘1')
                        
            if 시작("ㅇ") and message.channel.id == 785059965794517002:
                if random.choice([1, 0]):
                    global note
                        
                    if note is None:
                        note = await client.get_channel(842585693524197406).fetch_message(842585796695425054)

                    user = f"<@{message.author.id}>"

                    if not (user in note.content):
                        await note.edit(content = f"{note.content}\n{user} : 0")
                    notec = note.content
                    notec = notec.split("\n")[1:]
                    for i in range(len(notec)):
                        if notec[i].startswith(user):
                            noten = i
                    last_money = int(notec[noten][24:])+1
                    notec[noten] = notec[noten][:24] + str(last_money)
                    notem = "이름 : 돈\n" + "\n".join(notec)
                    await note.edit(content = notem)
                    
                    last_role_number = last_money//100
                    
                    if last_role_number:
                        last_role = discord.utils.get(message.guild.roles, name=tears[last_role_number])
                        if not (last_role in message.author.roles): # 티어업했을경우
                            if last_role_number != 1: # 이전 역할이 있다면
                                # 그거 지움
                                await message.author.remove_role(discord.utils.get(message.author.roles, name=tears[last_role_number-1]))
                            #추가하기
                            await message.author.add_roles(last_role)
                    await message.channel.send(f"{tears[(last_money-1)//100]} {(last_money-1)%100} -> {tears[last_money//100]} {last_money%100}")
                    await message.add_reaction(체크)
                    
                else:
                    await message.add_reaction(엑스)
        
        ##### 여기서부터는 노가다 서버 랭크 관련 코드임. #####
        
        if message.guild.id == 766932314973929522:
            m = message.content
        
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
                    await message.channel.send("피버타임이 *켜*졌습니다")
                else:
                    await message.channel.send("피버타임이 *꺼*졌습니다")


            if (시작(",+") or 시작(",-")) and message.author.id in (647001590766632966, 725528129648721920):
                case = 1 # +-
            elif message.channel.id in (766932314973929527, 783516524685688842):
                case = 2 # 랭크업
            elif message.channel.id in (784228694940057640, 794146499034480661):
                case = 3 # 도박
            elif 시작(",일급") and message.author.id == 647001590766632966:
                case = 4 # 일급
            else:
                return

            if case == 1:
                money = int(m.split()[0][1:])
                users = [ (await message.guild.fetch_member(int(i[-18:] if i[-1] in "1234567890" else i[-19:-1]))) for i in m.split()[1:] ]
            elif case == 2:
                tryRank = None
                if 시작("ㅇ"):
                    tryRank = [1,1,0,0,0,0,0,0,0,0]
                if 시작("ㄱ"):
                    if 시간()[5:7] == "02" and 시간()[8:10] == "14" or\
                       시간()[5:7] == "03" and 시간()[8:10] == "14" or\
                       시간()[5:7] == "04" and 시간()[8:10] == "12" or\
                       시간()[5:7] == "05" and 시간()[8:10] == "05" or\
                       시간()[5:7] == "05" and 시간()[8:10] == "08" or\
                       시간()[5:7] == "06" and 시간()[8:10] == "06" or\
                       시간()[5:7] == "09" and 시간()[8:10] == "01" or\
                       시간()[5:7] == "11" and 시간()[8:10] == "11" or\
                       시간()[5:7] == "12" and 시간()[8:10] == "01" or\
                       시간()[5:7] == "12" and 시간()[8:10] == "25":
                        tryRank = [1,1,1,0,0,0,0,0,0,0]
                    else:
                        await message.channel.send("현재 사용할수 없는 커맨드입니다.") ; return
                if 시작("ㅅ"):
                    if 시간()[5:7] == "03" and 시간()[8:10] == "01" or\
                       시간()[5:7] == "07" and 시간()[8:10] == "17" or\
                       시간()[5:7] == "08" and 시간()[8:10] == "15" or\
                       시간()[5:7] == "10" and 시간()[8:10] == "03" or\
                       시간()[5:7] == "10" and 시간()[8:10] == "09":
                        tryRank = [1,1,1,1,0,0,0,0,0,0]
                    else:
                        await message.channel.send("현재 사용할수 없는 커맨드입니다.") ; return
                if 시작("ㅌ"):
                    if 시간()[5:7] == "01" and 시간()[8:10] == "01" or\
                       시간()[5:7] == "08" and 시간()[8:10] == "30" or\
                       시간()[5:7] == "10" and 시간()[8:10] == "09" or\
                       시간()[5:7] == "12" and 시간()[8:10] == "04" or\
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
                    else:
                        await message.channel.send("현재 사용할수 없는 커맨드입니다.") ; return
                if 시작("ㅊ"):
                    if 시간()[5:7] == "01" and 시간()[8:10] == "26":
                        tryRank = [1,1,1,1,1,1,0,0,0,0]
                    else:
                        await message.channel.send("현재 사용할수 없는 커맨드입니다.") ; return
                if 시작("ㄹ"):
                    if discord.utils.get(message.guild.roles, name="랭커") in message.author.roles:
                        tryRank = [1,1,1,0,0,0,0,0,0,0]
                    else:
                        await message.channel.send("랭커만 사용할 수 있는 커맨드입니다.") ; return
                if 시작("ㅍ"):
                    if discord.utils.get(message.guild.roles, name="마스터(칭호)") in message.author.roles or\
                       discord.utils.get(message.guild.roles, name="신") in message.author.roles or\
                       discord.utils.get(message.guild.roles, name="챔피언(칭호)") in message.author.roles:
                        tryRank = [1,1,1,1,0,0,0,0,0,0]
                    else:
                        await message.channel.send("마스터 이상만 사용할 수 있는 커맨드입니다.") ; return
                if 시작("ㅂ"):
                    if 피버:
                        tryRank = [1,1,1,0,0,0,0,0,0,0]
                    else:
                        await message.channel.send("현재 사용할수 없는 커맨드입니다.") ; return
                if not tryRank:
                    return
                if not random.choice(tryRank):
                    await message.channel.send("랭크업에 실패하였습니다...")
                    return
                money = 1
                users = [message.author, ]
            elif case == 3:
                #도박 아니면 제거
                if 시작("ㄷ"):
                    dp = random.choice([2, 2, 1.5, 1.5, 1.5, 1.5, 1, 1, 0.5, 0.5])
                elif 시작("ㅅ"):
                    dp = random.choice([2, 2, 2, 1.5, 1.5, 1.5, 1.5, 1, 1, 0.5])
                else:
                    return
                if dp == 1: # 1배는 계산할 필요가 없음
                    await message.channel.send("1배")
                    await message.add_reaction(체크)
                    return
                money = None # 도박은 지금 money를 계산할수가 없음
                users = [message.author, ]
            elif case == 4:
                m = ' '.join(m.split(' ')[1:])
                try:
                    a = int(m)
                except:
                    a = 1

                users = {}

                ilGup = {
                    '인턴' : 20,
                    '과장' : 50,
                    '부장' : 150,
                    '사장' : 250,
                    '부회장' : 500,
                    }

                for i in ilGup:
                    for o in discord.utils.get(client.get_guild(766932314973929522).roles, name=i).members:
                        users[o] = ilGup[i]

            for user in users:
                if case == 4: # 일급일때
                    money = users[user] * a
                # 역할 찾아서 랭크 계산
                userRank = 0

                userGod = ''
                for i in God1:
                    if i in [i.name for i in user.roles]:
                        userGod += i

                userGod = God2.index(userGod) if userGod in God2 else 0

                for i in range(len(Ranks_10)):
                    if Ranks_10[i] in [i.id for i in user.roles]:
                        userRank += i*10 ; break
                else:
                    await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; continue
                for i in range(len(Ranks_01)):
                    if Ranks_01[i] in [i.id for i in user.roles]:
                        userRank += i ; break
                else:
                    await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; continue

                for i in range(len(Tears)):
                    if Tears[i] in [i.name for i in user.roles]:
                        userTear = i ; break
                else:
                    await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; continue

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

                userTotalRank = 0
                userTotalRank += userRank
                userTotalRank += userTear *number_1
                userTotalRank += userAgain *number_2
                userTotalRank += userGod *number_3
                userTotalRank += userGodAgain *number_4

                if case in (1, 2, 4): # (money가 정해져있음)
                    userTotalRank += money

                if case == 3: #도박일때
                    #얼마나 걸었는지
                    try:
                        dmoney = int(message.content.split()[1])
                    except:
                        if 시작("ㄷ"):
                            dmoney = 100+userAgain*50
                        elif 시작("ㅅ"):
                            dmoney = 100+userAgain*100
                        await message.channel.send(f"{dmoney}을 겁니다...")
                    
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
                            reaction, _ = await client.wait_for('reaction_add', timeout=60.0, check=lambda r, u: str(r.emoji) in "0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣" and u == message.author)
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

                        elif reaction == "2️⃣":
                            if random.choice([1,1,0,0,0]):
                                money = round(-40)
                                await message.channel.send(f"실드 사용에 성공함 ({money})")
                            else:
                                money = round(-40-dmoney+dmoney*dp)
                                await message.channel.send(f"실드 사용에 실패함 ({money})")

                        elif reaction == "3️⃣":
                            if random.choice([1,1,1,0,0]):
                                money = round(-60)
                                await message.channel.send(f"실드 사용에 성공함 ({money})")
                            else:
                                money = round(-60-dmoney+dmoney*dp)
                                await message.channel.send(f"실드 사용에 실패함 ({money})")

                        elif reaction == "4️⃣":
                            if random.choice([1,1,1,1,0]):
                                money = round(-80)
                                await message.channel.send(f"실드 사용에 성공함 ({money})")
                            else:
                                money = round(-80-dmoney+dmoney*dp)
                                await message.channel.send(f"실드 사용에 실패함 ({money})")

                        elif reaction == "5️⃣":
                            money = round(-100)
                            await message.channel.send(f"실드 사용에 성공함 ({money})")

                    else:
                        money = round(-dmoney+dmoney*dp)
                    #랭크적용...
                    userTotalRank += money
                    if userTotalRank < 0:
                        await message.channel.send("랭크가 부족합니다.")
                        return

                # 역할 제거
                for i in user.roles:
                    if i.id in Ranks_10 or \
                       i.id in Ranks_01 or \
                       i.name in Tears or \
                       i.name in Agains_10 or \
                       i.name in Agains_01 or \
                       i.name in God1 or \
                       i.name in God_Agains_10 or \
                       i.name in God_Agains_01:
                        await user.remove_roles(i)

                #신급환생적용
                await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_10[(userTotalRank//number_4) // 10]))
                await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_01[(userTotalRank//number_4) %  10]))
                userTotalRank %= number_4
                #신급적용
                for i in God2[userTotalRank // number_3]:
                    await user.add_roles(discord.utils.get(message.guild.roles, name=i))
                userTotalRank %= number_3
                #환생횟수 적용
                await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_10[(userTotalRank//number_2) // 10]))
                await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_01[(userTotalRank//number_2) %  10]))
                userTotalRank %= number_2
                #티어 적용 (0이어도 0번째(아톰))
                await user.add_roles(discord.utils.get(message.guild.roles, name=Tears[userTotalRank//number_1]))
                userTotalRank %= number_1
                #랭크 적용 (0이어도 0번째(L))
                await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_10[userTotalRank // 10]))
                await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_01[userTotalRank %  10]))

                if case == 2:
                    await message.channel.send("랭크업에 성공하였습니다!")
            await message.add_reaction(체크)
#########






    except Exception as e:
        await message.add_reaction(엑스)
        await log(f"""
-----
<@526889025894875158> 에러!!!
{시간()}

에러::
e: ```\n{e}\n```
sys.exc_info(): ```\n{sys.exc_info()}\n```
traceback.format_exc(): ```\n{traceback.format_exc()}\n```

메시지::
링크: {message.jump_url}
서버: {message.guild}
채널: {message.channel}
보낸이: {message.author}

{message}
-----
""")

access_token = os.environ["BOR_TOKEN"]
client.run(access_token)
