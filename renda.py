from pynput.mouse import Button, Controller
ctrl1 = Controller()
from pynput.keyboard import Key, Listener, Controller
ctrl2 = Controller()
import pyautogui
import threading, time
import json
import os
import time
import win32gui
import win32con
import win32api
import pyautogui
import colorama
from colorama import Fore
colorama.init(autoreset=True)

url = "https://"
try:
    with open("config.json", 'r', encoding='utf-8') as setting:
        set = json.load(setting)
except:
    print('config.json が見つかりませんでした\n再ダウンロードしますか？\nY/N')
    ask = input('>> ')
    if ask == "Y" or ask == "y":
        open('')
try:
    k_or_m = set['Keyboard or Mouse']
    use_key = set['Use_Key']
    mouse = set['Mouse_Click']
    keyboard = set['Press_Key']
except:
    print('config.json が間違っています\n修正するか再ダウンロードしてください')

app_name = "連打ツール"
os.system(
f"TITLE {app_name}"
)

try:
    os.mkdir('連打間隔.txt')
except:
    pass


try:
    with open('連打間隔.txt', 'r') as f:
        data = f.read()
        set = float(data)
        f.close()
    print(Fore.LIGHTGREEN_EX+f'現在の連打間隔: {set}秒')
except:
    default = "1"
    with open('連打間隔.txt', 'w') as f:
        data = f.write(default)
        set = float(data)
        f.close()
    print(Fore.YELLOW+'txtファイルに不備があったためデフォルトに書き換えられました')
    print(Fore.LIGHTGREEN_EX+f'現在の連打間隔: {set}秒 (デフォルト)')



import ctypes
from tkinter import messagebox
import tkinter as tk
root = tk.Tk()
root.withdraw()

res = messagebox.askyesno(f'{app_name} - 連打間隔の調整', f'連打間隔を変更をしますか？\n\n現在の連打間隔は{set}秒です')
if res == True:
    memoapp = win32gui.FindWindow(None,f'{app_name}')
    win32gui.SetForegroundWindow(memoapp)
    print('変更する値を入力してください')
    def input_miss():
        txt = input('>> ')
        try:
            with open('連打間隔.txt', 'w') as f:
                data = f.write(txt)
                set = float(txt)
            print(f'{set}秒に設定しました')
        except:
            print(Fore.YELLOW+'数字を入力してください')
            input_miss()
    input_miss()

with open('連打間隔.txt', 'r') as f:
    data = f.read()
    set = float(data)

def mouseclick(e):
    while True:
        if e.isSet():
            if k_or_m == "m" or k_or_m == "M":
                if mouse == "left":
                    ctrl1.click(Button.left) #左クリック
                elif mouse == "right":
                    ctrl1.click(Button.right) #左クリック
                else:
                    print('"Mouse_Click" には"left"又は"right"と入力してください')
            elif k_or_m == "k" or k_or_m == "K":
                ctrl2.press(keyboard) #a連打
            else:
                print('"Keyboard or Mouse" の設定が間違っています\n"m"(mouse)又は"k"(keyboard)と入力してください')
                open('config.json')
        time.sleep(set)

e = threading.Event()
t = threading.Thread(target=mouseclick, args=(e,))
t.setDaemon(True)
t.start()

def on_press(key):
    global e
    if key == Key.insert:
        if e.isSet():
            e.clear()
            print(Fore.RED+'×無効化しました')
        else:
            print(Fore.LIGHTGREEN_EX+'○有効化しました')
            e.set()

    if key == Key.esc:
        print('終了しました')
        exit(3)

with Listener(on_press=on_press) as listener:
    listener.join()
