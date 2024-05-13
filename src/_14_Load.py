import argparse
import os
import sys

def main():
     #argument parser dengan deskripsi program
    parser = argparse.ArgumentParser(description="Menjalankan main.py dalam folder yang spesifik di dalam folder parent 'data'")
     #argumen non-opsional
    parser.add_argument("nama_folder", nargs='?', help="Nama folder di dalam parent 'data'")
     #mengurai argumen
    args = parser.parse_args()

    if args.nama_folder is None:#tidak ada input
        print("Tidak ada nama folder yang diberikan!\nUsage : python main.py <nama_folder>")
        sys.exit()

    folder_path = f"data/{args.nama_folder}"

    #memeriksa apakah folder yang dimasukkan ada
    if os.path.isdir(folder_path):
        print("Loading...")
        print("Selamat Datang di program OWCA!")
        #mencari jalur (path) main.py di folder yang dituju
        main_py_path = f"{folder_path}/main.py"
        #eksekusi main.py
        os.system(f"python {main_py_path}")
    else:print(f"Folder '{args.nama_folder}' tidak ditemukan.")

if __name__ == "__main__":
    main()