import curses.textpad
import random
from time import sleep, time, gmtime, strftime
from curses import wrapper
from constants import *
import texts_es
import texts_en
import string


def bye_bye(stdscreen, lang):
    if lang == 0:
        bye_bye_text = texts_en.bye_bye_text
    else:
        bye_bye_text = texts_es.bye_bye_text

    stdscreen.clear()
    stdscreen.addstr(MIDDLE_Y, MIDDLE_X - len(bye_bye_text) // 2, bye_bye_text)
    stdscreen.refresh()
    stdscreen.getch()
    exit()


def language(stdscreen):
    stdscreen.clear()
    current_text = list()
    while True:
        stdscreen.clear()
        stdscreen.addstr(
            MIDDLE_Y - 2, MIDDLE_X - len(texts_en.lang_0) // 2, texts_en.lang_0
        )
        stdscreen.addstr(
            MIDDLE_Y - 1, MIDDLE_X - len(texts_en.lang_1) - 1, texts_en.lang_1
        )
        stdscreen.addstr(MIDDLE_Y - 1, MIDDLE_X + 2, texts_en.lang_2)

        for current_text_index, letter in enumerate(current_text):
            color = curses.color_pair(GREEN)
            try:
                if texts_en.lang_1[current_text_index] != letter:
                    if letter == " ":
                        color = curses.color_pair(WRONG_SPACE)
                    else:
                        color = curses.color_pair(RED)
            except IndexError:
                if letter == " ":
                    color = curses.color_pair(WRONG_SPACE)
                else:
                    color = curses.color_pair(RED)

            stdscreen.addstr(
                MIDDLE_Y - 1,
                MIDDLE_X + current_text_index - len(texts_en.lang_1) - 1,
                letter,
                color,
            )
            color = curses.color_pair(GREEN)
            try:
                if texts_en.lang_2[current_text_index] != letter:
                    if letter == " ":
                        color = curses.color_pair(WRONG_SPACE)
                    else:
                        color = curses.color_pair(RED)
            except IndexError:
                if letter == " ":
                    color = curses.color_pair(WRONG_SPACE)
                else:
                    color = curses.color_pair(RED)
            stdscreen.addstr(
                MIDDLE_Y - 1,
                MIDDLE_X + current_text_index + 2,
                letter,
                color,
            )

        stdscreen.refresh()

        key = stdscreen.getkey()
        if (
            key in string.ascii_letters
            or key in ("KEY_BACKSPACE", "\b", "\x7f")
            or key == "Ã"
        ):
            if key in ("KEY_BACKSPACE", "\b", "\x7f"):
                if len(current_text) > 0:
                    current_text.pop()
            elif key == "Ã":
                current_text.append("ñ")
            elif len(current_text) <= len(texts_en.lang_1):
                current_text.append(key)
        elif ord(key) == 10:
            if texts_en.lang_1 == "".join(current_text):
                lang = 0
                return start(stdscreen, lang)
            elif texts_en.lang_2 == "".join(current_text):
                lang = 1
                return start(stdscreen, lang)


def start(stdscreen, lang):
    if lang == 0:
        start_0 = texts_en.start_0
        start_1 = texts_en.start_1
        start_2 = texts_en.start_2
        start_3 = texts_en.start_3
        start_4 = texts_en.start_4
        start_5 = texts_en.start_5
        start_6 = texts_en.start_6
        me = texts_en.me
    else:
        start_0 = texts_es.start_0
        start_1 = texts_es.start_1
        start_2 = texts_es.start_2
        start_3 = texts_es.start_3
        start_4 = texts_es.start_4
        start_5 = texts_es.start_5
        start_6 = texts_es.start_6

        me = texts_es.me

    stdscreen.clear()
    stdscreen.addstr(MIDDLE_Y - 7, MIDDLE_X - len(start_0) // 2, start_0, curses.A_BOLD)

    stdscreen.addstr(MIDDLE_Y - 5, MIDDLE_X - len(start_1) // 2, start_1)
    stdscreen.addstr(MIDDLE_Y - 4, MIDDLE_X - len(start_2) // 2, start_2)
    stdscreen.addstr(MIDDLE_Y - 3, MIDDLE_X - len(start_3) // 2, start_3)
    stdscreen.addstr(MIDDLE_Y - 2, MIDDLE_X - len(start_4) // 2, start_4)

    stdscreen.addstr(MIDDLE_Y, MIDDLE_X - len(start_5) // 2, start_5, curses.A_BLINK)

    stdscreen.addstr(
        MIDDLE_Y + 2, MIDDLE_X - len(start_6) // 2, start_6, curses.A_BLINK
    )

    stdscreen.addstr(MAX_Y - 2, MIDDLE_X - len(me) // 2, me, curses.A_ITALIC)

    stdscreen.refresh()

    key = stdscreen.getkey()

    if ord(key) == 27:
        return bye_bye(stdscreen, lang)

    if key.lower() == "l":
        return language(stdscreen)
    else:
        return primary_main(stdscreen, lang)


def reset_users(stdscreen, lang):
    if lang == 0:
        users_reset = texts_en.users_reset
        end_0 = texts_en.end_0
        end_1 = texts_en.end_1

    else:
        users_reset = texts_es.users_reset
        end_0 = texts_es.end_0
        end_1 = texts_es.end_1

    stdscreen.clear()
    stdscreen.addstr(MIDDLE_Y, MIDDLE_X - len(users_reset) // 2, users_reset)
    stdscreen.addstr(MIDDLE_Y + 2, MIDDLE_X - len(end_0) // 2, end_0, curses.A_BLINK)
    stdscreen.addstr(MIDDLE_Y + 4, MIDDLE_X - len(end_1) // 2, end_1, curses.A_BLINK)

    with open(".users_top", "w") as texts:
        texts.write(f"")

    stdscreen.refresh()
    key = stdscreen.getkey()
    if ord(key) == 27:
        curses.curs_set(1)
        return
    if ord(key) == 10:
        main(stdscreen)


def store_users(stdscreen, user, lang, wpm_speed):

    if lang == 0:
        top_users = texts_en.top_users
        end_0 = texts_en.end_0
        end_1 = texts_en.end_1
        end_2 = texts_en.end_2
        wpm = texts_en.wpm

    else:
        top_users = texts_es.top_users
        end_0 = texts_es.end_0
        end_1 = texts_es.end_1
        end_2 = texts_es.end_2
        wpm = texts_es.wpm

    stdscreen.clear()

    date_and_time = strftime("%d/%b/%Y-%H:%M:%S", gmtime())

    with open(".users_top", "a") as texts:
        texts.write(f"{user.strip()} {wpm_speed} {date_and_time}\n")

    with open(".users_top", "r") as texts:
        lines = texts.readlines()
    users_data = list()
    for y, line in enumerate(lines):
        stdscreen.addstr(MIDDLE_Y - 13, MIDDLE_X - len(top_users) // 2, top_users)
        y += 1
        line = line.split(" ")
        date = line[-1]
        users = line[:-2][0]
        wpm = line[-2]

        users_dict = {"user": users, "wpm": wpm, "date": date}
        users_data.append(users_dict)

    users_data.sort(key=lambda item: item["wpm"], reverse=True)
    for y, x in enumerate(users_data):
        y += 1
        user = x["user"]
        if len(user) < 10:
            user += " " * (10 - len(user))
        user_print = f'{y}: {user} -> {x["wpm"]} {wpm} - {x["date"]}'
        stdscreen.addstr(MIDDLE_Y - 13 + y, MIDDLE_X - len(user_print) // 2, user_print)
        if y == 10:
            break
    stdscreen.addstr(MAX_Y - 5, MIDDLE_X - len(end_0) // 2, end_0, curses.A_BLINK)
    stdscreen.addstr(MAX_Y - 6, MIDDLE_X - len(end_1) // 2, end_1, curses.A_BLINK)
    stdscreen.addstr(MAX_Y - 7, MIDDLE_X - len(end_2) // 2, end_2, curses.A_BLINK)
    stdscreen.refresh()

    return


def ending(stdscreen, lang, wpm_speed):

    if lang == 0:
        finish_0 = texts_en.finish_0
        finish_1 = texts_en.finish_1
        alias = texts_en.alias

    else:
        finish_0 = texts_es.finish_0
        finish_1 = texts_es.finish_1
        alias = texts_es.alias

    stdscreen.addstr(MAX_Y - 6, MIDDLE_X - len(finish_0) // 2, finish_0)
    stdscreen.addstr(MAX_Y - 5, MIDDLE_X - len(finish_1) // 2, finish_1)
    stdscreen.addstr(MAX_Y - 4, MIDDLE_X - len(alias) // 2, alias)
    stdscreen.refresh()
    win = curses.newwin(1, 10, MAX_Y - 4, MIDDLE_X + len(alias) // 2 + 2)
    tb = curses.textpad.Textbox(win)
    tb.edit()
    return store_users(
        stdscreen, tb.gather().strip().replace(" ", "_"), lang, wpm_speed
    )


def load_texts():
    with open("sentences.txt", "r") as texts:
        lines = texts.readlines()
        return str(random.choice(lines).strip())


def display_text(stdscreen, text, current_text, wpm_speed, lang):

    if lang == 0:
        wpm = texts_en.wpm

    else:
        wpm = texts_es.wpm

    stdscreen.addstr(MIDDLE_Y, MIDDLE_X - len(text) // 2, text)

    if 30 < wpm_speed < 39:
        color = curses.color_pair(WHITE)
    elif 39 <= wpm_speed < 49:
        color = curses.color_pair(GREEN)
    elif wpm_speed >= 49:
        color = curses.color_pair(CYAN)
    else:
        color = curses.color_pair(RED)

    stdscreen.addstr(MIDDLE_Y + 1, MIDDLE_X - 4, f"{wpm} -> {wpm_speed}", color)

    for current_text_index, letter in enumerate(current_text):
        color = curses.color_pair(GREEN)
        if text[current_text_index] != letter:
            if letter == " ":
                color = curses.color_pair(WRONG_SPACE)
            else:
                color = curses.color_pair(RED)

        stdscreen.addstr(
            MIDDLE_Y, MIDDLE_X + current_text_index - len(text) // 2, letter, color
        )

    return


def type_speed(stdscreen, lang):
    text = load_texts()
    current_text = list()

    text_len = text.split(" ")
    media_word_length = len(text) / len(text_len)

    start_time = time()
    stdscreen.nodelay(True)

    while True:
        end_time = max(time() - start_time, 1)
        wpm_speed = round((len(current_text) / (end_time / 60)) / media_word_length)

        stdscreen.erase()

        display_text(stdscreen, text, current_text, wpm_speed, lang)

        stdscreen.refresh()
        try:
            key = stdscreen.getkey()
        except curses.error:
            continue

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif ord(key) == 27:
            break
        elif len(current_text) < len(text) and key != "KEY_ENTER":
            current_text.append(key)
        elif text == "".join(current_text):
            stdscreen.nodelay(False)
            ending(stdscreen, lang, wpm_speed)
            break


def most_long_text():
    with open("sentences.txt", "r") as texts:
        lines = texts.readlines()

    max_line = 0
    max_line_text = ""
    for line in lines:
        if len(line) > max_line:
            max_line = len(line)
            max_line_text = line

    return max_line, max_line_text


def main(stdscreen):
    n_cols, text = most_long_text()
    cols = n_cols + SECURITY_COLS

    if curses.LINES < LINES or curses.COLS < cols:
        print(
            f"\n[ERROR ENGLISH] -> Verify that you have a terminal with {LINES} lines and {cols} columns."
            f"I think that actually you have a terminal with {curses.LINES} lines and {curses.COLS} columns."
            f"You can solve this error this by resizing the terminal."
            f"The terminal lines are specified by the long of the length of the texts specified on the sentences.txt "
            f"file.This window its gonna close in 10 seconds."
            f"[ERROR ESPAÑOL] -> Verfica que tengas una terminal con {LINES} lineas y {cols} columnas."
            f"Creo que actualmente tenes una terminal con {curses.LINES} lineas y {curses.COLS} columnas."
            f"Podes arreglar este error agrandando la terminal."
            f"Las lineas necesarias son especificadas por la longitud de los textos especificados en el archivo "
            f"sentences.txt. Esta ventana se cerrara en 10 segundos"

        )
        sleep(10)
        exit()

    curses.init_pair(GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(ORANGE, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(CYAN, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(WRONG_SPACE, curses.COLOR_RED, curses.COLOR_RED)

    curses.curs_set(0)

    language(stdscreen)


def primary_main(stdscreen, lang):
    while True:
        type_speed(stdscreen, lang)
        key = stdscreen.getkey()
        if ord(key) == 27:
            curses.curs_set(1)
            return bye_bye(stdscreen, lang)
        if ord(key) == 10:
            primary_main(stdscreen, lang)
            return bye_bye(stdscreen, lang)
        if key == "r":
            reset_users(stdscreen, lang)
            return bye_bye(stdscreen, lang)


wrapper(main)
