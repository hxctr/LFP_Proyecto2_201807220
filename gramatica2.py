import string



class Produccion2():
    def __init__(self,inicial,ladoDerecho, auxiliares=None):
        self.inicial = inicial
        self.auxiliares = []
        self.ladoDerecho = ladoDerecho
        

class Gramatica2():
    
    def __init__(self,nombre,terminales,noTerminales,noTerminalInicial,producciones, auxis=None, contadores = True, producs=None):
        self.nombre = nombre
        self.terminales = terminales
        self.producs = list()
        self.noTerminales = noTerminales
        self.contadores = True
        self.noTerminalInicial = noTerminalInicial
        self.auxis = list()
        self.producciones = producciones
        
        

    def crearTerminal(self,terminal):
              
        terminales2 = [terminal]
        aux = False

              
        if terminales2[0].lower() in self.terminales:
            aux = True
        
              
        if aux:
            return"El terminal ya se encuentra en la gramatica"
        else:
                  
            self.terminales.append(terminales2[0].lower())
            return"El terminal a sido ingresado exitosamente"
    
    def modificarInicial(self,inicial):
        aux = [False]

        if inicial in self.noTerminales:
            aux[0] = True
        
        if aux[0]:
            self.noTerminalInicial = inicial 
            return"Se a modificado el no terminal inicial"
        else:
            return"El no terminal ingresado no se encuentra en la gramatica"

    def crearNoTerminal(self,noTerminal):
        noTer = [noTerminal]
        mayusculas = string.ascii_uppercase

              
        aux = False

        for it in mayusculas:
            if noTer[0].startswith(it):
                aux = True

        if aux:
            aux = False
                  
            if noTer[0].upper() in self.noTerminales:
                aux = True
            
                  
            if aux:
                return"El no terminal ya se encuentra en la gramatica"
            else:
                self.noTerminales.append(noTer[0])
                return"El no terminal a sido ingresado con exito" 
        else:
            return"Los no terminales solo pueden empezar con letra mayuscula"
   
    def removerRecursividad(self,inicial,derecha):
              
        aux = False

              
        nuevoNoTerminal = [inicial+"_P", [], []]      

              
        for valor in self.producciones:
            if valor.inicial == nuevoNoTerminal[0]:
                aux = True
                break
        
        if aux:
            aux = False

                  
            derecha = derecha[2:len(derecha)]
            derecha += " "+nuevoNoTerminal[0]

                  
            if derecha in valor.ladoDerecho:
                aux = True
            
            if aux:
                nuevoNoTerminal[1] = True
                return"La produccion ya se encuentra en la gramatica"
            else:
                      
                valor.ladoDerecho.append(derecha)

                      
                nuevoNoTerminal[1] = False
                for valor in self.producciones:
                    if valor.inicial == inicial:
                        for it in range(len(valor.ladoDerecho)):
                                  
                            nuevoNoTerminal[1] = True
                            if valor.ladoDerecho[it].endswith(nuevoNoTerminal[0]) == False:
                                valor.ladoDerecho[it] += " "+nuevoNoTerminal[0]
                        break
                
                return"Se a creado la produccion"
        else:
                  
            nuevoNoTerminal[1] = derecha
            derecha = derecha[2:len(derecha)]
            derecha += " "+nuevoNoTerminal[0]

                  
            self.noTerminales.append(nuevoNoTerminal[0])
            self.producciones.append(Produccion2(nuevoNoTerminal[0],[derecha,"epsilon"]))

                  
            for valor in self.producciones:
                if valor.inicial == inicial:
                    
                    for it in range(len(valor.ladoDerecho)):
                        nuevoNoTerminal[2] = valor.inicial
                              
                        if valor.ladoDerecho[it].endswith(nuevoNoTerminal[0]) == False:
                            valor.ladoDerecho[it] += " "+nuevoNoTerminal[0]
                    break

            return"Se a creado la produccion"

    def crearProduccion(self,produccion):
              
        aux = [False, [], []]

              
        produccion = produccion.split(">")
        aux[1] = True
        inicial = produccion[0].rstrip(" ")
        derecha = [produccion[1].lstrip(" ")]
        aux[2] = True
              
        if inicial in self.noTerminales:
            aux[0] = True
        
        if aux[0]:
            mayusculas = string.ascii_uppercase

                  
                  
            it = 0
            recursividad = 0
            aux[0] = False

                  
            der = derecha[0].split(" ")

                  
            while it < len(der):
                aux[0] = False

                      
                if der[it].islower() or der[it].isdigit():
                    if der[it] in self.terminales:
                        aux[0] = True
                      
                else:
                    if der[it] in self.noTerminales:
                        aux[1] = False
                        aux[0] = True

                      
                if der[it] in mayusculas:
                    if it == 0 and der[it] == inicial:
                        recursividad = 1
                        aux[1] = True

                      
                if aux[0] == False:
                    break

                      
                it += 1

            if aux[0]:
                if recursividad == 1:
                          
                   return self.removerRecursividad(inicial,derecha[0])
                else:
                          
                          
                          
                    auxi = False
                    aux[0] = False
                    nuevoNoTerminal = inicial+"_P"

                          
                    for asociada in self.producciones:
                        if asociada.inicial == nuevoNoTerminal:
                            aux[1] = True
                            auxi = True
                            break

                          
                    for valor in self.producciones:
                        if valor.inicial == inicial:
                            aux[0] = True
                            break

                    if aux[0]:
                        if auxi:
                            aux[0] = False

                                  
                            derecha[0] +=" "+nuevoNoTerminal

                                  
                            for derecho in valor.ladoDerecho:
                                if derecho == derecha[0]:
                                    aux[1] = False
                                    aux[0] = True
                                    break

                            if aux[0]:
                                return"La produccion ya se encuentra en la gramatica"
                            else:
                                      
                                valor.ladoDerecho.append(derecha[0])
                                return"Se a creado la produccion"
                        else:
                            aux[0] = False

                                  
                            for derecho in valor.ladoDerecho:
                                if derecho == derecha[0]:
                                    aux[1] = False
                                    aux[0] = True
                                    
                                    break

                            if aux[0]:
                                return"La produccion ya se encuentra en la gramatica"
                            else:
                                      
                                valor.ladoDerecho.append(derecha[0])
                                return"Se a creado la produccion"
                    else:
                        if auxi:
                                  
                            derecha[0] += " "+nuevoNoTerminal

                            self.producciones.append(Produccion2(inicial,[derecha[0]]))
                            return"Se a creado la produccion"
                        else:
                            self.producciones.append(Produccion2(inicial,[derecha[0]]))
                            return"Se a creado la produccion"
            else:
                return"Alguno de los terminales o no terminales del lado derecho de la produccion no existe"
        else:
            return"El no terminal inicial no se encuentra en la gramatica"


