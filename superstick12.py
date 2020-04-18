import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("!도움")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!엠엔"):
        await message.channel.send("위도우의 신")
    if message.content.startswith("!트위치"):
        await message.channel.send("https://www.twitch.tv/mn3_")
    if message.content.startswith("!유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCf91U-PfFdn74tC6v24X6ZQ")
    if message.content.startswith("!디코"):
        await message.channel.send("https://discord.gg/rDmbQT2")
    if message.content.startswith("!도움"):
        await message.channel.send("```접두사는 !입니다 명령어:엠엔,트위치,유튜브,디코 입니다 엠엔 잘생김```")
        
         

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
