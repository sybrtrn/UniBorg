from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

@borg.on(events.NewMessage(pattern=".ytso ?(.*)", from_users=("@meanii","@Seemybio","@spearwolf","@piyushsharmaxyz","@medevilofmarvel","@IFTTT","@artificialHuman","@FeelTheDomination","@Master_yodhaaa","@Kirito_Kiri","@Fideliu_s","@SharpEXE","@spookyenvy","@Chinmay888","@Lordpeng","@ANDR0_HACKS","@Kochiro","@professionalnoob","@KamleshDunDunWala","@Pranav_19",287535035,1006226527)))
async def test(event):
    if event.fwd_from:
        return
    uwu = event.pattern_match.group(1)
    await borg.send_message("@AudioTubeBot", "{}".format(uwu))