async def vmtk(discord, client, message):
    await message.channel.send(embed=discord.Embed(title="프사", color=0xffccff).set_image(url=message.author.avatar_url))
