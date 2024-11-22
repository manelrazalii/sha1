import hashlib

def convertirsha1(text):
        return hashlib.sha1(text.encode()).hexdigest()

def main():
    objet_sha1= input("entrez le hash sha1 a decrypter : ")
    objetsha1= objet_sha1.strip().lower()
    found = False
    with open('./cummonpasswords.txt') as cp: 
        for line in cp:
            password = line.strip()
            if objetsha1 == convertirsha1(password): 
                print(f"password trouvé ! {password}")
                found= True
                break
        if not found:
            print("password non trouvé :( ")
        

if __name__=="__main__": main()