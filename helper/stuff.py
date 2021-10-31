#    This file is part of the CompressorBot distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"Hi `{ok.user.first_name}`\n👋, I am **RPLAY ™** `RENISH COMPRESSOR BOT` @Rplay_compressor_bot!\n\n\nI can COMPRESS VIDEO & Can Encode Videos. \n\nReduce Size of Videos With Negligible Quality Change. \n\nYOU can Generate SAMPLES VIDEO & SCREENSHOTS too.\n\n Made by @renishrplay",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url(
                    "Developer - @RPLAY ™ ", url="t.me/renishrplay"),
            ],
            [
                Button.url(
                    "MAKE OWN",
                    url="github.com/Rplayoriginal/RPLAY-VIDEO-COMPRESSOR-BOT",
                ),
                Button.url("CONTACT BOT", url="t.me/Rplay_renish_bot"),
            ],
            [
                Button.url(
                    "RPLAY ™ MOVIE",
                    url="t.me/rplaymovie",
                ),
                Button.url(
                    "RPLAY ™ STICKERS",
                    url="t.me/addstickers/Rplay_movies_stickers_by_stickersthiefbot",
                ),
            ],
            [
                Button.url(
                    "SUPPORT",
                    url="t.me/rplay_support",
                ),
                Button.url(
                    "DONATE",
                    url="www.paypal.com/signin?returnUri=https%3A%2F%2Fwww.paypal.com%2Fmyaccount%2Ftransfer%2Fhomepage%2Fexternal%2Fprofile%3FflowContextData%3DMTmBtYhrkZP8YFR-JHtgXOUrxejjPEh9HS56sk7xZrppgt-1uDDEe4amvWiOxFkKxbAfcNKLkf7viZbjvFboJ6NIosgnmFsJ9djlWz06a3lBM4QCkVCaxInU-S1wnY2bywgHXq0QGfQBVuzKD3iLj25qfqWugUxLezZC4-2qEwkHwkWlB6CwIycu5bvyC4IxsO29MpDtWfojP9Rf3xwQJzxrsE3dEHGenrO9rTGkJlfimzCwFJbOEHVFCzo9ZpU5cMrR70qBd-FX6LIC&onboardData=%7B%22country.x%22%3A%22CD%22%2C%22locale.x%22%3A%22en_US%22%2C%22intent%22%3A%22paypalme%22%2C%22redirect_url%22%3A%22https%253A%252F%252Fwww.paypal.com%252Fmyaccount%252Ftransfer%252Fhomepage%252Fexternal%252Fprofile%253FflowContextData%253DMTmBtYhrkZP8YFR-JHtgXOUrxejjPEh9HS56sk7xZrppgt-1uDDEe4amvWiOxFkKxbAfcNKLkf7viZbjvFboJ6NIosgnmFsJ",
                ),
            ],
            [
                Button.url(
                    "VIDEO COMPRESSOR BOT", url="t.me/Rplay_compressor_bot"),
            ],
            [
                Button.url(
                    "VIDEO MERGE BOT", url="t.me/Rplay_video_mergebot"),
            ],
            [
                Button.url(
                    "VIDEO RENAME BOT", url="t.me/Rplay_rename_bot"),
            ],
            [
                Button.url(
                    "ABOUT ME", url="t.me/I_AM_RENISH"),
            ],
            [
                Button.url(
                    "FOR DYNO", url="t.me/dynos_rplay"),
            ],
        ],
    )

async def help(event):
    await event.reply(
        "**🐠 A Quality CompressorBot**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Generate Sample Compressed Video\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options"
    )


async def ihelp(event):
    await event.edit(
        "**🐠 A Quality CompressorBot**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Generate Sample Compressed Video\n+Screenshots Too\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options",
        buttons=[Button.inline("BACK", data="beck")],
                [
                Button.url(
                    "Developer - @RPLAY ™ ", url="t.me/renishrplay"),
            ],
            [
                Button.url(
                    "MAKE OWN",
                    url="github.com/Rplayoriginal/RPLAY-VIDEO-COMPRESSOR-BOT",
                ),
                Button.url("CONTACT BOT", url="t.me/Rplay_renish_bot"),
            ],
            [
                Button.url(
                    "RPLAY ™ MOVIE",
                    url="t.me/rplaymovie",
                ),
                Button.url(
                    "RPLAY ™ STICKERS",
                    url="t.me/addstickers/Rplay_movies_stickers_by_stickersthiefbot",
                ),
            ],
            [
                Button.url(
                    "SUPPORT",
                    url="t.me/rplay_support",
                ),
                Button.url(
                    "DONATE",
                    url="www.paypal.com/signin?returnUri=https%3A%2F%2Fwww.paypal.com%2Fmyaccount%2Ftransfer%2Fhomepage%2Fexternal%2Fprofile%3FflowContextData%3DMTmBtYhrkZP8YFR-JHtgXOUrxejjPEh9HS56sk7xZrppgt-1uDDEe4amvWiOxFkKxbAfcNKLkf7viZbjvFboJ6NIosgnmFsJ9djlWz06a3lBM4QCkVCaxInU-S1wnY2bywgHXq0QGfQBVuzKD3iLj25qfqWugUxLezZC4-2qEwkHwkWlB6CwIycu5bvyC4IxsO29MpDtWfojP9Rf3xwQJzxrsE3dEHGenrO9rTGkJlfimzCwFJbOEHVFCzo9ZpU5cMrR70qBd-FX6LIC&onboardData=%7B%22country.x%22%3A%22CD%22%2C%22locale.x%22%3A%22en_US%22%2C%22intent%22%3A%22paypalme%22%2C%22redirect_url%22%3A%22https%253A%252F%252Fwww.paypal.com%252Fmyaccount%252Ftransfer%252Fhomepage%252Fexternal%252Fprofile%253FflowContextData%253DMTmBtYhrkZP8YFR-JHtgXOUrxejjPEh9HS56sk7xZrppgt-1uDDEe4amvWiOxFkKxbAfcNKLkf7viZbjvFboJ6NIosgnmFsJ",
                ),
            ],
            [
                Button.url(
                    "VIDEO COMPRESSOR BOT", url="t.me/Rplay_compressor_bot"),
            ],
            [
                Button.url(
                    "VIDEO MERGE BOT", url="t.me/Rplay_video_mergebot"),
            ],
            [
                Button.url(
                    "VIDEO RENAME BOT", url="t.me/Rplay_rename_bot"),
            ],
            [
                Button.url(
                    "ABOUT ME", url="t.me/I_AM_RENISH"),
            ],
            [
                Button.url(
                    "FOR DYNO", url="t.me/dynos_rplay"),
            ],
        ],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        f"Hi `{ok.user.first_name}`\nThis is A CompressorBot Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change\nU can Generate Samples/screenshots too.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url(
                    "Developer - @RPLAY ™ ", url="t.me/renishrplay"),
            ],
            [
                Button.url(
                    "MAKE OWN",
                    url="github.com/Rplayoriginal/RPLAY-VIDEO-COMPRESSOR-BOT",
                ),
                Button.url("CONTACT BOT", url="t.me/Rplay_renish_bot"),
            ],
            [
                Button.url(
                    "RPLAY ™ MOVIE",
                    url="t.me/rplaymovie",
                ),
                Button.url(
                    "RPLAY ™ STICKERS",
                    url="t.me/addstickers/Rplay_movies_stickers_by_stickersthiefbot",
                ),
            ],
            [
                Button.url(
                    "SUPPORT",
                    url="t.me/rplay_support",
                ),
                Button.url(
                    "DONATE",
                    url="www.paypal.com/signin?returnUri=https%3A%2F%2Fwww.paypal.com%2Fmyaccount%2Ftransfer%2Fhomepage%2Fexternal%2Fprofile%3FflowContextData%3DMTmBtYhrkZP8YFR-JHtgXOUrxejjPEh9HS56sk7xZrppgt-1uDDEe4amvWiOxFkKxbAfcNKLkf7viZbjvFboJ6NIosgnmFsJ9djlWz06a3lBM4QCkVCaxInU-S1wnY2bywgHXq0QGfQBVuzKD3iLj25qfqWugUxLezZC4-2qEwkHwkWlB6CwIycu5bvyC4IxsO29MpDtWfojP9Rf3xwQJzxrsE3dEHGenrO9rTGkJlfimzCwFJbOEHVFCzo9ZpU5cMrR70qBd-FX6LIC&onboardData=%7B%22country.x%22%3A%22CD%22%2C%22locale.x%22%3A%22en_US%22%2C%22intent%22%3A%22paypalme%22%2C%22redirect_url%22%3A%22https%253A%252F%252Fwww.paypal.com%252Fmyaccount%252Ftransfer%252Fhomepage%252Fexternal%252Fprofile%253FflowContextData%253DMTmBtYhrkZP8YFR-JHtgXOUrxejjPEh9HS56sk7xZrppgt-1uDDEe4amvWiOxFkKxbAfcNKLkf7viZbjvFboJ6NIosgnmFsJ",
                ),
            ],
            [
                Button.url(
                    "VIDEO COMPRESSOR BOT", url="t.me/Rplay_compressor_bot"),
            ],
            [
                Button.url(
                    "VIDEO MERGE BOT", url="t.me/Rplay_video_mergebot"),
            ],
            [
                Button.url(
                    "VIDEO RENAME BOT", url="t.me/Rplay_rename_bot"),
            ],
            [
                Button.url(
                    "ABOUT ME", url="t.me/I_AM_RENISH"),
            ],
            [
                Button.url(
                    "FOR DYNO", url="t.me/dynos_rplay"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "Choose Mode",
        buttons=[
            [
                Button.inline("Default Compress", data=f"encc{key}"),
                Button.inline("Custom Compress", data=f"ccom{key}"),
            ],
            [Button.inline("Back", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "🐠  **What To Do** 🐠",
        buttons=[
            [
                Button.inline("GENERATE SAMPLE", data=f"gsmpl{key}"),
                Button.inline("SCREENSHOTS", data=f"sshot{key}"),
            ],
            [Button.inline("COMPRESS", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("Send Ur Custom Name For That File")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1], ("@R.Play™✓")[+1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + "@R.Play™✓.mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"Custom File Name : {g}\n\nSend Thumbnail Picture For it."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"Thumbnail {tb} Setted Successfully")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
