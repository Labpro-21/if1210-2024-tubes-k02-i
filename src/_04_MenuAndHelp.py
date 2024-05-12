
def help_menu(username: str)->None:
    '''
    menampilkan menu help di game
    '''
    if username == '':
        pretext = 'Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.'
        
        main_text =  '''
        1. Login: Masuk ke dalam akun yang sudah terdaftar
        2. Register: Membuat akun baru
        3. Exit: keluar dari game
        '''
    
    else:
        pretext = f'Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang'
        
        main_text = '''
            1. Logout: Keluar dari akun yang sedang digunakan
            2. Menu: Memasuki main menu dan mulai petualanganmu!
        '''
    print(pretext)   
    print(main_text)
    cmd = input('Tekan apapun untuk kembali: ')
    return None


    
if __name__ == '__main__':
    help_menu('')
    