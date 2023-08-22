import random

def main():
    print("Khansole Academy")
 
    var1 = random.randint(10, 99)
    var2 = random.randint(10, 99)
 
    print("What is " + str(var1) + " + " + str(var2) + "?")
    user_input = input('Your answer: ')
    player_answer = int(user_input)
    
    var3 = var1 + var2
    
    if player_answer == var1 + var2:
        print("Correct!")
    
    if player_answer != var1 + var2:
        print("Incorrect.")
        print("The expected answer is " + str(var3))
        
        
        
        
if __name__ == '__main__':
    main()