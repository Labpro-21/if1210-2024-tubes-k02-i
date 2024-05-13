import os
dirname = os.path.dirname(__file__)
import CSVfunction as csv
import DataPath as dp
import PlayerInventory as pi
import time

def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(3)
    os.system('cls')
    

def shop_currency_page(username:str, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , player_inventory , coin):
    '''
    Membuat fitur shop dalam game dengan fungsi ini sebagai page pertamanya
    
    '''
    print('Irrasshaimase! Selamat datang di SHOP!!')
    cmd = input('Pilih aksi (lihat/beli/keluar): ')
    # user id
    for data in user_data:
        if username == data['username']:
            user_id = data['id'] 
    
    # monster shop data
    monster_shop_array = []
    for monster in monster_data:
        monster_id = monster['id']
        for data in monster_shop_data:
            if monster_id == data['monster_id']:
                monster['stock'] = data['stock']
                monster['price'] = data['price']
                
                monster_shop_array.append(monster)
    item_shop_array = []
    for potion in item_shop_data:
        potion_type = potion['type']
        for data in potion_data:
            if potion_type == data['potion_name']:
                potion['id'] = data['id']
        item_shop_array.append(potion)

    # item shop data
    if cmd == 'lihat':
        return lihat(monster_shop_array, item_shop_array, monster_shop_data, item_shop_data, potion_data, username, monster_inventory_data , item_inventory , monster_data , user_data , player_inventory , coin)
    elif cmd == 'beli':
        return beli(coin,username, user_id, monster_shop_data, player_inventory)
    elif cmd == 'keluar':
        pass
    else:
        print('Perintah anda salah! Ulangi perintah anda.')
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , player_inventory , coin)

def lihat(monster_shop_array, item_shop_array, monster_shop_data, item_shop_data, potion_data, username, monster_inventory_data , item_inventory , monster_data , user_data , player_inventory , coin):
    '''
    Membuat fungsi untuk melihat item apa saja yang dijual
    '''
    cmd = input('Mau lihat apa? (monster/potion)?: ')          
    if cmd == 'monster':
        print("ID  |   Name/Type  | ATK Power | DEF Power | HP     | Stock  | Harga    ")
        print("-"*70)
        for data in monster_shop_array :
            print(f"{data['id']:<3} | {data['type']:<12} | {data['atk_power']:<9} | {data['def_power']:<9} | {data['hp']:<6} | {data['stock']:<6} | {data['price']}")
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , player_inventory , coin)
    elif cmd == 'potion':
        print('ID  | Type         | Stok   | Harga')
        print("-"*40)
        for data in item_shop_array :
            print(f"{data['id']:<3} | {data['type']:<12} | {data['stock']:<6} | {data['price']}")
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data,  monster_inventory_data , item_inventory , monster_data , user_data , player_inventory , coin)
    else:
        print('Perintah anda salah! Ulangi perintah anda.')
        delay()
        return lihat(monster_shop_array, item_shop_array, potion_data, monster_shop_data, item_shop_data, username, monster_inventory_data , item_inventory , monster_data , user_data , player_inventory , coin)
        
def beli(coin,username,user_id):
    '''
    Membuat fungsi untuk membeli item yang dijual
    '''
    print(f'Jumlah O.W.C.A coin mu sekarang {coin}')
    print()
    
    cmd = input('Mau beli apa? (monster/potion): ')
    if cmd == 'monster':

        pass
    elif cmd == 'potion':
        pass
    else:
        print('Perintah anda salah! Ulangi perintah anda!')
        return beli(coin,username,user_id)

def beli_monster(coin,username, user_id, monster_shop_data, player_inventory):
    
    coin = int(coin)
    monster_id = input('Masukkan monster id: ')
    for data in monster_shop_data:
        if monster_id == data['id']:
            monster_type = data['type']
            monster_cost = int(data['price'])
            monster_stock = int(data['stock'])
    
    if monster_stock == 0:
        print('Stock monster sudah habis, silahkan pilih yang lain')
    
    if monster_cost > coin :
        print('OC-mu tidak cukup')
    
    for data in player_inventory:
        if monster_id == data['id']:
            print(f'Monster{monster_type}, sudah ada dalam inventory-mu! Pembelian dibatalkan.')
            pass
    
    else:
        pass
        
'''
ongoing
'''
    
    
    
        
    

if __name__ == '__main__':
    monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data = dp.data_path(dirname)
    player_inventory , coin = pi.player_inventory('bimo', user_data , monster_inventory_data , item_inventory , monster_data)
    shop_currency_page('bimo', monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data, player_inventory, coin)