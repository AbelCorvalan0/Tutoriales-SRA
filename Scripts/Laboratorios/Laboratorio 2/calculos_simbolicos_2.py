 
 # calculo simbolico, para eso importamos
from sympy import *

# definimos las variables simbolicas
Rf1, Rf2, Rf3 = symbols('Rf1 Rf2 Rf3')

# definimos las ecuaciones

# ecuacion 1
Rp = Rf2*Rf3/(Rf2+Rf3)

Vx = Rp/(Rp+Rf1)

Vx_sim = simplify(Vx)

print("Vx = ", Vx_sim)


# ecuacion 2
If = Vx/Rf2 

If_sim = simplify(If)

print("If = ", If_sim)



# ecuacion ipol 
Ipol, Ad, R = symbols('Ipol Ad R')

Req = Rf2 + (Rf1*Rf3)/(Rf1+Rf3)

Req_sim = simplify(Req)

print("Req = ", Req_sim)

delta_V_ipol = Ipol*Ad*(Req*R)/(R + 2*Req)

print("delta_V_ipol = ", delta_V_ipol)

delta_V_ipol_sim = simplify(delta_V_ipol)

print("delta_V_ipol_sim = ", delta_V_ipol_sim)

