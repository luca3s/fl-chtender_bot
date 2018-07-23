import discord
import os

TOKEN = os.environ['TOKEN']

client = discord.Client()

fortnite-infos_id = '466665501247012874'
regeln_id = '466671498149625887'
infos_id = '467369390086815755'
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
    fortnite-infos = client.get_channel(fortnite-infos_id)
    regeln = client.get_channel(regeln_id)
    infos = client.get_channel(infos_id)
    
    if message.channel == channel:
        if message.author == client.user or message.author.top_role.name == role_1 or message.author.top_role.name == role_2:
            return
        else:
            warning = 'Wer in diesen Channel schreibt wird gebannt vergisst es nicht. Es wurde schon einer dafür gebannt'.format(message)

            await client.send_message(fortnite-infos, warning)
            await client.send_message(infos, warning)
            await client.send_message(regeln, warning)
            
            await client.ban(message.author)
            await client.delete_message(message)
            
client.run(TOKEN)
