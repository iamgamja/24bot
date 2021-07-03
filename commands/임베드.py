async def 임베드(discord, client, message, **_):
    inputdict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
    look_dict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
    mymsg = await message.channel.send("준비중...")
    for i in range(len(list(inputdict.keys()))):
        await mymsg.delete()
        mymsg = await message.channel.send(str(i) + ". " + list(inputdict.keys())[i] + "을(를) 입력해주세요.\n```yaml\n" + '\n'.join([ key + ' : ' + look_dict[key] for key in look_dict ]) + '\n```')
        inputmsg = await client.wait_for('message', timeout=30.0, check=lambda m: m.channel.id == message.channel.id and m.author == message.author)
        inputmsg = inputmsg.content
        inputdict[list(inputdict.keys())[i]] = inputmsg
        look_dict[list(inputdict.keys())[i]] = inputmsg[:7]+'...' if len(inputmsg) > 10 else inputmsg
    await mymsg.delete()
    try:
        embed = discord.Embed(title=inputdict["제목"], color=int(inputdict["색"], 16))
    except:
        embed = discord.Embed(title=inputdict["제목"], color=0x000000)
    embed.add_field(name=inputdict["소제목"], value=inputdict["내용"], inline=False)
    embed.set_footer(text=inputdict["푸터"])
    await message.channel.send(embed=embed)
