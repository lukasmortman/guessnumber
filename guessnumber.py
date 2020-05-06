import random

x = random.randint(1, 20)
print(x)

while True:
    guess = int(input("Gissa vilket nummer datorn har valt"))

    if guess == x:
        print("du gissade rätt!")
        break

    if guess < x:
        print("högre")

    else:
        print("lägre")
