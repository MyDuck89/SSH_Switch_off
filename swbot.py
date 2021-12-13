import telebot
import paramiko

HELP = '''
/reboot - перезагрузка устройства
/shutdown - выключение устройства
/help - список действий
'''
token = '' #Токен Вашего Телеграм-бота


ip = '192.168.0.105' #ip Вашего устройства
port = 22 #порт 22 - оставляем
user = 'amatveev' #имя пользователя на устройстве
password = 'password' #пароль пользователя на устройстве


bot = telebot.TeleBot(token)


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, port, user, password)


@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['shutdown'])
def shutdown(message):
    bot.send_message(message.chat.id, 'Выключение системы Ubuntu')
    stdout = client.exec_command('shutdown')
    result = stdout.read()
    
@bot.message_handler(commands=['reboot'])
def reboot(message):
    bot.send_message(message.chat.id, 'Перезагрузка системы Ubuntu')
    stdout = client.exec_command('reboot')
    result = stdout.read()
    

bot.polling(none_stop=True)
