import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Bot está online e conectado ao Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ola'):
        await message.channel.send('Olá!')


client.run('Token')
