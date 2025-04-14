# src/controllers/manager.py

import numpy as np
from .block import BlockProcessor

class Manager:
    def __init__(self, estado_fijo: np.ndarray, block_size: int):
        """
        Inicializa el gestor del procesamiento en bloques.
        """
        # Si el estado_fijo ya es una matriz 2D, no hace falta transformarlo
        self.estado = estado_fijo  # Lo dejamos como está, ya es un np.array 2D
        self.processor = BlockProcessor(self.estado, block_size)

    def obtener_bloques(self):
        """
        Devuelve los bloques procesados.
        """
        return self.processor.blocks

    def process_blocks(self):
        """
        Divide los datos en bloques y los procesa iterativamente.
        (Método extendido que puedes usar para estrategias futuras)
        """
        num_blocks = len(self.estado) // self.processor.block_size + \
                     (len(self.estado) % self.processor.block_size > 0)

        results = []
        for i in range(num_blocks):
            start = i * self.processor.block_size
            end = start + self.processor.block_size
            block = self.estado[start:end]

            if self.should_process_block(block):
                result = self.processor.process(block)
                results.append(result)

        return results

    def should_process_block(self, block):
        """
        Lógica para determinar si un bloque debe procesarse.
        """
        return block.sum() > 0  # Solo procesar bloques con contenido
