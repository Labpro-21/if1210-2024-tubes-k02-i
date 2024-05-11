#F15-Save
# Menyimpan data pada folder dengan parent folder "save"
import os
#Fungsi ()
#Deskripsi
def save(users : Data, item_inventories : Data, item_shop : Data, monster : Data, monster_shop : Data, monster_inventory : Data) -> None:
# KAMUS LOKAL  
    # Tentukan folder utama sebagai "save"
    parent_folder= "save"
    # Menerima data sebagai list atau dictionary
    folder = "save/" + input("Masukkan nama folder: ")
    print("Saving...")
    # Periksa apakah folder /save sudah ada
    if not os.path.exists(parent_folder):
        print("Membuat folder data")
        # Buat parent folder jika belum ada
        os.makedirs(parent_folder)
    # Periksa apakah folder sudah ada
   
    if not  os.path.exists(folder):
        print(f"Membuat folder {folder}.")
        # Buat folder baru
        os.makedirs(folder)

    # Simpan data
    data_save(folder, "user", users)
    data_save(folder, "item_inventory", item_inventories)
    data_save(folder, "item_shop", item_shop)
    data_save(folder, "monster", monster)
    data_save(folder, "monster_shop", monster_shop)
    data_save(folder, "monster_inventory", monster_inventory)

    print(f"Berhasil menyimpan data di folder {folder}!")

#Fungsi ()
#Deskripsi
def data_save(path : str, nama_file : str, data : Data) -> None:
    file_path = os.path.join(path, f"{nama_file}.csv")
#KAMUS LOKAL
    # tulis header
    with open(file_path, 'w') as file:
        if nama_file == "item_inventory":
            header = "user_id;type;quantity\n"
        elif nama_file == "item_shop":
            header = "type;stock;price\n"
        elif nama_file == "monster":
            header = "id;type;atk_power;def_power;hp\n"
        elif nama_file == "monster_inventory":
            header = "user_id;monster_id;level\n"
        elif nama_file == "monster_shop":
            header = "monster_id;stock;price\n"
        elif nama_file == "user":
            header = "id;username;password;role;oc\n"
        file.write(header)
        
        # Tulis data ke file
        for baris in data:
            line = ";".join(map(str, baris.values()))  
            file.write(line + "\n")

#Contoh data
users=[{'id': 1, 'username': 'Mr_Monogram', 'password': 'monogrammer77', 'role': 'admin', 'oc': 0}, {'id': 2, 'username': 'Asep_Spakbor', 'password': 'asepwow123', 'role': 'agent', 'oc': 9999,}, {'id': 3, 'username': 'Agen_P', 'password': 'platypus123', 'role': 'agent', 'oc': 0}, {'id': 4, 'username': 'B4ngk1dd0ssss', 'password': 'bangkitganteng', 'role': 'agent', 'oc': 1337}, {'id': 5, 'username': 'Kenny_agen_rahasia', 'password': 'kribogeming55', 'role': 'agent', 'oc': 6699}, {'id': 6, 'username': 'bimo', 'password': 'gant3nk', 'role': 'agent', 'oc': 0}]
item_inventories=[{'user_id': 2, 'type': 'strength', 'quantity': 5}, {'user_id': 2, 'type': 'resilience', 'quantity': 3}, {'user_id': 3, 'type': 'resilience', 'quantity': 7}, {'user_id': 4, 'type': 'healing', 'quantity': 3}, {'user_id': 5, 'type': 'strength', 'quantity': 20}]
item_shop=[{'type': 1, 'stock': 10, 'price': 500}, {'type': 2, 'stock': 4, 'price': 700}, {'type': 3, 'stock': 3, 'price': 1000}, {'type': 4, 'stock': 8, 'price': 550}, {'type': 5, 'stock': 7, 'price': 600}]
monster=[{'id': 1, 'type': 'Pikachow', 'atk_power': 125, 'def_power': 10, 'hp': 600}, {'id': 2, 'type': 'Bulbu', 'atk_power': 50, 'def_power': 50, 'hp': 1200}, {'id': 3, 'type': 'Zeze', 'atk_power': 300, 'def_power': 10, 'hp': 100}, {'id': 4, 'type': 'Zuko', 'atk_power': 100, 'def_power': 25, 'hp': 800}, {'id': 5, 'type': 'Chacha', 'atk_power': 80, 'def_power': 30, 'hp': 700}]
monster_shop=[{'monster_id': 4, 'stock': 10, 'price': 5000},{'monster_id': 1, 'stock': 5, 'price': 300},{'monster_id': 3, 'stock': 3, 'price': 2000}]
monster_inventories=[{'user_id': 2, 'monster_id': 1, 'level': 1}, {'user_id': 3, 'monster_id': 2, 'level': 2}, {'user_id': 3, 'monster_id': 3, 'level': 1}, {'user_id': 4, 'monster_id': 4, 'level': 1}, {'user_id': 5, 'monster_id': 5, 'level': 5}, {'user_id': 6, 'monster_id': 4, 'level': 1}, {'user_id': 7, 'monster_id': 1, 'level': 1}, {'user_id': 8, 'monster_id': 1, 'level': 1}, {'user_id': 9, 'monster_id': 1, 'level': 1}, {'user_id': 6, 'monster_id': 1, 'level': 1}]
# Panggil fungsi save dengan data yang diinginkan
save(users, item_inventories, item_shop, monster, monster_shop, monster_inventories)
