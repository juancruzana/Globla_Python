class Detector:
    def __init__(self, matriz):
        self.matriz = matriz

    def detectar_mutantes(self):

        mensajes = []  # Almacena mensaje según forma de mutación
        if self.detector_horizontal():
            mensajes.append('Tienes una mutación horizontal.')
        if self.detector_vertical():
            mensajes.append('Tienes una mutación vertical.')
        if self.detector_diagonal():
            mensajes.append('Tienes una mutación diagonal.')    
        return mensajes != [], '\n'.join(mensajes) if mensajes else 'No hay mutaciones detectadas.'  
    
    def detector_vertical(self):
        for col in range(6):
            contador = 1  # Cuenta de caracteres consecutivos
            for fila in range(1, 6): 
                # Compara el carácter actual con el anterior en la misma columna
                if self.matriz[fila][col] == self.matriz[fila - 1][col]:
                    contador += 1
                    # Si hay 4 consecutivos iguales, retorna True
                    if contador == 4:
                        return True
                else:
                    contador = 1  # Reinicia el contador si no son iguales
        # Si no encuentra secuencia de 4 consecutivos iguales en ninguna columna, retorna False
        return False
    
    def detector_horizontal(self):
        for fila in self.matriz:
            contador = 1  # Cuenta de caracteres consecutivos
            for i in range(1, len(fila)):
                if fila[i] == fila[i - 1]:  # Comparamos con el elemento anterior de la fila
                    contador += 1
                    if contador == 4:  # Si hay 4 consecutivos iguales, retorna True
                        return True
                else:
                    contador = 1  # Reinicia el contador si no hay coincidencia
        # Si no encuentra secuencia de 4 consecutivos iguales en las filas, retorna False
        return False
    
    def detector_diagonal(self):
        matriz = self.matriz
        
        # Dimensiones de la matriz
        filas = len(matriz)
        columnas = len(matriz[0])
        
        # Verificar diagonales de izquierda a derecha
        for i in range(filas - 3):
            for j in range(columnas - 3):
                if (matriz[i][j] == matriz[i+1][j+1] == matriz[i+2][j+2] == matriz[i+3][j+3]):
                    return True
        
        # Verificar diagonales de derecha a izquierda
        for i in range(filas - 3):
            for j in range(3, columnas):
                if (matriz[i][j] == matriz[i+1][j-1] == matriz[i+2][j-2] == matriz[i+3][j-3]):
                    return True
        return False

   
class Mutador(): 
    def __init__(self, adn, base_nitrogenada, forma, posicion_inicial):
        self.adn = adn
        self.base_nitrogenada = base_nitrogenada.upper() # De que tipo de base nitrogenada será la mutación
        self.forma = forma.lower() # Forma en la q se mutará v,(vertica), h(horizontal), d (diagonal)
        self.posicion_inicial = posicion_inicial # Posición de la mutación en el adn

    def crear_mutante(self): 
        pass


class Radiacion(Mutador):  
    def __init__(self, adn, base_nitrogenada, forma, posicion_inicial):
        super().__init__(adn, base_nitrogenada, forma, posicion_inicial) 
    
    def crear_mutante(self): 
        
        if self.forma == 'h': 
            self.adn[self.posicion_inicial] = (self.base_nitrogenada * 4) + (self.adn[self.posicion_inicial][4:]) # Agrega base nitrogenada en la posicion seleccionada
            return print(self.adn)

        if self.forma == 'v':
            for x in range(4):
                self.adn[x] = self.adn[x][:self.posicion_inicial] + self.base_nitrogenada + self.adn[x][self.posicion_inicial+1:] # Replaza fila por fila en la columna seleccionada
            return print(self.adn)


class Virus(Mutador):
    def __init__(self, adn, base_nitrogenada, forma, posicion_inicial):
        super().__init__(adn, base_nitrogenada, forma, posicion_inicial)
    
    def crear_mutante(self):
        if self.forma == 'd':
            fila = self.posicion_inicial[0]
            col = self.posicion_inicial[1]

            if self.posicion_inicial[1] < 3: # Mutar de izquierda a derecha
                for i in range(4):
                    self.adn[fila] = self.adn[fila][:col] + self.base_nitrogenada + self.adn[fila][col+1:] # Agrega la mutación desde posición_inicial
                    fila += 1
                    col += 1
                return [print(self.adn[x]) for x in range(len(self.adn))]
            
            else: # Mutar de derecha a izquierda
                for i in range(4):
                    self.adn[fila] = self.adn[fila][:col] + self.base_nitrogenada + self.adn[fila][col+1:] # Agrega la mutación desde posición_inicial
                    fila += 1
                    col -= 1
                return [print(self.adn[x]) for x in range(len(self.adn))]



class Sanador(Detector): 
    def __init__(self, lista_adn):
        super().__init__(lista_adn)
    
    def sanar_mutantes(self): 
        pass