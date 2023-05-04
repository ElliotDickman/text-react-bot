import discord
import os
import re
import random
import openai

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

token = os.getenv('APP_TOKEN')
openai_token = os.getenv('OPENAI_TOKEN')
openai.api_key = openai_token

@client.event
async def on_message(message):

    hasReacted = False

    print(message.channel.name)
    channel = message.channel.id

    # Only process messages in guilds with names starting with "anim-"
    if not message.channel.name.startswith("anim-"):
        return

    print(f"Received message: {message.content}")

    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    #####
    # ChatGPT responses
    #####

    prefixes = ["hey maple, ", "hey bot, ", "hey corn, ", "hey cornelius, "]
    if any(message.content.lower().startswith(prefix) for prefix in prefixes):
        storybackground = "Sprouting Spirit is an animated short film about a young girl named Maple and her imaginary friend Cornelius. As a child, Maple moves from a rural area to a big city, and is scared of the new city. The home she moves into is a rowhome with a garden attached to it. When she first moves there, she explores the garden. It is old and dilapidated, with debris, dead plants, and cardboard boxes everywhere. The garden also has a pergola fence, and an old stone fountain. When young Maple first goes into the old garden, she meets her imaginary friend Cornelius. Cornelius is a big fluffy bird-plant hybrid who looks like a pink fluffy ball with two long retractable wobbly legs. Together, Maple and Cornelius enter a magical fantasy world where objects in the garden inrpire fantastical landscapes. They first enter an imaginary flower field, with a pink sky and giant magical plants. They then enter a world where it is night and full of water, where glowing colorful plants illuminate the environment and giant lawn flamingos loom in the distance. There, Cornelius helps Maple gain the courage to jump across large rocks that protrude from the water. After this, they enter a world with giant pinwheels and paper airplanes, where Maple rides on Cornelius as they traverse the landscape. At this point, a breeze blows Maple's favorite yellow bucket hat off her head - and out of the old garden, taking her out of the fantasy imaginary world and snapping back to reality. Her hat rests against a fire hydrant on the sidewalk, but Maple is afraid to leave the safety of her garden to retrieve it. Her imaginary friend Cornelius encourages her to go out and get her hat, and she realizes that the new city isn't so scary after all. The film begins and ends with Maple as she is older and about to leave for the airport to go to college. At the beginning, she looks down at her plane ticket while standing outside the garden gate, and remembers all the events from when she first moved to the city. At the end, as young Maple steps back into the garden after getting her hat, it cuts to older Maple looking around at a rejuvinated garden and reminiscing about her adventures with her imaginary friend Cornelius. Your job is to pretend to be a writer on this story. The user may ask a question about the story, in which case you should answer based on the story. If the user asks a question that the story so far doesn't discuss, you should make up an answer as though you were writing the story yourself. Never, under any circumstances, say that the story doesn't discuss an answer that you need to provide."

        if message.content.lower().startswith("hey maple, "):
            question = message.content.lower()[len("hey maple, "):]
            print(message.channel_id)
            print(question)
            mapleCompletion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": storybackground},
                    {"role": "user", "content": f'Lets play a game where you pretend to be Maple. Answer the following question as young Maple would: {question}'}
                ]
            )
        
            await channel.send(mapleCompletion.choices[0].message.content)
            return
        
        if message.content.lower().startswith("hey corn, ") or message.content.lower().startswith("hey cornelius, "):
            print(message.channel_id)
            print("Corn")
            cornCompletion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": "Let's play a game where you pretend to be Cornelius, an imaginary bird-plant hybrid. Cornelius doesn't know English, he only speaks in imaginary bird-plant sounds. Respond with a sentence in an imaginary Cornelius language, where he makes bird-plant sounds. Do not respond with any real English words, only as Cornelius. Your response should begin and end with an asterisk."}
                ]
            )
        
            await channel.send(cornCompletion.choices[0].message.content)
            return
        
        if message.content.lower().startswith("hey bot, "):
            question = message.content.lower()[len("hey bot, "):]
            print(message.channel_id)
            print(question)
            storyCompletion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": storybackground},
                    {"role": "user", "content": f'Answer the following question in a fun and excited tone: {question}'}
                ]
            )
        
            await channel.send(storyCompletion.choices[0].message.content)
            return



    #####
    # Emotes
    #####
    
    if "cool" in message.content.lower() and not hasReacted:
        cool_emoji = "\N{Squared Cool}"  # This is the Unicode character for the cool emoji
        beans_emoji = "🫘"
        await message.add_reaction(cool_emoji)
        await message.add_reaction(beans_emoji)
        hasReacted = True

    if "pushed" in message.content.lower() and not hasReacted:
        right_emoji = "\N{Black Rightwards Arrow}"
        fire_emoji = "🔥"
        face_emoji = "😩"
        bite_lip_emoji = "🫦"
        drops_empji = "💦"
        await message.add_reaction(right_emoji)
        await message.add_reaction(fire_emoji)
        await message.add_reaction(bite_lip_emoji)
        await message.add_reaction(face_emoji)
        await message.add_reaction(drops_empji)
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