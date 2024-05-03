import function

# KAMUS
# user_data, monster_data = array
# username, password = string


# ALGORITMA
user_data = function.read_csv('data/user.csv')
monster_data = function.read_csv('data/monster.csv')

# KAMUS
def validate_username(username: str)->bool:
    valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-0123456789")
    for char in username:
        if char not in valid_characters:
            return False
    return True

def choose_monster(monster_data: list[str]):
    print('Silahkan pilih salah satu monster sebagai monster awalmu.')
    for i in range(1,len(monster_data)):
        print(f'{i}. {monster_data[i][1]}')
    monster_id = int(input('Monster pilihanmu: '))
    
    if monster_id <= len(monster_data):
        print(f'Selamat datang agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster_data[monster_id][1]}!')
        return 
    
    else: 
        print('Monster pilihan anda tidak ada, silahkan pilih kembali.')
        return choose_monster(monster_data)
    
    
def register(username):
    if not validate_username(username):
        print('Username hanya boleh berisi alfabet, angka, underscore, dan strip!')
        return False
    for j in range(1,len(user_data)):
        if username == user_data[j][1]:
            print(f'Username {username} sudah terpakai, silahkan gunakan username lain!')
            return False
    else: return True

def user_input():
    global username
    global password
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    if not register(username):
        return user_input()
    else : return None


if __name__ == '__main__':
    # print(len(user_data))
    user_input()
    choose_monster(monster_data)       
            
    

