import math as m
def g(x):
    return 2*(x**2)+1-4*x*m.cos(x)+m.cos(2*x)
def Diff_g(x):
    return 4*x+4*x*m.sin(x)-2*m.sin(2*x)-4*m.cos(x)


def NEWTONS_METHOD(p0,TOL,N0,a,b): 
    i=1
    print("[i]\t [p_]\t [p]")
    while(i<= N0 and p0>=a and p0<=b):
     p = p0 - (g(p0)/Diff_g(p0))
     print(i,"\t",p0,"\t",p)
     if(abs(p-p0)<TOL):
        print("Abs error is less than TOL!")
        print("STOP!")
        return p
     i = i+1
     p0 = p
    return print("Method failed after %d iterations"%(N0))   
  
print("[The solution is ",NEWTONS_METHOD(0,10**(-6),50,0,1),']')