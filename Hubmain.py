# hubert.py
import os
import datetime
import discord
import aiosqlite
import pandas as pd
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = discord.Client()
intents=discord.Intents.all()
bot = commands.Bot(command_prefix='$', description="Hi I'm Hubert Bot" , intents=intents,)


#bot.db = None # In the global scope




@bot.event
async def on_member_join(member):
    await member.send(f"This is all the space sucks info you need:")


@bot.event
async def on_ready():
            #bot.db = aiosqlite.connect("database.db")
            guild = discord.utils.get(bot.guilds, name=GUILD)
            print (
                    f'{bot.user} is connected to the following guild:\n'
                    f'{guild.name}(id: {guild.id}):\n'
                    f'DB Connected '
    )


#commands

    
@bot.command()
async def test1(ctx):
    db = await aiosqlite.connect("database.db")
    cursor = await db.execute('SELECT * FROM Stars')
    row = await cursor.fetchone()
    rows = await cursor.fetchall()
    df = pd.DataFrame(row)
    print(df)
    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="")

    await ctx.send(embed=embed)
    
#asyncio.get_event_loop().run_until_complete(setup())
bot.run(TOKEN)

#bot.add_command(test)