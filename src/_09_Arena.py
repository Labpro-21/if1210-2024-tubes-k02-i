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




print('Selamat datang di Arena !!!\n')
print('Silahkan pilih monster yang anda ingin latih !!!\n')
print('============ MONSTER LIST ============')

# Mengeluarkan nama-nama dari monster yang tersedia
for idx in range(1, len(new_list) + 1):
    monster_list_name = new_list[idx - 1] 
    print(f'{idx}. {monster_list_name[1]}')

monster_list_name = new_list[1] # Mengambil nama dari element list

def is_include(user_monster_choice: int, idx: int) -> int :
    '''
    Fungsi untuk mengembalikan pilihan monster di range yang tersedia
    '''
    return 0 < user_monster_choice <= idx

print('')

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


def get_entries_and_monster_ids_with_level(data_list, target_level):
    '''
    Fungsi yang mengembalikan list berisi monster_id dengan level yang diinginkan
    '''
    # Initialize a list to store the filtered entries
    filtered_entries = []

    # Iterate over each entry
    for entry in data_list:
        user_id, monster_id, level = entry
        
        # Check if the level matches the target_level
        if level == str(target_level):
            filtered_entries.append(entry)
    
    # Collect all monster_id values that have the target_level
    monster_ids = [entry[1] for entry in filtered_entries]
    
    return monster_ids



#monster_enemy = [['1', 'Pikachow', '125', '10', '600'], ['2', 'Bulbu', '50', '50', '1200'], ['3', 'Zeze', '300', '10', '100'], ['4', 'Zuko', '100', '25', '800'], ['5', 'Chacha', '80', '30', '700'], ['6', 'Bimosaurus', '175', '30', '600'], ['7', 'Arceus', '100', '10', '1000'], ['8', 'Squirex', '250', '20', '500'], ['9', 'Mewthree', '100', '50', '200'], ['10', 'Luigi', '150', '30', '700']]


def print_monster_by_id(monster_id):
    '''
    Fungsi untuk mengembalikan sebuah list monster berdasarkan monster_id yang diinginkan 
    '''
    for monster in new_list:
        if monster[0] == str(monster_id):
            return monster

def search_level_by_id(monster_id):
    '''
    Fungsi untuk mengembalikan level monster sesuai dengan monster_id-nya
    '''
    for levels in new_list_2:
        if levels[1] == str(monster_id):
            return levels[2]

# Insialisasi variabel untuk digunakan dalam loop
over = False
clear = False
lose = False
win = False
total_attack_user = 0
total_attack_enemy = 0
turn_round = 1
stage_round = 1
oc_prize = 0

while not clear:
    print(f'============ STAGE {stage_round} ============')
    
    # Algoritma mencari monster musuh berdasarkan level yang setara dengan stage    
    monster_ids = get_entries_and_monster_ids_with_level(new_list_2, stage_round)
    length_monsterids = len(monster_ids)
    x = lcg.LCG(-1, length_monsterids-1) # Memilih monster_id secara random dengan rng
    monster_id_enemy = monster_ids[x]
    desired_monster_enemy = print_monster_by_id(monster_id_enemy)

    # Memilah nama, atk, def, dan health power monster musuh
    monster_enemy_name = desired_monster_enemy[1]
    attack_power_monster_enemy = int(desired_monster_enemy[2])
    defense_power_monster_enemy = int(desired_monster_enemy[3])
    health_monster_enemy = int(desired_monster_enemy[4])

    # Mencari level monster musuh dari database inventory
    monster_enemy_id_inventory = search_level_by_id(monster_id_enemy)
    level_monster_enemy = int(monster_enemy_id_inventory)

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
    health_monster_enemy_max = health_monster_enemy
    

    while not over:
        # RNG user
        attack_user_rng = lcg.LCG(30 * user_monster_choice_attack_power/100, 70 * user_monster_choice_attack_power/100)
        defense_user_rng = lcg.LCG(0, defense_power_monster_enemy)
        reduced_attack_user = ((100 - defense_user_rng) * attack_user_rng/100)

        # RNG musuh
        attack_enemy_rng = lcg.LCG(30 * attack_power_monster_enemy/100, 70 * attack_power_monster_enemy/100)
        defense_enemy_rng = lcg.LCG(0, user_monster_choice_defense_power)
        reduced_attack_enemy = ((100 - defense_enemy_rng) * attack_enemy_rng/100)
        
        print(f'============ TURN {turn_round} ({user_monster_choice_name}) ============')
        print('''1. Attack\n2. Use Potion\n3. Quit\n''')

        user_choice = int(input('Pilih perintah: ')) # User memilih perintah
        
        if user_choice == 1: # Ketika user memilih untuk Attack
            health_monster_enemy = math.floor(health_monster_enemy - reduced_attack_user) # HP monster musuh berkurang oleh ATK monster user yg sudah ter-RNG
            total_attack_user += reduced_attack_user
            
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
                # Permainan selesai
                over = True
                clear = True
                break
            
            # Monster musuh gantian menyerang
            print(f'============ TURN {turn_round} ({monster_enemy_name}) ============')
            user_monster_choice_health_power = math.floor(user_monster_choice_health_power - reduced_attack_enemy) # HP monster user berkurang oleh ATK monster user yg sudah ter-RNG
            total_attack_enemy += reduced_attack_enemy
            
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
                # Permainan selesai
                over = True 
                clear = True
            
            turn_round += 1

        elif user_choice == 2: # Ketika user memilih potion
            print('============ POTION LIST ============')
            # Deskripsi potion yang tersedia
            print(f'''1. Strength Potion (Qty: {strength_qty}) - Increases ATK Power\n2. Resilience Potion (Qty: {resilience_qty}) - Increases DEF Power\n3. Healing Potion (Qty: {healing_qty}) - Restores Health\n4. Cancel''')
            
            user_potion_choice = int(input('Pilih perintah: \n')) # User memilih potion atau cancel
           
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
            lose = True
            clear = True
            break
        
        else: 
            print('Perintah yang diberikan tidak tersedia, coba ulangi!')
        
    if stage_round >= 5: # Jika stage telah selesai
        print('Selamat! Anda telah menyelesaikan semua stage')
        print('============== STATS ==============')
        print(f'OC Prize : {oc_prize}\nJumlah stage : {stage_round}\nDamage diberikan : {math.floor(total_attack_user)}\nDamage diterima : {math.floor(total_attack_enemy)}\n')
        clear = True
        
    elif lose: # Jika kalah dalam battle di arena
        print(f'GAME OVER! Sesi latihan berakhir pada stage {stage_round}')
        print('============== STATS ==============')
        print(f'OC Prize : {oc_prize}\nJumlah stage : {stage_round}\nDamage diberikan : {math.floor(total_attack_user)}\nDamage diterima : {math.floor(total_attack_enemy)}\n')

    elif win: # Jika menang dalam battle di arena
        print('Menuju ke stage berikutnya....')
        over = False
        clear = False
        lose = False
        win = False
        user_monster_choice_health_power = user_monster_choice_health_power_max
        health_monster_enemy = health_monster_enemy_max
        oc_prize += 30
        stage_round += 1
        turn_round = 1
