import os
dirname = os.path.dirname(__file__)
import CSVfunction as csv
import DataPath as dp
import time

def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(1)
    os.system('cls')
    

def shop_currency_page(username:str, monster_shop_data:list[dict] , item_shop_data:list[dict] , potion_data:list[dict], monster_inventory_data :list[dict], item_inventory:list[dict] , monster_data:list[dict] , user_data:list[dict] ):
    '''
    Membuat fitur shop dalam game dengan fungsi ini sebagai page pertamanya
    
    '''
    print('Irrasshaimase! Selamat datang di SHOP!!')
    cmd = input('Pilih aksi (lihat/beli/keluar): ')
    # user id
    for data in user_data:
        if username == data['username']:
            user_id = data['id'] 
                
    # item shop data
    if cmd == 'lihat':
        return lihat(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
    elif cmd == 'beli':
        return beli(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , user_id)
    elif cmd == 'keluar':
        print(f'Selamat tinggal {username}! Sampai bertemu lagi.')
    else:
        print('Perintah anda salah! Ulangi perintah anda.')
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)

####################################################### FUNGSI UNTUK MELIHAT DATA #######################################################
def lihat(username:str, monster_shop_data:list[dict] , item_shop_data :list[dict], potion_data:list[dict], monster_inventory_data:list[dict] , item_inventory :list[dict], monster_data:list[dict] , user_data:list[dict]):
    '''
    Membuat fungsi untuk melihat item apa saja yang dijual
    '''
    cmd = input('Mau lihat apa? (monster/potion)?: ')          
    if cmd == 'monster':
        print("ID  |   Name/Type  | ATK Power | DEF Power | HP     | Stock  | Harga    ")
        print("-"*70)
        for data in monster_shop_data :
            for subdata in monster_data:
                if subdata['id'] == data['monster_id']:
                    print(f"{subdata['id']:<3} | {subdata['type']:<12} | {subdata['atk_power']:<9} | {subdata['def_power']:<9} | {subdata['hp']:<6} | {data['stock']:<6} | {data['price']}")
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
    elif cmd == 'potion':
        print('ID  | Type         | Stok   | Harga')
        print("-"*40)
        for data in potion_data:
            for subdata in item_shop_data:
                if data['potion_name'] == subdata['type']:
                    print(f"{data['id']:<3} | {subdata['type']:<12} | {subdata['stock']:<6} | {subdata['price']}")
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data,  monster_inventory_data , item_inventory , monster_data , user_data )
    else:
        print('Perintah anda salah! Ulangi perintah anda.')
        delay()
        return lihat(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , )
####################################################### FUNGSI UNTUK MELIHAT DATA #######################################################        


####################################################### FUNGSI UNTUK MEMBELI #######################################################
def beli(username:str, monster_shop_data :list[dict], item_shop_data :list[dict], potion_data:list[dict], monster_inventory_data :list[dict], item_inventory :list[dict] , monster_data :list[dict], user_data :list[dict], user_id:str):
    '''
    Membuat fungsi untuk membeli item atau monster yang dijual
    '''
    for data in user_data:
        if username == data['username']:
            coin = data['oc']
            
    print(f'Jumlah O.W.C.A coin mu sekarang {coin}')
    print()
    
    cmd = input('Mau beli apa? (monster/potion): ')
    if cmd == 'monster':
        beli_monster(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , user_id, coin)
    elif cmd == 'potion':
        beli_potion(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , user_id, coin)
    else:
        print('Perintah anda salah! Ulangi perintah anda!')
        return beli(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data ,user_id)
    
###################### MEMBELI MONSTER ########################
def beli_monster(username:str, monster_shop_data :list[dict] , item_shop_data :list[dict], potion_data:list[dict], monster_inventory_data :list[dict], item_inventory:list[dict] , monster_data:list[dict] , user_data:list[dict] ,user_id:str, coin:str):
    '''
    Membuat fungsi untuk membeli monster yang dijual
    '''
    coin = int(coin)
    ids_list = []
    for data in monster_shop_data:
        ids_list.append(data['monster_id'])
    monster_id = input('Masukkan monster id: ')
    if monster_id not in ids_list:
        print('Id tidak tersedia, silahkan coba id yang lain.')
        delay()
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
    for data in monster_data:
        for subdata in monster_shop_data:
            if monster_id == data['id']:
                monster_type = data['type']
                monster_cost = int(subdata['price'])
                monster_stock = int(subdata['stock'])
    for data in monster_inventory_data:
        if monster_id == data['monster_id'] and user_id == data['user_id'] :
            print(f'Monster{monster_type}, sudah ada dalam inventory-mu! Pembelian dibatalkan.')
            return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
        
    if monster_stock == 0:
        print('Stock monster sudah habis, silahkan pilih yang lain')
    
    elif monster_cost > coin :
        print('OC-mu tidak cukup')
    
    else:
        monster_inventory_data.append({'user_id': user_id,'monster_id':monster_id,'level': '1'})
        print(f'Berhasil membeli item {monster_type}. Item sudah masuk ke inventory-mu!')
        for subdata in monster_shop_data:
            if monster_id == subdata['monster_id']:
                subdata['stock'] = str(monster_stock-1)
        for data in user_data:
            if user_id == data['id']:
                data['oc'] = str(coin-monster_cost)
                
    return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
###################### MEMBELI MONSTER ########################


###################### MEMBELI POTION ########################
def beli_potion(username:str, monster_shop_data:list[dict] , item_shop_data:list[dict] , potion_data:list[dict], monster_inventory_data:list[dict] , item_inventory :list[dict], monster_data :list[dict], user_data :list[dict],user_id:str, coin:str):
    '''
    Membuat fungsi untuk membeli item/potion yang dijual
    '''
    coin = int(coin)
    ids_list = []
    for data in item_shop_data:
        for subdata in potion_data:
            if data['type'] == subdata['potion_name']:
                ids_list.append(subdata['id'])
            
    item_id = input('Masukkan id potion: ')
    if item_id not in ids_list:
        print('Id tidak tersedia, silahkan coba id yang lain.')
        delay()
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
    
    qty = int(input('Masukkan jumlah: '))
    for data in potion_data:
        for subdata in item_shop_data:
            if item_id == data['id']:
                item_type = subdata['type']
                item_cost = int(subdata['price'])
                item_stock = int(subdata['stock'])
                
    if item_stock == 0:
        print('Stock item sudah habis, silahkan pilih yang lain')
    
    elif item_cost*qty > coin :
        print('OC-mu tidak cukup')
    elif qty>item_stock:
        print('Kuantitas barang tidak mencukupi, silahkan ulangi')
    else:
        print(f'Berhasil membeli item: {qty} {item_type}. Item sudah masuk ke inventory-mu!')
        for subdata in item_shop_data:
            if item_type == subdata['type']:
                subdata['stock'] = str(item_stock-qty)
        for data in user_data:
            if user_id == data['id']:
                data['oc'] = str(coin-(qty*item_cost))
        for data in item_inventory:
            if user_id == data['user_id'] and item_type == data['type']:
                data['type'] = str(int(data['type']+qty))
                
    return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)   
###################### MEMBELI POTION ########################
####################################################### FUNGSI UNTUK MEMBELI #######################################################
if __name__ == '__main__':
    monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data = dp.data_path('data')
    #  = pi.player_inventory('Asep_Spakbor', user_data , monster_inventory_data , item_inventory , monster_data)
    shop_currency_page('Asep_Spakbor', monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)