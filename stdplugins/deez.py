from telethon import events
import os
import requests
import json
from uniborg.util import admin_cmd

@borg.on(events.NewMessage(pattern=".deez ?(.*)", from_users=("@meanii","@Seemybio","@spearwolf","@piyushsharmaxyz","@medevilofmarvel","@IFTTT","@artificialHuman","@FeelTheDomination","@Master_yodhaaa","@Kirito_Kiri","@Fideliu_s","@SharpEXE","@spookyenvy","@Chinmay888","@Lordpeng","@ANDR0_HACKS","@Kochiro","@professionalnoob","@KamleshDunDunWala","@Pranav_19",287535035,1006226527)))
async def _(event):
    if event.fwd_from:
        return
    input_str = "https://song.link/redirect?url=" + event.pattern_match.group(1) + "&to=deezer&web=true"
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith('3'):
        await borg.send_message("@deezloadertcbot", "{}".format(r.headers["Location"]))
    else:
        await event.reply("Input URL {} returned status_code {}".format(input_str, r.status_code))
