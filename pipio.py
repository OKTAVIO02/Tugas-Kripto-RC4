# ==========================================
# TUGAS KRIPTOGRAFI: IMPLEMENTASI RC4
# Nama: Oktavio Dwi Prasetyo
# NIM: 25051204342
# ==========================================

def ksa(key):
    """
    Key Scheduling Algorithm (KSA)
    Tahap inisialisasi S-Box (array S) menggunakan kunci.
    """
    key_length = len(key)
    
    S = list(range(256)) 
    j = 0
    for i in range(256):
       
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  
    return S

def prga(S):
    """
    Pseudo-Random Generation Algorithm (PRGA)
    Menghasilkan aliran kunci (keystream) secara kontinu.
    """
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  
        K = S[(S[i] + S[j]) % 256]
        yield K

def rc4_process(data, key):
    """
    Proses Utama RC4 (Bisa digunakan untuk Enkripsi maupun Dekripsi)
    Karena XOR bersifat reversibel.
    """
    
    key = [ord(c) for c in key]
    data = [ord(c) for c in data]

    
    print(f"[LOG] Memulai KSA dengan kunci...")
    S = ksa(key)
    
    
    keystream = prga(S)
    res = []
    print(f"[LOG] Melakukan proses XOR pada setiap karakter...")
    for char in data:

        processed_byte = char ^ next(keystream)
        res.append(processed_byte)
    
    return res



if __name__ == "__main__":
    print("=== PROGRAM KRIPTOGRAFI RC4 FROM SCRATCH ===")
    
    plaintext = input("Masukkan pesan: ")
    kunci = input("Masukkan kunci (bebas): ")

  
    print("\n--- TAHAP ENKRIPSI ---")
    encrypted_bytes = rc4_process(plaintext, kunci)
    ciphertext_hex = ''.join([f"{b:02x}" for b in encrypted_bytes])
    print(f"Plaintext  : {plaintext}")
    print(f"Ciphertext (Hex): {ciphertext_hex}")

   
    print("\n--- TAHAP DEKRIPSI ---")
    
    decrypted_bytes = rc4_process("".join([chr(b) for b in encrypted_bytes]), kunci)
    decrypted_text = "".join([chr(b) for b in decrypted_bytes])
    
    print(f"Ciphertext  : {ciphertext_hex}")
    print(f"Hasil Dekripsi: {decrypted_text}")

    if plaintext == decrypted_text:
        print("\n[SUKSES] Pesan kembali sempurna!")
