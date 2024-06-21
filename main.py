"""
Aplikasi deteksi gempa terkini
Modularisasi dengan Package
"""
import gempaterkini

if __name__ == '__main__':
    print('BMKG.go.id')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)
