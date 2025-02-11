#!/usr/bin/env python3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from morsecodelib import sound as morseSound
from morsecodelib.config import config as morseConfig
import tkinter as tk
import random
import argparse
import time

def play_character():
    c = random.choice(characters)
    lbl.configure(text=c)
    app.update()
    player.text_to_sound(c)
    for r in range(conf.repeat-1):
        time.sleep(morseConfig.DAH_DURATION)
        player.text_to_sound(c)
    app.after(conf.delay, play_character) 

def parse_config():
    parser = argparse.ArgumentParser(description='Learn CW while you work!')
    parser.add_argument('-w', '--wpm', action='store', dest='wpm', type=int, default=20, help='Speed in WPM. Default 20')
    parser.add_argument('-t', '--tone', action='store', dest='tone', type=int, default=600, help='Tone frequency in Hz. Default 600')
    parser.add_argument('-d', '--delay', action='store', dest='delay', type=int, default=1000, help='Delay between characters in ms. Default 1000')
    parser.add_argument('-r', '--repeat', action='store', dest='repeat', type=int, default=1, help='Number of repetitions of each character.')
    parser.add_argument('-s', '--size', action='store', dest='size', type=str, default='normal', help='Windows size in small, normal or big. Default is normal')
    parser.add_argument('--debug', action='store_true', dest='debug', default=False, help='Dispaly debug information.')
    return parser.parse_args()

def w_size(size):
        if size == 'small':
                return "100x60"
        if size == 'normal':
                return "200x120"
        if size == 'big':
                return "400x240"

def f_size(size):
        if size == 'small':
                return 40
        if size == 'normal':
                return 75
        if size == 'big':
                return 140


characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "O", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

if __name__ == '__main__':
    conf = parse_config()
    if conf.debug:
        print('Speed     = {!r}'.format(conf.wpm))
        print('Tone      = {!r}'.format(conf.tone))
        print('Delay     = {!r}'.format(conf.delay))
        print('Repeat    = {!r}'.format(conf.repeat))
        print('Size      = {!r}'.format(conf.size))

    morseConfig.WORDS_PER_MINUTE = conf.wpm
    morseConfig.FREQUENCY = conf.tone

    app = tk.Tk()
    player = morseSound.MorseSoundPlayer()

    app.title('Subliminal CW')
    app.geometry(w_size(conf.size))
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    
    lbl = tk.Label(app, font=("Courier", f_size(conf.size), 'bold'), text='')
    lbl.grid(column=0, row=0)
    
    app.after(conf.delay, play_character)
    app.mainloop()
