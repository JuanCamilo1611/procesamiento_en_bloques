import numpy as np

def dividir_en_bloques(array, tam_bloque):
    """
    Divide un array de NumPy en bloques más pequeños.
    Si el array es multidimensional, se dividirá por filas.

    :param array: np.ndarray, el array a dividir.
    :param tam_bloque: int, tamaño de cada bloque.
    :return: lista de bloques (np.ndarray).
    """
    # Verificamos si el array es 1D o 2D
    if len(array.shape) == 1:
        # Si es un array 1D, lo dividimos como un array plano
        num_bloques = int(np.ceil(len(array) / tam_bloque))
        return [array[i * tam_bloque:(i + 1) * tam_bloque] for i in range(num_bloques)]
    
    elif len(array.shape) == 2:
        # Si es un array 2D, dividimos por filas
        num_filas = array.shape[0]
        num_bloques = int(np.ceil(num_filas / tam_bloque))
        return [array[i * tam_bloque:(i + 1) * tam_bloque] for i in range(num_bloques)]
    
    else:
        raise ValueError("Solo se admiten arrays 1D y 2D.")

def reconstruir_array(bloques):
    """
    Reconstruye un array a partir de una lista de bloques.

    :param bloques: lista de np.ndarray.
    :return: np.ndarray, el array reconstruido.
    """
    return np.concatenate(bloques, axis=0)

def imprimir_info_array(array):
    """
    Imprime información útil sobre un array de NumPy.

    :param array: np.ndarray
    """
    print(f"Forma: {array.shape}, Tipo: {array.dtype}, Tamaño: {array.nbytes / 1024:.2f} KB")
