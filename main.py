from logging import info
from time import sleep
from token import ATEQUAL
import discord
from discord.ext import commands
from discord.player import FFmpegPCMAudio
from requests import get
import asyncio

token = ''
client = commands.Bot(command_prefix='>')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print('im on')


@client.command()
async def ping(ctx):
    await ctx.send('pong')

@client.command()
async def abuelo(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('abuelo.wav')
        player = voice.play(source)
        sleep(2)
        await ctx.guild.voice_client.disconnect()

    else:
        await ctx.send('no')

@client.command()
async def comandos(ctx):
    await ctx.send('>comandos\n>ping \n >ip = da la ip del server de minecraft \n >join \n >leave \n >abuelo \n >whouare')

@client.command()
async def whouare(ctx):
    await ctx.send("Soy Wrench jr.\nMi padre es @kali.\nPor el momento no puedo hacer mucho, ya que soy una versión en prueba.\nMi padre está trabajando en mis mejoras para versiones futuras donde si podre cantar.\nDe momento no hago mucho pero es trabajo honesto ")

@client.command()
async def ip(ctx):
    ip =  get('https://api.ipify.org').text
    await ctx.send(ip)

@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('in.wav')
        player = voice.play(source)

    else:
        await ctx.send('no')

@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('si')

@client.command(pass_context = True)
async def p(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('no hay audio')

@client.command(pass_context = True)
async def r(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_pause():
        voice.resume()
    else:
        await ctx.send('no hay audio')

@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    voice.stop()




client.run(token)
