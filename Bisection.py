import math as m

def f(x):
    return 2*m.sin(m.pi*x)-x-1
def signum(x):
    if(x>0):
        return 1
    elif(x==0):
        return 0
    elif(x<0):
        return -1
    


def Bisection (a,b,TOL,N0):
     i=1 
     FA = f(a)
     print("[i]\t [p]\t [FP]")
     while(i<N0):
         p = a+((b-a)/2)
         p = (a+b)/2
         FP = f(p)
         if(FP==0 ):
            print("FP=0")
            print("STOP!")
            return p
         if( (b-a)/2 < TOL):
            print("STOP!")
            return p
         print(i,"\t",p,"\t",FP)
         i=i+1
         if(signum(f(a)) * signum(f(p)) > 0):
             print("The Sign is same")
             a = p
             FA = FP
         else:
         # print("The Sign is diff")
          b = p
     return print("Method failed after %d iterations",N0)  

print("[The Solution 1 is ",Bisection(0,0.5,10**(-6),50),']')
print("[The Solution 2 is ",Bisection(0.5,1,10**(-6),50),']')


 
     


             