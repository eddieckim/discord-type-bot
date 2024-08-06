import os
import discord
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands
import random
import time
import asyncio
import json


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")


@client.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands")
    embed.add_field(name="!info", value="Shows info about the bot", inline=False)
    await ctx.send(content=None, embed=embed)

def get_random_words_from_file(file_path, num_words):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    words = data['words']

    selected_words = [random.choice(words) for _ in range(num_words)]
    
    words_string = ' '.join(selected_words)
    
    return words_string

prompts = [
    "The quick brown fox jumps over the lazy dog.",
    "Hello world! This is a typing speed test.",
    "Typing speed and accuracy are important skills.",
    "Practice makes perfect. Keep typing!",
    "Measure your typing speed with this bot.",
]

user_typing_data = {}

@client.command()
async def type(ctx):
    await ctx.send("Do you want to begin the typing test? Type 'yes' to start.")
    
    def check(m):
        return (
            m.author == ctx.author
            and m.content.lower() == "yes"
            and m.channel == ctx.channel
        )

    try:
        await client.wait_for("message", check=check, timeout=30.0)
        await ctx.send("Starting the typing test in 3 seconds...")
        await asyncio.sleep(1)
        await ctx.send("3...")
        await asyncio.sleep(1)
        await ctx.send("2...")
        await asyncio.sleep(1)
        await ctx.send("1...")

        # prompt = random.choice(prompts)
        prompt = get_random_words_from_file('words.json', 15)
        user_typing_data[ctx.author.id] = {"prompt": prompt, "start_time": time.time()}

        await ctx.send(
            f"Type the following prompt as quickly and accurately as possible:\n\n{prompt}"
            )
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond. Please try again.")
            
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == 'yes':
        return ctx.send(
        f"Type the following prompt as quickly and accurately as possible:\n\n`{prompt}`"
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id in user_typing_data:
        data = user_typing_data[message.author.id]
        prompt = data["prompt"]
        start_time = data["start_time"]
        end_time = time.time()

        typed_text = message.content
        elapsed_time = end_time - start_time

        correct_chars = sum(1 for a, b in zip(prompt, typed_text) if a == b)
        accuracy = correct_chars / len(prompt) * 100

        words_per_minute = (len(typed_text) / 5) / (elapsed_time / 60)

        await message.channel.send(
            f"Time taken: {elapsed_time:.2f} seconds\n"
            f"Words per minute: {words_per_minute:.2f}\n"
            f"Accuracy: {accuracy:.2f}%"
        )

        del user_typing_data[message.author.id]

    await client.process_commands(message)


client.run(TOKEN)