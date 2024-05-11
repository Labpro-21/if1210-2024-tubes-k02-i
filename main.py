
####################################### IMPORTING SOME MODULES ######################################
import sys
sys.path.append('if1210-2024-tubes-k02-i\src')

import os
import time

from src import (
    _00_LCG as lcg,
    _01_Register as register,
    _02_Login as login,
    _03_Logout as logout,
    _04_MenuAndHelp as menu_and_help,
    _05_Monster as monster,
    _06_Potion as potion,
    _07_Inventory as inventory,
    _08_Battle as battle,
    _09_Arena as arena,
    _10_ShopAndCurrency as shop_and_currency,
    _11_Laboratory as laboratory,
    _12_ShopManagement as shop_management,
    _13_MonsterManagement as monster_management,
    _14_Load as load,
    _15_Save as save,
    _16_Exit as exit_module,
    DesignUtilities as design,
    
)
from src.GameState import game_state, username #const

####################################### IMPORTING SOME MODULES ######################################
def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(3)
    os.system('cls')
    
################################ START MENU ####################################### 
def start_menu():
    '''
    Menu awal yang ditampilkan ketika memulai game
    '''
    global game_state
    global username
    design.print_centered_start(design.start_menu_interface())
    command = input('Masukkan command (lowercase): ')
    # print(game_state)
    if command == 'login':
        login.login_page(game_state)
        game_state = login.game_state
        username = login.username
        delay()
    elif command == 'help':
        menu_and_help.help_menu(username)
        delay()
        start_menu()
    elif command == 'register':
        register.register_page(game_state,username)
        delay()
    elif command == 'menu':
        if game_state == 1:
            print('Anda akan masuk ke main menu! Selamat datang pejuang.')
            delay()
            return main_menu(username)
        else:
            print('Anda belum login! silahkan login terlebih dahulu.')
            delay()
    elif command == 'logout':
        logout.logout(game_state)
        game_state = logout.game_state
        delay()
    elif command == 'exit':
        exit_module.game_exit(username)
    else:
        print('Perintah anda salah, ulangi!')
        delay()
    return start_menu()
################################ START MENU ####################################### 
################################ MAIN MENU ######################################## 
def main_menu(username):
    '''
    Menu ketika menampilkan game
    '''
    username = username
    design.print_centered_menu(design.ascii_art())
    command = input('Masukkan command (lowercase): ')
    if command == 'inventory':
        inventory.user_inventory(username)
        delay()
    elif command == 'battle':
        pass
        
    elif command == 'arena':
        pass
    elif command == 'laboratory':
        pass
    elif command == 'back':
        print('Akan kembali ke start menu.')
        delay()
        return start_menu()
    else:
        print('Perintah anda salah, ulangi!')
        delay()
    # 1. inventory
    # 2. battle
    # 3. arena
    # 4. laboratory
    # 5. shop
    return main_menu(username)
################################ MAIN MENU ######################################## 

################################ GAME START ########################################
start_menu()


