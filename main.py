def karatsuba(x,y):   
    if len(str(x)) <= 3 or len(str(y)) <= 3: # Se o número de digitos de algum dos números for menor que 3, utiliza o algoritmo padrão. Condição de parada da recursão
        return x*y
    
    n = max(len(str(x)), len(str(y))) # número de digitos
    m = n // 2 

    a = x // 10**m # n/2 primeiros digitos de x
    b = x % 10**m # n/2 ultimos digitos de y
    c = y // 10**m # n/2 primeiros digitos de y
    d = y % 10**m # n/2 ultimos digitos de y

    ac = karatsuba(a, c) #multiplicações recursivas
    bd = karatsuba(b, d)
    adbc = karatsuba(a + b, c + d) - ac - bd # para encontrar ad+bc subtraindo ac e bd do produto de a+b e c+d -> (a+b)(c+d)=ac+ad+bc+bd

    return ac * 10**(2*m) + adbc * 10**m + bd # ac * 10^2m + (ad+bc) * 10^m + bd



def main():

    in01 = int(input("Digite o primeiro número: "))
    in02 = int(input("Digite o segundo número: "))

    print("Analisando...")

    out = karatsuba(in01, in02)

    print(f"Resultado da multiplicação: {out}")

if __name__ == "__main__":
    main()