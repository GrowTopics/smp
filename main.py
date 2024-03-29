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

@client.command(name='vault',aliases=['balance','bal'])
async def check_balance(ctx,useriden=None):
    async with ctx.typing():
        if useriden == None:
            await ctx.send("No User Given")
            return

        if useriden == "me":
            userid = ctx.author.id
        else:
            try:
                user = await commands.MemberConverter().convert(ctx,useriden)
                userid = user.id
            except Exception as e:
                print(e)
                await ctx.send("Member not Seen or Invalid member")
                return
        vals,gen_dura = get_user_values(userid)
        mc_username = vals[1]
        dmnd_count = vals[2]

        embed = discord.Embed(
            title = settings.vault_embed["title"].replace("%%mc_username%%",mc_username),
            description = settings.vault_embed['content'].replace("%%diamond_count%%",dmnd_count),
            colour = settings.vault_embed['colour']
        )
        embed.set_footer(text=settings.vault_embed['footer'].replace("%%userid%%",str(userid)).replace("%%gen_dura%%",str(gen_dura)))
    await ctx.send(embed=embed)

@client.command(name='profile',aliases=['p','stats'])
async def check_balance(ctx,useriden=None):
    async with ctx.typing():
        if useriden == "me" or useriden == None:
            userid = ctx.author.id
        else:
            try:
                user = await commands.MemberConverter().convert(ctx,useriden)
                userid = user.id
            except Exception as e:
                print(e)
                await ctx.send("Member not Seen or Invalid member")
                return
        vals,gen_dura = get_user_values(userid)
    if vals==False:
        await ctx.send("Member not in SMP")
    else:
        await generate_profile(ctx,vals,gen_dura)

@client.command("set")
async def set_cmd(ctx,to_change=None):
    to_change = to_change.lower()
    avail_change = ["description","desc"]
    if to_change not in avail_change:
        await ctx.send("You **Cannot** set this...")
        return
    elif to_change in ["description","desc"]:
        sheet = get_sheet("Vault")
        users = sheet.col_values(1)
        if str(ctx.author.id) not in users:
            await ctx.send("You are NOT in **The SMP**")
            return
        value = await generate_prompt(client,ctx,"**Send** your Description **__HERE__**",60)
        index = users.index(str(ctx.author.id))+1
        try:
            start = time.time()
            prev_desc = sheet.acell(f"J{index}").value
            sheet.update(f"J{index}",value)
        except Exception as err:
            await ctx.send(embed=discord.Embed(title="An Error Occurred...",description=err,colour=discord.Colour.red()))
            return
        await ctx.send(embed=discord.Embed(
            title = settings.set_description["title"],
            description = settings.set_description["content"].replace("%%old_desc%%",prev_desc).replace("%%cur_desc%%",value),
            colour = settings.set_description["colour"]
        ).set_footer(text=settings.set_description["footer"].replace("%%gen_dura%%",str(round(time.time()-start,4)))))

client.run(os.getenv('token'))
