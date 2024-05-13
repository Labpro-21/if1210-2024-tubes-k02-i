
import CSVfunction as csv

import os
dirname = os.path.dirname(__file__)

import DataPath as dp

def player_inventory(username, user_data , monster_inventory_data , item_inventory , monster_data):
    '''
    Membuat fungsi player inventory pada player
    '''
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
    for potion in item_inventory:
        if user_id == potion['user_id']:
            player_inventory.append(potion)
            
    return player_inventory, coin


