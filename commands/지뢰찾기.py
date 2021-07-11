async def 지뢰찾기(message, asyncio, random, 시작, 지뢰, **_):
    m = ' '.join(m.split(' ')[1:])
    #제대로 input 했는지 확인
    if m.startswith("랜덤"):
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
