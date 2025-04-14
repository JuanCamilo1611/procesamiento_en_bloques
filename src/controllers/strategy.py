from abc import ABC, abstractmethod

class BlockProcessingStrategy(ABC):
    """
    Clase base para definir estrategias de procesamiento en bloques.
    Las estrategias deben implementar el método `process_block`.
    """
    
    @abstractmethod
    def process_block(self, block):
        """
        Método abstracto para procesar un bloque.
        Debe ser implementado por clases derivadas.
        
        :param block: np.ndarray, bloque de datos a procesar.
        :return: Resultado del procesamiento.
        """
        pass

class DefaultStrategy(BlockProcessingStrategy):
    """
    Estrategia de procesamiento por defecto: simplemente retorna la suma de los valores del bloque.
    """
    
    def process_block(self, block):
        """
        Suma los elementos del bloque.
        
        :param block: np.ndarray, bloque de datos.
        :return: Suma de los valores del bloque.
        """
        return block.sum()  # Ejemplo: sumar los valores del bloque.

class MeanStrategy(BlockProcessingStrategy):
    """
    Estrategia de procesamiento que calcula el promedio de los valores del bloque.
    """
    
    def process_block(self, block):
        """
        Calcula el promedio de los valores del bloque.
        
        :param block: np.ndarray, bloque de datos.
        :return: Promedio de los valores del bloque.
        """
        return block.mean()

class MaxStrategy(BlockProcessingStrategy):
    """
    Estrategia de procesamiento que obtiene el valor máximo del bloque.
    """
    
    def process_block(self, block):
        """
        Obtiene el valor máximo del bloque.
        
        :param block: np.ndarray, bloque de datos.
        :return: Valor máximo del bloque.
        """
        return block.max()
