#WAP to recognize strings under 'a",'a*b+','babb'.
def initialStateA(value):

    if(value[0]=='a'):
        secondFinalStateB(value[1:])

    else:
        fourthFinalStateD(value[1:])

def secondFinalStateB(value):
    if (len(value)== 0):
        print("recognized")
    else:
        if(value[0]=='b'):
           thirdFinalStateC(value[1:])
        else:
            fifthStateE(value[1:])

def thirdFinalStateC(value):
    if (len(value)== 0):
        print("recognized")
    else:
        if(value[0]=='b'):
           thirdFinalStateC(value[1:])
        else:
            deadStateF(value[1:])

def fourthFinalStateD(value):
    if (len(value)== 0):
        print("recognized")
    else:
        if(value[0]=='b'):
            sixthFinalStateG(value[1:])
        else:
            seventhStateH(value[1:])

def fifthStateE(value):
    if (len(value)== 0):
        print("not recognized")
    else:
        if(value[0]=='a'):
            fifthStateE(value[1:])
        else:
            sixthFinalStateG(value[1:])

def sixthFinalStateG(value):
    if (len(value)== 0):
        print("recognized")
    else:
        if(value[0]=='b'):
            sixthFinalStateG(value[1:])
        else:
            deadStateF(value[1:])

def seventhStateH(value):
    if (len(value)== 0):
        print("not recognized")
    else:
        if(value[0]=='b'):
            eigthStateI(value[1:])
        else:
            deadStateF(value[1:])

def eigthStateI(value):
    if (len(value)== 0):
        print("not recognized")
    else:
        if(value[0]=='b'):
            ninthFinalStateJ(value[1:])
        else:
            deadStateF(value[1:])


def ninthFinalStateJ(value):
    if (len(value)== 0):
        print("string  accepted")
    else:
        if(value[0]=='a'):
            deadStateF(value[1:])
        else:
            deadStateF(value[1:])

def deadStateF(value):
    if (len(value)== 0):
        print("not recognized")
    else:
        if(value[0]=='a'):
            deadStateF(value[1:])
        else:
            deadStateF(value[1:])
            
if __name__ == "__main__":
    value = input("enter any string which may or maynot contain a or b: ")
    initialStateA(value)