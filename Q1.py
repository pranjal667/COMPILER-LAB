# WAP to simulate DFA for the language over Σ = {0,1} starting with 1 and ending with 0.
def initialState(x):
    if x[0] == "0" :
        deadState(x)
    elif x[0] == "1":
        secondState(x)
    else:
        print("Enter a valid number.")
    return

def secondState(x):
    a = len(str(x))-1
    q = "false"
    for i in range(0,a):
        if x[i] == "0" or x[i] == "1":
            q = "true" 
            continue
        else:
            q = "false"
            print("The entered value is invalid. Please enter a number which consists of only 0 and 1.")
            break
    if q == "true":
        finalState(x)
    else:
        print("The value is rejected.")
    return

def finalState(x):
    b = len(str(x))-1
    if x[b] == "0" :
        print ("The given value is accepted.")
    else:
        print("The value is rejected.")    
    return

def deadState(x):
    print("This is dead state. Hence given value is rejected.")
    return

if __name__ == "__main__" :
    x = input("Enter a value consisting only of 0 and 1: ")
    initialState(x)
