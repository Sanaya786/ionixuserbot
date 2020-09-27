# Originally By ionix userbot
"""COMMAND : .loveu"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 30
    

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "loveu":

        await event.edit(input_str)

        animation_chars = [

            "My friends: You okay?",
            "Me: Yeah, I’m fine.",

            "My headphones:",

            "DJ Snake ft. Justin Bieber - Let Me Love You",
            "0:35 ━❍──────── -5:32",
            "↻     ⊲  Ⅱ  ⊳     ↺",
            "VOLUME: ▁▂▃▄▅▆▇ 100%",
        ]

        for i in animation_ttl:

          
            await event.edit(animation_chars[i % 103])
            await event.edit ("My friends: You okay?\n"
            "Me: Yeah, I’m fine.\n"

            "My headphones:\n"

            "DJ Snake ft. Justin Bieber - Let Me Love You\n"
            "0:35 ━❍──────── -5:32\n"
            "↻     ⊲  Ⅱ  ⊳     ↺\n"
            "VOLUME: ▁▂▃▄▅▆▇ 100%\n")
