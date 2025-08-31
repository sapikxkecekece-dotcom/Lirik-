import sys
from time import sleep
import time

def printLyrics():
    lines = [
         ("karna kamu cantik", 0.12),
         ("kan ku beri segalanya apa yg ku punya", 0.09),
         ("dan hatimu baik     ", 0.13),
         ("sempurnalah duniaku saat kau di sisiku\n", 0.09),
         ("bukan karna make up di wajah mu", 0.09),
         ("atau lipstik merah itu    ", 0.11),
         ("lembut hati tutur kata", 0.09),
         ("terciptalah cinta yg kupuja\n", 0.11),
    ]

    delays = [0.6] * len(lines)  # delay antar baris lebih panjang

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        print()
        time.sleep(delays[i])

printLyrics()