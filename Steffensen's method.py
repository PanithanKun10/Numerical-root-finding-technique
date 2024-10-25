import math as m

def g(x):
    return (1/m.pi)*m.asin((x+1)/2)

def STEFFENSEN(p0,TOL,N0,a,b):
    i=1
  #  print("[i]\t [p0]\t [p1] \t [p2] \t [p]")
    while (i<=N0 and p0>=a and p0<=b):
        p1=g(p0)
        p2=g(p1)
        p=p0-((p1-p0)**2/(p2-2*p1+p0))
        print(i,"\t",p0,"\t",p1,"\t",p2,"\t",p)
        if(abs(p-p0)<TOL):
            print("abs error is less than TOL!")
            print("STOP")
            return p
        i = i+1
        p0 = p
    return print("Method failed after %d iterations"%(N0))

print("[The Solution is",STEFFENSEN(0,10**(-6),50,0,0.5),']')