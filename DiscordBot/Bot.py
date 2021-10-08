import sys
import random
import datetime
import discord
import asyncio

import CommandFunctions as CF

MyToken = "ODgzMzc4MTAzNjM4OTYyMjU2.YTJD-A.BHSIugqsRFFTCKIPPbG-Uct5gC0"
LogPath = "C:\MyFile\Visual Studio_2019\Bot_test\DiscordDevelop\Log.txt"


c_intents = discord.Intents.default()
c_intents = c_intents.all()

client = discord.Client(intents=c_intents)
#[Server List]/[Channel List]
#0: MinaminTest- 835081736093827082 -- #0: 一般 - 835081736093827086

#テスト用サーバーにテキストを送信します。
async def Send(text):
    current = client.guilds[0].text_channels[0]
    await current.send(text)

#指定されたサーバー、チャンネルにテキストを送信します。
async def SendTo(g_num,ch_num,text):
    current = client.guilds[g_num].text_channels[ch_num]
    await current.send(text)

#メッセージに返信します。
async def Reply(text,msg):
    await msg.reply(text)

#テスト用サーバーを取得します。(サーバー=Guild)
def GetGuild():
    current = client.guilds[0]
    return current

#テスト用サーバーのチャンネルを取得します。
def GetChannel():
    current = client.guilds[0].text_channels[0]
    return current

#指定された番号からテスト用サーバーを取得します。
def GetGuildFrom(g_num):
    current = client.guilds[g_num]
    return current

#指定されたサーバーの指定された番号のチャンネルを取得します。
def GetTXTChannelFrom(guild,ch_num):
    current = guild.text_channels[ch_num]
    return current

#テキストファイルにログを出力します。
def PrintLog(FPath,text):
    try:
        with open(FPath,"x") as f:
            pass

    except FileExistsError:
        with open(FPath,"a") as f:
            f.write(text + "\n")


@client.event
async def on_ready():
    print("Active.")
    print(client.user.name)
    print(client.user.id)
    await Send("Open!")
    print(client.guilds[0].id)

@client.event
async def on_message(message):
    content = str(message.content)

    if message.author != client.user:
        if content.startswith("!test"):
            print(message.author)
            print(content)
            current = "テスト。" + message.author.name;
            await message.channel.send(current)
        
        if content.startswith("!exit"):
            await Send("Close...")
            await client.close()
        
        if content.startswith("!dice"):
            if CF.c_dice(content) != None:
                await Send("Generating...")
                await asyncio.sleep(3)
                #await Send(CF.c_dice(content))
                await Reply(CF.c_dice(content),message)
                for m in client.guilds[0].members:
                    print(str(m))

    p = f"[{datetime.datetime.now()}] Send from:{message.author},content:{content}"
    print(p)
    PrintLog(LogPath,p)
    return

@client.event
async def on_typing(channel, user, when):
    p = f"[{datetime.datetime.now()}] Begin type:{user.name},On channel: {channel.name}, date:{when}"
    print(p)
    PrintLog(LogPath,p)
    return

@client.event
async def on_message_delete(message):
    p = f"[{datetime.datetime.now()}] Deleted message :[{message.author}] {message.content}"
    print(p)
    PrintLog(LogPath,p)
    return

@client.event
async def on_raw_message_delete(payload):
    if payload.cached_message == None:
        p = f"[{datetime.datetime.now()}] Deleted message: unknown"
        print(p)
        PrintLog(LogPath,p)

    return

@client.event
async def on_message_edit(before, after):
    p = f"[{datetime.datetime.now()}] Edited message: [{before.author}] {before.content}"
    pp = f"-> {after.content}"
    print(p)
    print(pp)
    PrintLog(LogPath,p)
    PrintLog(LogPath,pp)

@client.event
async def on_raw_message_edit(payload):
    if payload.cached_message == None:
        p = f"[{datetime.datetime.now()}] Edited message: unknown"
        print(p)
        PrintLog(LogPath.p)
        return

@client.event
async def on_reaction_add(reaction, user):
    p = f""
    if type(reaction.emoji) is discord.Emoji:
        p = f"[datetime.datetime.now()] Added Reaction by: {user.name}"
        pp = f"{reaction.emoji.name} -> [{reaction.message.author}] {reaction.message.content}"
        print(p)
        print(pp)
        PrintLog(LogPath,p)
        PrintLog(LogPath,pp)

    elif type(reaction.emoji) is discord.PartialEmoji:
        p = f"[datetime.datetime.now()] Added Reaction by: {user.name}"
        pp = f"{reaction.emoji.name} -> [{reaction.message.author}] {reaction.message.content}"
        print(p)
        print(pp)
        PrintLog(LogPath,p)
        PrintLog(LogPath,pp)

    elif type(reaction.emoji) is str:
        p = f"[datetime.datetime.now()] Added Reaction by: {user.name}"
        pp = f"{reaction.emoji} -> [{reaction.message.author}] {reaction.message.content}"
        print(p)
        print(pp)
        PrintLog(LogPath,p)
        PrintLog(LogPath,pp)
    return

#@client.event


client.run(MyToken)
CF.PrintLog("Ended by Command.")
