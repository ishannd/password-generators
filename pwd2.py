import string,random

map=list(string.ascii_letters)
map.append("-")
map.append("-")
map.extend(range(10))

n=int(input("how many characters you want in your password?"))
password=""

while len(password)<n:password+=str(map[random.randint(0,len(map)-1)])

print(f"here is your generated password \n:{password}")

