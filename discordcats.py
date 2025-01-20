import discord
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        content = message.content.replace(f'<@{client.user.id}>', '').strip()

        if content.startswith('Hello'):
            await message.channel.send('Hello!')

        elif content.startswith('catgifs'):  
            url = "https://api.thecatapi.com/v1/images/search?mime_types=gif"
            headers = {
                'x-api-key': 'your_cat_api'  
            }
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                gif_url = data[0]['url']
                embed = discord.Embed(
                    title="Random Cat GIF",
                    description="Here's a cat GIF",
                    color=discord.Color.blue()
                )
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("No cat gif found")


        else:
            await message.channel.send('No commands given')

client.run('your_key')



