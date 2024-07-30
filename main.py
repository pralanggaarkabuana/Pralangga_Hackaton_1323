import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!! bot is ready, I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    # kode untuk bot menerima gambar
    if ctx.message.attachments: 
        for file in ctx.message.attachments: 
            file_name = file.filename 
            file_url = file.url
            await file.save(f'./{file.filename}')
            hasil = get_class(model_path='keras_model.h5', labels_path='labels.txt', image_path=f'./{file.filename}')
            
            # kode untuk memproses gambar (ubah dengan melihat labels.txt)
            if hasil[0] == 'organik\n' and hasil[1] >= 0.65:
                await ctx.send('Ini merupakan sampah organik, sampah ini aman jika dibiarkan dan dapat terurai dengan mudah')
                await ctx.send('Sampah ini dapat diolah menjadi beragam pupuk')
                await ctx.send('Kamu dapat membuang sampah organik ini di tempat sampah di bawah ini')
                gambar1 = 'organik.jpg'
                with open(gambar1, 'rb') as f:
                    pictures = discord.File(f)
                await ctx.send(file=pictures)

            elif hasil[0] == 'anorganik\n' and hasil[1] >= 0.65:
                await ctx.send('Ini merupakan sampah anorganik, sampah ini dapat mencemari lingkungan dan sampah ini dapat terurai dengan waktu yang lama hingga 1 abad lebih')
                await ctx.send('Tetapi sampah ini bisa di daur ulang')
                await ctx.send('Kamu dapat membuang sampah anorganik ini di tempat sampah di bawah ini')
                gambar2 = 'anorganik.jpeg'
                with open(gambar2, 'rb') as f:
                    pictures = discord.File(f)
                await ctx.send(file=pictures)

            elif hasil[0] == 'b3\n' and hasil[1] >= 0.65:
                await ctx.send('Ini merupakan sampah b3, sampah ini sangat berbahaya apabila dibiarkan hingga dapat merusak lingkungan')
                await ctx.send('Sampah ini harus ditanangi secara serius untuk menghindari segala bahaya')
                await ctx.send('Kamu dapat membuang sampah b3 ini di tempat sampah di bawah ini')
                gambar3 = 'b3.jpeg'
                with open(gambar3, 'rb') as f:
                    pictures = discord.File(f)
                await ctx.send(file=pictures)
            else:
                await ctx.send('GAMBAR MU KEMUNGKINAN: salah format/blur/corrupt')
                await ctx.send('KIRIM GAMBAR BARU!!!')
    else:
        await ctx.send('GAMBAR TIDAK VALID/GAADA >:/')


bot.run("TOKEN")