
### IMPORTING SOME MODULES ###
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
from src.GameState import game_state, username

def delay():
    time.sleep(3)
    os.system('cls')
    
def start_menu():
    global game_exit
    global game_state
    global username
    design.print_centered(design.login_interface())
    command = input('Masukkan command (lowercase): ')
    # print(game_state)
    if command == 'login':
        login.login_page(game_state)
        game_state = login.game_state
        username = login.username
        delay()
        return command
    elif command == 'help':
        return command
    elif command == 'register':
        register.register_page(game_state,username)
        delay()
        return command
    elif command == 'menu':
        return command
    elif command == 'logout':
        logout.logout(game_state)
        game_state = logout.game_state
        delay()
        return command
    elif command == 'exit':
        exit_module.game_exit(username)
        return command
    else:
        print('Perintah anda salah, ulangi!')
        delay()
    return start_menu()

def main_menu():
    pass

### IMPORTING SOME MODULES ###

#### START MENU ####
stage = "menu"
game_exit = False
while not game_exit:
    start_menu()
    if stage == "exit":
        game_exit = True

#### START MENU ####

### MAIN MENU ###

### MAIN MENU ###
