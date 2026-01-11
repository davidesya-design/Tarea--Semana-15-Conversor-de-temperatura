"""
Archivo principal del Conversor de Temperatura
Inicializa los objetos y ejecuta la conversión.
"""
#          |
#          |   .
#   `.  *  |     .'
#     `. ._|_* .'  .
#   . * .'   `.  *
#-------|     |-------
#   .  *`.___.' *  .
#      .'  |* `.  *
#    .' *  |  . `.
#        . |
#          | Autor: Andreww Valenzuela

from modelos.temperatura import Temperatura
from servicios.conversor_servicio import ConversorServicio

# Crear objeto temperatura entrada predefinida
temperatura = Temperatura(32.0)

# Crear servicio conversor
conversor_servicio = ConversorServicio()

# Convertir temperatura
temperatura_fahrenheit = conversor_servicio.convertir_a_fahrenheit(temperatura)

# Verificar si la temperatura es alta
es_temperatura_alta = conversor_servicio.es_temperatura_alta(temperatura)

# Mostrar resultados
print("Temperatura en Celsius:", temperatura.valor_celsius)
print("Temperatura en Fahrenheit:", temperatura_fahrenheit)

if es_temperatura_alta:
    print("La temperatura es alta.")
else:
    print("La temperatura es normal o baja.")
