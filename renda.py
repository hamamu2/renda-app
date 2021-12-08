from pynput.mouse import Button, Controller
ctrl1 = Controller()
from pynput.keyboard import Key, Listener, Controller
ctrl2 = Controller()
import pyautogui
import threading, time
import json
import os
import webbrowser
import time
import win32gui
import win32con
import win32api
import pyautogui
import colorama
from colorama import Fore
colorama.init(autoreset=True)

url = "https://github.com/hamamu2/renda-app/archive/refs/heads/main.zip"
try:
    with open("config.json", 'r', encoding='utf-8') as setting:
        set = json.load(setting)
except:
    print(Fore.YELLOW+'config.json が間違っているか存在しません\n'+Fore.RESET+'修正しますか？ 再ダウンロードしますか？\n1 修正する\n2 再ダウンロードする')
    def ee1():
        e2 = input('>> ')
        if e2 == "1" or e2 == "１":
            try:
                webbrowser.open("config.json")
                exit(2)
            except:
                print('config.json が存在しません\n再ダウンロードしますか？\nY/N')
                def ee2():
                    e3 = input('>> ')
                    if e3 == "Y" or e3 == "y":
                        webbrowser.open("https://github.com/hamamu2/renda-app/archive/refs/heads/main.zip")
                        exit(2)
                    elif e3 == "N" or e3 == "n":
                        print('再ダウンロードはこちらからできます\nhttps://github.com/hamamu2/renda-app/archive/refs/heads/main.zip')
                        exit(10)
                    else:
                        print(Fore.LIGHTRED_EX+'Y/N')
                        ee2()
                ee2()
        elif e2 == "2" or e2 == "２":
            webbrowser.open("https://github.com/hamamu2/renda-app/archive/refs/heads/main.zip")
            exit(2)
        else:
            print(Fore.LIGHTRED_EX+'1 or 2')
            ee1()
    ee1()

k_or_m = set['Keyboard or Mouse']
use_key = set['Use_Key']
mouse = set['Mouse_Click']
keyboard = set['Press_Key']

default = "1.0"
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
    reset = "1"
    with open('連打間隔.txt', 'w') as f:
        data = f.write(reset)
        set = float(data)
        f.close()
    print(Fore.YELLOW+'txtファイルに不備があったためデフォルトに書き換えられました')
    print(Fore.LIGHTGREEN_EX+f'現在の連打間隔: {set}秒 (デフォルト)')



import ctypes
from tkinter import messagebox
import tkinter as tk
root = tk.Tk()
root.withdraw()


res = messagebox.askyesno(f'{app_name} - 連打間隔の調整', f'連打間隔を変更をしますか？\n\n現在の連打間隔は{set}秒です\nデフォルトは{default}秒です')
if res == True:
    memoapp = win32gui.FindWindow(None,f'{app_name}')
    win32gui.SetForegroundWindow(memoapp)
    print('変更する値を入力してください')
    try:
        def input_miss():
            txt = input('>> ')
            try:
                with open('連打間隔.txt', 'w') as f:
                    data = f.write(txt)
                    set = float(txt)
                print(Fore.LIGHTGREEN_EX+f'{set}秒に設定しました')
            except:
                print(Fore.YELLOW+'数字を入力してください')
                input_miss()
        input_miss()
    except:
        print('連打間隔が小さすぎます')

with open('連打間隔.txt', 'r') as f:
    data = f.read()
    set = float(data)

if k_or_m == "m" or k_or_m == "M":
    print(f'{use_key}キーを押してマウス{mouse}の連打を{set}秒ごとに行います')
elif k_or_m == "k" or k_or_m == "K":
    print(f'{use_key}キーを押してキーボード{keyboard}の連打を{set}秒ごとに行います')

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
                try:
                    ctrl2.press(keyboard) #a連打
                except:
                    print('連打可能なキーは 0～9 , a～z です')
                    exit(2)
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
    if use_key == "insert" or use_key == "ins" or use_key == "INSERT" or use_key == "INS":
        if key == Key.insert:
            if e.isSet():
                e.clear()
                print(Fore.RED+'×連打を停止します')
            else:
                print(Fore.LIGHTGREEN_EX+'○連打を開始します')
                e.set()

        if key == Key.esc:
            print('終了しました')
            exit(3)
    elif use_key == "f12" or use_key == "F12":
        if key == Key.f12:
            if e.isSet():
                e.clear()
                print(Fore.RED+'×連打を停止します')
            else:
                print(Fore.LIGHTGREEN_EX+'○連打を開始します')
                e.set()

        if key == Key.esc:
            print('終了しました')
            exit(3)
    elif use_key == "f11" or use_key == "F11":
        if key == Key.f11:
            if e.isSet():
                e.clear()
                print(Fore.RED+'×連打を停止します')
            else:
                print(Fore.LIGHTGREEN_EX+'○連打を開始します')
                e.set()

        if key == Key.esc:
            print('終了しました')
            exit(3)
    else:
        print('使用可能なキーは現在 insert , f11 , f12 のみです')

with Listener(on_press=on_press) as listener:
    listener.join()
