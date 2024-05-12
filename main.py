
####################################### IMPORTING SOME MODULES ######################################
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import time

from src import (
    _00_LCG as lcg,
    _01_Register as register,
    _02_Login as login,
    _03_Logout as logout,
    _04_MenuAndHelp as menu_and_help,
    # _05_Monster as monster,
    # _06_Potion as potion,
    _07_Inventory as inventory,
    # _08_Battle as battle,
    _09_Arena as arena,
    _10_ShopAndCurrency as shop_and_currency,
    _11_Laboratory as laboratory,
    _12_ShopManagement as shop_management,
    _13_MonsterManagement as monster_management,
    _14_Load as load,
    # _15_Save as save,
    _16_Exit as exit_module,
    DesignUtilities as design,
    
)
from src.GameState import game_state, username, is_admin #const

####################################### IMPORTING SOME MODULES ######################################
def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(3)
    os.system('cls')
    
################################ START MENU ####################################### 
def start_menu(game_state:int,is_admin:bool,username:str,):
    '''
    Menu awal yang ditampilkan ketika memulai game
    '''
    design.print_centered_start(design.start_menu_interface())
    command = input('Masukkan command (lowercase): ')
    if command == 'login':
        game_state, is_admin, username = login.login_page(game_state,username)

        delay()
    elif command == 'help':
        if game_state == 0:
            username = ''
        menu_and_help.help_menu(username)
        delay()
        start_menu(game_state, is_admin, username)
    elif command == 'register':
        if is_admin:
            print('Anda tidak bisa register sebagai admin!')
            delay()
        else:
            register.register_page(game_state,username)
            delay()
    elif command == 'menu':
        if game_state == 1:
            print('Anda akan masuk ke main menu! Selamat datang pejuang.')
            delay()
            return main_menu(game_state, is_admin, username)
        else:
            print('Anda belum login! silahkan login terlebih dahulu.')
            delay()
    elif command == 'logout':
        game_state,is_admin = logout.logout(game_state,is_admin)
        username = ''
        delay()
    elif command == 'exit':
        exit_module.game_exit(username)
    elif command == 'asepspakbortheboss': # admin mode
        if is_admin:
            print('Halo , admin! silahkan mengatur universe kami.')
            delay()
            return admin_menu(game_state, is_admin, username)
            
        else:
            print('Anda bukan admin!')
            delay()
    else:
        print('Perintah anda salah, ulangi!')
        delay()
    return start_menu(game_state, is_admin, username)
################################ START MENU ####################################### 
################################ MAIN MENU ######################################## 
def main_menu(game_state, is_admin, username):
    '''
    Menu ketika menampilkan game
    '''
    print(username)
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
        return start_menu(game_state, is_admin, username)
    else:
        print('Perintah anda salah, ulangi!')
        delay()
    # 1. inventory
    # 2. battle
    # 3. arena
    # 4. laboratory
    # 5. shop
    return main_menu(game_state, is_admin, username)
################################ MAIN MENU ########################################

################################ ADMIN MENU ######################################## 
def admin_menu(game_state, is_admin, username):
    design.admin_menu_interface()
    command = input('Masukkan command (lowercase): ')
    if command == 'monster management' or command == '1':
        monster_management.tampilan_awal()
        delay()
    elif command == 'shop management' or command == '2':
        pass
    elif command == 'back'or command == '3':
        return main_menu(game_state, is_admin, username)
    else:
        print('Perintah anda salah, ulangi!')
    return admin_menu()

################################ ADMIN MENU ######################################## 

################################ GAME START ########################################
start_menu(game_state, is_admin, username)