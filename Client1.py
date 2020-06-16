import threading
import time
import ftplib
import discord
import asyncio

exitFlag = 0
global join_old 
global quit_old 


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('\n Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(***) # channel ID goes here
        join_old = 0
        quit_old = 0
        dead_old = 0

        while not self.is_closed():

            ftp_call()

            #parse join file contents into lines 
            File = open("join.txt", "r")
            jsonLineJ = File.readlines()
            File.close()

            join_new = len(jsonLineJ)

            #parse quit file contents into lines
            File = open("quit.txt", 'r')
            jsonLineQ = File.readlines()
            File.close

            #parse death file contents into lines
            File = open('deaths.txt', 'r')
            jsonLineD = File.readlines()
            File.close

            #update number of elements in join list
            join_new = len(jsonLineJ)

            #update number of elements in quit list
            quit_new = len(jsonLineQ)

            #update number of elements in deaths list
            dead_new = len(jsonLineD)

            #print new additions to join list
            if join_new > join_old:
                loggedin = join_new - join_old
                i = 1
                while i <= loggedin:
                    text = jsonLineJ[-i].split(" ")
                    await channel.send(" %s has logged onto Minecraft!" % text[1])
                    i = i +1
                    
                join_old = join_new
    
            if join_new < join_old:
                for element in jsonLineJ:
                    text = jsonLineJ[element].split(" ")
                    await channel.send(" %s has logged onto Minecraft!" %text[1])
                
                join_old = join_new 
           
            #print new additions to quit list
            if quit_new > quit_old:
                loggedout = quit_new - quit_old
                a = 1
                while a <= loggedout:
                    text = jsonLineQ[-a].split(" ")
                    await channel.send(" Boooooo %s logged off :triumph: " % text[1])
                    a = a +1
    
                quit_old = quit_new
    
            if quit_new < join_old:
                for element in jsonlineQ:
                    text = jsonLineQ[element].split(" ")
                    print(text[0])
                    await channel.send(" Boooooo %s logged off :triumph: " %text[1])

                quit_old = quit_new
            
            #print new deaths
            if dead_new > dead_old:
                died = dead_new - dead_old
                d = 1
                while d <= died:
                    text = jsonLineD[-d].split(" ")
                    await channel.send(" Can we get an F in chat, %s just died :/" %text[1])
                    await channel.send(jsonLine)
                
                dead_old = death_new
            
            if dead_new < dead_old:
                for element in jsonLineD:
                    text = jsonLined[element].split(" ")
                    await channel.send("The dumbass %s just died :/" %text[1])

                
                dead_old = dead_new

            
            await asyncio.sleep(300)  #task runs every 5 minutes
    
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!info':
            await message.channel.send(
                """User input: !online \nList of players currently online 
                \n\nUser input: woosh \nEnjoy a magical fairy cat woosh 
                \n\nUser input:hello \nTry it and find out""")

        if message.content == 'hello':
            await message.channel.send('fuck off :eyes:')

        if message.content == 'woosh':
            await message.channel.send( 
                """∧＿∧ \n
                  ( ･ω･｡)つ━☆・*。\n
                  ⊂  ノ    ・゜+.\n
                  しーＪ   °。+ *´¨)\n
                          .· ´¸.·*´¨) ¸.·*¨)\n
                                  (¸.·´ (¸.·* ☆ """)

        if message.content == '!online':
            #parse quit file contents into lines
            File = open("quit.txt", 'r')
            jsonLineQ = File.readlines()
            File.close

            #parse join file contents into lines 
            File = open("join.txt", "r")
            jsonLineJ = File.readlines()
            File.close()

            online = len(jsonLineJ) - len(jsonLineQ)

            if online > 0:
                on = 1
                print("These players are online right now:")
                while on <= online:
                    text = jsonLineJ[-on].split(" ")
                    await message.channel.send("\n%s" % text[1])
                    on = on + 1
            
            else:
                await message.channel.send("No one is currently online :sob: ")

def ftp_call():

    ftp = ftplib.FTP('***', '***','***') #FTP login goes here

    #Get the readme file for Join
    ftp.cwd("/plugins/ServerLog/Activity/Player Join")
    File = open("join.txt", "wb")
    contents = len(ftp.nlst())
    if contents > 0:
        ftp.retrbinary('RETR '+ftp.nlst()[0], File.write)
        File.close()
    
    #Get the readme file for Quit
    ftp.cwd("/plugins/ServerLog/Activity/Player Quit")
    File = open("quit.txt", "wb")
    contents = len(ftp.nlst())
    if contents > 0:
        ftp.retrbinary('RETR '+ftp.nlst()[0], File.write)
        File.close()

    #Get the readme file for Deaths
    ftp.cwd("/plugins/ServerLog/Players/Death")
    File = open("deaths.txt", "wb")
    contents = len(ftp.nlst())
    if contents > 0 :
        ftp.retrbinary('RETR '+ftp.nlst()[0], File.write)
        File.close

    ftp.close()


client = MyClient()
client.run('***') #bot ID goes here
