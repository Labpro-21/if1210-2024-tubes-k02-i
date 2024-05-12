import CSVfunction as csv
import os
import time
dirname = os.path.dirname(__file__)

def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(0.5)
    os.system('cls')
    
    
def tampilan_awal():
    monster_data_path = os.path.join(dirname, '../data/monster.csv')
    monster_data = csv.read_csv(monster_data_path)
    print("Selamat Datang Para Agen")
    print("Di sini adalah tempat database para monster.")
    return pilihan_monster_management(monster_data)

def pilihan_monster_management(monster_list):
    print("-"*50)
    print("[1] Tampilkan semua monster yang ada")
    print("[2] Tambahkan monster baru")
    print('[3] Untuk kembali ke menu admin')
    pil = int(input("Anda ingin pilih aksi mana (1/2)?: "))
    if pil==1 :
        delay()
        print("ID |   Name/Type   | ATK Power | DEF Power | HP ")
        print("-"*50)
        for data in monster_list :
            print(f"{data['id']:<3} | {data['type']:<12} | {data['atk_power']:<9} | {data['def_power']:<9} | {data['hp']} ")
        return tampilan_awal()
    elif pil==2:
        return tambah_monster_baru(monster_list)
    elif pil==3:
        return None
        
def cek_kesamaan_nama(monster_list, nama):
    for data in monster_list:
        if data['type']== nama:
            return True
        else: 
            return False

def tambah_monster_baru(monster_list):
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
    defense = int(input("DEF Power Monster Baru (0-50) : "))
    while defense<0 or defense>50 :
        print("Def Power Monster harus bernilai 0-50...")
        print("Silakan coba lagi!")
        defense = int(input("DEF Power Monster Baru (0-50) : "))
    print()
    hp = int(input("Nilai HP Monster Baru: "))

    ID = len(monster_list) + 1

    monster_baru = f'{ID};{nama};{Atk};{defense};{hp}\n'
    print()
    return tambah_monster_ke_database(monster_list,monster_baru)
    
def tambah_monster_ke_database(monster_list,monster_baru):
    monster_data_path = os.path.join(dirname, '../data/monster.csv')
    pilihan = input("Ingin menambahkan Monster baru ke database? (Y/N) : ")
    if pilihan.lower() == "y" :
        print("Monster baru berhasil ditambahkan ke database!")
        csv.write_csv(monster_data_path,monster_baru)
    elif pilihan.lower() == "n" :
        print("Monster baru gagal ditambahkan ke database!")
    else:
        print('Perintah anda salah')

if __name__ == "__main__":
    tampilan_awal()