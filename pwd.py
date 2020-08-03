import random

password=""

n=int(input("how many characters you want in your password?"))

for i in range(0,n):
    password+=str(random.randint(0,100))
    password+=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"
                            "r","s","t","u","v","w","x","y","z","#","!","*","&","$"])


print(f"here is your genereated password \n:{password[0:n]}")

