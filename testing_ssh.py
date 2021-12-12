import paramiko

ip = '192.168.0.105'
port = 22
user = 'amatveev'
password = 'password'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(ip, port, user, password)

print(f'reset - переапуск, off - выключение')

while True:
  
    temp = str(input('Введите уоманду: '))
#   
    if temp == 'reset':
        stdin, stdout, stderr = client.exec_command('reboot')
        result = stdout.read()
        print('Перезагрузка...')
    elif temp == 'off':
        stdin, stdout, stderr = client.exec_command('shutdown')
        result = stdout.read()
        print('Выключение...')
client.close()