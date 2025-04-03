import hashlib
import string

def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

target_hash = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"

# Definim seturile de caractere
litere_mari = list(string.ascii_uppercase)  # A-Z
litere_mici = list(string.ascii_lowercase)  # a-z
numere = list(string.digits)  # 0-9
charactere_speciale = ['!', '@', '#', '$']

# Contorizăm apelurile recursive
recursive_calls = 0

def dfs(parola_curenta, pozitii_ramase, litere_mari_counter, litere_mici_counter, numere_counter, charactere_speciale_counter):
    global recursive_calls
    recursive_calls += 1
    
    # Cazul de bază: nu mai avem poziții de completat
    if not pozitii_ramase:
        # Verificăm dacă hash-ul se potrivește
        current_hash = get_hash(parola_curenta)
        if current_hash == target_hash:
            return parola_curenta
        return None
    
    # Alegem prima poziție disponibilă
    position = pozitii_ramase[0]
    new_remaining = pozitii_ramase[1:]
    
    # Încercăm să punem o literă mare
    if litere_mari_counter > 0:
        for char in litere_mari:
            # Creăm o nouă parolă parțială adăugând caracterul la poziția curentă
            new_password = parola_curenta[:position] + char + parola_curenta[position+1:]
            rezultat = dfs(parola_curenta, pozitii_ramase, litere_mari_counter, litere_mici_counter, numere_counter, charactere_speciale_counter)
            if rezultat:
                return rezultat
    
    # Încercăm să punem o literă mică
    if litere_mici_counter > 0:
        for char in litere_mici:
            new_password = parola_curenta[:position] + char + parola_curenta[position+1:]
            rezultat = dfs(parola_curenta, pozitii_ramase, litere_mari_counter, litere_mici_counter, numere_counter, charactere_speciale_counter)
            if rezultat:
                return rezultat
    
    # Încercăm să punem o cifră
    if numere_counter > 0:
        for char in numere:
            new_password = parola_curenta[:position] + char + parola_curenta[position+1:]
            rezultat = dfs(parola_curenta, pozitii_ramase, litere_mari_counter, litere_mici_counter, numere_counter, charactere_speciale_counter)
            if rezultat:
                return rezultat
    
    # Încercăm să punem un caracter special
    if charactere_speciale_counter > 0:
        for char in charactere_speciale:
            new_password = parola_curenta[:position] + char + parola_curenta[position+1:]
            rezultat = dfs(parola_curenta, pozitii_ramase, litere_mari_counter, litere_mici_counter, numere_counter, charactere_speciale_counter)
            if rezultat:
                return rezultat
    
    return None


    # Inițializăm o parolă "goală" de 6 caractere și o listă cu pozițiile disponibile
parola_goala = " " * 6  # folosim un caracter placeholder
positions = list(range(6))

rezultat = dfs(parola_goala, positions, 1, 3, 1, 1)

if rezultat:
    print(f"Parola gasita: {rezultat}")
    print(f"Numar apeluri recursive: {recursive_calls}")
else:
    print("Parola nu a fost găsita.")

    