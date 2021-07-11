async def 한영(m, message, k2e, **_):
    m = ' '.join(m.split(' ')[1:])
    await message.channel.send(k2e(m))
    
