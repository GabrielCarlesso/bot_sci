from scidownl import scihub_download
import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
artigo_path = "./paper/one_paper.pdf"

async def download_one_paper(artigo):
    paper = artigo
    paper_type = "doi"
    out = artigo_path
    scihub_download(paper, paper_type=paper_type, out=out)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith('$'):
            print(message.content[1])
            artigo_msg = message.content[1:]
            await download_one_paper(artigo=artigo_msg)
        
            if os.path.isfile(artigo_path):
                pdf_file = discord.File(artigo_path)
                await message.channel.send(file=pdf_file)
                os.remove(artigo_path)
            else:
                await message.channel.send('Article not founded dude!')



            
intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run(bot_token)





