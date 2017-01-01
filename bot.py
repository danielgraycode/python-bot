

import discord
import asyncio
import sys

client = discord.Client()
prefix = "/pb "


@client.event
async def on_ready():
    print('I am logged in as...')
    print(client.user.name)
    print('---------------------')
    await client.change_presence(game=discord.Game(name='The Best Python Bot!'))

@client.event
async def on_message(message):
    if message.content.startswith(prefix + "test"):
        await client.send_message(message.channel, 'Yep, I am working and coded in python for a change!')

    else:
        if message.content.startswith(prefix + "embed"):
            embed = discord.Embed(description="I work!")
            embed.title = 'embed testing, 123!'
            embed.colour =  0x738bd7
            owner = await client.get_user_info('137957400765267968')
            embed.set_author(name=str(owner), icon_url=owner.avatar_url)
            await client.send_message(message.channel, embed=embed)

        else:
            if message.content.startswith(prefix + "status"):
                embed = discord.Embed(title="Python Bot Status", description="Python-Bot running on " + discord.__version__ + " \
                Maintained by https://danielgray.me ! ")
                owner = await client.get_user_info('137957400765267968')
                embed.set_author(name=str(owner), icon_url=owner.avatar_url)
                await client.send_message(message.channel, embed=embed)

            else:
                if message.content.startswith(prefix + "terminate"):
                    if message.author.id == '137957400765267968':
                        embed = discord.Embed(title="Shutting down....", description="Goodbye world!")
                        embed.colour = 0x00FF14
                        await client.send_message(message.channel, embed=embed)
                        sys.exit("Term_By_Owner")
                    else:
                        embed = discord.Embed(title="Permission DENIED", description="You do not have sufficient permissions to shut me down!")
                        embed.colour = 0xFF0000
                        await client.send_message(message.channel, embed=embed)


client.run('token')

