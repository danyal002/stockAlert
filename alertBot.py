import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()


def sendMessage(msg):
    @client.event
    async def on_ready():
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{client.guilds[0].name}(id: {client.guilds[0].id})'
        )
        await client.guilds[0].text_channels[0].send(msg)
    client.run(TOKEN)
    return

# members = '\n - '.join([member.name for member in client.guilds[0].members])
# print(f'Guild Members:\n - {members}')
# print(client.guilds[0].owner)
