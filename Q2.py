# WAP to identify whether a given line is a comment or not. 

def commentChecker(x,y):
    singleLineComment(x)
    multiLineComment(y)
    return 
        
def singleLineComment(x):
    if x[0] == "/" and x[1] == "/" :
        print(x,": It is a single line comment") 
    else:
        print("Not a comment")    

def multiLineComment(y):
    b = len(y) - 2
    c = len(y) - 1
    if y[0] == "/" and y[1] == "*" and y[b] == "*" and y[c] == "/":
        print(y,": Its a multi-line comment")
    else:
        print("Not a comment") 
            
if __name__ == "__main__" :
    x = "//I am a CS student."
    y = "/*I am a CS student.*/"
    commentChecker(x,y)
