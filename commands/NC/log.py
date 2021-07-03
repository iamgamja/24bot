async def log(self, s):
    s = str(s)
    
    print(s)
    if len(s) > 2000:
        await self.get_channel(762916201654386701).send(s[:2000])
        await log(s[2000:])
    else:
        await self.get_channel(762916201654386701).send(s)
