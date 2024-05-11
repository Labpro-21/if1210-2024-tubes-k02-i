# KAMUS
# seed : integer
# ALGORITMA
from time import time
seed = int(time())
# seed akan terus berubah
# Mengembalikan angka random dengan algoritma Linear Congruential Generator (LCG) dengan angka rentang 0 - batas_atas.
#seed: Nilai awal (biji) untuk memulai urutan.
#a: Pengganda dalam rumus LCG.
#c: Penambahan dalam rumus LCG.
#m: Modulus dalam rumus LCG.

#rumus LCG= (a * seed + b) mod m
#syarat : 0<m , 0 < a < m , 0 <= x < m, 0<seed<m
def LCG(batas_atas : int) -> int:
    # KAMUS LOKAL:
        # const a : integer = 1664525
        # constb c : integer = 1013904223
        # const m : integer = 2^32
    
    # ALGORITMA
    a = 1664525
    c = 1013904223
    m = 2**32
    global seed
    seed = (a*seed + c) % m
    return seed % (batas_atas + 1)

def head_csv(data: list[str])->list[str]:
    """
    Mengambil head dari list of list dalam csv
    """
    header = []
    for i in range(len(data[0])):
        header.append(data[0][i])
    return header

def list_of_dicts(head: list[str],data: list[str])->list[dict[str]]:
    """
    Membuat list of dictionary
    """
    list_of_dicts = []
    for inner_list in data:
        row_dict = {}
        for i, value in enumerate(inner_list):
            row_dict[head[i]] = value
        list_of_dicts.append(row_dict)
    return list_of_dicts

def data_csv(data: list[str])->list[str]:
    """
    Membuat data tanpa head
    """  
    datas = []
    for i in range(1,len(data)):
        datas.append(data[i])
    return datas

def read_csv(file_path: str)->list[dict[str]]:
    """
    Membaca file csv menjadi list of dictionarry
    """
    array = []
    temp = ''
    data_temp = []
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char != ';' and char != '\n':
                    temp += char
                else:
                    data_temp.append(temp)
                    temp = ''
            array.append(data_temp)
            data_temp = []
            
    head = head_csv(array)
    # print(head)
    array_data = data_csv(array)
    # print(array_data)
    data = list_of_dicts(head, array_data)
    return data
 

def write_csv(file_path: str,data: str)->str:
    """ 
    Menuliskan data ke file csv
    """
    with open(file_path, 'a') as csvfile:
        if csvfile.tell() != 0:
            csvfile.write('\n')
        csvfile.write(data)
        
def join_array(data:list[str])->str:
    """ 
    Menggabungkan kembali list of dictionarry menjadi format csv
    """
    csv = ''
    keys = list(data[0].keys())
    for i in range(len(keys)):
        if i == len(keys)-1:
            csv+=keys[i]
            csv+='\n'
        else:
            csv+=keys[i]
            csv+=';'

    for i in range(len(data)):
        values = list(data[i].values())
        for j in range(len(keys)):
            if j == (len(keys)-1):
                csv+=values[j]
                csv += '\n'
            else:
                csv+=values[j]
                csv+=';'
    return csv

def generate_id(data:list[str])->int:
    num_id = len(data)
    # for i in range(len(data)):
    #     if num_id == data[i][0]:
    #         return generate_id(data)
    return num_id
    

data = read_csv(r'monster.csv')
    
new_list = []

# Append header row
header_row = list(data[0].keys())
new_list.append(header_row)

# Append data rows
for entry in data:
    values = list(entry.values())
    new_list.append(values)
    
# Hapus baris pertama di list (baris yang berisi keterangan data)
new_list = new_list[1:]


x=LCG(len(new_list)) 

'''
len(new_list) mengasumsikan bahwa batas LGC sebanyak baris dari new_list
'''
desired_monster_enemy = new_list[x-1] #new_list[x-1] karena panjang list dihitung dari 0
monster_enemy_name = desired_monster_enemy[1]
attack_power_monster_enemy = int(desired_monster_enemy[2])
defense_power_monster_enemy = int(desired_monster_enemy[3])
health_monster_enemy = int(desired_monster_enemy[4])

# Output
print(f'''RAWRRR, Monster {monster_enemy_name} telah muncul !!!
      ''')

print(f'''Name : {monster_enemy_name}
ATK Power : {attack_power_monster_enemy}
DEF Power : {defense_power_monster_enemy}
HP : {health_monster_enemy}
Level : dari inventory
      ''')
print('============ MONSTER LIST ============')
# Memodifikasi list sebelumnya (new_list) dengan menghilangkan desired_monster_list dari new_list
index_to_remove = None
for idx in range(len(new_list)):
    if new_list[idx] == desired_monster_enemy:
        index_to_remove = idx
        break
    
if index_to_remove is not None:
    monster_list = new_list.pop(index_to_remove)

    # Panjang sisa dari list yang sudah termodifikasi 
    monster_list_row = len(new_list)
    
    # Output print nama tiap monster yang belum terpakai dari new_list (monster_list_name)
    for idx in range(1, len(new_list) + 1):
        monster_list_name = new_list[idx - 1]  # Adjust index to start from 0
        print(f'{idx}. {monster_list_name[1]}')


monster_list_name = monster_list[1] # Mengindikasikan sebuah variabel nama monster dari monster_list

# Fungsi untuk memeriksa apakah input user_monster_choice sudah sesuai dalam range
def is_include(user_monster_choice, idx):
    return 0 < user_monster_choice <= idx

# Input dan memanggil fungsi is_include
user_monster_choice = int(input('Pilih monster untuk bertarung: '))
is_include(user_monster_choice, idx)

# Looping terjadi apabila inputan user_monster_choice tidak sesuai dalam range
# Looping menghasilkan input baru untuk diperiksa dalam fungsi hingga berhasil
while not is_include(user_monster_choice, idx):
    print('''Pilihan monster tidak tersedia!
Coba lagi!''')
    user_monster_choice = int(input('Pilih monster untuk bertarung: '))

# Apabila input berhasil
user_monster_choice_list = new_list[user_monster_choice - 1]
user_monster_choice_name = user_monster_choice_list[1]
user_monster_choice_attack_power = int(user_monster_choice_list[2])
user_monster_choice_defense_power = int(user_monster_choice_list[3])
user_monster_choice_health_power = int(user_monster_choice_list[4])


print(f'''RAWRRR, Agent X mengeluarkan monster {user_monster_choice_name} !!!
      ''')

print(f'''Name : {user_monster_choice_name}
ATK Power : {user_monster_choice_attack_power}
DEF Power : {user_monster_choice_defense_power}
HP : {user_monster_choice_health_power}
Level : dari inventory
      ''')

over = False
lose = False
win = False
turn_round = 1
while not over:
    print(f'============ TURN {turn_round} ({user_monster_choice_name}) ============')
    print('''1. Attack
2. Use Potion
3. Quit''')
    user_choice = int(input('Pilih perintah: '))
    
    if user_choice == 1:
        health_monster_enemy = health_monster_enemy - user_monster_choice_attack_power
        
        if health_monster_enemy <= 0:
            health_monster_enemy = 0
            win = True

        print(f'''SKADIDODOO, {user_monster_choice_name} menyerang {monster_enemy_name} !!!
              ''')
        print(f'''Name : {monster_enemy_name}
ATK Power : {attack_power_monster_enemy}
DEF Power : {defense_power_monster_enemy}
HP : {health_monster_enemy}
Level : dari inventory
      ''')
        
        if win:
            print(f'Selamat anda mengalahkan monster {monster_enemy_name} !!!')
            over = True
            break
        
        print(f'============ TURN {turn_round} ({monster_enemy_name}) ============')
        user_monster_choice_health_power = user_monster_choice_health_power - attack_power_monster_enemy
        
        if user_monster_choice_health_power <= 0:
            user_monster_choice_health_power = 0
            lose = True
            
        print(f'''SKADLIDODOR, {monster_enemy_name} menyerang {user_monster_choice_name} !!!
              ''')
        print(f'''Name : {user_monster_choice_name}
ATK Power : {user_monster_choice_attack_power}
DEF Power : {user_monster_choice_defense_power}
HP : {user_monster_choice_health_power}
Level : dari inventory''')
        
        if lose:
            print(f'Tidakkk, kamu telah dikalahkan oleh {monster_enemy_name} !!!')
            over = True
            break
    
    #elif user_choice == 2:
        #print('============ POTION LIST ============')
        #print(f'''1. Strength Potion (Qty: {}) - Increases ATK Power
#2. Resilience Potion (Qty: {}) - Increases DEF Power
#3. Healing Potion (Qty: {}) - Restores Health
#4. Cancel''')
       #user_potion_choice = int(input('Pilih perintah: '))
        
        #if user_potion_choice == 1:
            
    turn_round += 1
    
'''
ongoing

'''