import CSVfunction as csv

def user_inventory(username):
    '''
    Mencari inventory user berdasarkan idnya dan menampilkannya di layar
    '''
    user_data = csv.read_csv(r'if1210-2024-tubes-k02-i\data\user.csv')
    monster_data = csv.read_csv(r'if1210-2024-tubes-k02-i\data\monster.csv')
    item_data = csv.read_csv(r'if1210-2024-tubes-k02-i\data\item_inventory.csv')
    monster_inventory_data = csv.read_csv(r'if1210-2024-tubes-k02-i\data\monster_inventory.csv')
    # print(user_data)
    ### mencari ID username dan coin
    for name in user_data:
        if username == name['username']:
            # print(name)
            user_id = name['id']
            coin = name['oc']
        
    ### mencari monster, potion, item, dan owc yang dimiliki berdasarkan ID
    
    ### monster yang dimiliki user
    player_inventory=[]
    for monster in monster_inventory_data:
        if user_id == monster['user_id']:
            level = monster['level']
            monster_id = monster['monster_id']
            for data in monster_data:
                if monster_id == data['id']:
                    data['level'] = level
                    player_inventory.append(data)
    
    ### item / potion yang dimiliki user
    for potion in item_data:
        if user_id == potion['user_id']:
            player_inventory.append(potion)
            
    ### print(player_inventory)
    return display_inventory(player_inventory,coin)


def print_monster(cnt,monster):
    '''
    Mengeprint monster
    '''
    name = monster['type']
    level = monster['level']
    hp = monster['hp']
    print(f"{cnt}.Monster       (Name: {name}, Lvl: {level}, HP: {hp})")


def print_potion(cnt,potion):
    '''
    Mengeprint potion
    '''
    potion_type = potion['type']
    quantity = potion['quantity']
    print(f"{cnt}.Potion        (Type: {potion_type}, Qty: {quantity})")

def print_monster_ball(cnt,monster_ball):
    '''
    Mengeprint monster ball
    '''
    quantity = monster_ball['quantity']
    print(f"{cnt}.Monster Ball  (Qty: {quantity})")

def display_inventory(player_inventory,coin):
    '''
    Menampilkan inventory user di layar
    '''
    # print(player_inventory) 
    print(f'Jumlah O.W.C.A Coin-mu sekarang {coin}\n')
    for index, item in enumerate(player_inventory, start=1):
        if 'id' in item:
            print_monster(index,item)
        elif 'quantity' in item: 
            if item['type'] != 'monster ball':
                print_potion(index,item)
            else:
                print_monster_ball(index,item)
    print()
    return print_details_by_id(player_inventory)
                    

def print_monster_details(monster):
    '''
    Mengeprint detail monster
    '''
    print("Monster")
    print(f"Name      : {monster['type']}")
    print(f"ATK Power : {monster['atk_power']}")
    print(f"DEF Power : {monster['def_power']}")
    print(f"HP        : {monster['hp']}")
    print(f"Level     : {monster['level']}")


# Function to print potion details
def print_potion_details(potion):
    '''
    Mengeprint detail potion atau monster ball
    '''
    if potion['type'] != 'Monster Ball':
        print("Potion")
    else:
        print('Monster Balls')
    print(f"Type      : {potion['type']}")
    print(f"Quantity  : {potion['quantity']}")


def print_details_by_id(data):
    '''
    Mengeprint detail item yang terdapat dalam inventory player
    '''
    while True:
        print('!Input "back" untuk kembali!')
        item_id = input("Ketikkan id untuk menampilkan detail item:\n>>> ")
        ids = []
        for i in range(1,len(data)+1):
            ids.append(str(i))
        if item_id == 'back':
            return None
        elif item_id in ids:
            for index, item in enumerate(data, start=1):
                if index == int(item_id):
                    if 'id' in item:
                        print_monster_details(item)
                    elif 'quantity' in item:
                        print_potion_details(item)
        else:
            print('Id item tidak ada di inventory, gunakan Id lain.')
    
if __name__ == '__main__' :
    user_inventory('Asep_Spakbor')
    
    