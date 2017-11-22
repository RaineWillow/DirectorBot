import discord
import asyncio

class DirectorBot(discord.Client):

    def __init__(self):
        super(DirectorBot, self).__init__()

    @asyncio.coroutine
    def on_ready(self):
        print('Logged in as:')
        print(self.user.name)
        print(self.user.id)


    @asyncio.coroutine
    def on_message(self, message):
        if self.user.mentioned_in(message): #checks to see if bot was mentioned in message
            if message.content.split(' ')[1] == "read": #checks to see if the content of the message's first word is 'ping'
                yield from self.send_message(message.channel, "Ok.")
                with open("../script.txt") as f:
                    lines = list(f)
                for line in lines:
                    msg = yield from self.send_message(message.channel, "!1235 "+line)
                    print(msg.content)
                    yield from self.wait_for_reaction('👍', message=msg)
