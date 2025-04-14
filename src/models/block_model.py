import numpy as np

class BlockModel:
    """
    Modelo de un bloque del espacio de estados.

    Atributos:
        datos (np.ndarray): Submatriz que representa el bloque.
        posicion (tuple): Tupla con las coordenadas de inicio (fila, columna).
        resultado (any): Resultado del procesamiento aplicado al bloque.
    """
    def __init__(self, datos: np.ndarray, posicion: tuple):
        self.datos = datos
        self.posicion = posicion
        self.resultado = None  # Se llenará después del procesamiento

    def set_resultado(self, resultado):
        """
        Guarda el resultado del procesamiento del bloque.
        """
        self.resultado = resultado

    def __str__(self):
        return f"Bloque en {self.posicion}, resultado: {self.resultado}"
