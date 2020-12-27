# client_event.py
import os
import random
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

# # Subclass version for creating custom client and overriding on_ready.
# class CustomClient(discord.Client):
#     async def on_ready(self):
#         print(f"{self.user} is connected to Discord.")
#
#
# client = CustomClient()
# client.run(TOKEN)

# Decorator version for creating and running client.
client = discord.Client()


@client.event
async def on_ready():
    # Type 1:
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break

    # Type 2:
    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

    # Type 3:
    # guild = discord.utils.get(client.guilds, name=GUILD)
    #
    # print(f"{client.user} has connected to the following guild:\n"
    #       f"{guild.name}(id: {guild.id})")

    # members = '\n -'.join([member.name for member in guild.members])
    # print(f"Guild members:\n - {members}")

    print(f"{client.user.name} has connected to Discord!")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, Welcome to my Discord server!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise



client.run(TOKEN)
