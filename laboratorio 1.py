#Usamos recursion con memoizacion para  calcular numeros de Fibonacci
def fibonacci(n, nemo={}):
    if n in nemo:
        return nemo[n]
    if n <= 1:
        return n
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]
# Calcular el número de Fibonacci de 50
resultado = fibonacci(50)
print("Fibonacci de 50 es:", resultado)
