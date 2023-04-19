import flywithWings
import noWings
import Quack
import noQuack
import squeak

obj1 = flywithWings.flywithWings
obj2 = noWings.noWings
obj3 = Quack.Quack
obj4 = noQuack.noQuack
obj5 = squeak.Squeak

val = " "
while val != 0:
    print("Enter the duck you want to select: \n 1.   Mallard Duck \n 2.   Rubber Duck \n 3.   Redhead Duck \n 4.   Decoy Duck")
    val = input()
    if val == "1":
        print("This is a Mallard Duck.")
        obj1.fly()
        obj3.quack()
    elif val == "2":
        print("This is a Rubber Duck.")
        obj2.nowings()
        obj5.Squeak()
    elif val == "3":
        print("This is a Readhead Duck.")
        obj1.fly()
        obj4.noQuack()
    elif val == "4":
        print("This is a Decoy Duck.")
        obj1.fly()
        obj3.quack()
    elif val == "0":
        break
    else:
        print("Enter valid input")