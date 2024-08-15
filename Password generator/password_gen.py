import random
import string

length=int(input("Enter the desired size of your password:"))
chars= string.ascii_letters+string.digits
password="".join(random.choices(chars,k=length))
print(password)