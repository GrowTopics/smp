import discord,settings,socket,datetime,gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

async def help_cmd(client,channel):
    formatted_commands_list = ""
    for i in settings.help_embed["content"]:
        formatted_commands_list+=f"\n__**{i}**__\n"
        for n in settings.help_embed["content"][i]:
            formatted_commands_list+=f"• `{n}` - {settings.help_embed['content'][i][n]}\n"
    await channel.send(embed=discord.Embed(
        title=settings.help_embed["title"],
        description = f"**My Prefix: `{settings.prefix}`**{formatted_commands_list}",
        colour = settings.restart_embed["colour"]).set_footer(text=settings.help_embed['footer'])
    )

async def show_restart(client):
    print(f"Bot Already Online...Running on {socket.gethostname()}")
    await client.get_channel(settings.restart_embed["channel_id"]).send(embed=discord.Embed(
        title = settings.restart_embed["title"],
        description = settings.restart_embed["content"].replace("%%hostname%%",socket.gethostname()).replace("%%date_time%%",datetime.datetime.now().strftime('%c')),
        colour = settings.restart_embed["colour"]
    ).set_footer(text=settings.restart_embed["footer"].replace("%%server_time%%",datetime.datetime.now().strftime("%H:%M:%S"))))

def get_sheet(sheetname):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = sac.from_json_keyfile_name("growtopicsgclient.json", scope)
    google_client = gspread.authorize(creds)
    sheet = google_client.open_by_key("1AdopKs21DHR7DYmg5qT5K3-uKvSifhnWnAh1HfPwFTk")
    return sheet.worksheet(sheetname)
