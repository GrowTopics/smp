import os,discord,settings
from function import *
from discord.ext import commands

client = commands.Bot(command_prefix=settings.prefix)
client.remove_command("help")

@client.event
async def on_ready():
    return
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

@client.command('join')
async def req_join(ctx):
    async with ctx.typing():
        sheet = get_sheet("Cache")
        data = get_sheet("Vault")
        print("Sheet>>>",sheet)
        wait_list = sheet.acell('B1').value.split(",")
        print(wait_list)
        if str(ctx.author.id) in wait_list:
            await ctx.send("Join Request has Failed. You have Already Requested..")
            return
        elif str(ctx.author.id) in data.col_values(1):
            await ctx.send(f"You are **already** part of the SMP\nDo `{settings.prefix}profile me` to check your profile")
            return
        wait_list.append(str(ctx.author.id))
        sheet.update("B1",",".join(wait_list))
    embed = discord.Embed(
        title = settings.join_request_embed["title"],
        description = settings.join_request_embed["content"].replace("%%username%%",ctx.author.name).replace("%%userid%%",str(ctx.author.id)),
        colour = settings.join_request_embed["colour"]
    )
    embed.set_footer(text=settings.join_request_embed["footer"].replace("%%server_time%%",datetime.datetime.now().strftime("%c")))
    await client.get_channel(settings.join_request_embed["channel_id"]).send(embed=embed)
    embed = discord.Embed(
        title = settings.join_response_embed["title"],
        description = settings.join_response_embed["content"],
        colour = settings.join_response_embed["colour"]
    )
    embed.set_footer(text=settings.join_response_embed["footer"].replace("%%server_time%%",datetime.datetime.now().strftime("%c")))
    await ctx.send(embed=embed)

@client.command(name='vault',aliases=['balance','bal','p','profile'])
async def check_balance(ctx,useriden=None):
    async with ctx.typing():
        if useriden == None:
            await ctx.send("No User Given")
            return

        sheet = get_sheet("Vault").get_all_values()[1:]
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

client.run("ODYzMzU0MTcwODQ5MjMwODQ4.YOlrOg.vQ6YLIxVnEouNdD271tKXiW9Gx8")
#client.run(os.getenv('token'))
