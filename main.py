"""
Aplikasi deteksi gempa terkini
Modularisasi dengan Function
Modularisasi dengan Package
"""
from gempaterkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)
