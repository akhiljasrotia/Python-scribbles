import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Here goes nothing "
    print "And you got "
    x=random.randint(min, max)
    print x
    if(x==6):
    	print"Damn Boi you sure lucky as hell"
    elif(x==1):
    	print"Ohh so that's why the dinosaurs died"

    roll_again = raw_input("Wanna try your luck again fam?")


print"Looks like you just lost your house"