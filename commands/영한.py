async def 영한(m, message, e2k, **_):
    m = ' '.join(m.split(' ')[1:])
    await message.channel.send(e2k(m))
