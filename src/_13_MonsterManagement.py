
def pilihan_monster_management(monster_list):
    print("Selamat Datang Para Agen")
    print("Di sini adalah tempat database para monster.")
    print("--------------------------------------------------")
    print("[1] Tampilkan semua monster yang ada")
    print("[2] Tambahkan monster baru")
    pil = int(input("Anda ingin pilih yang mana? [] : "))
    if pil==1 :
        for i in range (len(monster_list)) :
            print(monster_list[i])
        return False
    elif pil==2:
        return True
        
def cek_kesamaan_nama(monster_list, nama):
    for data in monster_list:
        if data[0] == nama:
            return True
        else: 
            return False

def tambah_monster_baru(monster_list):
    if pilihan_monster_management==True :
        print("... Proses pembuatan monster baru dimulai ...")    
        print()
        nama = input("Nama/Type Monster Baru : ")
        while cek_kesamaan_nama(monster_list, nama)==True:
            print("Ups.. Nama Monster sudah terdaftar...")
            print("Silakan masukkan nama lain!")
            nama = input("Nama/Type Monster Baru : ")
        print()
        valid_int = set("0123456789")
        atk = input("ATK Power Monster Baru : ")
        while atk not in valid_int :
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

        monster_baru = [nama, Atk, defense, hp]
        print()
        print("Monster baru berhasil dibuat!")
        return monster_baru
    
def tambah_monster_ke_database(monster_list,monster_baru):
    pilihan = input("Ingin menambahkan Monster baru ke database? (Y/N) : ")
    if pilihan == ("Y" or "y") :
        print("Monster baru berhasil ditambahkan ke database!")
        monster_list.append(monster_baru)
    elif pilihan == ("N" or "n") :
        print("Monster baru gagal ditambahkan ke database!")
    for i in range (len(monster_list)) :
        print(monster_list[i])
 