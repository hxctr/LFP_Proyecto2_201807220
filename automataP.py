class AutomataP():
    def __init__(self,nombre,estados,noTerminalInicial,alfabeto,simbolosPila,transiciones, nodos=None, puntos=None):
        self.nombre = nombre
        self.estados = estados
        self.nodos = list()
        self.noTerminalInicial = noTerminalInicial
        self.alfabeto = alfabeto
        self.simbolosPila = simbolosPila
        self.puntos = list()
        self.transiciones = transiciones
        

    def crearEstados(self):
        self.nodos = ['', '', '', '']
        self.estados.append(EstadoP("i",0))
        self.nodos[0] = self.estados.append(EstadoP("i",0))
        self.estados.append(EstadoP("p",0))
        self.nodos[1] = self.estados.append(EstadoP("p",0))
        self.estados.append(EstadoP("q",0))
        self.nodos[2] = self.estados.append(EstadoP("q",0))
        self.estados.append(EstadoP("f",1))
        self.nodos[3] = self.estados.append(EstadoP("f",1))
        

    def crearTransiciones(self,gramatica):
        dolar = "\0024"
        self.transiciones = []
        
        
        alpha = "\u03BB"

        self.transiciones.append(TransicionP("i",alpha,alpha,"p","#"))
        
        if gramatica.noTerminalInicial == "":
                  
            pass
        else:
            self.transiciones.append(TransicionP("p",alpha,alpha,"q",gramatica.noTerminalInicial))

        if len(gramatica.terminales) == 0:  
                  
            pass
        else:
            for terminal in gramatica.terminales:
                self.transiciones.append(TransicionP("q",terminal,terminal,"q",alpha))
    
        if len(gramatica.producciones) == 0:
                  
            pass
        else:
            for produccion in gramatica.producciones:
                for derecha in produccion.ladoDerecho:
                    self.transiciones.append(TransicionP("q",alpha,produccion.inicial,"q",derecha))
                    alpha = "\u03BB"

        self.transiciones.append(TransicionP("q",alpha,"#","f",alpha))
        alpha = "\u03BB"
        return "Se ha creado el automata de pila de forma exitosa"

    def generarGrafo(self):
        dot = ["digraph G{\nrankdir=LR\n", list(), list()]

              
        for estados in self.estados:
            if estados.aceptacion == 1:
                dot[1].append(estados.valor)
                dot[0] += estados.valor + " [ label = "+ '"' + estados.valor + '" shape = "doublecircle" ] \n'
            else:
                dot[0] += estados.valor + " [ label = "+ '"' + estados.valor + '" shape = "circle" ] \n'
                dot[1].append(estados.valor)
    
              
        for transicion in self.transiciones:
            valor = transicion.entrada+","+transicion.lecturaPila+";"+transicion.guardarEnPila
            dot[0] += transicion.actual + " -> " + transicion.nuevoEstado + "[ label = " + '"' + valor + '" ]\n'

              
        dot[0] += "init [label = " + '"' + "inicio" + '" shape =' + '"' + "plaintext" + '" ]\n' 
        dot[0] += "init -> i \n }"

        return dot[0]

class EstadoP():
    def __init__(self,valor,aceptacion, numeroEstado= None):
        self.valor = valor
        self.numeroEstado = list()
        self.aceptacion = aceptacion

class TransicionP():
    def __init__(self,actual,entrada,lecturaPila,nuevoEstado,guardarEnPila, numeroTransicion=None):
        self.actual = actual
        self.entrada = entrada
        self.lecturaPila = lecturaPila
        self.numeroTransicion = list()
        self.nuevoEstado = nuevoEstado
        self.guardarEnPila = guardarEnPila