list_siswa = [
    ['Prayoga',70, 90, 80,85,52608, 'otomotif'],
    ['Diah', 65, 87, 92,90, 67913, 'multimedia'],
    ['Amanda', 80, 70, 72,75, 45821, 'multimedia'],
    ['Anisa', 85, 70, 84,90, 73596, 'otomotif'],
    ['Joko', 76, 68, 90,86, 69785, 'otomotif'],
    ['Heri', 85, 75, 60,65, 79612, 'multimedia']
]

def menu_opsi():
       print('''
    --------------------------------
    |SELAMAT DATANG DI SMKN 1 BENDO|
    --------------------------------

        === MAIN MENU ===
    ---------------------------
    1. Melihat Menu Data Siswa
    2. Membuat Data Siswa
    3. Merubah Data Siswa
    4. Hapus Data Siswa
    5. Menampilkan Kelulusan Data Siswa
    6. Keluar
''')

def check_nis(cek,nis):  #  fungsi cek duplikat no induk siswa
    for cek in list_siswa:
        if cek[5] == nis:
            return cek
    return None

def validasi_nis(nis):#  fungsi validasi  input untuk harus angka untuk fitur delet data
    if not nis.isdigit():
        print("Input NIS harus berupa angka!")
        return False
    nis = int(nis)
    return any(siswa[5] == nis for siswa in list_siswa)

# fungsi untuk cek duplikat dan panjang 
def is_valid_nis(nis):
    if not nis.isdigit() or len(nis) != 5:
        return False
    for siswa in list_siswa:
        if siswa[5] == int(nis):
            return False
    return True
# fungsi untuk mencari nama itu huruf dan tidak boleh dari 10 huruf
def is_valid_nama(nama):
    if not nama.isalpha() or len(nama) > 10:
        return False
    return True
# fungsi untuk mentukan nilai tidak boleh lebih dari 100 dan harus angka
def is_valid_nilai(nilai):
    if not nilai.isdigit() or int(nilai) > 100:
        return False
    return True
# fungsi untuk menentukan jurusan
def is_valid_jurusan(jurusan):
    if jurusan.lower() not in ['otomotif', 'multimedia']:
        return False
    return True
# fungsi untuk no 1 yaitu read data 
def melihat_menu_data_siswa():
    while True:
        print('\n\t-------------------------')
        print("\t|MELIHAT MENU DATA SISWA| ")
        print('\t-------------------------')
        opsi_melihat = input('''
            PILIHAN OPTION
        -----------------------
        1. Tampilkan semua data
        2. Cari berdasarkan NIS
        3. Kembali ke Main Menu
        
        Masukkan pilihan (1-3): ''')

        #tampilkan semua data
        if opsi_melihat == '1': 
            if not list_siswa:
                print("\n\tData tidak ada!")
                continue

            print("\n\t\t  === DATA SISWA ===")
            print('--------------------------------------------------------')
            print("NAMA\tMTK\tB.INDO\tB.ING\tTEKNIK\tNIS\tJURUSAN")
            print('--------------------------------------------------------')
            for siswa in list_siswa:
                print('\t'.join(str(data) for data in siswa))

        #cari berdasarkan nis
        elif opsi_melihat == '2': 
            nis = int(input("\n\tMasukkan NIS siswa yang ingin dicari: "))

            hasil = check_nis(list_siswa,nis)
            if hasil:
                print("\n\t\t=== DATA SISWA ===")
                print('---------------------------------------------------------')
                print("NAMA\tMTK\tB.INDO\tB.ING\tTEKNIK\tNIS\tJURUSAN")
                print('---------------------------------------------------------')
                for siswa in list_siswa:
                    if siswa[5] == int(nis):
                        print('\t'.join(str(data) for data in siswa))
            else:
                print('\n\tnis siswa tidak di temukan')
        elif opsi_melihat == '3':
            break

        else:
            print("\n\tPilihan tidak valid!")

        # tampilkan kelulusan
        

# fungsi untuk no 2 untuk add data
def membuat_data_siswa():
    while True:  # fungsi untuk terus melakukan perulangan
        print('\n\t--------------------')
        print("\t|MEMBUAT DATA SISWA| ")
        print('\t--------------------')
        opsi_membuat = input('''
            PILIHAN OPTION
        -----------------------
        1. Tambah siswa
        2. Kembali ke Main Menu
        Masukkan pilihan (1/2): ''')

        # untuk membuat data 
        if opsi_membuat == '1':
            while True: # fungsi untuk terus melakukan perulangan
                no_nis = input("\n\tMasukkan NIS siswa baru: ")
                if not is_valid_nis(no_nis):
                    print('\n\tNIS tidak valid! Pastikan NIS berupa 5 angka dan belum ada sebelumnya.')
                    continue
                break

            while True: # fungsi untuk terus melakukan perulangan
                nama = input("\tMasukkan nama siswa baru: ")
                if not is_valid_nama(nama):
                    print('\n\tNama tidak valid! Pastikan nama hanya terdiri dari huruf dan maksimal 10 karakter.')
                    continue
                break

            while True: # fungsi untuk terus melakukan perulangan
                matematika = input("\tMasukkan nilai matematika siswa: ")
                if not is_valid_nilai(matematika):
                    print('\n\tNilai matematika tidak valid! Pastikan nilai berupa angka dan tidak lebih dari 100.')
                    continue
                break
 
            while True: # fungsi untuk terus melakukan perulangan
                indonesia = input("\tMasukkan nilai B.Indonesia siswa: ")
                if not is_valid_nilai(indonesia):
                    print('\n\tNilai B. Indonesia tidak valid! Pastikan nilai berupa angka dan tidak lebih dari 100.')
                    continue
                break

            while True: # fungsi untuk terus melakukan perulangan
                inggris = input("\tMasukkan nilai B.Inggris siswa: ")
                if not is_valid_nilai(inggris):
                    print('\n\tNilai B. Inggris tidak valid! Pastikan nilai berupa angka dan tidak lebih dari 100.')
                    continue
                break

            while True: # fungsi untuk terus melakukan perulangan
                teknik = input("\tMasukkan nilai teknik siswa: ")
                if not is_valid_nilai(teknik):
                    print('\n\tNilai teknik tidak valid! Pastikan nilai berupa angka dan tidak lebih dari 100.')
                    continue
                break

            print('\n\t===PILIHAN JURUSAN===\n\tOtomotif/Multimedia')
            while True: # fungsi untuk terus melakukan perulangan
                jurusan = input("\tMasukkan jurusan siswa: ")
                if not is_valid_jurusan(jurusan):
                    print('\n\tJurusan tidak valid! Pastikan jurusan hanya otomotif atau multimedia.')
                    continue
                break

            siswa = [nama, int(matematika), int(indonesia), int(inggris), int(teknik), int(no_nis), jurusan]
            while True: # fungsi untuk terus melakukan perulangan
                update_konfirmasi = input("\n\tLanjutkan membuat data? (ya/tidak): ")
                if update_konfirmasi.lower() == 'ya':
                    list_siswa.append(siswa)
                    print("\n\tData siswa berhasil ditambahkan.")
                    break
                elif update_konfirmasi.lower() == 'tidak':
                    print('\n\tdata tidak jadi di buat!')
                    break
                else:
                    print('\n\tPilihan tidak valid')
        elif opsi_membuat == '2':
            break
        else:
            print("\n\tPilihan tidak valid!")
        break


# fungsi untuk no.3 yaitu update data
def merubah_data_siswa():  
    while True: # fungsi untuk terus melakukan perulangan
        print('\n\t     --------------------')
        print("\t     |MERUBAH DATA SISWA|")
        print('\t     --------------------')
        opsi_merubah = input('''
                PILIHAN OPTION
        -------------------------------
        1. Masukkan NIS dan update data
        2. Kembali ke Main Menu
                             
        Masukkan pilihan (1/2): ''')

        # untuk menentukan NIS nya
        if opsi_merubah == '1':
            nis = input("\n\tMasukkan NIS siswa yang ingin diubah: ")
            while not nis.isdigit():
                print("\n\tInput harus berupa angka!. Silakan coba lagi.")
                nis = input("\n\tMasukkan NIS siswa yang ingin diubah: ")
                
            nis = int(nis)
            cek = check_nis(list_siswa, nis)
            if not cek:
                print("\n\tData siswa dengan NIS tersebut tidak ditemukan!.")
            else:
                found = False

                for siswa in list_siswa:
                    if siswa[5] == nis:
                        found = True
                        print("\n\t\t=== DATA SISWA ===")
                        print('--------------------------------------------------------')
                        print("NAMA\tMTK\tB.INDO\tB.ING\tTEKNIK\tNIS\tJURUSAN")
                        print('--------------------------------------------------------')
                        print('\t'.join(str(data) for data in siswa))
                        break  # agar berhenti dari perulangan 

                if found:
                    while True: # untuk agar terus melakukan perulangan
                        update_konfirmasi = input("\nLanjutkan update? (ya/tidak): ")
                        if update_konfirmasi.lower() == 'ya':
                            while True: # fungsi untuk terus melakukan perulangan
                                opsi_update = input('''
            ------------------------                                            
            DATA YANG INGIN DIUPDATE 
            ------------------------
            - Nama
            - Nilai matematika
            - Nilai b.indonesia
            - Nilai b.inggris
            - Nilai teknik
            - NIS
            - Jurusan
            - Kembali

        pastikan input sama seperti di pilihan di atas!
        
        Masukkan pilihan (nama - kembali): ''')

                                # merubah NIS
                                if opsi_update == 'nis': 
                                    no_nis = input("\n\tMasukkan NIS siswa baru: ")
                                    if not is_valid_nis(no_nis):
                                        print('\n\tNIS tidak valid! Pastikan NIS berupa 5 angka dan belum ada sebelumnya.')
                                    else:
                                        no_nis = int(no_nis)
                                        while True: # fungsi untuk terus melakukan perulangan
                                            update_konfirmasi = input("\tLanjutkan update? (ya/tidak): ")
                                            if update_konfirmasi.lower() == 'tidak':
                                                print("\tUpdate Data Gagal!")
                                                break
                                            elif update_konfirmasi.lower() == 'ya':
                                                siswa[5] = no_nis
                                                print('\tUpdate Data Sukses.')
                                                break
                                            else:
                                                print('\n\tpilihan tidak valid!')
                                    break
                                    
                                    # merubah nama
                                elif opsi_update == 'nama':
                                    nama = input('\n\tMasukkan nama baru: ')
                                    if not is_valid_nama(nama):
                                        print('\n\tInput tidak valid. Nama harus berupa huruf!')
                                    else:
                                        while True: # fungsi untuk terus melakukan perulangan
                                            update_konfirmasi = input("\tLanjutkan update? (ya/tidak): ")
                                            if update_konfirmasi.lower() == 'ya':
                                                siswa[0] = nama
                                                print('\tUpdate Data Sukses.')
                                                break
                                            elif update_konfirmasi.lower() == 'tidak':
                                                print("\tUpdate Data Gagal!")
                                                break
                                            else:
                                                print('\n\tpilihan tidak valid!')
                                    break

                                # merubah nilai matematika
                                elif opsi_update == 'nilai matematika':
                                    matematika = input('\n\tMasukkan nilai matematika baru: ')
                                    if not is_valid_nilai(matematika):
                                        print('\n\tInput tidak valid. Nilai matematika harus berupa angka!')
                                    else:
                                        while True: # fungsi untuk terus melakukan perulangan
                                            update_konfirmasi = input("\n\tLanjutkan update? (ya/tidak): ")
                                            if update_konfirmasi.lower() == 'ya':
                                                siswa[1] = int(matematika)
                                                print('\tUpdate Data Sukses.')
                                                break
                                            elif update_konfirmasi.lower() == 'tidak':
                                                print("\tUpdate Data Gagal!")
                                                break
                                            else:
                                                print('\n\tpilihan tidak valid!')
                                    break

                                 # merubah nilai b.indonesia
                                elif opsi_update == 'nilai b.indonesia':
                                    indonesia = input('\n\tMasukkan nilai B.Indonesia baru: ')
                                    if not is_valid_nilai(indonesia):
                                        print('\n\tInput tidak valid. Nilai B.Indonesia harus berupa angka!')
                                    else:
                                        while True:  # fungsi untuk terus melakukan perulangan
                                            update_konfirmasi = input("\n\tLanjutkan update? (ya/tidak): ")
                                            if update_konfirmasi.lower() == 'ya':
                                                siswa[2] = int(indonesia)
                                                print('\tUpdate Data Sukses.')
                                                break
                                            elif update_konfirmasi.lower() == 'tidak':
                                                print("\tUpdate Data Gagal!")
                                                break
                                            else:
                                                print('\n\tpilihan tidak valid!')
                                    break

                                #merubah nilai b.inggris
                                elif opsi_update == 'nilai b.inggris':
                                    inggris = input('\n\tMasukkan nilai B.Inggris baru: ')
                                    if not is_valid_nilai(inggris):
                                        print('\n\tInput tidak valid. Nilai B.Inggris harus berupa angka!')
                                    else:
                                        while True: # fungsi untuk terus melakukan perulangan
                                            update_konfirmasi = input("\n\tLanjutkan update? (ya/tidak): ")
                                            if update_konfirmasi.lower() == 'ya':
                                                siswa[3] = int(inggris)
                                                print('\tUpdate Data Sukses.')
                                                break
                                            elif update_konfirmasi.lower() == 'tidak':
                                                print("\tUpdate Data Gagal!")
                                                break
                                            else:
                                                print('\n\tpilihan tidak valid!')
                                    break

                                 # merubah nilai teknik
                                elif opsi_update == 'nilai teknik':
                                    teknik = input('\n\tMasukkan nilai teknik baru: ')
                                    if not is_valid_nilai(teknik):
                                        print('\n\tInput tidak valid. Nilai teknik harus berupa angka!')
                                    else:
                                        while True: # fungsi untuk terus melakukan perulangan
                                            update_konfirmasi = input("\n\tLanjutkan update? (ya/tidak): ")
                                            if update_konfirmasi.lower() == 'ya':
                                                siswa[4] = int(teknik)
                                                print('\tUpdate Data Sukses.')
                                                break
                                            elif update_konfirmasi.lower() == 'tidak':
                                                print("\tUpdate Data Gagal!")
                                                break
                                            else:
                                                print('\n\tpilihan tidak valid!')
                                    break

                                 # merubah jurusan sekolah
                                elif opsi_update == 'jurusan':
                                    jurusan = input('\n\tMasukkan jurusan baru (otomotif/multimedia): ')
                                    if not is_valid_jurusan(jurusan):
                                        print('\n\tInput tidak valid. Nama harus berupa huruf!')
                                    else:
                                        while True: # fungsi untuk terus melakukan perulangan
                                            update_konfirmasi = input("\n\tLanjutkan update? (ya/tidak): ")
                                            if update_konfirmasi.lower() == 'ya':
                                                siswa[6] = jurusan
                                                print('\tUpdate Data Sukses.')
                                                break
                                            elif update_konfirmasi.lower() == 'tidak':
                                                print("\tUpdate Data Gagal!")
                                                break
                                            else:
                                                print('\n\tpilihan tidak valid!')
                                    break

                                elif opsi_update == 'kembali':
                                    break

                                else:
                                    print('\n\t pilihan tidak valid!')

                            break
                        elif update_konfirmasi.lower() == 'tidak':
                            print('\n\tdata tidak jadi di rubah!')
                            break
                        else:
                            print('\n\ttidak valid!')

        # kembali ke main menu
        elif opsi_merubah == '2':
            break  

        else:
            print("\n\tPilihan tidak valid. Silakan coba lagi!.")

 # menampilkan fungsi delet data
def menghapus_data_siswa(): 
    while True: # fungsi untuk terus melakukan perulangan
        print('\n\t     ------------------')
        print("\t     |HAPUS DATA SISWA|")
        print('\t     ------------------')
        opsi_menghapus = input('''
               PILIHAN OPTION
        -----------------------------
        1. Hapus data berdasarkan NIS
        2. Kembali ke Main Menu
        Masukkan pilihan (1/2): ''')

        # hapus data berdasarkan nis
        if opsi_menghapus == '1': 
            nis = input("\n\tMasukkan NIS siswa yang ingin dihapus: ")
            if validasi_nis(nis):
                nis = int(nis)
                for siswa in list_siswa:
                    if siswa[5] == nis:
                        print("\n\t\t=== DATA SISWA ===")
                        print('--------------------------------------------------------')
                        print("NAMA\tMTK\tB.INDO\tB.ING\tTEKNIK\tNIS\tJURUSAN")
                        print("--------------------------------------------------------")
                        print('\t'.join(str(data) for data in siswa))
                        hapus_konfirmasi = input("\n\tAnda yakin ingin menghapus data siswa ini? (ya/tidak): ")
                        if hapus_konfirmasi.lower() == 'ya':
                            list_siswa.remove(siswa)
                            print("\n\tData siswa berhasil dihapus!.")
                            break
                        elif hapus_konfirmasi.lower() == 'tidak':
                            print('\n\tData siswa tidak jadi dihapus!.')
                        break
            else:
                print("\n\tData siswa tidak ditemukan!")
        elif opsi_menghapus == '2': # kembali ke main menu
            break
        else:
            print("\n\tPilihan tidak valid,harus berupa angka!")

def kelulusan_data_siswa():
    while True: # menampilkan kelulusan data siswa
        print('\n\t-------------------------')
        print("\t|MELIHAT KELULUSAN SISWA|")
        print('\t-------------------------')
        opsi_kelulusan = input('''
            PILIHAN OPTION
        -----------------------
        1. Tampilkan kelulusan
        2. Tampilkan Rangking
        3. Cari  data kelulusan berdasarkan NIS
        4. Kembali ke Main Menu
        
        Masukkan pilihan (1-6): ''')
        if opsi_kelulusan== '1': 
            lulus = []
            tidak_lulus = []

            for siswa in list_siswa:
                nis = siswa[5]
                nama = siswa[0]
                jurusan = siswa[6]
                nilai_rata_rata = sum(siswa[1:5]) / 4
                

                if nilai_rata_rata >= 80:
                    lulus.append([nis,nama, jurusan, nilai_rata_rata])
                else:
                    tidak_lulus.append([nis,nama, jurusan, nilai_rata_rata])

            print("\nSISWA YANG LULUS:")
            print("---------------------------------------------------------")
            print("NIS\t\tNama\t\tJurusan\t\tRata-rata")
            print("---------------------------------------------------------")
            for siswa in lulus:
                print(f"{siswa[0]}\t\t{siswa[1]}\t\t{siswa[2]}\t{siswa[3]}")

            print("\nSISWA YANG TIDAK LULUS:")
            print("---------------------------------------------------------")
            print("NIS\t\tNama\t\tJurusan\t\tRata-rata")
            print("---------------------------------------------------------")
            for siswa in tidak_lulus:
                print(f"{siswa[0]}\t\t{siswa[1]}\t\t{siswa[2]}\t{siswa[3]}")

        # tampilkan rangking
        elif opsi_kelulusan == '2': 
            list_siswa.sort(key=lambda x: sum(x[1:5]) / 4, reverse=True)
            print("\nRANGKING SISWA:")
            print("---------------------------------------------------------")
            print("Peringkat\tNama\t\tJurusan\t\tRata-rata")
            print("---------------------------------------------------------")
            for i, siswa in enumerate(list_siswa, 1):
                print(f"{i}\t\t{siswa[0]}\t\t{siswa[6]}\t{sum(siswa[1:5]) / 4}")
        
        elif opsi_kelulusan == '3':
            # Input NIS dari user
            nis_input = int(input("\n\tMasukkan NIS: "))

            # Mencari siswa berdasarkan NIS
            siswa = None
            for data_siswa in list_siswa:
                if data_siswa[5] == nis_input:
                    siswa = data_siswa
                    break

            # Jika siswa ditemukan
            if siswa is not None:
                nama = siswa[0]
                nis = siswa[5]
                jurusan = siswa[6]
                nilai_rata_rata = sum(siswa[1:5]) / 4
                kelulusan = "Lulus" if nilai_rata_rata >= 80 else "Tidak Lulus"

                # Menampilkan informasi siswa
                print('\n---------------------')
                print('HASIL PENCARIAN DATA')
                print('---------------------')
                print("Nama      :", nama)
                print("NIS       :", nis)
                print("Jurusan   :", jurusan)
                print("Kelulusan :", kelulusan)
                print("Rata-rata :", nilai_rata_rata)
            else:
                print("\n\tNIS tidak ditemukan!.")
        elif opsi_kelulusan == '4':
            break

        else:
            print("\n\tPilihan tidak valid!")

# Program utama
while True: # fungsi untuk terus melakukan perulangan
    menu_opsi()
    opsi = input("Masukkan pilihan (1-6): ")

    if opsi == '1':
        melihat_menu_data_siswa() # menampilkan read data
    elif opsi == '2':
        membuat_data_siswa() #membuat data baru
    elif opsi == '3':
        merubah_data_siswa() #merubah data 
    elif opsi == '4':
        menghapus_data_siswa() #menghapus data
    elif opsi == '5':
        kelulusan_data_siswa() #kelulusan data siswa , "fitur tambahan"
    elif opsi == '6':
        print('''
    Terima kasih :)
    SAMPAI JUMPA KEMBALI.
              
    Program selesai.
              
    ''') # keluar dari program
        break
    else:
        print("Pilihan harus angka. Silakan coba lagi!")