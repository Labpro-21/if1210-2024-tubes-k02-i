from GameState import game_state

def logout(game_state):
    '''
    User akan logout dari permainan dan perlu login kembali
    '''
    if game_state == 1:
        print('Anda telah logout!')
        game_state = 0
        return game_state
    else:
        print('Logout gagal!')
        print('Anda belum login, solahkan login terlebih dahulu sebelum melakukan logout!')
    return None

if __name__== '__main__':
    logout(1)
    print(game_state)