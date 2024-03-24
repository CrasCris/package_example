import pandas as pd
import numpy as np

def celsius_to_fahrenheit(data):
    """
    Convierte temperaturas en grados Celsius a grados Fahrenheit.

    Args:
    - data (pandas.DataFrame): DataFrame de Pandas que contiene una columna 'Celsius' con las temperaturas en grados Celsius.

    Returns:
    - pandas.DataFrame: DataFrame de Pandas con una nueva columna 'Fahrenheit' que contiene las temperaturas convertidas a grados Fahrenheit.
    """
    # Verificar si la columna 'Celsius' existe en el DataFrame
    if 'Celsius' not in data.columns:
        raise ValueError("El DataFrame debe contener una columna llamada 'Celsius'.")

    # Aplicar la conversión de Celsius a Fahrenheit utilizando NumPy
    data['Fahrenheit'] = data['Celsius'].apply(lambda x: (x * 9/5) + 32)

    return data

# # Ejemplo de uso:
# # Crear un DataFrame de ejemplo con temperaturas en grados Celsius
# data = pd.DataFrame({'Celsius': [0, 10, 20, 30, 40]})
# print("Datos originales:")
# print(data)

# # Aplicar la función para convertir a grados Fahrenheit
# data = celsius_to_fahrenheit(data)
# print("\nDatos convertidos a Fahrenheit:")
# print(data)
