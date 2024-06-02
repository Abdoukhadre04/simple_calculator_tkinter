import random
import math

lower = (int)(input("Entrer la plage inferieure: "))
upper = (int)(input("Entrer la plage superieure: "))

print("vous avez entre: ", lower, upper)
x = random.randint(lower, upper)



print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

count = 0

while count< math.log(upper - lower + 1, 2):
    count += 1
    val = int(input("choisir un nombre en la plage: "))
    if(x == val):
        print("Bravo, vous avez trouve le nombre en ", count)
        break
    elif(x > val):
        print("trop petit")
    elif(x < val):
        print("trop grand")
    if count >= math.log(upper - lower + 1,2):
        print("Vous avez perdu, le nombre etait: ", x)
        print("Bonne chance la prochaine fois")






