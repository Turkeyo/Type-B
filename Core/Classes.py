import discord
from discord.ext import commands

#繼承commands.cog類別
class Bot_Cog(commands.Cog):    
    def __init__(self,bot):    #初始化
        self.bot = bot         #main.py 裡的bot等於Bot_Cog 的bot
