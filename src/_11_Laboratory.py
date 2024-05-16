import os
dirname = os.path.dirname(__file__)
import DataPath as dp

monster_list=[]
def laboratory(username:str, monster_inventory_data , user_data , monster_list, price):
    '''
    Membuat fitur shop dalam game dengan fungsi ini sebagai page utamanya
    
    '''
   
    # user id
    for name in user_data:
        if username == name['username']:
            user_id = name['id']
            coin=int(name['oc'])
            

    print(f'Selamat datang di laboratory {username}!!')
    display_monster_inventory(user_id,monster_inventory_data)
    display_upgrade_price()
    monster_id = int(input("Pilih monster: "))

    if 1 <= monster_id <= len(monster_list):
        selected_monster = monster_list[monster_id - 1]
        monster_id, monster_name, level = selected_monster
        level = int(level)
        price=price(level)
        if level >= 5:
            print('Maaf,monster yang Anda pilih sudah memiliki level maksimum')
        else:
            level_up = level + 1
            print(f"{monster_name} akan di upgrade ke level {level_up}.") 
            confirm = input("Lanjutkan upgrade (Y/N): ")
            if confirm == 'Y':
                if coin >= price:
                    coin -= price
                    level = level_up
                    print(f"Selamat, {monster_name} berhasil di-upgrade ke level {level_up} !")
                    print(f"Jumlah O.W.C.A. Coin kamu sekarang {coin}.")
                    # Update jumlah coin
                    for user in user_data:
                        if user['id'] == user_id:
                            user['oc'] = str(coin)  
                    # Update data level 
                    for monster in monster_inventory_data:
                        if monster['user_id'] == user_id and monster['monster_id'] == monster_id:
                            monster['level'] = str(level)
                    return laboratory(username, monster_inventory_data , user_data , monster_list, price)
                    
                else:
                    print("Maaf, Anda tidak memiliki cukup O.W.C.A. Coin untuk melakukan upgrade.")
            elif confirm == 'N':
                print("Upgrade monster dibatalkan.")
            else:
                print('masukkan tidak valid')
    else:
        print("Tidak ada monster tersebut")
def price (level : int)-> int:
    """
    fungsi untuk menentukan harga upgrade ke level berikutny
    """
    if level == 1:
        price = 300
    elif level == 2:
        price = 500
    elif level == 3:
        price = 800
    elif level == 4:
        price = 1000
    return price
    
def display_monster_inventory(user_id : str,monster_inventory_data)->str:
    '''
    Fungsi untuk menampilkan inventaris monster.
    '''
    print("============ MONSTER LIST ============")
    index = 1
    
    for data in monster_inventory_data:
        if user_id == data['user_id']:
            level = int(data['level'])
            monster_id = data['monster_id']
            for subdata in monster_data:
                if monster_id == subdata['id']:
                    monster_name = subdata['type']
                    print(f"{index}. {monster_name} (Level: {level})")
                    monster_list.append((monster_id, monster_name, level))
                    index += 1
    return monster_list
def display_upgrade_price():
    '''
    Fungsi untuk menampilkan harga upgrade monster.
    '''
    print("============ UPGRADE PRICE ============")
    print("1. Level 1 -> Level 2: 300 OC")
    print("2. Level 2 -> Level 3: 500 OC")
    print("3. Level 3 -> Level 4: 800 OC")
    print("4. Level 4 -> Level 5: 1000 OC")
if __name__ =='__main__':
    monster_shop_data , item_shop_data , potion_data,  monster_inventory_data , item_inventory , monster_data, user_data = dp.data_path('data')
    laboratory('Agen_P', monster_inventory_data , user_data , monster_list, price)
