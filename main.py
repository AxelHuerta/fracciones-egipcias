import math


# Tipos
class Fraccion:
    def __init__(self, numerador: int, denominador: int):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


class FraccionEgipcia:
    def __str__(self):
        return f"{self.fracciones}"

    def convertir(a: Fraccion):
        # Caso base
        if a.numerador == 1:
            return [a]

        is_egipcia = False
        listado: list[Fraccion] = [a]

        while not is_egipcia:
            elemento: Fraccion = listado[-1]
            listado.pop()
            aprox: Fraccion = Fraccion(
                1, (math.floor(elemento.denominador / elemento.numerador) + 1)
            )
            diferencia: Fraccion = Fracciones.restar(elemento, aprox)

            listado.append(aprox)
            listado.append(diferencia)

            if diferencia.numerador == 1:
                is_egipcia = True

        return listado


# Operaciones
class Fracciones:
    # Sumar fracciones
    def sumar(a: Fraccion, b: Fraccion):
        numerador = a.numerador * b.denominador + b.numerador * a.denominador
        denominador = a.denominador * b.denominador
        resultado = Fraccion(numerador, denominador)

        return Fracciones.simplificar(resultado)

    # Restar fracciones
    def restar(a: Fraccion, b: Fraccion):
        numerador = a.numerador * b.denominador - b.numerador * a.denominador
        denominador = a.denominador * b.denominador
        resultado = Fraccion(numerador, denominador)
        return Fracciones.simplificar(resultado)

    # Multiplicar fracciones
    def multiplicar(a: Fraccion, b: Fraccion):
        numerador = a.numerador * b.numerador
        denominador = a.denominador * b.denominador
        resultado = Fraccion(numerador, denominador)
        return Fracciones.simplificar(resultado)

    # Dividir fracciones
    def dividir(a: Fraccion, b: Fraccion):
        numerador = a.numerador * b.denominador
        denominador = a.denominador * b.numerador
        resultado = Fraccion(numerador, denominador)
        return Fracciones.simplificar(resultado)

    # Simplificar fracciones
    def simplificar(a: Fraccion):
        def mcd(a: int, b: int):
            while b:
                a, b = b, a % b
            return a

        divisor = mcd(a.numerador, a.denominador)
        resultado = Fraccion(a.numerador // divisor, a.denominador // divisor)
        return resultado


x = Fraccion(7, 8)
result: list[Fraccion] = FraccionEgipcia.convertir(x)

for i in result:
    print(i)
