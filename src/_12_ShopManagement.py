
#monster_shop_gabungan_list : list dictionary (gabungan dari monster_list dan monster_shop_list) yang ada di database
#jadi, monster_shop_gabungan_list berisi id, type, atk, def, hp, stock, dan price dari monster

#monster_list : list dari data monster.csv (berisi id, type, atk, def, hp dari monster)
#monster_shop_list : list dari data monster_shop.csv (berisi stock dan price dari mosnter)

#monster_not_in_shop_list : list dari monster yang ada pada database tetapi tidak ada pada shop
#item_not_in_shop_list : list dari potion yang ada pada database tetapi tidak ada pada shop

#item_shop_ : list dari data item_shop.csv (berisi type, stock, dan price) dari potion
#item_shop_list : penambahan id pada data item_shop_ jadi, data berisi id, type, stock, dan price dari potion

#username : username yang digunakan agen dalam game ini


item_shop_list = []
index = 1  
for item in item_shop_:
    tambah_id = {'id': index}  
    tambah_id.update(item) 
    item_shop_list.append(tambah_id)  
    index += 1 

for item in item_not_in_shop_list :
    item['stock'] = ""
    item['price'] = ""


monster_shop_gabungan_list = []
monster_not_in_shop_list = []
for item1 in monster_list :
    kecocokan = False
    for item2 in monster_shop_list :
        if item1["id"] == item2["id"] :
            gabungan_list = item1.copy()
            gabungan_list.update(item2)
            monster_shop_gabungan_list.append(gabungan_list)
            kecocokan = True
            break
    if not kecocokan :
        gabungan_list = item1.copy()
        gabungan_list.update({'stock': "", 'price': ""})
        monster_shop_gabungan_list.append(gabungan_list)
        monster_not_in_shop_list.append(gabungan_list)


def tampilan_awal(username):
    #Tampilan awal 
    print(f"Halo {username}, Selamat datang kembali!")
    print("-~"*22)
    print("Terdapat beberapa pilihan aksi :")
    return memilih()

def memilih():
    print("[1] lihat, [2] tambah, [3] ubah, [4] hapus, [5] keluar ")
    pilihan = input("Mau pilih aksi yang mana? : ")
    if pilihan=="lihat" or pilihan=="1" :
        jenis = input("Mau lihat apa? (monster/potion) : ")
        if jenis=="monster" :
            return lihat_monster(monster_shop_gabungan_list)
        elif jenis=="potion" :
            return lihat_potion(item_shop_list)
    elif pilihan=="tambah" or pilihan=="2" :
        jenis = input("Mau tambah apa? (monster/potion) : ")
        if jenis=="monster" :
            return tambah_monster(monster_not_in_shop_list, monster_shop_gabungan_list)
        elif jenis=="potion" :
            return tambah_potion(item_not_in_shop_list, item_shop_list)
    elif pilihan=="ubah" or pilihan=="3" :
        jenis = input("Mau ubah apa? (monster/potion) : ")
        if jenis=="monster" :
            return ubah_monster(monster_shop_gabungan_list)
        elif jenis=="potion" :
            return ubah_potion(item_shop_list)
    elif pilihan=="hapus" or pilihan=="4" :
        jenis = input("Mau hapus apa? (monster/potion) : ")
        if jenis=="monster" :
            return hapus_monster(monster_shop_gabungan_list)
        elif jenis=="potion" :
            return hapus_potion(item_shop_list)
    elif pilihan=="keluar" or pilihan=="5" :
        return keluar(username)

def lihat_monster(monster_shop_gabungan_list):
    print(" ID |   Name/Type   | ATK Power | DEF Power | HP | Stok | Harga")
    print("-"*60)
    for monster in monster_shop_gabungan_list :
        print ("{:<3} | {:<13} | {:<9} | {:<9} | {:<2} | {:<4} | {:<6} ".format(monster['id'], monster['type'], monster['atk_power'], monster['def_power'], monster['hp'], monster['stock'], monster['price']))
    return memilih()

def lihat_potion(item_shop_list):
    print(" ID |   Name/Type   | Stok | Harga")
    print("-"*40)
    for monster in item_shop_list :
        print ("{:<3} | {:<13} | {:<4} | {:<6} ".format(monster['id'], monster['type'], monster['stock'], monster['price']))
    return memilih()

def tambah_monster(monster_not_in_shop_list, monster_shop_gabungan_list):
    print("Memuat data Monster yang belum ada di shop")
    print(" ID |   Name/Type   | ATK Power | DEF Power | HP")
    print("-"*50)
    for monster in monster_not_in_shop_list :
        print ("{:<3} | {:<13} | {:<9} | {:<9} | {:<3} ".format(monster['id'], monster['type'], monster['atk_power'], monster['def_power'], monster['hp']))
    
    Id = input("Masukkan id monster yang ingin ditambah ke dalam shop : ")
    stok_baru = input("Masukkan stok baru monster : ")
    harga_baru = input("Masukkan harga baru monster : ")

    for monster in range (len(monster_shop_gabungan_list)) :
        if monster_shop_gabungan_list[monster]['id'] == (Id):
            monster_shop_gabungan_list[monster]['stock'] = (stok_baru)
            monster_shop_gabungan_list[monster]['price'] = (harga_baru)
            urutan_monster = monster
    nama = monster_shop_gabungan_list[urutan_monster]['type']
    print(f"Proses menambahkan {nama} ke dalam shop telah berhasil!")
    return memilih()

def tambah_potion(item_not_in_shop_list, item_shop_list):
    print("Memuat data Potion yang belum ada di shop")
    print(" ID |   Name/Type   ")
    for monster in item_not_in_shop_list :
        print ("{:<3} | {:<14} ".format(monster['id'], monster['type']))

    Id = input("Masukkan id potion yang ingin ditambahkan ke dalam shop : ")
    stok_baru = input("Masukkan stok baru potion : ")
    harga_baru = input("Masukkan harga baru potion : ")

    for monster in range (len(item_not_in_shop_list)) :
        if item_not_in_shop_list[monster]['id'] == (Id):
            item_not_in_shop_list[monster]['stock'] = (stok_baru)
            item_not_in_shop_list[monster]['price'] = (harga_baru)
            urutan_potion = monster
    nama = item_not_in_shop_list[urutan_potion]['type']
    for monster in item_not_in_shop_list:
        if monster['type'] == nama:
            item_shop_list.append(monster)
    print(f"Proses menambahkan {nama} ke dalam shop telah berhasil!")
    return memilih()

def ubah_monster(monster_shop_gabungan_list):
    print("Memuat keadaan Monster saat ini...")
    print(" ID |   Name/Type   | ATK Power | DEF Power | HP | Stok | Harga")
    print("-"*60)
    for monster in monster_shop_gabungan_list :
        print ("{:<3} | {:<13} | {:<9} | {:<9} | {:<2} | {:<4} | {:<6} ".format(monster['id'], monster['type'], monster['atk_power'], monster['def_power'], monster['hp'], monster['stock'], monster['price']))

    Id = input("Masukkan id monster yang ingin diubah : ")
    stok_baru = input("Masukkan stok baru monster : ")
    harga_baru = input("Masukkan harga baru monster : ")

    if stok_baru != "" and harga_baru != "" :
        for monster in range (len(monster_shop_gabungan_list)) :
            if monster_shop_gabungan_list[monster]['id'] == (Id):
                monster_shop_gabungan_list[monster]['stock'] = (stok_baru)
                monster_shop_gabungan_list[monster]['price'] = (harga_baru)
                urutan_monster = monster
        nama = monster_shop_gabungan_list[urutan_monster]['type']
        print("Pembaharuan data berhasil dilakukan pada monster ", nama, " dengan stok baru berjumlah ", stok_baru, " dan harga baru ", harga_baru)

    elif stok_baru == "" and harga_baru != "" :
        for monster in range (len(monster_shop_gabungan_list)) :
            if monster_shop_gabungan_list[monster]['id'] == (Id):
                monster_shop_gabungan_list[monster]['price'] = (harga_baru)
                urutan_monster = monster
        nama = monster_shop_gabungan_list[urutan_monster]['type']
        print("Pembaharuan data berhasil dilakukan pada monster ", nama, " dan harga baru ", harga_baru)

    elif stok_baru != "" and harga_baru == "" :
        for monster in range (len(monster_shop_gabungan_list)) :
            if monster_shop_gabungan_list[monster]['id'] == (Id):
                monster_shop_gabungan_list[monster]['stock'] = (stok_baru)
                urutan_monster = monster
        nama = monster_shop_gabungan_list[urutan_monster]['type']
        print("Pembaharuan data berhasil dilakukan pada monster ", nama, " dan stok baru ", stok_baru)
    return memilih()

def ubah_potion(item_shop_list) :
    print("Memuat keadaan potion saat ini...")
    print(" ID |   Name/Type   | Stok | Harga")
    print("-"*40)
    for monster in item_shop_list :
        print ("{:<3} | {:<13} | {:<4} | {:<6} ".format(monster['id'], monster['type'], monster['stock'], monster['price']))

    Id = int(input("Urutan ke berapa yang ingin diganti? : "))
    stok_baru = input("Masukkan stok baru potion : ")
    harga_baru = input("Masukkan harga baru potion : ")

    if Id > len(item_shop_list):
        print("Maaf, potion saat ini hanya sampai dengan ", (len(item_shop_list)))
    elif Id <= len(item_shop_list):
        if stok_baru != "" and harga_baru != "" :
            item_shop_list[Id-1]['stock'] = (stok_baru)
            item_shop_list[Id-1]['price'] = (harga_baru)
            nama_potion = item_shop_list[Id-1]['type']
            print("Pembaharuan data berhasil dilakukan pada potion jenis ", nama_potion, " dengan stok baru berjumlah ", stok_baru, " dan harga baru ", harga_baru)

        elif stok_baru == "" and harga_baru != "" :
            item_shop_list[Id-1]['price'] = (harga_baru)
            nama_potion = item_shop_list[Id-1]['type']
            print("Pembaharuan data berhasil dilakukan pada potion jenis ", nama_potion, " dengan harga baru ", harga_baru)

        elif stok_baru != "" and harga_baru == "" :
            item_shop_list[Id-1]['stock'] = (stok_baru)
            nama_potion = item_shop_list[Id-1]['type']
            print("Pembaharuan data berhasil dilakukan pada monster ", nama_potion, " dengan stok baru ", stok_baru)
    return memilih()

def hapus_monster(monster_shop_gabungan_list): 
    print("Memuat keadaan Monster saat ini...")
    print(" ID |   Name/Type   | ATK Power | DEF Power | HP | Stok | Harga")
    print("-"*60)
    for monster in monster_shop_gabungan_list :
        print ("{:<3} | {:<13} | {:<9} | {:<9} | {:<2} | {:<4} | {:<6} ".format(monster['id'], monster['type'], monster['atk_power'], monster['def_power'], monster['hp'], monster['stock'], monster['price']))

    Id = ("Pilih ID monster yang ingin dihapus : ")

    for monster in range (len(monster_shop_gabungan_list)) :
        if monster_shop_gabungan_list[monster]['id'] == (Id):
            type_monster = monster_shop_gabungan_list[monster]['type']

    yes_no = input(f"Anda yakin ingin menghapus {type_monster} dari shop? (y/n) : ")
    if yes_no == "y" :
        monster_shop_gabungan_list_baru = []
        for monster in monster_shop_gabungan_list:
            if monster['type'] != type_monster:
                monster_shop_gabungan_list_baru.append(monster)
        monster_shop_gabungan_list = monster_shop_gabungan_list_baru
        print(f"Done, {type_monster} telah berhasil dihapus dari shop.")
    elif yes_no == "n" :
        print(f"{type_monster} dibatalkan untuk dihapus dari shop.")
    return memilih()

def hapus_potion(item_shop_list):
    print("Memuat keadaan potion saat ini...")
    print(" ID |   Name/Type   | Stok | Harga")
    print("-"*40)
    for monster in item_shop_list :
        print ("{:<3} | {:<13} | {:<4} | {:<6} ".format(monster['id'], monster['type'], monster['stock'], monster['price']))

    Id = input("Pilih ID potion yang ingin dihapus : ")

    for monster in range (len(item_shop_list)) :
        if item_shop_list[monster]['id'] == (Id):
            type_potion = item_shop_list[monster]['type']

    yes_no = input(f"Anda yakin ingin menghapus {type_potion} dari shop? (y/n) : ")
    if yes_no == "y" :
        item_shop_list_baru = []
        for potion in item_shop_list:
            if potion['type'] != type_potion:
                item_shop_list_baru.append(potion)

        item_shop_list = item_shop_list_baru
        print(f"Done, {type_potion} telah berhasil dihapus dari shop.")

    elif yes_no == "n" :
        print(f"{type_potion} dibatalkan untuk dihapus dari shop.")
    return memilih()

def keluar(username) :
    return (f"Sampai jumpa lagi, {username}...")
