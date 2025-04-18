import math


# Tipos
class Fraccion:
    def __init__(self, numerador: int, denominador: int):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    # Sumar fracciones
    def __add__(self, other):
        numerador = (
            self.numerador * other.denominador + other.numerador * self.denominador
        )
        denominador = self.denominador * other.denominador
        resultado = Fraccion(numerador, denominador)

        return Fraccion.simplificar(resultado)

    # Restar fracciones
    def __sub__(self, other):
        numerador = (
            self.numerador * other.denominador - other.numerador * self.denominador
        )
        denominador = self.denominador * other.denominador
        resultado = Fraccion(numerador, denominador)

        return Fraccion.simplificar(resultado)

    # Multiplicar fracciones
    def __mul__(self, other):
        numerador = self.numerador * other.numerador
        denominador = self.denominador * other.denominador
        resultado = Fraccion(numerador, denominador)

        return Fraccion.simplificar(resultado)

    # Dividir fracciones
    def __truediv__(self, other):
        numerador = self.numerador * other.denominador
        denominador = self.denominador * other.numerador
        resultado = Fraccion(numerador, denominador)

        return Fraccion.simplificar(resultado)

    # Simplificar fracciones
    @staticmethod
    def simplificar(a: "Fraccion"):
        def mcd(a: int, b: int):
            while b:
                a, b = b, a % b
            return a

        divisor = mcd(a.numerador, a.denominador)
        resultado = Fraccion(a.numerador // divisor, a.denominador // divisor)
        return resultado


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
            diferencia: Fraccion = elemento - aprox

            listado.append(aprox)
            listado.append(diferencia)

            if diferencia.numerador == 1:
                is_egipcia = True

        return listado

    def to_string(fracciones: list[Fraccion]) -> str:
        return " + ".join(str(fraccion) for fraccion in fracciones)
