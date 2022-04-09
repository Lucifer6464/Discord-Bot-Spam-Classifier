from discord.ext import commands
from classifier import spam_classifier
import asyncio

client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    print("Running")
    while True:
        await asyncio.sleep(300)
        with open('spam_list.txt', 'r+') as f:
            f.truncate(0)
        print('List of spammers has been cleared')


@client.event
async def on_message(message):
    counter = 0
    if spam_classifier(message.content):
        print('User sent spam')
        await message.delete()
        await message.channel.send(
            "I have deleted that message because it appears to be spam. Please don't spam or you will be banned")
        with open('spam_list.txt', 'r+') as f:
            f.write(f'{message.author}\n')
            for line in f:
                if f'{message.author}' in line:
                    counter += 1
            if counter > 4:
                await message.channel.send(f'{message.author} has been kicked for spamming')
                # await message.guild.ban(message.author, readon="spammer")
                # await asyncio.sleep(1)
                # await message.guild.unban(message.author)


client.run("OTYyMDk5Mzk2MjYxMDc3MDQz.YlCm4w.oMWzClLChSp3pOzl_lqk-VTWRa0")
