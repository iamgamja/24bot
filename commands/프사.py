async def 프사(discord, message, **_):
    await message.channel.send(embed=discord.Embed(title="프사", color=0xffccff).set_image(url=message.author.avatar_url))
