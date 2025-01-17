import random

def hamming_encode(dataword):
    """4-bitlik bir veri alıp 7-bitlik Hamming Code (7,4) oluşturur"""
    d1, d2, d3, d4 = map(int, dataword)

    # Parity bitlerini hesapla (Çift Parite - Even Parity)
    p1 = d1 ^ d2 ^ d4  # 1. parity bit (1,3,5,7 kontrol eder)
    p2 = d1 ^ d3 ^ d4  # 2. parity bit (2,3,6,7 kontrol eder)
    p3 = d2 ^ d3 ^ d4  # 3. parity bit (4,5,6,7 kontrol eder)

    # Hamming kodu ile oluşturulmuş 7-bitlik kod
    codeword = [p1, p2, d1, p3, d2, d3, d4]
    
    return ''.join(map(str, codeword))

def hamming_decode(codeword):
    """7-bitlik Hamming Code alıp hata tespiti ve düzeltme yapar"""
    c = list(map(int, codeword))

    # Hata konumlarını hesapla (Çift Parite Kontrolleri)
    p1_check = c[0] ^ c[2] ^ c[4] ^ c[6]  # 1. parity bit kontrolü
    p2_check = c[1] ^ c[2] ^ c[5] ^ c[6]  # 2. parity bit kontrolü
    p3_check = c[3] ^ c[4] ^ c[5] ^ c[6]  # 3. parity bit kontrolü

    # Hata pozisyonunu belirle
    error_pos = (p3_check * 4) + (p2_check * 2) + (p1_check * 1)

    if error_pos != 0:
        print(f"Hata tespit edildi! Hatalı bit pozisyonu: {error_pos}")
        c[error_pos - 1] ^= 1  # Hatalı biti ters çevir
        print(f"Hata düzeltildi! Yeni Codeword: {''.join(map(str, c))}")
    else:
        print("Hata tespit edilmedi!")

    # Orijinal 4-bit veri geri döndürülüyor
    dataword = [c[2], c[4], c[5], c[6]]
    return ''.join(map(str, dataword))

# Kullanıcıdan 4-bit veri girişi al
data = input("4-bitlik veriyi girin (örnek: 1011): ")

# Hamming (7,4) kodlaması
encoded = hamming_encode(data)
print(f"Dataword: {data} → Hamming Code (7,4): {encoded}")

# Hata ekleme (kullanıcı belirli bir biti bozabilir)
error_index = int(input(f"Bozulacak bit pozisyonunu seçin (1-{len(encoded)}) veya 0 (hata ekleme): "))

if error_index > 0:
    encoded = list(encoded)
    encoded[error_index - 1] = '1' if encoded[error_index - 1] == '0' else '0'  # Bit ters çevrilir
    encoded = ''.join(encoded)
    print(f"Hata eklendi! Bozuk Codeword: {encoded}")

# Hata tespiti ve düzeltme
decoded = hamming_decode(encoded)
print(f"Çözümlenen Dataword: {decoded}")