import random
import string

uzunluk = int(input("Parola uzunluğu: "))
karakterler = string.ascii_letters + string.digits + string.punctuation
parola = ''.join(random.choice(karakterler) for _ in range(uzunluk))
print("Oluşturulan parola:", parola)
