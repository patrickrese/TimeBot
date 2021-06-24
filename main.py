import discord
import pandas as pd

client = discord.Client()


async def get_times(message):
    data = pd.DataFrame(columns=['date', 'time', 'user'])

    async for msg in message.channel.history(limit=1000):
        if msg.author != client.user:
            datetime = msg.content.split(' : ')
            data = data.append({'date': datetime[0],
                                'time': datetime[1],
                                'user': msg.author.name})
    return data


@client.event
async def on_ready():
    print("time tracker is ready :)")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$time'):
        data = get_times(message)
        await message.channel.send(data)


client.run('''token''')
