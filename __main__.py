#╔═══╗╔╗──╔╗╔═╗─╔╗╔════╗╔═══╗╔═══╗╔═══╗╔═══╗
#║╔══╝║╚╗╔╝║║║╚╗║║║╔╗╔╗║║╔═╗║║╔═╗║║╔═╗║║╔══╝
#║╚══╗╚╗╚╝╔╝║╔╗╚╝║╚╝║║╚╝║║─║║║╚═╝║║║║║║║╚══╗
#║╔═╗║─╚╗╔╝─║║╚╗║║──║║──║╚═╝║║╔╗╔╝║║║║║╚══╗║
#║╚═╝║──║║──║║─║║║──║║──║╔═╗║║║║╚╗║╚═╝║╔══╝║
#╚═══╝──╚╝──╚╝─╚═╝──╚╝──╚╝─╚╝╚╝╚═╝╚═══╝╚═══╝ ™
#   VK MsgAssistant v.0.1
#   Каждая строчка вашего хорошего кода откидывает SkyNet в развитии. Давайте поможем проекту.
#   ЯП: Python 3(.8)
#   Контакты: https://vk.com/6yntar05
#             https://github.com/6yntar05
###################################################
#
#   Подробная инструкция: README
#   
###################################################

import os
import sys
import time
import requests
import random  
os.system("color F0");os.system("mode con:cols=55 lines=30")
print("___________________6yntar05___________________[- □ X]");print()
print("[6yntar05] VK MsgAssistant v.0.1");print()

try:
    from zalgo_text import zalgo
    errZalgo = False
except:
    print("[!!]Ошибка импорта zalgo_text")
    print("Попробуйте pip install zalgo_text");print()
    errZalgo = True
try:
    import tenorpy
    errTenorpy = False
except:
    print("[!!]Ошибка импорта zalgo_text")
    print("Попробуйте pip install tenorpy");print()
    errTernorpy = True

################### Проверка токена

try:
    txtTokenRead = open('token.txt', 'r', encoding = 'utf8')
    token = txtTokenRead.read()
    txtTokenRead.close()
except:
    txtTokenWrite = open('token.txt', 'w', encoding = 'utf8')
    txtTokenWrite.write("ВВЕДИТЕ ТОКЕН")
    txtTokenWrite.close()
    txtTokenRead = open('token.txt', 'r', encoding = 'utf8')
    token = txtTokenRead.read()
    txtTokenRead.close()


if len(token) < 85 :
    if token != "ВВЕДИТЕ ТОКЕН":
        print("[ii]Токен имеет неверную длинну")
        msgbuff = str(len(token)) + " Вместо 85 символов"
        print(msgbuff)
        print("Убедитесь, что ввели его правильно, все 85 символов")
    else:
        print("[ii]Не найден токен в файле token.txt")
    print("Инструкция по получению токена есть в README файлах")
    while True:
        print()
        token = input("> Вставьте токен (85 символов):")
        if len(token) == 85:
            break
        else:
            msgbuff = "Вы ввели " + str(len(token)) + " вместо 85 символов"
            print(msgbuff)
    txtTokenRead.close()
    txtTokenWrite = open('token.txt', 'w', encoding = 'utf8')
    txtTokenWrite.write(token)
    txtTokenWrite.close()
elif len(token) == 85:
    print("[ОК]Токен найден");print()
elif len(token) > 85:
    print("[ii]Токен найден, но имеет неправильную длинну >85");
    print("Отбрасываю остальные символы");print()
    token = token[0:85]

################### Запуск
print("[..]Запуск бота");print();
auth_handler_err = False
try:
    import vk_api
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.utils import get_random_id
except:
    print("[!!]Ошибка импорта библиотек!");
    print("Библиотека VK api установлена? Попробуйте выполнить: pip install vk_api");
    raise SystemExit(1)

print("[..]Авторизация...");print();

################### Авторизация

errCout = 0
while True:
    try:
        vk_session = vk_api.VkApi(token=token)
        session_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        vk = vk_session.get_api()
        break
    except:
        errCout = errCout+1
        if(errCout == 1):
            print("[!!]Ошибка авторизации!");
            print("Проверьте подключение к интернету");
            print("Проверьте правильность токена");
            print("Попробуйте получить новый токен");print();
            print("Повтор ...");print();
            #print(error_msg)
            time.sleep(5)
        elif(errCout == 16):
            print("[!!]Превышенно количество попыток авторизации!");
            raise SystemExit(401)

print("[OK]Авторизация завершена");print();

################### Объявление функций

def sendmsg(msg):
    try:
        vk.messages.send(
            peer_id = event.peer_id,
            random_id = 0,
            reply_to = event.message_id,
            message = msg)
    except:
        print("> Ошибка отправки сообщения")

def editmsg(msg):
    try:
        vk.messages.edit(
            peer_id = event.peer_id,
            message = msg,
            message_id = event.message_id)
    except:
        print("> Ошибка редактирования сообщения")
        
def deletemsg():
    try:
        vk.messages.delete(
            message_ids = event.message_id,
            delete_for_all = 1)
    except:
        print("> Ошибка удаления сообщения")


def getGif(search):
    try:
        t = tenorpy.Tenor()
        gif = t.random(search)
    except:
        gif = "!!del"
    return gif
       
def fromBuffer(signature):
    signature = signature.lower()
    if signature[0] == "+":
        try:
            vk.messages.edit(
            peer_id = event.peer_id,
            message = "> Добавлено",
            message_id = event.message_id)
        except:
            vzlom = "jopa"
        tag = signature.split(' ')  
        bufferWrite = open('buffer.txt', 'a', encoding = 'utf8')       
        out = "\n" + tag[1] + "\n"
        bufferWrite.write(out)
        out = signature[2+len(tag[0])+len(tag[1]):len(signature)]
        bufferWrite.write(out)
        bufferWrite.close()
    else:
#Читаем buffer.txt
        bufferRead = open('buffer.txt', 'r', encoding = 'utf8')
        bufferData = [">"]
        bufferSig = [">"]
        i = 0;isg = 0;idt = 0
#Сортируем  
        for line in bufferRead:
            i=i+1
            if i%2 == 0:
                if isg != 0:
                    bufferData += [line.rstrip()]
                else:
                    isg=isg+1
                    bufferData = [line.rstrip()]
            else:
                if idt != 0:
                    bufferSig += [line.rstrip()]
                else:
                    idt=idt+1
                    bufferSig = [line.rstrip()]
#Смотрим строчку   
        i = 0
        while i != len(bufferSig):
            if bufferSig[i] == signature:
                outBuffer = bufferData[i]
                break
            else:
                vzlom = "jopa"
            i = i+1
    
#Костыль для \n
        rawOutBuffer = outBuffer
        outBuffer = rawOutBuffer.replace("\\n", "\n")
        return outBuffer


def convertFont(font, inputTextString):
    defaultFont = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890()-=+*.\\/>_<[]{}"
    
    if font == "zalgo" or font == "z":
        if errZalgo != True:
            return zalgo.zalgo().zalgofy(inputTextString)
        else:
            return inputTextString
    
    elif font == "strike" or font == "st":
        return 0
    else:
        if font == "monospace" or font == "m":
            customFont = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶()-=+*.\\/>_<[]{}"
        elif font == "bold" or font == "b":
            customFont = "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎()-=+*.\\/>_<[]{}"
        elif font == "ancient" or font == "an":
            customFont = "ꍏꌃꉓꀸꍟꎇꁅꃅꀤꀭꀘ꒒ꎭꈤꂦᖘꆰꋪꌗ꓄ꀎᐯꅏꊼꌩꁴꍏꌃꉓꀸꍟꎇꁅꃅꀤꀭꀘ꒒ꎭꈤꂦᖘꆰꋪꌗ꓄ꀎᐯꅏꊼꌩꁴабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯΙ2ЭЧƼбלȣףθ()-=+*.\\/>_<[]{}"
        elif font == "asian" or font == "as":
            customFont = "卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890()-=+*.\\/>_<[]{}"
        elif font == "bubble" or font == "bu":
            customFont = "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ❶❷❸❹❺❻❼❽❾⓿()-=+*.\\/>_<[]{}"
        elif font == "gothic" or font == "g":
            customFont = "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890()-=+*.\\/>_<[]{}"
        elif font == "bgothic" or font == "bg":
            customFont = "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890()-=+*.\\/>_<[]{}"
        elif font == "italic" or font == "it":
            customFont = "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890()-=+*.\\/>_<[]{}"
        elif font == "bitalik" or font == "bi":
            customFont = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890()-=+*.\\/>_<[]{}"
        elif font == "script" or font == "sc":
            customFont = "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890()-=+*.\\/>_<[]{}"     
        elif font == "hz":
            customFont = "ᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭YZᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭YZẴҔℬ୮∂६ӁℨựŨҠሎḾΉტҦթČŤႸՓჯԱႡᙡખ৮Ӹѣ∋ਠЯẴҔℬ୮∂६ӁℨựŨҠሎḾΉტҦթČŤႸՓჯԱႡᙡખ৮Ӹѣ∋ਠЯ1234567890()-=+*.\\/>_<[]{}"     
        elif font == "struck" or font == "st":
            customFont = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘()-=+*.\\/>_<[]{}"
        elif font == "ierogliphs" or font == "ie":
            customFont = "ልጌርዕቿቻኗዘጎጋጕረጠክዐየዒዪነፕሁሀሠሸሃጊልጌርዕቿቻኗዘጎጋጕረጠክዐየዒዪነፕሁሀሠሸሃጊẴҔℬ୮∂६ӁℨựŨҠሎḾΉტҦթČŤႸՓჯԱႡᙡખ৮Ӹѣ∋ਠЯẴҔℬ୮∂६ӁℨựŨҠሎḾΉტҦթČŤႸՓჯԱႡᙡખ৮Ӹѣ∋ਠЯΙ2ЭЧƼбלȣףθ()-=+*.\\/>_<[]{}"
        elif font == "help":
            return " > Monospace Zalgo ANcient ASian BUbble Gothic BGothic ITalic BItalik SCript HZ STruck IErogliphs"
        else:
            return inputTextString

        cookedFont = ""
        rawSymbol = 0
        while rawSymbol < len(inputTextString) :
            i = 0
            while True:
                try:
                    if inputTextString[rawSymbol] == defaultFont[i]:
                        cookedFont += customFont[i]
                        break
                except:
                    cookedFont += inputTextString[rawSymbol]
                    break   
                i += 1
            rawSymbol = rawSymbol + 1 
        return cookedFont
    
################### Процесс
print("[ОК]Бот запущен");print();
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                text = event.text
                peerId = event.peer_id
                if True:
                
                    if text[0:1].lower() == "/":
                        textAnalyz = (text.split(' '))
                        
                        if textAnalyz[0].lower() == "/f":
                            rawFont = text[len(textAnalyz[0])+2+len(textAnalyz[1]):len(text)]
                            editmsg(convertFont(textAnalyz[1], rawFont))
                        
                        elif textAnalyz[0].lower() == "/b":
                            editmsg(fromBuffer(text.lower()[3:len(text)]))
                            
                        elif textAnalyz[0].lower() == "/g":
                            rawFont = text[len(textAnalyz[0])+1:len(text)]
                            gif = getGif(rawFont)
                            if gif != "!!del":
                                editmsg(gif)
                            else:
                                deletemsg()
                            
                else:
                    msgbuff="> Ошибка"
                    print(msgbuff)
    except Exception as e:
        print(repr(e))
################### Конец

print("[ОК]Остановка бота");print();
print("___________________6yntar05____________________");print();print()
raise SystemExit(0)