import random
import logger_new
from telegram import Update
from telegram.ext import ConversationHandler


user_step: int
ai_step: int
info: str
heap_value: int
candies_remained: int
max_candies_per_move: int

USER_STEP, GAME_ERROR = range(2)


def start_game_bot(update: Update, _):
    global info

    global heap_value, max_candies_per_move, candies_remained

    heap_value = random.randint(35, 3001)
    candies_remained = heap_value
    max_candies_per_move = random.randint(heap_value // 7, heap_value // 3 + 1)

    info = f'{update.message.from_user.first_name}' + ', ' + f'{update.message.from_user.id}'

    logger_new.logger.info(f'Пользователь // {info} // вошёл в чат')

    update.message.reply_text('Привет! Готов начать игру?\n\nВ игре тебе будет необходимо брать '
                              'конфеты, отправляя в сообщении их количество.\n'
                              'Побеждает тот, кто первым забирает последнюю кучу конфет\n'
                              '/game - начать игру\n'
                              '/return - начать сначала\n'
                              '/exit - закончить игру')


def start(update: Update, _):

    global candies_remained, max_candies_per_move

    logger_new.logger.info('Start')

    update.message.reply_text(f'Осталось {candies_remained} конфет.\nВведи количество конфет, от 1 до {max_candies_per_move}, которое хочешь взять')
    return USER_STEP


def game_step(update: Update, _):
    # принимает сообщение юзера от start, главный цикл игры

    global user_step
    global ai_step
    global candies_remained
    global heap_value
    global max_candies_per_move

    user_step = update.message.text
    if user_step.isdigit():
        if 1 <= int(user_step) <= max_candies_per_move:
            candies_remained = candies_remained - int(user_step)
        else:

            logger_new.logger.error('Некорректное число')

            update.message.reply_text(f'Тебе необходимо взять от 1 до {max_candies_per_move} конфет.\nВведи корректное число')
            update.message.reply_text(f'Введи количество конфет, которое хочешь взять')
            return USER_STEP
    else:

        logger_new.logger.error('Некорректное сообщение')

        update.message.reply_text(f'Тебе необходимо взять от 1 до {max_candies_per_move} конфет.\nВведи корректное число')
        update.message.reply_text(f'Введи количество конфет, которое хочешь взять')
        return USER_STEP

    ai_step = candies_remained % (max_candies_per_move + 1)
    update.message.reply_text(f'Осталось {candies_remained} конфет')
    if candies_remained <= 0:
        update.message.reply_text(f'Ты победил!')
        return ConversationHandler.END
    candies_remained = candies_remained - ai_step
    update.message.reply_text(f'Бот взял {ai_step} конфет.\nОсталось {candies_remained} конфет')
    if candies_remained <= 0:
        update.message.reply_text(f'Ты проиграл!')
        return ConversationHandler.END
    update.message.reply_text(f'Введи количество конфет, которое хочешь взять')
    return USER_STEP


def exit_user(update: Update, _):

    #выход из бота, конец диалога

    logger_new.logger.info(f'Пользователь // {info} // вышел из чата')

    update.message.reply_text('Игра окончена.\nЧтобы начать заново, введи /game')
