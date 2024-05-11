# if __name__ == '__main__':
import CSVfunction
from GameState import game_state
import _02_Login
# else:
#     from . import CSVfunction

user_data_path = r'if1210-2024-tubes-k02-i\data\user.csv'
monster_inventory_path = r'if1210-2024-tubes-k02-i\data\monster_inventory.csv'
user_data = CSVfunction.read_csv(r'if1210-2024-tubes-k02-i\data\user.csv')
monster_data = CSVfunction.read_csv(r'if1210-2024-tubes-k02-i\data\monster.csv')

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

def choose_monster(monster_data: list[str]):
    '''
    Memilih monster
    '''
    global monster_id
    monster_data = CSVfunction.read_csv(r'if1210-2024-tubes-k02-i\data\monster.csv')
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
    
    
def check_register(username):
    '''
    Meregister username dan memvalidasinya
    '''
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
    global username
    global password
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    if not check_register(username):
        return False
    else : 
        return True
    
def register_page(game_state,username):
    '''
    Membuat laman register untuk user
    '''
    global user_data
    user_data = CSVfunction.read_csv(r'if1210-2024-tubes-k02-i\data\user.csv')
    if game_state == 0:
        if user_input():
            choose_monster(monster_data)
            CSVfunction.write_csv(user_data_path, f'{len(user_data)+1};{username};{password};agent;{0}\n')
            CSVfunction.write_csv(monster_inventory_path,f'{len(user_data)+1};{monster_id};{1}\n')
            game_state = 1
            return game_state
        else:
            return None
    else:
        print(f'Register gagal!\nAnda telah login dengan username {username}, silahkan lakukan "LOGOUT" sebelum melakukan register!')


if __name__ == '__main__':
    # print(game_state)
    register_page(game_state,'bimo') 
    print(username)
    

