import numpy as np

class BlockProcessor:
    """
    Clase para dividir un espacio de estados en bloques y procesarlos iterativamente.
    """
    
    def __init__(self, data: np.ndarray, block_size: int):
        """
        Inicializa el procesador de bloques.
        
        :param data: Matriz de datos a procesar.
        :param block_size: Tamaño de cada bloque a procesar.
        """
        # Verificar que 'data' sea un np.ndarray 2D
        if not isinstance(data, np.ndarray):
            raise ValueError("Los datos deben ser un objeto np.ndarray.")
        if len(data.shape) != 2:
            raise ValueError("Los datos deben ser una matriz 2D, no un vector 1D o una matriz de más de 2 dimensiones.")
        
        self.data = data
        self.block_size = block_size
        self.blocks = self._divide_into_blocks()
    
    def _divide_into_blocks(self):
        """
        Divide la matriz en bloques del tamaño especificado.
        
        :return: Lista de bloques extraídos de la matriz.
        """
        blocks = []
        rows, cols = self.data.shape
        for i in range(0, rows, self.block_size):
            for j in range(0, cols, self.block_size):
                block = self.data[i:i+self.block_size, j:j+self.block_size]
                blocks.append(block)
        return blocks
    
    def process_blocks(self, process_function):
        """
        Procesa los bloques aplicando una función dada.
        
        :param process_function: Función que se aplicará a cada bloque.
        """
        processed_blocks = []
        for block in self.blocks:
            processed_blocks.append(process_function(block))
        return processed_blocks

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una matriz de ejemplo
    data_matrix = np.random.rand(10, 10)  # Asegúrate de que sea una matriz 2D
    
    # Verificar la forma de la matriz de datos
    print("Forma de la matriz de datos:", data_matrix.shape)
    
    # Definir un tamaño de bloque
    block_size = 3
    
    # Instanciar el procesador de bloques
    processor = BlockProcessor(data_matrix, block_size)
    
    # Definir una función de procesamiento (ejemplo: calcular la media de cada bloque)
    def mean_block(block):
        return np.mean(block)
    
    # Procesar los bloques
    results = processor.process_blocks(mean_block)
    
    # Mostrar los resultados
    print("Resultados del procesamiento de bloques:", results)
