from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
from fayl1 import registruser
from fayl2 import kanalbutton
import sqlite3

api = '6732856375:AAGHGho-Z8PMrsegTIXYpX65UadZkFEPON8'
bot = Bot(api)
dp = Dispatcher(bot)



CHANNEL = 'feberlik84'
birknopka = ReplyKeyboardMarkup(
    [
        [KeyboardButton('📜Mahsulotlar')],
        [KeyboardButton('✅Ushbu kompaniya haqida')],
        [KeyboardButton('🟢Botni boshqaruchi')],

    ],
    resize_keyboard=True
)
ikkiknopka = ReplyKeyboardMarkup(
    [
        [KeyboardButton('Botni boshqaruchi')],
        [KeyboardButton('Boshqaruchidan malumot')],
        [KeyboardButton('Orqaga')],

    ],
    resize_keyboard=True
)



@dp.message_handler(commands='start')
async def start(messaeg: Message):
    chatid = messaeg.chat.id

    fullname = messaeg.from_user.full_name
    username = messaeg.from_user.username
    check = await bot.get_chat_member(CHANNEL, chatid)
    ism = messaeg.from_user.full_name
    if check.status == 'left':
        await bot.send_message(chat_id=chatid, text='Botimizdan foydalanish uchun kanalimizga azo boling va /start ni bosing👇👇👇', reply_markup=kanalbutton())
    else:
        database = sqlite3.connect('baza.sqlite')
        cursor = database.cursor()
        cursor.execute('''SELECT chatid FROM users WHERE chatid = ?''', (chatid, ))
        user = cursor.fetchone()
        if not user:
            registruser(ism=fullname, faydalanuvchinomi=username, chat_id=chatid)
        await bot.send_message(chat_id=chatid, text=f'Assalomu alaykum, {ism}! Faberlik parifmeriya telegram botiga xush kelibsiz😀')
        await bot.send_message(chat_id=chatid, text='Bizning botni tanlaganingiz uchun rahmat', reply_markup=birknopka)





@dp.message_handler(text='📜Mahsulotlar')
async def kurslar(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='📜Mahsulotlar')


@dp.message_handler(text='🟢Botni boshqaruchi')
async def orqaga(message: Message):
    chatid = message.chat.id

    await bot.send_message(chat_id=chatid, text='🟢Botni boshqaruchi', reply_markup=ikkiknopka)


@dp.message_handler(text='Botni boshqaruchi')
async def pythonkussi(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='https://t.me/Muqaddas8440')


@dp.message_handler(text='Boshqaruchidan malumot')
async def pythonkussi(message: Message):
    chatid = message.chat.id
    text = """Kurs nomi: Grafik dizayn

Har qanday biznesning o‘z uslubi, timsoli, shakli bo‘ladi. Dunyoda bizneslar, kompaniyalar, firmalar, mahsulotlar bor ekan, reklama sohasi o‘lmaydi. Reklama sohasining markazida esa – aynan grafik dizayner turadi.
dtrfyghuolp[
Bizning “Grafik dizayn” o‘quv kursimizda taʼlim olib, siz eng mashhur Adobe Photoshop, Abobe Illustrator va CorelDRAW dasturlarini puxta egallaysiz va mehnat bozorida yuqori talabga ega soha vakiliga aylanasiz!

Kurs narxi: 300 000 so'mgvbnjkl;'
fuyufufyuyufyuygytyfthyhfhghghghggvhvghvghhhh
Birinchi oy uchun chegirmadagi narx: 150000 so'm
Kurs davomiyligi: 6 oy"""
    await bot.send_message(chat_id=chatid, text=text)


@dp.message_handler(text='Orqaga')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Asosiy menu', reply_markup=birknopka)


@dp.message_handler(text='💻  Konpyuter savotxonligi')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    ol = """Ism, familiya va yoshingizni kiritng"""
    await bot.send_message(chat_id=chatid, text=ol)


@dp.message_handler(text='💻 Grafik dizayn')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    op = """Kurs nomi: Grafik dizayn

Har qanday biznesning o‘z uslubi, timsoli, shakli bo‘ladi. Dunyoda bizneslar, kompaniyalar, firmalar, mahsulotlar bor ekan, reklama sohasi o‘lmaydi. Reklama sohasining markazida esa – aynan grafik dizayner turadi.

Bizning “Grafik dizayn” o‘quv kursimizda taʼlim olib, siz eng mashhur Adobe Photoshop, Abobe Illustrator va CorelDRAW dasturlarini puxta egallaysiz va mehnat bozorida yuqori talabga ega soha vakiliga aylanasiz!

Kurs narxi: 300 000 so'm
Birinchi oy uchun chegirmadagi narx: 150000 so'm
Kurs davomiyligi: 6 oy"""
    await bot.send_message(chat_id=chatid, text=op)

    await bot.send_message(chat_id=chatid, text=op)


@dp.message_handler(text='💻  Grafik dizayn')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    op = """Ism, familiya va yoshingiznikiritng"""


@dp.message_handler(text='💻 Autocad (uylarni loyihalash)')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    ok = """Kurs nomi:  Autocad (uylarni loyihalash)

        AUTOCAD TIZIMDA LOYIHALASH VA MUHANDISLIK

        AutoCAD grafik ilovasi yordamida tezda ko'nikmalarga ega bo'lishni xohlaysizmi? AutoCAD kursi uning noyob xususiyatlaridan foydalanishni o'rganishi kerak bo'lgan har bir kishi uchun mo'ljallangan. Sinflar o'quvchilar o'quv jarayonida amaliy qatnashish, AutoCAD tamoyillarini tez va etarli darajada o'zlashtirish imkoniyatiga ega bo'ladigan tarzda yaratilgan.
        AutoCAD kursining o'quv dasturi dizayn va muhandislik hujjatlarini ishlab chiqish jarayonini avtomatlashtirish imkoniyatlarini o'zlashtirishga qaratilgan. AutoCAD tizimining asosiy maqsadi turli xil mavzudagi loyihalar uchun chizmalar yaratishdir. Bu ob'ektlar, turli mexanizmlarning loyihalari, shuningdek, elektr sxemalarini ishlab chiqish bo'lishi mumkin.
        Kurs oxirida talabalar sertifikat oladilar.
        To'lovning har qanday shakli.

        Kurs narxi: 400 000 so'm
        Kurs davomiyligi: 3 oy"""
    await bot.send_message(chat_id=chatid, text=ok)


@dp.message_handler(text='💻  Autocad (uylarni loyihalash)')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    ok = """Ism, familiya va yoshingizni kiritng"""
    await bot.send_message(chat_id=chatid, text=ok)


@dp.message_handler(text='💻 Mukammal telegram bot')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    oma = """Kurs nomi: Mukammal telegram bot

Bugungi kunda korxonalarning yaratayotgan xizmat turlarining deyarli barchasi telegram orqali faoliyatni tashkil etgan. Foydalanuvchilarning asosiy trafigi aynan shu tarmoqqa tegishli ekanligi ham hech kimga sir emas. Bu kabi xizmat turlarini ishlab chiqish esa, o'z navbatida, yuqori darajali jarayonlarni bosib o'tadi.
Keling, dastlab bot tushunchasiga to'xtalib o'taylik. Telegram bot - shu tarmoqda ishlaydigan kichik bir dasturcha. U ma'lum bir tizimni boshqaradi. Ular orqali, kanallarni, guruhlarni nazorat qilish yoxud mavjud loyihalarni tanishtirish, shu bilan birgalikda, xizmat turlarini yo'lga qo'yish ancha oson kechadi.

Kurs narxi: 400 000 so'm
Birinchi oy uchun chegirmadagi narx: 200 000 so'm
Kurs davomiyligi: 3 oy"""
    await bot.send_message(chat_id=chatid, text=oma)


@dp.message_handler(text='💻  Mukammal telegram bot')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    oma = """Ism, familiya va yoshingizni kiritng"""
    await bot.send_message(chat_id=chatid, text=oma)


@dp.message_handler(text='💻 Backend')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    bak = """Kurs nomi: Backend

Backend dasturlash asosan saytning yoki mobile ilovalarni qanday ishlashini, server qismi, maʼlumotlar bazasi va brauzer oʻrtasida aloqani taʼminlaydi.

Xo'sh, bu kasb egalarining vazifalari nimalardan iborat?

▫️ Backend dasturchilar veb-sahifalar va ilovalarni bosilganda tez yuklanishini nazorat qiladi;

▫️ Backend dasturchilar shuningdek saytga obuna bo'lganlarni ma'lumotlar bazasiga qayd etib borilishi uchun ham javobgar hisoblanadi;

▫️ Veb-sayt yoki ilovada sodir bo'ladigan har qanday faoliyatni aniqlash va uni tezda hal qilish;

▫️ Shuningdek, foydalanuvchi tomonidan taqdim etilgan barcha ma'lumotlarni to'plashlari va bir xillikda birlashtirishlari kerak. Bu asosan ma'lumotlar bazasiga tegishli.


Kurs narxi: 400 000 so'm
Birinchi oy uchun chegirmadagi narx: 200 000 so'm
Kurs davomiyligi: 8 oy"""
    await bot.send_message(chat_id=chatid, text=bak)


@dp.message_handler(text='💻  Backend')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    bak = """Ism, familiya va yoshingizni kiritng"""
    await bot.send_message(chat_id=chatid, text=bak)


@dp.message_handler(text='💻 Front end')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    mop = """Kurs nomi: Front end


Front-End nima ?

Front-End dasturlovchi veb-saytning foydalanuvchiga ko’rinadigan qismini tayyorlash bilan shug’ullanadi. Masalan siz veb-saytlarda ko’radigan oddiygina tugma uchun ham Front-End dasturlovchi mehnat qilib kod yozadi. Ya’ni siz brauzer orqali ekranda ko’rib turadigan barcha narsani tayyorlash Front-End dasturchining vazifasi va mana shu tayyorlangan ishlarning jamlanmasi veb-saytning Front-End qismi deyiladi. Yanada soddaroq tushuntiradigan bo’lsam siz veb-sayt nomini brauzerga yozib, veb-saytga kirganingizda sizga ko’rinib turgan qismi Front-End qismi hisoblanadi.

Kurs narxi: 300 000 so'm
Birinchi oy uchun chegirmadagi narx: 150 000 so'm
Kurs davomiyligi: 8 oy"""
    await bot.send_message(chat_id=chatid, text=mop)


@dp.message_handler(text='💻  Front end')
async def Grafikdizayn(message: Message):
    chatid = message.chat.id
    mop = """Ism, familiya va yoshingizni kiritng"""
    await bot.send_message(chat_id=chatid, text=mop)


executor.start_polling(dp, skip_updates=True)

