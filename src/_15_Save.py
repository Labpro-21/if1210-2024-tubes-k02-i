
import os

def save(users : Data, item_inventories : Data, item_shop : Data, monster : Data, monster_shop : Data, monster_inventory : Data) -> None:
"""
memeriksa apakah folder yang dimaksud sudah ada dan akan membuat folder baru jika belum serta menyimpan file csv ke folder tersebut
"""
    # Tentukan folder utama sebagai "save"
    parent_folder= "data"
    # Menerima data sebagai list atau dictionary
    folder = "data/" + input("Masukkan nama folder: ")
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


def data_save(path : str, file_name : str, data : Data) -> None:
    file_path = path + "/" + file_name + ".csv"
"""
menyimpan data dari bentuk list of dictionaries menjadi csv di suatu folder
"""
    # tulis header
    with open(file_path, 'w') as file:
        if file_name == "item_inventory":
            header = "user_id;type;quantity\n"
        elif file_name == "item_shop":
            header = "type;stock;price\n"
        elif file_name == "monster":
            header = "id;type;atk_power;def_power;hp\n"
        elif file_name == "monster_inventory":
            header = "user_id;monster_id;level\n"
        elif file_name == "monster_shop":
            header = "monster_id;stock;price\n"
        elif file_name == "user":
            header = "id;username;password;role;oc\n"
        file.write(header)
        
        # Tulis data ke file
        for row in data:
            line = ""
            for row in baris:
                line += str(item) + ";"
            file.write(line[:-1] + "\n")


