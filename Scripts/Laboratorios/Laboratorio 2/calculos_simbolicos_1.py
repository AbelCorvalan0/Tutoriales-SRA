from sympy import symbols, Eq, solve, simplify

# Definir las variables
Ad, R, Rf = symbols('Ad R Rf') 
Toriginal = (-Ad) * ( (R*R)/(R+R) ) / (( (R*R)/(R+R) ) + Rf) 
T = simplify(Toriginal)
 
print("T = ", T, "\n")

# Definir las variables
Iosn = symbols('Iosn')

V_ios_original = Ad * Iosn * 1 /( (1/R) + (1/R) +  (1/Rf) )
V_ios = simplify(V_ios_original )

print ("Vios = ", V_ios, "\n")

V_iosf_original = V_ios/(1-T)

V_iosf = simplify(V_iosf_original)

print ("Viosf = ", V_iosf, "\n")


# Definir las variables
Vos = symbols('Vos')

delta_vos_original = Ad * Vos / (1 - T)

delta_vos = simplify(delta_vos_original)

print ("delta_vos = ", delta_vos, "\n") 


## Para Ad menor a infinito

Avf_original = Ad*(Rf /(Rf + R)) * (1/(1-T))

Avf = simplify(Avf_original)

print ("Avf = ", Avf, "\n")
