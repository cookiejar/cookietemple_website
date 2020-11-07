import discord
import json
from datetime import date


def fetch_cookiejar_server_member():
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        cookiejar_guild = [guild for guild in client.guilds if 'Cookiejar' == guild.name]
        server_member = len(cookiejar_guild[0].members)
        today = str(date.today())
        with open('../../discord_user.json', 'r') as f:
            data = json.load(f)

        data.update({today: server_member})
        keys, ordered_data = sorted(data.keys()), dict()
        for key in keys:
            ordered_data[key] = data[key]

        with open('../discord_user.json', 'w') as f:
            json.dump(ordered_data, f)
        await discord.Client.close(client)

    client.run('my_secret_bot_token')
