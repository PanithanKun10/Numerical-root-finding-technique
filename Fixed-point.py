import math as m
def g(x):
    return (1/m.pi)*m.asin((x+1)/2)

def FIXED_POINT(p0,TOL,N0,a,b):
    
    i=1
    print("[i]\t [p]\t [gp]")
    while(i<= N0 and p0>=a and p0<=b):
     p = g(p0)
     if(abs(p-p0)<TOL):
        print("Abs error is less than TOL!")
        print("STOP!")
        return p
     print(i,"\t",p0,"\t",g(p0))
     i = i+1
     p0 = p
    return print("Method failed after %d iterations"%(N0))   
  
     
print("[The solution is",FIXED_POINT(0,10**(-6),20,0,0.5),']')