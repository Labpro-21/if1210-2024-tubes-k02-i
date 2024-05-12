import CSVfunction
import os
dirname = os.path.dirname(__file__)
from GameState import game_state


user_data_path =  os.path.join(dirname, '../data/user.csv')
monster_inventory_path =  os.path.join(dirname, '../data/monster_inventory.csv')
monster_user_data_path =  os.path.join(dirname, '../data/_05_Monster.csv')
user_data = CSVfunction.read_csv(user_data_path)
monster_data = CSVfunction.read_csv(monster_user_data_path)

# KAMUS
def validate_username(username: str)->bool:
    '''
    Memvalidasi username
    '''
    valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-0123456789")
    for char in username:
        if char not in valid_characters:
            return False
    return True

def choose_monster(monster_data: list[str],username:str):
    '''
    Memilih monster
    '''
    monster__user_data_path =  os.path.join(dirname, '../data/_05_Monster.csv')
    monster_data = CSVfunction.read_csv(monster__user_data_path)
    print('Silahkan pilih salah satu monster sebagai monster awalmu.')
    for monster in monster_data:
        print(f"{monster['id']}. {monster['type']}")
    
    ids = []
    for monster in monster_data:
        ids.append(int(monster['id']))   
    monster_id = int(input('Monster pilihanmu: '))
    
    if monster_id in ids:
        print(f"Selamat datang agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster_data[monster_id-1]['type']}!")
        return monster_id
    
    else: 
        print('Monster pilihan anda tidak ada, silahkan pilih kembali.')
        return choose_monster(monster_data)
    
    
def check_register(username: str)->bool:
    '''
    Meregister username dan memvalidasinya
    '''
    user_data_path =  os.path.join(dirname, '../data/user.csv')
    user_data = CSVfunction.read_csv(user_data_path)
    if not validate_username(username):
        print('Username hanya boleh berisi alfabet, angka, underscore, dan strip!')
        return False
    for data in user_data:
        if username == data['username']:
            print(f'Username {username} sudah terpakai, silahkan gunakan username lain!')
            return False
    else: return True

def user_input():
    '''
    Input username dan password user
    '''
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    if not check_register(username):
        return False
    else : 
        return username , password
    
def register_page(game_state: int, username:str)->int:
    '''
    Membuat laman register untuk user
    '''
    monster_inventory_path =  os.path.join(dirname, '../data/monster_inventory.csv')
    user_data_path =  os.path.join(dirname, '../data/user.csv')
    user_data = CSVfunction.read_csv(user_data_path)
    if game_state == 0:
        username,password = user_input()
        if username:
            monster_id = choose_monster(monster_data,username)
            CSVfunction.write_csv(user_data_path, f'{len(user_data)+1};{username};{password};agent;{0}\n')
            CSVfunction.write_csv(monster_inventory_path,f'{len(user_data)+1};{monster_id};{1}\n')
            game_state = 1
            return game_state
    else:
        print(f'Register gagal!\nAnda telah login dengan username {username}, silahkan lakukan "LOGOUT" sebelum melakukan register!')


if __name__ == '__main__':
    # print(game_state)
    register_page(game_state,'bimo') 
    

