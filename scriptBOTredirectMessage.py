from telethon import TelegramClient, events  # Імпортуємо потрібні бібліотеки

api_id = 20802036 # Вводимо id нашого телеграм клієнта, та записуємо номер щоб не загубити +380673418119
api_hash = '983427892ee83cb60e343d28c0413093'  # Вводимо hash нашого телеграм клієнта

client = TelegramClient("Test", api_id, api_hash)  # Збираемо клієнта до купи
target_can = -1001894914843  # Вводимо id в який будемо пересилати повідомлення
key_words = ["Яка ситуація","яка ситуація","Друзі, усі новини нашого міста рекомендуємо дивитись",
             "Надіслати інформацію - @Lvivpredloj_bot"
             ,"Побачили де вручають? (обов'язково вказуйте місце, час і адресу)",
             "повне відео","Повне відео","http","telegram"]  # Вводимо ключові слова які будемо шукати в повідомленнях


@client.on(events.NewMessage(chats=[-1001622151427, -1001549627161]))  # Запускаємо наш клієнт та сказуемо на які саме канали реагувати
async def normal_handler(event):  # Обробляємо подію
    est = False
    for i in range(len(key_words)):  # Перебираємо всі ключові слова з нашого списку
        if key_words[i] in event.message.message:  # Перевіряємо коне слово на наявність його в нашому повідомленні
            est = True
            print(event.message)
            print(event.message.peer_id,event.message.message)  # Роздруковуемо в консоль id чату/групи та текст знайденного повідомлення (не обов'язково)

    if not est:
            await client.send_message(target_can, event.message)  # Пересилаємо знайдене повідомлення


client.start()  # Запускаємо кліент
client.run_until_disconnected()  # Ставимо його в бескінечний цикл
