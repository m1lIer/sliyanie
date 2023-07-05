from PIL import Image, ImageDraw, ImageFont
import os
from disnake.ext import commands
import disnake
import datetime
import run
import random
import json
duels = {}
duels_bet = {}
class Distribution(commands.Cog):
    def __init__(self, bot):
            self.bot = bot  
    @commands.Cog.listener()
    async def on_ready(self):
        print("\033[35m\DISTRIBUTION LOADED\033[0m")
    
    @commands.slash_command(name="message", description="message")
    async def _message(inter, message: str  = commands.Param(description = "Сообщение")):
        await inter.response.defer()
        embed = {
      "id": 49439273,
      "description": "**Strawberry Community** проводит слияние с **DEFFKI**\nПосле слияние сервер **DEFFKI** будет признан недействительным\n\n",
      "fields": [
        {
          "id": 104980666,
          "name": "**Хочешь своего друга? Подругу? Общения или тиммейтов?**",
          "value": "\n*Залетай на **Strawberry** с двух ног, здесь тебе точно\nбудут рады* <:logo_png_min:1116107491525283881> \n\n**У нас есть:**\n\n>>> <a:6544_heartarrow_purple:1106302180971004085> **Ивенты**\n\n<a:4533_heartarrow_pink:1106302171005329539> **Турниры по CS:GO и другим играм**\n\n<a:6664_heartarrow_red:1106302184804581507> **Активное общение в текстовых и голосовых каналах**\n\n<a:5574_heartarrow_yellow:1106302177888190564> **Отзывчивая администрация**\n\n<a:7826_heartarrow_green:1106302125354524855> [**Telegram чат**](https://t.me/sbcommunityds) **(все интересные моменты и постоянное общение именно тут!)**\n\n"
        },
        {
          "id": 928773272,
          "name": "Ждем тебя!",
          "value": " **В Strawberry Community!**"
        },
        {
          "id": 412917477,
          "name": " ",
          "value": "Подробности можете уточнить у владельцев серверов - <@341399475174244372> и <@450329247924355096>"
        }
      ],
      "color": 3466239,
      "title": "Слияние серверов!",
      "image": {
        "url": "https://media.discordapp.net/attachments/1107610429485748325/1124741032928616519/test1_1.png?width=840&height=473"
      },
      "thumbnail": {
        "url": "https://images-ext-2.discordapp.net/external/0BL093Q862oyIPwEbUkS_clHGLJt1DMirr9chMG41IE/%3Fsize%3D1024/https/cdn.discordapp.com/icons/784421051828142080/a_40e43f0f2f01a432a56b7346ab7a79de.webp?width=473&height=473"
      },
                    "components": [
                                    {
                                        "type": 1,
                                        "components": [
                                            {
                                                "type": 2,
                                                "style": 5,
                                                "url": "https://t.me/sbcommunityds",
                                                "label": "Telegram чат сервера"
                                            }
                                        ]
                                    }
                                    ]
    }
        buttons = disnake.ui.View()
        buttons.add_item(disnake.ui.Button(style=disnake.ButtonStyle.secondary, url = "https://t.me/sbcommunityds", label = "Telegram чат сервера"))        
            
        guild = inter.guild
        for member in guild.members:
            try:
                await member.send(embed = disnake.Embed.from_dict(embed), view=buttons)
            except:
                print("ERROR")
        await inter.author.send("https://discord.gg/TQyaTm7UhX")
        await inter.edit_original_message("Готово!")
    
    @commands.slash_command(name="messagetest", description="message")
    async def _message_test(inter, message: str  = commands.Param(description = "Сообщение")):
        await inter.response.defer()
        embed = {
      "id": 49439273,
      "description": "**Strawberry Community** проводит слияние с **DEFFKI**\nПосле слияние сервер **DEFFKI** будет признан недействительным\n\n",
      "fields": [
        {
          "id": 104980666,
          "name": "**Хочешь своего друга? Подругу? Общения или тиммейтов?**",
          "value": "\n*Залетай на **Strawberry** с двух ног, здесь тебе точно\nбудут рады* <:logo_png_min:1116107491525283881> \n\n**У нас есть:**\n\n>>> <a:6544_heartarrow_purple:1106302180971004085> **Ивенты**\n\n<a:4533_heartarrow_pink:1106302171005329539> **Турниры по CS:GO и другим играм**\n\n<a:6664_heartarrow_red:1106302184804581507> **Активное общение в текстовых и голосовых каналах**\n\n<a:5574_heartarrow_yellow:1106302177888190564> **Отзывчивая администрация**\n\n<a:7826_heartarrow_green:1106302125354524855> [**Telegram чат**](https://t.me/sbcommunityds) **(все интересные моменты и постоянное общение именно тут!)**\n\n"
        },
        {
          "id": 928773272,
          "name": "Ждем тебя!",
          "value": " **В Strawberry Community!**"
        },
        {
          "id": 412917477,
          "name": " ",
          "value": "Подробности можете уточнить у владельцев серверов - <@341399475174244372> и <@450329247924355096>"
        }
      ],
      "color": 3466239,
      "title": "Слияние серверов!",
      "image": {
        "url": "https://media.discordapp.net/attachments/1107610429485748325/1124741032928616519/test1_1.png?width=840&height=473"
      },
      "thumbnail": {
        "url": "https://images-ext-2.discordapp.net/external/0BL093Q862oyIPwEbUkS_clHGLJt1DMirr9chMG41IE/%3Fsize%3D1024/https/cdn.discordapp.com/icons/784421051828142080/a_40e43f0f2f01a432a56b7346ab7a79de.webp?width=473&height=473"
      },
                    "components": [
                                    {
                                        "type": 1,
                                        "components": [
                                            {
                                                "type": 2,
                                                "style": 5,
                                                "url": "https://t.me/sbcommunityds",
                                                "label": "Telegram чат сервера"
                                            }
                                        ]
                                    }
                                    ]
    }
        buttons = disnake.ui.View()
        buttons.add_item(disnake.ui.Button(style=disnake.ButtonStyle.secondary, url = "https://t.me/sbcommunityds", label = "Telegram чат сервера"))        
         
        await inter.author.send("https://discord.gg/TQyaTm7UhX")
        await inter.author.send(embed = disnake.Embed.from_dict(embed), view=buttons)

    

        
    
             


def setup(bot):
    bot.add_cog(Distribution(bot))  