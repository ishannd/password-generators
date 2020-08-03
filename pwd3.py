import string,secrets


n=input("how many characters you want in your password?")
alpha=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.hexdigits

password="".join(secrets.choice(alpha)for i in range(int(n)-1))

print(password)
