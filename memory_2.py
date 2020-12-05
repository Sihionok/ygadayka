import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
key = "c4cf0a0661e38f87149ffdb72f81e97ef81fd4fec7c597d196bdc4e9a10291e328b0ea49cbd92693bd805"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)


def send_message(user_id, message, file_vk_url = None, keyboard = None):
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           "random_id":randint(1,1000) ,
                           'message': message,
                           'attachment':file_vk_url,
                           'keyboard':keyboard}
                          )

def get_keyboard_x_y(x,y):
    keyboard = VkKeyboard(one_time=True)
    first = True
    for i in range(y):
        if not first:
            keyboard.add_line()  # Переход на вторую строку
        first = False
        for j in range(x):
            keyboard.add_button('y '+str(i)+','+'x '+str(j))
    return keyboard.get_keyboard()
def generate_keyboard(variants, w=3):
    n = len(variants)
    x = w
    y = n//w
    if n%w:
        y+=1
    n_var = 0
    keyboard = VkKeyboard(one_time=True)
    first = True
    for i in range(y):
        if not first:
            keyboard.add_line()  # Переход на вторую строку
        first = False
        for j in range(x):
            if n_var < n:
                keyboard.add_button(variants[n_var], color=VkKeyboardColor.POSITIVE)
                n_var += 1
    return keyboard.get_keyboard()

main_keyboard = generate_keyboard(['об авторе','игра','тест','пинг'], w=3)
game_keyboard = generate_keyboard(['камень','ножницы','бумага','назад'], w=1)
back_keyboard = generate_keyboard(['назад'], w=1)
ping_keyboard = generate_keyboard(['назад','пинг'], w=1)
users = {} #       kryakrya

    # Работа с сообщениями

  def random_guesses(message):
  guesses_made = 0

  name = str(message.chat.first_name) + " " + str(message.chat.last_name)

  number = random.randint(1, 30)
    bot.send_message(message.chat.id, '{0}, я загадал число между 1 и 30. Сможешь угадать?'.format(name))

  while guesses_made < 6:

     bot.send_message(message.chat.id, "Введите число")
    guess = int(message.text)

    guesses_made += 1

    if guess < number:
        bot.send_message(message.user_id, 'Твое число меньше того, что я загадал.')

    if guess > number:
        bot.send_message(message.user_id, 'Твое число больше загаданного мной.')

    if guess == number:
        bot.send_message(message.user_id, 'Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
    else:
        bot.send_message(message.user_id, 'не угадал! Я загадал число {0}'.format(number))
  
  
  
  
  
  
  longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            user_id = event.user_id
            text = event.text.lower()
            if text == 'об авторе':
                send_message(user_id, 'Damir',  keyboard = back_keyboard )
            elif text == 'игра':
                send_message(user_id, 'GAME',  keyboard = game_keyboard )
                
            elif text == 'тест':
                send_message(user_id, 'тест',  keyboard = back_keyboard )
            elif text == 'пинг':
                send_message(user_id, 'понг',  keyboard = ping_keyboard )
            else:
                send_message(user_id, 'Привет',  keyboard = main_keyboard )

                
            
