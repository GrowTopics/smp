from discord import Colour as C
#Colour Functions. Use as such: C.colourname()    Example: C.blue()
#Available Colours: https://discordpy.readthedocs.io/en/latest/api.html#colour

prefix = ".."

#Shown when bot is restarted
restart_embed = {
    #Channel where this embed will be posted
    "channel_id" : 847602473627025448,
    "title" : "TheSMP Status Logging",
    "content" : "TheSMP running on `%%hostname%%`\nServer Time: %%date_time%%",
    "footer" : "Current Server Time: %%server_time%%",
    "colour" : C.blurple()
}

#Shown when User Mentions Bot or uses the help command
help_embed = {
    "title" : "I'm The SMP Bot, in-charge of @CVXSL's Minecraft SMP",
    "content" :
        {
            "Basic Commands":
                {
                    f"{prefix}help" : "**Shows this Message**",
                    f"{prefix}ping" : "Get Bot Latency in MS",
                },
            "SMP Commands":
                {
                    f"{prefix}join" : "Request to Join the SMP. Doing this multiple time will not make a difference. **(Coming Soon)**",
                    f"{prefix}vault <user_identifier>" : "Check the **Diamond Count** of a user or do `me` to check yourself"
                }
        },
    "footer" : "Made by @Fishball_Noodles",
    "colour" : C.teal()
}

#Shown when user us the ping command
ping_embed = {
    "title" : "Client Latency",
    "content" : "About %%ping%% ms",
    "colour" : C.orange()
}

#Shows when user checks profile
profile_embed = {
    "title" : "%%mc_username%%'s Profile",
    "content" : "**Diamond Count** : `%%diamond_count%%`",
    "colour" : C.purple(),
    "footer" : "User ID: %%userid%%"
}
