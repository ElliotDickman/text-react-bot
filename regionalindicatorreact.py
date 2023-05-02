import discord
import os
import re
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

token = os.getenv('APP_TOKEN')

@client.event
async def on_message(message):

    hasReacted = False

    print(message.guild.name)

    # Only process messages in guilds with names starting with "anim-"
    if not message.channel.name.startswith("anim-"):
        return

    print(f"Received message: {message.content}")

    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    if "cool" in message.content.lower() and not hasReacted:
        cool_emoji = "\N{Squared Cool}"  # This is the Unicode character for the cool emoji
        beans_emoji = "🫘"
        await message.add_reaction(cool_emoji)
        await message.add_reaction(beans_emoji)
        hasReacted = True
    
    if ("yee haw" in message.content.lower() or "yeehaw" in message.content.lower()) and not hasReacted:
        cowboy_emoji = "\N{Face with Cowboy Hat}"
        await message.add_reaction(cowboy_emoji)
        hasReacted = True

    if "yikes" in message.content.lower() and not hasReacted:
        yikes_emoji = discord.utils.get(message.guild.emojis, name="cornDeath")
        if yikes_emoji:
            await message.add_reaction(yikes_emoji)
            hasReacted = True
    
    if "corn" in message.content.lower() and not hasReacted:
        corn1 = discord.utils.get(message.guild.emojis, name="corn-1")
        corn2 = discord.utils.get(message.guild.emojis, name="cornAHH")
        corn3 = discord.utils.get(message.guild.emojis, name="cornANGRY")
        corn4 = discord.utils.get(message.guild.emojis, name="cornCute")
        corn5 = discord.utils.get(message.guild.emojis, name="cornEvil")
        corn6 = discord.utils.get(message.guild.emojis, name="cornHappy")
        corn7 = discord.utils.get(message.guild.emojis, name="cornOO")
        corn8 = discord.utils.get(message.guild.emojis, name="corn_oog")
        all_corns = [corn1, corn2, corn3, corn4, corn5, corn6, corn7, corn8]

        this_corn = random.choice(all_corns)

        if this_corn:
            await message.add_reaction(this_corn)
            hasReacted = True
    
    if "christian" in message.content.lower() and not hasReacted:
        corn1 = discord.utils.get(message.guild.emojis, name="christianFlex")
        corn2 = discord.utils.get(message.guild.emojis, name="schleep")
        all_corns = [corn1, corn2]

        this_corn = random.choice(all_corns)

        if this_corn:
            await message.add_reaction(this_corn)
            hasReacted = True

    if re.search(r"\bboo\b", message.content.lower()) and not hasReacted:
        ghost_emoji = "👻"
        down_emoji = "\N{Thumbs Down Sign}"
        await message.add_reaction(down_emoji)
        await message.add_reaction(ghost_emoji)
        hasReacted = True

    # Get the unique alphanumeric characters in the message
    unique_chars = set(filter(lambda x: x.isalnum() or x.isspace(), message.content))
    
    if len(unique_chars) == len(message.content) and not hasReacted:
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