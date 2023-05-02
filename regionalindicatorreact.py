import discord
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

token = os.getenv('APP_TOKEN')

@client.event
async def on_message(message):

    print(message.guild.name)

    # Only process messages in guilds with names starting with "anim-"
    if not message.channel.name.startswith("anim-"):
        return

    print(f"Received message: {message.content}")

    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    if "cool" in message.content.lower():
        cool_emoji = "\N{Squared Cool}"  # This is the Unicode character for the cool emoji
        await message.add_reaction(cool_emoji)
    
    if "yee haw" in message.content.lower():
        cowboy_emoji = "\N{Face with Cowboy Hat}"  # This is the Unicode character for the cool emoji
        await message.add_reaction(cowboy_emoji)

    if message.content.lower() == "boo":
        ghost_emoji = "👻"  # This is the Unicode character for the cool emoji
        down_emoji = "\N{Thumbs Down Sign}"
        await message.add_reaction(down_emoji)
        await message.add_reaction(ghost_emoji)

    # Get the unique alphanumeric characters in the message
    unique_chars = set(filter(lambda x: x.isalnum() or x.isspace(), message.content))
    
    if len(unique_chars) == len(message.content):
        # Only react with alphanumeric characters
        for char in message.content:
            if char.isalnum():
                # Convert the character to its lowercase representation
                char_lower = char.lower()
                
                # Get the Unicode code point of the lowercase character
                code_point = ord(char_lower) - 97 + 0x1f1e6
                
                # Convert the code point to the corresponding Unicode character
                emoji = chr(code_point)
                
                # React with the emoji
                await message.add_reaction(emoji)

client.run(token)