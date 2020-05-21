import discord
import asyncio
client = discord.Client()
token = 'NzEyOTM5Mzk2NDQ1MzcyNDY2.XsY3GA.RWeLRR1RKg2QMYSZFPr7RKmK2NY'
@client.event
async def on_ready():
             print("Logged in as ")
             print(client.user.name)
             print(client.user.id)
             game = discord.Game("테스트인거임")
             await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
               if message.content.startswith("테스트"):
                              await message.channel.send("ㅎㅇ")


client.run(token)