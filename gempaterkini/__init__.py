import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        kedalaman = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text

            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return
    print('Gempa terakhir bedasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: LS = {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(result['dirasakan'])
