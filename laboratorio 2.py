from decimal import Decimal, getcontext

#establecemos un contexto de presicion alta
getcontext().prec = 50 

#Realizamos una operacion matematica precisa
numero1 = Decimal('1.123456789123456789')
numero2 = Decimal(('2.987654321987654321'))

resultado = numero1 * numero2

#Mostramos el resultado con alta prsicion
print(f"Resultado preciso: {resultado}")