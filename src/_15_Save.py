import CSVfunction as csv
import DataPath as dp
import os

def save(user, item_inventories, item_shop, monster, monster_shop, monster_inventory) -> None:
    """
    memeriksa apakah folder yang dimaksud sudah ada dan akan membuat folder baru jika belum serta menyimpan file csv ke folder tersebut
    """
    # Tentukan folder utama sebagai "data"
    parent_folder= "data"
    # Menerima data sebagai list atau dictionary
    folder = "data/" + input("Masukkan nama folder: ")
    print("Saving...")
    # Periksa apakah folder /data sudah ada
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
    data_save(folder, "user", user)
    data_save(folder, "item_inventory", item_inventories)
    data_save(folder, "item_shop", item_shop)
    data_save(folder, "monster", monster)
    data_save(folder, "monster_shop", monster_shop)
    data_save(folder, "monster_inventory", monster_inventory)

    print(f"Berhasil menyimpan data di folder {folder}!")


def data_save(path : str, file_name : str, data ) -> None:
    file_path = path + "/" + file_name + ".csv"
    """
    menyimpan data dari bentuk list of dictionaries menjadi csv di suatu folder
    """
    if file_name == "item_inventory":
        sort_data(data,'user_id')
    elif file_name == "monster":
        sort_data(data,'id')
    elif file_name == "monster_inventory":
        sort_data(data, 'user_id')
    elif file_name == "monster_shop":
        sort_data(data, 'monster_id')
    elif file_name == "user":
        sort_data(data, 'id')
        
    data = csv.join_array(data)
    
    with open(file_path, 'w') as csvfile:
        csvfile.write(data)
            
def sort_data(data,sortby):
    '''
    Mengurutkan data sesuai urutannya
    '''
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(data[j][sortby]) > int(data[j+1][sortby]):
                data[j], data[j+1] = data[j+1], data[j]
            
if __name__ == "__main__":
    monster_shop_data , item_shop_data, potion_data, monster_inventory_data, item_inventory, monster_data, user_data = dp.data_path('data')
    save(user_data, item_inventory, item_shop_data, monster_data, monster_shop_data, monster_inventory_data)
    pass
    # save(users, item_inventories, item_shop, monster, monster_shop, monster_inventory)

