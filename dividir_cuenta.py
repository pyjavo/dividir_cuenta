import math

def dividir_cuenta(total, numero_de_personas):
	if numero_de_personas <= 1:
	    raise ValueError("Se requiere más de 1 persona para dividir la cuenta")
	return math.ceil(total / numero_de_personas)

try:
    total_debido = float(input("¿Cuánto es el total?  ")) 
    nro_personas = int(input("¿Cuántas personas?  "))
    cantidad_debida = dividir_cuenta(total_debido, nro_personas)
except ValueError as error:
	print("¡Ohh no! Ese valor no es válido. Intente de nuevo...")
	print("{}".format(error))
else:
    print("Cada persona debe ${}".format(cantidad_debida))
