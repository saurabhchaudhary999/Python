import random, time
print("Welcome to game zone...!")
time.sleep(2)
print("***** Bored?")
time.sleep(3)
print("**** Frustrated?")
time.sleep(2)
print("*** Tired?")
time.sleep(2)
print("** Grilled?")
time.sleep(2)
print("* Chill Buddy..!")
print("***Lets Play Game***")
time.sleep(2)

n = random.randint(0,40)
turns= 10

while turns > 0:
    print()
    guess= int(input("Enter number: "))

    if guess == n:
        print("*********You win***********")
        print("You win at", + turns ,"turns")
        break

    if turns!=0 :
        turns-=1
        print("you have remain", +turns, "turns")
        if turns == 0:
            print("***You Loose***")

    if guess > n :
        print("Guess is high")
        print("**********")

    elif guess < n:
        print("Guess is low")
        print("**********")
