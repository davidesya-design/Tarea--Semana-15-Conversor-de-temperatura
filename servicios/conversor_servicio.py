"""
Servicio ConversorServicio
Contiene la lógica de conversión y validación.
"""

class ConversorServicio:

    def convertir_a_fahrenheit(self, temperatura):
        return (temperatura.valor_celsius * 9 / 5) + 32

    def es_temperatura_alta(self, temperatura):
        temperatura_referencia = 30.0
        return temperatura.valor_celsius >= temperatura_referencia
