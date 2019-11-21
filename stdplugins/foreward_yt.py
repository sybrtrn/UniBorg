from telethon import events

@borg.on(events.NewMessage(from_users="@AudioTubeBot"))
async def handler(event):
    # check media type
    if event.audio:
    	await borg.forward_messages("@sothisismusic", event.message)