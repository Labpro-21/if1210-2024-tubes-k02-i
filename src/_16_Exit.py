import sys
import os
import time
import _02_Login

def game_exit(username):
    '''
    Fungsi untuk keluar dari game
    '''
    exit_input = input('Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ')
    if exit_input != 'y' and exit_input!='n':
        return game_exit()
    else:
        print(f'Selamat tinggal agent {username}!')
        time.sleep(3)
        os.system('cls')
        sys.exit()

if __name__ == '__main__' :
    game_exit('bimo')