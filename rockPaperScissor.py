import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you == 's':
           return False 
        elif you=='p':
               return True
    elif comp=='p':
        if you == 'r':
           return False 
        elif you=='s':
               return True    
    elif comp=='s':
        if you == 'p':
           return False 
        elif you=='r':
               return True    

print("Comp Turn: Rock(r) Paper(p) or Sisor(s)?")
randNo = random.randint(1,3)
if randNo==1:
    comp = 'r'
elif randNo==2:
    comp = 'p'
elif randNo==3:
    comp = 's'

you = input("Your Turn: Rock(r) Paper(p) or Sisor(s)?")
a = gameWin(comp,you)
print(f"Computer chose {comp}")
print(f"You choose {you}")
if a == None:
    print("Its a tie")
elif a:
    print("You Win!")
else:
    print("You Loose!")
