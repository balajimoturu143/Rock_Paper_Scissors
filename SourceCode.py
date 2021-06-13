# condition for winning
def wins(choice, choice_2) :    
    if(choice==choice_2) :
        print ("No one wins")
    elif((choice == 1 and choice_2 == 2) or
      (choice == 2 and choice_2 ==1 )): 
                return "Paper"
          
    elif((choice == 1 and choice_2 == 3) or
        (choice == 3 and choice_2 == 1)): 
        return  "Rock"
    else: 
                return "Scissor"
# Print multiline instruction 
print("Winning rules of rock paper and scissor game as follows : \n 1.Rock vs Paper = > Paper wins\n 2.Paper vs Scissor = > Scissor Wins\n 3.Scissor vs Rock = > Rock Wins\n")
n=int(input("Enter no.of times to be game repeated : "))
for i in range (1,n+1):
    print ("Enter choice \n 1.Rock\n 2.Paper\n 3.Scissor\n")
    # Enter users choice 
    choice=int(input("User 1 turn : "))
    
    # or is a short-circuit operator 
    #if any one of the condition is true is returns true
    
    #Looping until they enter valid input
    while (choice>3 or choice <1) :
        choice = int(input("Enter valid input : "))
    
    #initialize choice_name variable with corresponding choice value
    
    if(choice == 1) :
        choice_name = "Rock"
    elif (choice == 2) :
        choice_name ="Paper"
    else :
        choice_name ="Scissor"
    
    # Printing the user 1 choice
    
    print ("User 1 choice is : ",choice_name)
    
    # Now its user 2 turn
    
    choice_2=int(input("User 2 turn : "))
    
    ##Looping until they enter valid input
    
    while (choice_2>3 or choice_2<1) :
        choice_2 = int(input("Enter valid input : "))
        
    # initialize choice_name2 variable with corresponding choice_2 value
    
    if(choice_2 == 1) :
        choice_name2 = "Rock"
    elif (choice_2 == 2) :
        choice_name2 ="Paper"
    else :
        choice_name2 ="Scissor"
        
    ## Printing the user 1 choice
    
    print ("User 2 choice is : ",choice_name2)
    
    print (choice_name +" vs "+ choice_name2)
    
    # calling the wins function
    
    result = wins(choice,choice_2)
    c=0
    c1=0
    if result == choice_name: 
        c+=1 
    elif (result == choice_name2): 
        c1+=1 
if(c==c1) :
    print("Draw match")
elif(c>c1) :
    print("User 1 wins")
else:
    print("User 2 wins")
# after coming out of while loop
# We print thanks for playing 

print ("\nThanks for playing\n")
