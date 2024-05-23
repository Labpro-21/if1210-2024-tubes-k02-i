
####################################### IMPORTING SOME MODULES ######################################
import sys
import os
dirname = os.path.dirname(__file__)
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import time
import argparse

from src import (
    _00_LCG as lcg,
    _01_Register as register,
    _02_Login as login,
    _03_Logout as logout,
    _04_MenuAndHelp as menu_and_help,
    _07_Inventory as inventory,
    _08_Battle as battle,
    _09_Arena as arena,
    _10_ShopAndCurrency as shop_and_currency,
    _11_Laboratory as laboratory,
    _12_ShopManagement as shop_management,
    _13_MonsterManagement as monster_management,
    _16_Exit as exit_module,
    DesignUtilities as design,
    DataPath as dp,
    PlayerInventory 
)
from src.GameState import game_state, username, is_admin #const

####################################### IMPORTING SOME MODULES ######################################
def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(1)
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')
####################################### IMPORTING SOME MODULES ######################################   




################################ START MENU ####################################### 
def start_menu(game_state:int,is_admin:bool,username:str, monster_shop_data:list[dict] , item_shop_data:list[dict] , potion_data:list[dict],  monster_inventory_data:list[dict] , item_inventory:list[dict] , monster_data:list[dict] , user_data:list[dict]):
    '''
    Menu awal yang ditampilkan ketika memulai game
    '''
    design.print_centered_start(design.start_menu_interface())
    command = input('Masukkan command (lowercase): ')
    if command == 'login': ### LOGIN ####
        if not is_admin:
            game_state, is_admin, username = login.login_page(game_state,username,user_data)
        else:
            print('Anda sudah login sebagai admin!')
    elif command == 'help': ### HELP ####
        if game_state == 0:
            username = ''
        menu_and_help.help_menu(username,is_admin)
    elif command == 'register': ### REGISTER ####
        if is_admin:
            print('Anda tidak bisa register sebagai admin!')
        else:
            username , game_state = register.register_page(game_state, username, monster_data, monster_inventory_data, user_data)
    elif command == 'menu': ### MENU ####
        if game_state == 1:
            print('Anda akan masuk ke main menu! Selamat datang pejuang.')
            delay()
            return main_menu(game_state, is_admin, username, monster_shop_data, item_shop_data, potion_data, monster_inventory_data, item_inventory, monster_data, user_data)
        else:
            print('Anda belum login! silahkan login terlebih dahulu.')
    elif command == 'logout': ### LOGOUT ####
        game_state,is_admin = logout.logout(game_state,is_admin)
        username = ''
    elif command == 'exit':
        exit_module.game_exit(username, user_data,item_inventory,item_shop_data,monster_data,monster_shop_data,monster_inventory_data)
    elif command == 'asepspakbortheboss': ### ADMIN ####
        if is_admin:
            print('Halo , admin! silahkan mengatur universe kami.')
            delay()
            return admin_menu(game_state, is_admin, username, monster_shop_data , item_shop_data, potion_data,  monster_inventory_data, item_inventory, monster_data, user_data)
        else: 
            print('Anda bukan admin!')
    else: ### BACK TO MENU  ####
        print('Perintah anda salah, ulangi!')
    delay()
    return start_menu(game_state, is_admin, username, monster_shop_data , item_shop_data ,potion_data,  monster_inventory_data , item_inventory , monster_data , user_data)
################################ START MENU ####################################### 




################################ MAIN MENU ######################################## 
def main_menu(game_state:int, is_admin:bool, username:str, monster_shop_data:list[dict] , item_shop_data:list[dict] , potion_data:list[dict],  monster_inventory_data:list[dict] , item_inventory:list[dict] , monster_data:list[dict] , user_data:list[dict]):
    '''
    Menu ketika menampilkan game
    '''
    design.print_centered_menu(design.ascii_art())
    command = input('Masukkan command (lowercase): ')
    if command == 'inventory': ### INVENTORY ####
        delay()
        player_inventory , coin = PlayerInventory.player_inventory(username, user_data , monster_inventory_data , item_inventory , monster_data)
        inventory.display_inventory(player_inventory,coin)
        
    elif command == 'battle': ### BATTLE ####
        print('Anda akan memasuki medan pertempuran! Semangat')
        delay()
        battle.battle(username, monster_data, monster_inventory_data, potion_data, item_inventory, user_data)
        
    elif command == 'arena': ### ARENA ####
        print('Anda akan memasuki daerah arena!')
        arena.arena(username, monster_data, monster_inventory_data, potion_data, item_inventory, user_data)
        
    elif command == 'laboratory': ### LABORATORY ####
        print('Anda akan memasuki lab! Silahkan upgrade monster kesayangan anda!')
        delay()
        laboratory.laboratory(username, monster_inventory_data , user_data , monster_data)
        
    elif command == 'shop': ### SHOP ####
        print('Anda akan memasuki shop! Silahkan beli barang dan monster kesukaan anda!')
        delay()
        shop_and_currency.shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
        
    elif command == 'back': ### BACK TO START ####
        print('Akan kembali ke start menu.') 
        delay()
        return start_menu(game_state, is_admin, username, monster_shop_data, item_shop_data, potion_data, monster_inventory_data, item_inventory, monster_data, user_data)
    
    else:
        print('Perintah anda salah, ulangi!') ### FALSE ####

    delay()
    return main_menu(game_state, is_admin, username, monster_shop_data , item_shop_data, potion_data,  monster_inventory_data, item_inventory, monster_data, user_data)
################################ MAIN MENU ########################################






################################ ADMIN MENU ######################################## 
def admin_menu(game_state, is_admin, username, monster_shop_data:list[dict] , item_shop_data:list[dict] , potion_data:list[dict], monster_inventory_data:list[dict] , item_inventory:list[dict] , monster_data:list[dict] , user_data:list[dict]):
    design.admin_menu_interface()
    command = input('Masukkan command (lowercase): ')
    if command == 'monster management' or command == '1': ### MONSTER MANAGEMENT ####
        delay()
        monster_management.pilihan_monster_management(monster_data)
    elif command == 'shop management' or command == '2': ### SHOP MANAGEMENT ####
        delay()
        shop_management.tampilan_awal(username, item_shop_data, monster_shop_data, monster_data, potion_data)
    elif command == 'back'or command == '3': ### BACK TO STAR ####
        delay()
        return start_menu(game_state, is_admin, username, monster_shop_data , item_shop_data, potion_data,  monster_inventory_data, item_inventory, monster_data, user_data)
    else:
        print('Perintah anda salah, ulangi!')
    delay()
    return admin_menu(game_state, is_admin, username, monster_shop_data, item_shop_data, potion_data,  monster_inventory_data, item_inventory, monster_data, user_data)

################################ ADMIN MENU ######################################## 




################################ F14 Load ##########################################

# Inisialisasi Argument Parser
parser = argparse.ArgumentParser(description='Buka folder.')
# Menambahkan argumen posisional
parser.add_argument('folder', nargs='?', default=None, help='mengakses folder csv ')
# Penguraian Argumen
args = parser.parse_args()
# jika input tidak ada
if args.folder is None:
    print("Tidak ada nama folder yang diberikan!\nUsage : python main.py <data/nama_folder>")
    sys.exit()
# memeriksa keberadaan folder
if not os.path.exists(args.folder):
    print(f"Folder \"{args.folder}\" tidak ditemukan!")
    sys.exit()

print("Loading...")
delay()
print("Selamat Datang di program OWCA!")
################################ GAME START ########################################
monster_shop_data , item_shop_data, potion_data, monster_inventory_data, item_inventory, monster_data, user_data = dp.data_path(args.folder)
start_menu(game_state, is_admin, username, monster_shop_data, item_shop_data, potion_data,  monster_inventory_data, item_inventory, monster_data, user_data)