from telethon import events

@borg.on(events.NewMessage(from_users="@deezloadertcbot"))
async def handler(event):
    # check media type
    if event.audio:
    	await borg.forward_messages("@xda_music", event.message)