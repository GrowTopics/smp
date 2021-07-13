from discord import Colour as C
#Colour Functions. Use as such: C.colourname()    Example: C.blue()
#Available Colours: https://discordpy.readthedocs.io/en/latest/api.html#colour
#Use hex coding as such: C(0x<hex code>)   Example: C(0xFFFFFF)

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
                    f"{prefix}vault <@user | me>" : "Check the **Diamond Count** of a user or do `me` to check yourself"
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

#Shows when user checks vault/balance
vault_embed = {
    "title" : "%%mc_username%%'s Profile",
    "content" : "**Diamond Count** : `%%diamond_count%%`",
    "colour" : C.purple(),
    "footer" : "User ID: %%userid%% | Generated in %%gen_dura%% seconds"
}

#This embed is a response  when user successfully requests to Join TheSMP
join_response_embed = {
    "title" : "✅ Your Request has Been Sent!",
    "content" : "Please wait patiently before an admin **Verifies and Accepts** you in the SMP",
    "colour" : C.green(),
    "footer" : "Time of Request: %%server_time%%"
}

#Join Message Shows when user requests to Join TheSMP
join_request_embed = {
    "title" : "SMP Join Request",
    "content" : "%%username%% `%%userid%%` has requested to join the SMP",
    "colour" : C.green(),
    "footer" : "Time of Request: %%server_time%%",
    "channel_id" : 845476323005956116
}

profile_embed = {
    "title" : "%%minecraft_username%%'s Profile",
    "content" : "**Diamond Count** : `%%diamond_count%%`\n**War Count** : `%%war_count%%`\n**Team Name** : `%%team_name%%`\n**Team Owner** : `%%team_owner%%`\n**Rank** : `%%rank%%`\n**Home Town** : `%%home_town%%`\n**Towns Owned** : `%%towns_owned%%`\n\n**Profile Description** : `%%description%%`\n(Change this by using the `.setdescription <description>` command).",
    "colour" : C.green(),
    "footer" : "Generated in %%gen_dura%% Seconds"
}
