
import time


name = raw_input("Sup homie , what's your name? ")

print "Yo, " + name, "Let's play hangman!"

print " "

time.sleep(0.3)

print "Take a shot "

word = "linkinpark"

print "HINT: The word is 10 letters long "

var = ''

t = 10


while t > 0:         

    
    var1 = 0             

        
    for char in word:      

   
        if char in var:    
    
        
            print char,    

        else:
    
        
            print "_",     
       
        
            var1 = var1 + 1    



    
    if var1 == 0:   
    	time.sleep(0.5)     
        print "Woah you hit the jackpot"  

    
        break              

    print

    
    x = raw_input("\nC'mon guess a character:") 

    
    var = var + x                    

    
    if x not in word:  
 
     
        t = t - 1        
 
    
        print "Wrong duh"    
 
    
        print "Man you have", + t, 'more guesses' 
 
     
        if t == 0:           
    
       
            print "\nDamn Dude You Lost"  