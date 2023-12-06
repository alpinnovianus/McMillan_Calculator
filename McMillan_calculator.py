#simple calculator for the McMillan formula
#Tc = (omega_ln / 1.2) exp [(-1.04(1+lambda))/(lambda-mu_star(1+0.62lambda))]

from numpy import exp

# Prompt for user input

OmegaValue = float(input("Enter the value for omega_ln: "))
LambdaValue= float(input("Enter the value for lambda: "))
MuValue = float(input("Enter the value for mu_star: "))

Tc = (OmegaValue / 1.2) * exp((-1.04*(1+LambdaValue))/(LambdaValue-MuValue*(1+0.62*LambdaValue)))
print("The superconducting transition temperature is ", round(Tc,2)) 