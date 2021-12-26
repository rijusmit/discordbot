import discord
from discord.ext import commands

from logging import FileHandler
from discord.utils import find
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mynameisriju2021"
)

mycursor=mydb.cursor()
mycursor.execute("use simbot")
mycursor.execute("select phrase,n_phrase from statement")
list_phrase=list()
myresult=mycursor.fetchall()

client= discord.Client()


@client.event
async def on_ready():
    print("We Have Logged in a {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    gg=find(lambda x:x[0]==message.content,myresult)
    print((gg[1]))
    await message.channel.send(gg[1])
    """if message.content.startswith("&hello"):
        await message.channel.send("Hello")
    if message.content.startswith("&hi"):
        await message.channel.send("Kamon Achhish")
    if message.content.startswith("&good"):
        await message.channel.send("Bhalo achhi")"""
async def kick(ctx, member : discord.member,*,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User{member} has been kicked')
async def ban(ctx, member : discord.member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User{member} has been banned')



client.run("OTI0MDA0NTgxMzg0NTI3ODgz.YcYQUw.XeFssGJctv2pgI9M2leVY3ZLydo")
