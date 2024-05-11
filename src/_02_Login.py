import CSVfunction as csv
from GameState import game_state,username

user_data = csv.read_csv(r'if1210-2024-tubes-k02-i\data\user.csv')

def check_input(username: str, password:str)->bool:
    '''
    Mengecek input dari user
    '''
    global game_state
    for data in user_data:
        if username == data['username']:
            if password == data['password']:
                print(f'Selamat datang, Agent {username}!\nMasukkan command "help" untuk daftar command yang dapat kamu panggil.')
                game_state = 1
                return  game_state
            else:
                print('Password salah!')
                return None
            
    print('Username tidak terdaftar!')
    return None

        
def user_login():
    '''
    Membuat fungsi login untuk menerima input dari user
    '''
    global username
    username = str(input('Username: '))
    password = str(input('Password: '))
    
    check_input(username,password)
    return username


def login_page(game_state):
    '''
    Membuat lama login untuk user
    '''
    global user_data
    user_data = csv.read_csv(r'if1210-2024-tubes-k02-i\data\user.csv')
    if game_state == 0:
        user_login()
        return game_state
    else:
        print(f'Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan "LOGOUT" sebelum melakukan login kembali!')
    return None

if __name__ == '__main__' :
    # username , password = user_login()
    # print(username)
    # print(user_data)
    print(game_state)
    login_page(game_state)
    print(game_state)