import hashlib
import string

def password():
    while True: 
        mot_de_passe = input ("Veuillez entrer votre mot de passe :" )

        if len(mot_de_passe) < 8:
            print ("Le mot de passe doit contenir au moins 8 caractères")
            continue

        if not any(char.isupper() for char in mot_de_passe):
            print ("Le mot de passe doit contenir au moins une lettre majuscule")
            continue

        if not any(char.islower() for char in mot_de_passe):
            print ("Le mot de passe doit contenir au moins une lettre minuscule")
            continue

        if not any(char.isdigit() for char in mot_de_passe):
            print("Le mot de passe doit contenir au moins un chiffre")
            continue

        if not any(char.isascii() and not char.isalnum() for char in mot_de_passe):
            print("Le mot de passe doit contenir au moins un caractère spécial")
            continue

        break

    return mot_de_passe

def crypter_mot_de_passe(mot_de_passe):
    hasher = hashlib.sha256()
    hasher.update(mot_de_passe.encode('utf-8'))
    mot_de_passe_crypte = hasher.hexdigest()
    return mot_de_passe_crypte

mot_de_passe_non_crypte = password()

mot_de_passe_crypte = crypter_mot_de_passe(mot_de_passe_non_crypte)

print("Mot de passe choisi :", mot_de_passe_non_crypte)
print("Mot de passe crypté :", mot_de_passe_crypte)
    