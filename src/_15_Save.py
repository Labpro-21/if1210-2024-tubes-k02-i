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
     file_path = path + "/" + nama_file + ".csv"
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
            line = ""
            for item in baris:
                line += str(item) + ";"
            file.write(line[:-1] + "\n")


