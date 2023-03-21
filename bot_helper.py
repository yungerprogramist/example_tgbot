# from curses import has_extended_color_support
import telebot 
from telebot import types
from random import randint
import requests as r
from bs4 import BeautifulSoup as bs 
from time import sleep

bot = telebot.TeleBot ("5495359403:AAEle1nDgZyencs-zUCO0p-2knWJo10yCrI")

@bot.message_handler (commands= ["help"])
def help (hep):
    hep1= types.ReplyKeyboardMarkup (resize_keyboard= True, row_width=2)
    hep2 = types.KeyboardButton ("общение")
    hep3= types.KeyboardButton ("погода")
    hep4= types.KeyboardButton ("оцени фото")
    hep5= types.KeyboardButton ("напомни мне...")
    hep6= types.KeyboardButton ("найди трек")
    hep7 = types.KeyboardButton ("оцени фото")
    hep8 = types.KeyboardButton ("правда?")
    hep1.add (hep2, hep3, hep4 , hep5, hep6, hep7, hep8) 
    bot.send_message (hep.chat.id , "возможные команды" , reply_markup= hep1)


@bot.message_handler (content_types= ["text"])
def text (sms):
    if sms.text == "общение":
        mrk = types.ReplyKeyboardMarkup( resize_keyboard=True )
        mrk.add  (types.KeyboardButton ("как дела") , types.KeyboardButton ("мне скучно"))
        mes = bot.send_message (sms.chat.id, "давайте пообщаемся", reply_markup= mrk) 
        bot.register_next_step_handler (mes , how)

    elif sms.text == "погода":
        bot.send_message (sms.chat.id , "введите <погода-город>")
    elif "погода в" in sms.text or "Погода в" in sms.text :
        mes = sms.text
        mes1= mes.split("-")
        town = mes1[1]
        url=f"http://wttr.in/{town}?0T"
        search_parameters={"0" : "","M" : ""}                 
        accept_headers={"Accept-Language":"ru"}              
        a=r.get(url,params=search_parameters,headers=accept_headers)   
        bot.reply_to(sms, a.text)

    elif sms.text == "оцени фото":
        mes = bot.send_message (sms.chat.id , "отправь мне это фото")
        bot.register_next_step_handler (mes , pho)

    elif sms.text == "правда?":
        mes = bot.send_message (sms.chat.id , "введите вопрос")
        bot.register_next_step_handler (mes , tru)

    elif sms.text == "автор":
        photo = open ('D://phyton//training//TB.BOT.py//tree.jpg', 'rb')
        mrk = types.InlineKeyboardMarkup()
        mrk.add (types.InlineKeyboardButton("посетить страницу", url = "https://vk.com/id438126854"))
        bot.send_photo (sms.chat.id, photo , reply_markup= mrk )

    elif sms.text == "книги":
        def parser ():
            url = "https://www.labirint.ru/genres/2993/?display=table"

            headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" , "cookie": "id_post=3152; UserSes=labk95kmf228np0tcg; br_webp=8; tmr_lvid=799c3f9d73ff1b12827183bd98cb38b1; tmr_lvidTS=1666157771315; _ym_uid=1666157771680651910; _ym_d=1666157771; adrcid=Aw6tAnXLYyOhd9v5U5695ag; begintimed=MTY2NzI5MzE1Ng%3D%3D; _gid=GA1.2.481460594.1667293159; PHPSESSID=75s6s6ur8g6skg49evlbpnanso; referrer=https%3A%2F%2Fyandex.ru%2F; _ym_visorc=b; _ym_isad=2; cookie_policy=1; _ga=GA1.2.1140209040.1666157771; tmr_detect=0%7C1667382766509; _ga_283NG2S1HR=GS1.1.1667380763.4.1.1667382772.0.0.0; _dc_gtm_UA-3229737-21=1; _dc_gtm_UA-3229737-1=1; _ga_21PJ900698=GS1.1.1667380762.4.1.1667382810.0.0.0; tmr_reqNum=81", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36"}

            session = r.session ()
            response = session.get (url= url , headers = headers )
            soup = bs (response.content , "lxml")

            book = soup.find ("tbody", class_= "products-table__body").find_all ("tr")
            for boks in book :
                book_data = boks.find_all ("td")
                try:
                    book_title = book_data[0].find ("a", class_ = "book-qtip").text.strip()
                except: 
                    book_title = "error"
                try :
                    book_price = book_data [3].find ("span", class_ = "price-val").text.strip()
                    
                except:
                    book_price = "error"
                try: 
                    book_dis = book_data [3].find ("span" , class_ = "price-gray").text.strip()
                except:
                    book_dis= "error"
                # try:
                #     book_skid = round(int((book_dis-book_price)*100/book_dis))
                # except:
                #     book_skid = "error"
                bot.send_message (sms.chat.id ,(f"{book_title} : {book_price} : без скидки {book_dis}") )
                sleep(2)

        def main ():
            parser ()  
        if __name__ == "__main__":
            main()

    else:
        bot.send_message (sms.chat.id , "я не понимаю тебя")

def how (howy):
    if howy.text == "как дела":
        mrk1 = types.ReplyKeyboardMarkup( resize_keyboard=True)
        mrk1.add  (types.KeyboardButton ("отлично") , types.KeyboardButton ("не очень "))
        mes = bot.send_message (howy.chat.id, "у меня все отлично, как дела у тебя?", reply_markup= mrk1)
        bot.register_next_step_handler (mes , how2)
    
    elif howy.text == "мне скучно":
        mrk2 = types.ReplyKeyboardMarkup( resize_keyboard=True)
        mrk2.add  (types.KeyboardButton ("давай") , types.KeyboardButton ("не хочу"))
        mes = bot.send_message (howy.chat.id, "можем поиграть в игру угадай число", reply_markup= mrk2)
        bot.register_next_step_handler (mes , how3)

def how2 (howy):
    if howy.text == "отлично":
        mrk1 = types.ReplyKeyboardMarkup( resize_keyboard=True)
        mrk1.add  (types.KeyboardButton ("спасибо"))
        mes = bot.send_message (howy.chat.id, "это замечательно, продолжай в том же духе", reply_markup= mrk1)
        bot.register_next_step_handler (mes , help)

    elif howy.text == "не очень":
        mrk1 = types.ReplyKeyboardMarkup( resize_keyboard=True)
        mrk1.add  (types.KeyboardButton ("да, ты прав"))
        mes = bot.send_message (howy.chat.id, "не грусти, все проблемы это решаемый пустяк", reply_markup= mrk1)
        bot.register_next_step_handler (mes , help)

def how3 (howy):
    if howy.text == "не хочу":
        mrk2 = types.ReplyKeyboardMarkup( resize_keyboard=True)
        mrk2.add  (types.KeyboardButton ("ага"))
        mes = bot.send_message (howy.chat.id, "хорошо, в другой раз")
        bot.register_next_step_handler (mes , help)

    elif howy.text == "давай" or "попробовать еще раз":
        mrk1 = types.ReplyKeyboardMarkup( resize_keyboard=True)
        mrk1.add  (types.KeyboardButton ("1"), types.KeyboardButton ("2"), types.KeyboardButton ("3"), types.KeyboardButton ("4"), types.KeyboardButton ("5"))
        mes = bot.send_message (howy.chat.id, "угадай число от 1 до 5", reply_markup= mrk1)
        bot.register_next_step_handler (mes , how4)

def how4 (howy):
    if howy.text == "1" or "2" or "3" or "4" or "5":
        ran = randint (1,5)
        if howy.text == ran:
            mes = bot.send_message (howy.chat.id , f"угадал это- {ran}")
            bot.register_next_step_handler (mes , help )

        else :
            mes1 = bot.send_message (howy.chat.id , f"не угадал, это было число- {ran}")
    bot.register_next_step_handler ( mes1 , help ) 
#доделать

def tru (tr):
    run = randint (1,100)
    bot.send_message (tr.chat.id , f"это правда на {run}%" )

@bot.message_handler (content_types= ["photo"])
def pho (photo):
    ran = randint (1,10)
    # if photo.photo == :
     # else :
    # bot.send_message (photo.chat.id , "это не фото")
    bot.send_message (photo.chat.id , f"оценка - {ran}")
   #доделать










# @bot.message_handler (commands=["utr"])
# def how (howy):
#     mrk = types.ReplyKeyboardMarkup( resize_keyboard=True )
#     mrk.add  (types.KeyboardButton ("все хорошо") , types.KeyboardButton ("не очень"))

#     mes = bot.send_message (howy.chat.id, "у меня все хорошо, как дела у вас?", reply_markup= mrk) 
#     bot.register_next_step_handler (mes , how1)

# def how1 (howy):
#     if howy.text == "все хорошо":
#         mrk1 = types.ReplyKeyboardMarkup( resize_keyboard=True)
#         mrk1.add  (types.KeyboardButton ("спасибо") , types.KeyboardButton ("ты лучший!"))
#         mes = bot.send_message (howy.chat.id, "я рад, продолжайте с таким же настроением", reply_markup= mrk1)
#         bot.register_next_step_handler (mes , how2)
    
#     elif howy.text == "не очень":
#         mrk2 = types.ReplyKeyboardMarkup( resize_keyboard=True)
#         mrk2.add  (types.KeyboardButton ("да ты прав") , types.KeyboardButton ("все равно не очень"))
#         mes = bot.send_message (howy.chat.id, "не растрайвайся, все проблемы это лишь пустяк", reply_markup= mrk2)
#         bot.register_next_step_handler (mes , how2)

#         mrk2 = types.ReplyKeyboardRemove (selective= False )

# def how2 (howy):
#     if howy.text == "спасибо" or "ты лучший!":
#         bot.send_message (howy.chat.id , "вперед к вершинам ;)", parse_mode = 'Markdown')
#     elif howy.text == "да ты прав" or "все равно не очень":
#         bot.send_message (howy.chat.id , "вперед к вершинам", parse_mode = 'Markdown')




bot.polling (none_stop=True)