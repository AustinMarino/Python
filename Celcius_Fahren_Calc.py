# Austin Marino
# Celcius/ Fahrenheit calculator


def Celsius(degC):
    degC=(degF - 32) * (5/9)
    degC=round(degC, 2)
    return(degC)

def Fahrenheit(degF):
    degF=(degC * (9/5)) + 32
    degF=round(degF, 2)
    return(degF)

degF = float(input("Enter a degree F value:"))
print(Celsius(degF), "°C")
degC = float(input("Enter a degree C value:"))
print(Fahrenheit(degC), "°F" )

