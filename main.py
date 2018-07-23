import discord

TOKEN = 'NDY5MTkzMTk1NDE5NTk4ODQ5.DjY0Vw.c7hiubSNrp6RVWTqJ7IN7F8nYtM'

client = discord.Client()

channel_id = '466665501247012874'
role_1 = 'Mod'
role_2 = 'Ober Wolf'

@client.event
async def on_ready():    
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    
@client.event
async def on_message(message):
    channel = client.get_channel(channel_id)

    if message.channel == channel:
        if message.author == client.user or message.author.top_role.name == role_1 or message.author.top_role.name == role_2:
            return
        else:
            warning = 'Wer in diesen Channel schreibt wird gebannt vergisst es nicht. Es wurde schon einer dafür gebannt'.format(message)
            await client.send_message(message.channel, warning)
    
client.run(TOKEN)