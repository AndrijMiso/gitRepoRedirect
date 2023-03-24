from telethon import TelegramClient, events

api_id = 20802036
api_hash = '983427892ee83cb60e343d28c0413093'

client = TelegramClient("Test", api_id, api_hash)
target_can = -1001894914843
key_words = ["Яка ситуація","яка ситуація","Друзі, усі новини нашого міста рекомендуємо дивитись",
             "Надіслати інформацію - @Lvivpredloj_bot"
             ,"Побачили де вручають? (обов'язково вказуйте місце, час і адресу)",
             "повне відео","Повне відео","http","telegram"]


@client.on(events.NewMessage(chats=[-1001622151427, -1001549627161])) 
async def normal_handler(event):
    est = False
    for i in range(len(key_words)):
        if key_words[i] in event.message.message:
            est = True
            print(event.message)
            print(event.message.peer_id,event.message.message)

    if not est:
            await client.send_message(target_can, event.message)


client.start()
client.run_until_disconnected()
