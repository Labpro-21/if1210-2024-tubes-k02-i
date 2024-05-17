import CSVfunction as csv
import os
import time
import DataPath as dp
dirname = os.path.dirname(__file__)

def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(0.5)
    os.system('cls')

def pilihan_monster_management(monster_list:list[dict]):
    '''
    Membuat fungsi untuk memilih dalam monster management
    '''
    print("Selamat Datang Para Agen")
    print("Di sini adalah tempat database para monster.")
    print("-"*50)
    print("[1] Tampilkan semua monster yang ada")
    print("[2] Tambahkan monster baru")
    print('[3] Untuk kembali ke menu admin')
    pil = input("Anda ingin pilih aksi mana (1/2/3)?: ")
    if pil=='1' :
        delay()
        print("ID |   Name/Type   | ATK Power | DEF Power | HP ")
        print("-"*50)
        for data in monster_list :
            print(f"{data['id']:<3} | {data['type']:<12} | {data['atk_power']:<9} | {data['def_power']:<9} | {data['hp']} ")
        return pilihan_monster_management(monster_list)
    elif pil=='2':
        return tambah_monster_baru(monster_list)
    elif pil=='3':
        return None
    else:
        print('Input anda salah, ulangi!')
        delay()
        return pilihan_monster_management(monster_list)
    
def cek_kesamaan_nama(monster_list:list[dict], nama:str):
    '''
    Mengecek nama yang sama dalam data
    '''
    for data in monster_list:
        if data['type']== nama:
            return True
        else: 
            return False

def tambah_monster_baru(monster_list:list[dict]):
    '''
    Fungsi untuk menambah atribut monster baru
    '''
    print("... Proses pembuatan monster baru dimulai ...")    
    print()
    nama = input("Nama/Type Monster Baru : ")
    while cek_kesamaan_nama(monster_list, nama):
        print("Ups.. Nama Monster sudah terdaftar...")
        print("Silakan masukkan nama lain!")
        nama = input("Nama/Type Monster Baru : ")
    print()
    valid_int = set("0123456789")
    atk = input("ATK Power Monster Baru : ")
    while not all(char in valid_int for char in atk):
        print("ATK Power harus dalam angka...")
        print("Silakan coba lagi!")
        atk = input("ATK Power Monster Baru : ")
    Atk = int(atk)
    print()
    while True:
        try:
            defense = int(input("DEF Power Monster Baru (0-50) : "))
            if 0 <= defense <= 50:
                break  # Exit the loop if defense is within the valid range
            else:
                print("Def Power Monster harus bernilai 0-50...")
                print("Silakan coba lagi!")
        except ValueError:
            print("Input harus berupa bilangan bulat!")
    while True:
        try:
            hp = int(input("Nilai HP Monster Baru: "))
            break  # Exit the loop if defense is within the valid range
        except ValueError:
            print("Input harus berupa bilangan bulat!")
    
    monster_id = len(monster_list) + 1

    monster_baru = {'id':str(monster_id),'type':str(nama),'atk_power':str(Atk),'def_power':str(defense),'hp':str(hp)}
    
    print()
    return tambah_monster_ke_database(monster_list,monster_baru)
    
def tambah_monster_ke_database(monster_list:list[dict],monster_baru:dict):
    '''
    Fungsi untuk menambah monster baru ke dalam data base
    '''
    pilihan = input("Ingin menambahkan Monster baru ke database? (Y/N) : ")
    if pilihan.lower() == "y" :
        print("Monster baru berhasil ditambahkan ke database!")
        monster_list.append(monster_baru)
    elif pilihan.lower() == "n" :
        print("Monster baru gagal ditambahkan ke database!")
        return pilihan_monster_management(monster_list)
    else:
        print('Perintah anda salah')
        return pilihan_monster_management(monster_list)

if __name__ == "__main__":
    monster_shop_data , item_shop_data , potion_data,  monster_inventory_data , item_inventory , monster_data, user_data = dp.data_path('data')
    pilihan_monster_management(monster_data)