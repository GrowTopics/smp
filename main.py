import os,discord,settings
from function import *
from discord.ext import commands

client = commands.Bot(command_prefix=settings.prefix)
client.remove_command("help")

@client.event
async def on_ready():
    await show_restart(client)

@client.event
async def on_message(message):
    if message.content == "<@!863354170849230848>":
        await help_cmd(client,message.channel)
    else:
        await client.process_commands(message)

@client.command('help')
async def help(ctx):
    await help_cmd(client,ctx.channel)

@client.command('ping')
async def ping(ctx):
    await ctx.send(embed=discord.Embed(title=settings.ping_embed["title"],description=settings.ping_embed["content"].replace("%%ping%%",str(round(client.latency*1000,2))),colour=settings.ping_embed["colour"]))

@client.command(name='vault',aliases=['check','balance','bal','p','profile'])
async def check_balance(ctx,useriden=None):
    async with ctx.typing():
        if useriden == None:
            await ctx.send("No User Given")
            return

        sheet = get_sheet().get_all_values()[1:]
        userids = [i[0] for i in sheet]
        mc_usernames = [i[1] for i in sheet]
        dmnd_counts = [i[2] for i in sheet]


        if useriden == "me":
            userid = ctx.author.id
        else:
            try:
                user = await commands.MemberConverter().convert(ctx,useriden)
                userid = user.id
            except Exception as e:
                print(e)
                await ctx.send("Member not Seen")
                return
        try:
            index = userids.index(str(userid))
        except ValueError:
            await ctx.send("Member not Found")
            return
        mc_username = mc_usernames[index]
        dmnd_count = dmnd_counts[index]
        embed = discord.Embed(
            title = settings.profile_embed["title"].replace("%%mc_username%%",mc_username),
            description = settings.profile_embed['content'].replace("%%diamond_count%%",dmnd_count),
            colour = settings.profile_embed['colour']
        )
        embed.set_footer(text=settings.profile_embed['footer'].replace("%%userid%%",str(userid)))
    await ctx.send(embed=embed)

client.run(os.getenv('token'))
