import discord
from discord.ext import commands

client=commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("We are online {0.user} now".format(client))

#The below code bans player.
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason= None):
    await member.kick(reason = reason)
    await ctx.send(f'User {member} has been kicked')

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'User {member} has been banned')

@client.command()

async def unban(ctx, * ,member):
    banned_users=await ctx.guild.bans()
    member_name,member_discriminator=member.split("#")
    for banned_entry in banned_users:
        user=banned_entry.user
        if (user.name,user.discriminator)==(member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"member{member} was unabanned")
client.run("OTI0MjQyOTE1MjE0MTEwNzMw.YcbuSg.SmlWgljsGvyPjiit7QcncqrC9KA")