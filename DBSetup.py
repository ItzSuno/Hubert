import discord
from discord.ext import commands
import aiosqlite

bot = discord.Client()

#file_name = # Enter your file_name which you created (Make sure to crate your file with [.db, .sql, .sqlite3]) , Example: economy.db

# Remove the below code after creating the table !
@bot.event
async def create_table(ctx):
    db = await aiosqlite.connect("Hubert\database.db")
    cursor = await db.cursor()
    
    cols = ["ID", "Stars"] # You can add as many as columns in this !!!
    
    await cursor.execute("""CREATE TABLE StarsTracker(userID BIGINT)""")
    await db.commit()
    
    for col in cols:
        await cursor.execute(f"ALTER TABLE economy ADD COLUMN {col}")

    await db.commit()

    await cursor.close()
    await db.close()

    await ctx.send("Table created successfully !")
