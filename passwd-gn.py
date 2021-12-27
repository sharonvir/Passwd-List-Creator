# Creator : MR.D3F417 > BLACK GUARD TM > 
# Discord : https://discord.gg/EZssbvh8UF
# Dont Copy kid

from itertools import product
import string   
from typing import Counter

min_len = int(input("BLACKGUARD : Enter Min Length passwd : "))
max_len = int(input("BLACKGUARD : Enter Max Lenght passwd : "))
Counter = 0
charater = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

file_open = open("BlackGuard-passwd.txt","w")

for i in range(min_len,max_len + 1):
    for j in product(charater,repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write("\n")
        Counter += 1
print("BLACKGUARD : Wordlist {} passwords Created! Enjoy My Love :)".format(Counter))