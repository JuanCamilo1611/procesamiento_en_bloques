# src/main.py

from controllers.manager import Manager
from controllers.strategy import DefaultStrategy
import numpy as np

def main():
    print("\n--- Procesamiento en Bloques ---\n")

    # Definición del estado fijo (puedes personalizar este ejemplo)
    estado_fijo = "101101011100111"

    # Tamaño del bloque (cantidad de bits por bloque)
    tamaño_bloque = 5

    # Convertir el estado fijo en una matriz 2D de 0s y 1s
    # Convertir la cadena binaria en una matriz de una fila
    data_matrix = np.array([int(bit) for bit in estado_fijo], dtype=np.int8).reshape(1, -1)

    # Inicializa el sistema con el estado
    manager = Manager(data_matrix, tamaño_bloque)

    # Obtener los bloques desde el estado
    bloques = manager.obtener_bloques()

    # Aplicar la estrategia de procesamiento por bloque
    estrategia = DefaultStrategy()

    resultados = {}
    for idx, bloque in enumerate(bloques):
        resultado = estrategia.process_block(bloque)
        resultados[f"Bloque {idx}"] = resultado

    print("\nResultado del procesamiento:\n")
    print("=" * 40)

    for idx, bloque in enumerate(bloques):
        bloque_str = ''.join(str(bit) for bit in bloque)  # Convertir array a string
        resultado = estrategia.process_block(bloque)
        
        print(f"🧩 Bloque {idx + 1}")
        print(f"Bits    : {bloque_str}")
        print(f"Resultado: {resultado}")
        print("-" * 40)


if __name__ == "__main__":
    main()

