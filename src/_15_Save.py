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
#KAMUS LOKAL
    file_path = os.path.join(path, f"{nama_file}.csv")
    # tulis header
    with open(file_path, 'w') as file:
        if nama_file == "item_inventory":
            file.write("user_id;type;quantity\n")
        elif nama_file == "item_shop":
            file.write("type;stock;price\n")
        elif nama_file == "monster":
            file.write("id;type;atk_power;def_power;hp\n")
        elif nama_file == "monster_inventory":
            file.write("user_id;monster_id;level\n")
        elif nama_file == "monster_shop":
            file.write("monster_id;stock;price\n")
        elif nama_file == "user":
            file.write("id;username;password;role;oc\n")
        
        # Tulis data ke file
        for baris in data:
            line = ";".join(map(str, baris))  
            file.write(line + "\n")


# Contoh penggunaan
users = [[1, 'Mr_Monogram', 'monogrammer77', 'admin', 0], [2, 'Asep_Spakbor', 'asepwow123', 'agent', 9999], [3, 'Agen_P', 'platypus123', 'agent', 0], [4, 'B4ngk1dd0ssss', 'bangkitganteng', 'agent', 1337], [5, 'Kenny_agen_rahasia', 'kribogeming55', 'agent', 6699], [6, 'bimo', 'gant3nk', 'agent', 0]]
item_inventories = [[2, 'strength', 5], [2, 'resilience', 3], [3, 'resilience', 7], [4, 'healing', 3], [5, 'strength', 20]]
item_shop = [[1, 10, 500], [2, 4, 700], [3, 3, 1000], [4, 8, 550], [5, 7, 600]]
monster=[[1, 'Pikachow', 125, 10, 600], [2, 'Bulbu', 50, 50, 1200], [3, 'Zeze', 300, 10, 100], [4, 'Zuko', 100, 25, 800], [5, 'Chacha', 80, 30, 700]]
monster_shop=[['strength', 10, 50], ['resilience', 5, 30], ['healing', 3, 20]]
monster_inventory=[[2, 1, 1], [3, 2, 2], [3, 3, 1], [4, 4, 1], [5, 5, 5], [6, 4, 1], [7, 1, 1], [8, 1, 1], [9, 1, 1], [6, 1, 1]]

# Panggil fungsi save dengan data yang diinginkan
save(users, item_inventories, item_shop, monster, monster_shop, monster_inventory)
