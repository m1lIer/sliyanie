import sys
sys.path.insert(1, 'settings/')
import config
import disnake
from disnake.ext import commands
from os import listdir
from asyncio import create_task, run
from enum import Enum

class Cogss(str, Enum):
    Dist = 'distribution'

intents = disnake.Intents.all()
bot = commands.InteractionBot(activity=disnake.Game(name="нарды"), intents = intents)

@bot.slash_command(name="load", description="FOR ADMINS")
@commands.is_owner()
async def load(inter, extension: Cogss):
    bot.load_extension(f"commands.{extension}")
    await inter.response.send_message("Cogs loaded")

@bot.slash_command(name="unload", description="FOR ADMINS")
@commands.is_owner()
async def unload(inter, extension: Cogss):
    bot.unload_extension(f"commands.{extension}")
    await inter.response.send_message("Cogs unloaded")

@bot.slash_command(name="reload", description="FOR ADMINS")
@commands.is_owner()
async def reload(inter, extension: Cogss):
    bot.reload_extension(f"commands.{extension}")
    await inter.response.send_message("Cogs reloaded")


def load_cogs():
    for filename in listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[:-3]}')


if __name__ == "__main__":
    load_cogs()
    activity = disnake.Activity(
    name="слияние",
    type=disnake.ActivityType.watching,
    )
    #run(main())
    #client.start(config.token)
    bot.run(config.token)
