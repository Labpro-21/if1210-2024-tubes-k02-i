import CSVfunction as csv
import _00_LCG as lcg
import os
import math
from GameState import username
dirname = os.path.dirname(__file__)
    
monster_path = os.path.join(dirname, '../data/monster.csv')
monster_inventory_path = os.path.join(dirname, '../data/monster_inventory.csv')
potion_path = os.path.join(dirname, '../data/_06_potion.csv')
item_inventory_path = os.path.join(dirname, '../data/item_inventory.csv')
user_inventory_path = os.path.join(dirname, '../data/user.csv')
data = csv.read_csv(monster_path)
data_2 = csv.read_csv(monster_inventory_path)
data_3 = csv.read_csv(potion_path)
data_4 = csv.read_csv(item_inventory_path)
data_5 = csv.read_csv(user_inventory_path)
    
new_list = []
# Mengubah data menjadi list
# Append header row
header_row = list(data[0].keys())
new_list.append(header_row)

# Append data rows
for entry in data:
    values = list(entry.values())
    new_list.append(values)
    
# Hapus baris pertama di list (baris yang berisi keterangan data)
new_list = new_list[1:]

new_list_2 = []
# Mengubah data_2 menjadi list
# Append header row
header_row = list(data_2[0].keys())
new_list_2.append(header_row)

# Append data rows
for entry in data_2:
    values = list(entry.values())
    new_list_2.append(values)
    
# Hapus baris pertama di list (baris yang berisi keterangan data)
new_list_2 = new_list_2[1:]


x=lcg.LCG(0, len(new_list)) # RNG mengasumsikan bahwa batas sebanyak baris dari list monster database

monster_enemy = [['1', 'Pikachow', '125', '10', '600'], ['2', 'Bulbu', '50', '50', '1200'], ['3', 'Zeze', '300', '10', '100'], ['4', 'Zuko', '100', '25', '800'], ['5', 'Chacha', '80', '30', '700'], ['6', 'Bimosaurus', '175', '30', '600'], ['7', 'Arceus', '100', '10', '1000'], ['8', 'Squirex', '250', '20', '500'], ['9', 'Mewthree', '100', '50', '200'], ['10', 'Luigi', '150', '30', '700']]
desired_monster_enemy = monster_enemy[x-1] # Mengambil monster musuh dengan fungsi RNG

# Memilah nama, atk, def, dan health power monster musuh
monster_enemy_name = desired_monster_enemy[1]
attack_power_monster_enemy = int(desired_monster_enemy[2])
defense_power_monster_enemy = int(desired_monster_enemy[3])
health_monster_enemy = int(desired_monster_enemy[4])
health_monster_enemy_max = int(desired_monster_enemy[4])

# Mencari level monster musuh dari database inventory
monster_enemy_id_inventory = new_list_2[x-1]
level_monster_enemy = int(monster_enemy_id_inventory[2])

print(f'''RAWRRR, Monster {monster_enemy_name} telah muncul !!!''')

# Mengeluarkan ASCII art monster musuh
print(r'''
          /\----/\_   
         /         \   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \  |   |   |
         |  |   |   |
          \._\   \._\ 

      ''')
    

# Mengeluarkan deskripsi monster musuh
print(f'Name : {monster_enemy_name}\nATK Power : {attack_power_monster_enemy}\nDEF Power : {defense_power_monster_enemy}\nHP : {health_monster_enemy}\nLevel : {level_monster_enemy}\n')

print('============ MONSTER LIST ============')

# Memodifikasi list sebelumnya (monster_enemy) dengan menghilangkan desired_monster_enemy dari monster_enemy
# Tujuan untuk monster musuh tidak sama dengan pilihan monster user
index_to_remove = None
for idx in range(len(new_list)):
    if new_list[idx] == desired_monster_enemy:
        index_to_remove = idx
        break
    
if index_to_remove is not None:
    monster_list = new_list.pop(index_to_remove)

    # Panjang sisa dari list yang sudah termodifikasi 
    monster_list_row = len(new_list)
    
    # Output print nama tiap monster yang belum terpakai
    for idx in range(1, len(new_list) + 1):
        monster_list_name = new_list[idx - 1] 
        print(f'{idx}. {monster_list_name[1]}')

monster_list_name = monster_list[1] # Mengambil nama monster yang tersisa

def is_include(user_monster_choice: int, idx: int) -> int :
    '''
    Fungsi untuk mengembalikan pilihan monster di range yang tersedia
    '''
    return 0 < user_monster_choice <= idx

# User memanggil monster yang tersedia dan memanggil fungsi is_include
user_monster_choice = int(input('Pilih monster untuk bertarung: '))
is_include(user_monster_choice, idx)

# Looping terjadi apabila inputan user_monster_choice tidak sesuai dalam range
while not is_include(user_monster_choice, idx):
    print('''Pilihan monster tidak tersedia! Coba lagi!\n''')
    user_monster_choice = int(input('Pilih monster untuk bertarung: ')) # Looping menghasilkan input baru untuk diperiksa dalam fungsi is_include hingga berhasil


user_monster_choice_list = new_list[user_monster_choice - 1] # Mengambil monster pilihan user

# Memilah nama, atk, defense, dan health power monster user
user_monster_choice_name = user_monster_choice_list[1]
user_monster_choice_attack_power = int(user_monster_choice_list[2])
user_monster_choice_defense_power = int(user_monster_choice_list[3])
user_monster_choice_health_power = int(user_monster_choice_list[4])
user_monster_choice_health_power_max = int(user_monster_choice_list[4]) # Inisialisasi besar maksimal HP monster user

# Mencari level monster user dari database inventory
user_monster_id_inventory = new_list_2[user_monster_choice - 1]
user_monster_level = int(user_monster_id_inventory[2])

print(f'''RAWRRR, Agent {username} mengeluarkan monster {user_monster_choice_name} !!!\n''')

# Mengeluarkan ASCII art monster user
print(r'''
           _/\----/\\   
          /         \\     /\\
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \\  |  |
        /   `^^^^^'    \\ |  |
      ./  /|            \\|  |_
     /   / |         |\\__     /
     \\  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__

      ''')

# Mengeluarkan deskripsi monster user
print(f'Name : {user_monster_choice_name}\nATK Power : {user_monster_choice_attack_power}\nDEF Power : {user_monster_choice_defense_power}\nHP : {user_monster_choice_health_power}\nLevel : {user_monster_level}\n')

# RNG user
attack_user_rng = lcg.LCG(30 * user_monster_choice_attack_power/100, 70 * user_monster_choice_attack_power/100)
defense_user_rng = lcg.LCG(0, defense_power_monster_enemy)
reduced_attack_user = ((100 - defense_user_rng) * attack_user_rng/100)

# RNG musuh
attack_enemy_rng = lcg.LCG(30 * attack_power_monster_enemy/100, 70 * attack_power_monster_enemy/100)
defense_enemy_rng = lcg.LCG(0, user_monster_choice_defense_power)
reduced_attack_enemy = ((100 - defense_enemy_rng) * attack_enemy_rng/100)

# RNG coin
oc_generator = lcg.LCG(4, 30)

# Mencari data pada database potion
strength_qty = 0
resilience_qty = 0
healing_qty = 0

for strength in data_4:
    if strength['type'] == 'strength':
        strength_qty += int(strength['quantity'])
for resilience in data_4:
    if resilience['type'] == 'resilience':
        resilience_qty += int(resilience['quantity'])      
for healing in data_4:
    if healing['type'] == 'healing':
        healing_qty += int(healing['quantity'])

for strength_ in data_3:
    if strength_['potion_name'] == 'strength':
        strength_percentage = int(strength_['percentage'])
for resilience_ in data_3:
    if resilience_['potion_name'] == 'resilience':
        resilience_percentage = int(resilience_['percentage'])
for healing_ in data_3:
    if healing_['potion_name'] == 'resilience':
        healing_percentage = int(healing_['percentage'])

# Insialisasi variabel untuk digunakan dalam loop
over = False
lose = False
win = False
turn_round = 1

while not over: # Ketika pertarungan belum usai
    print(f'============ TURN {turn_round} ({user_monster_choice_name}) ============')
    print('''1. Attack\n2. Use Potion\n3. Quit''')

    user_choice = int(input('Pilih perintah: ')) # User memilih perintah
    
    if user_choice == 1: # Ketika user memilih untuk Attack
        health_monster_enemy = math.floor(health_monster_enemy - reduced_attack_user) # HP monster musuh berkurang oleh ATK monster user yg sudah ter-RNG
        if health_monster_enemy <= 0: 
            health_monster_enemy = 0 # Mengembalikan HP monster musuh yang tidak boleh kurang dari 0
            win = True # Jika HP monster musuh sudah 0
            
        # Deskripsi penyerangan dan dampak pada monster musuh
        print(f'SKADIDODOO, {user_monster_choice_name} menyerang {monster_enemy_name} !!!\n')
        print(f'Name : {monster_enemy_name}\nATK Power : {attack_power_monster_enemy}\nDEF Power : {defense_power_monster_enemy}\nHP : {health_monster_enemy}\nLevel : {level_monster_enemy}\n')
        print(f'# Penjelasan: ATT: {attack_user_rng}, Reduced by: {defense_user_rng}, ATT Results: {reduced_attack_user}')
        
        # Jika menang
        if win:
            print(f'Selamat anda mengalahkan monster {monster_enemy_name} !!!')
            print(f'Total OC yang diperoleh: {oc_generator}') # User mendapatkan OC coin dari hasil RNG dan menambahkannya pada database user
            user_monster_choice_health_power = user_monster_choice_health_power_max
            health_monster_enemy = health_monster_enemy_max 
            over = True # Permainan selesai
            break
        
        # Monster musuh gantian menyerang
        print(f'============ TURN {turn_round} ({monster_enemy_name}) ============')
        user_monster_choice_health_power = math.floor(user_monster_choice_health_power - reduced_attack_enemy) # HP monster user berkurang oleh ATK monster user yg sudah ter-RNG
        
        if user_monster_choice_health_power <= 0:
            user_monster_choice_health_power = 0 # Mengembalikan HP monster user yang tidak boleh kurang dari 0
            lose = True # Jika HP monster user sudah 0
            
        # Deskripsi penyerangan dan dampak pada monster user    
        print(f'SKADLIDODOR, {monster_enemy_name} menyerang {user_monster_choice_name} !!!\n')
        print(f'Name : {user_monster_choice_name}\nATK Power : {user_monster_choice_attack_power}\nDEF Power : {user_monster_choice_defense_power}\nHP : {user_monster_choice_health_power}\nLevel : {user_monster_level}\n')
        print(f'# Penjelasan: ATT: {attack_enemy_rng}, Reduced by: {defense_enemy_rng}, ATT Results: {reduced_attack_enemy}')
        
        # Jika kalah
        if lose:
            print(f'Tidakkk, kamu telah dikalahkan oleh {monster_enemy_name} !!!')
            user_monster_choice_health_power = user_monster_choice_health_power_max
            health_monster_enemy = health_monster_enemy_max 
            over = True # Permainan selesai
            break
        turn_round += 1 # Round battle bertambah apabila kedua pihak monster selesai menyerang

    elif user_choice == 2: # Ketika user memilih potion
        print('============ POTION LIST ============')
        # Deskripsi potion yang tersedia
        print(f'''1. Strength Potion (Qty: {strength_qty}) - Increases ATK Power\n2. Resilience Potion (Qty: {resilience_qty}) - Increases DEF Power\n3. Healing Potion (Qty: {healing_qty}) - Restores Health\n4. Cancel''')
        
        user_potion_choice = int(input('Pilih perintah: ')) # User memilih potion atau cancel

        
        if user_potion_choice == 1: # Jika user memilih potion strength
            if strength_qty == 0: # Jika potion strength tidak tersedia
                print('Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!')
            else: # Jika potion strength tersedia
                user_monster_choice_attack_power *= (strength_percentage + 100) / 100 # Attack power bertambah
                strength_qty -= 1 # Ketersediaan potion berkurang 1
                
                # Deskripsi perubahan pada monster user
                print(f'Name : {user_monster_choice_name}\nATK Power : {user_monster_choice_attack_power}\nDEF Power : {user_monster_choice_defense_power}\nHP : {user_monster_choice_health_power}\nLevel : {user_monster_level}\n')
                print(f'# Penjelasan: Attack power monster bertambah sebesar {strength_percentage}% menjadi: {user_monster_choice_attack_power}')
                          
        elif user_potion_choice == 2: # Jika user memilih potion resilience
            if resilience_qty == 0: # Jika poton resilience tidak tersedia
                print('Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!')
            else: # Jika potion resilience tersedia
                user_monster_choice_defense_power *= (resilience_percentage + 100) / 100
                resilience_qty -= 1 # Ketersediaan potion berkurang 1
                
                # Deskripsi perubahan pada monster user
                print(f'Name : {user_monster_choice_name}\nATK Power : {user_monster_choice_attack_power}\nDEF Power : {user_monster_choice_defense_power}\nHP : {user_monster_choice_health_power}\nLevel : {user_monster_level}\n')
                print(f'# Penjelasan: Defense power monster bertambah sebesar {resilience_percentage}% menjadi: {user_monster_choice_defense_power}')
                
        elif user_potion_choice == 3: # Jika user memilih potion healing
            if healing_qty == 0: # Jika potion healing tidak tersedia
                print('Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!')
            else: # Jika potion healing tersedia
                user_monster_choice_health_power *= (healing_percentage + 100) / 100
                healing_qty -= 1           
                
                 # Deskripsi perubahan pada monster user
                print(f'Name : {user_monster_choice_name}\nATK Power : {user_monster_choice_attack_power}\nDEF Power : {user_monster_choice_defense_power}\nHP : {user_monster_choice_health_power}\nLevel : {user_monster_level}\n')
                print(f'# Penjelasan: Health power monster bertambah sebesar {healing_percentage}% menjadi: {user_monster_choice_health_power}')
            
            if user_monster_choice_health_power > user_monster_choice_health_power_max: # Jika HP monster user bertambah lebih dari maksimum HP-nya
                user_monster_choice_health_power = user_monster_choice_health_power_max # HP monster user akan sama dengan HP monster maksimumnya
                
        elif user_potion_choice == 4: # Jika user memilih cancel
            over = False # Kembali looping 
        
        else: # Jika pilihan user tidak tersedia
            print('Perintah yang diberikan tidak tersedia, coba ulangi!')

    elif user_choice == 3: # Jika user memilih Quit
        print('Anda berhasil kabur dari BATTLE !')
        break 
    
    else:
        print('Perintah yang diberikan tidak tersedia, coba ulangi!')