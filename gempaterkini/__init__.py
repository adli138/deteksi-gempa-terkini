def ekstraksi_data():
    """
    Tanggal: 21 Juni 2024,
    Waktu: 07:11:19 WIB
    Magnitudo: 5.7
    Kedalaman: 78 km
    Lokasi: 3.54 LS - 140.01 BT
    Pusat Gempa: Pusat gempa berada di darat 68 km timur laut Yalimo
    Dirasakan: Dirasakan (Skala MMI): II-III Wamena, II Kota Jayapura, II Kab. Jayapura
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '21 Juni 2024'
    hasil['waktu'] = '07:11:19 WIB'
    hasil['magnitudo'] = 4.0
    hasil['kedalaman'] = '78 KM'
    hasil['lokasi'] = {'ls': 1.48, 'bt': 134.01}
    hasil['pusat'] = 'Pusat gempa berada di darat 68 km timur laut Yalimo'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Wamena, II Kota Jayapura, II Kab. Jayapura'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir bedasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT:{result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")
