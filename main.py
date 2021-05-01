import os
import codecs
import webbrowser



from tkinter import Tk
from tkinter.filedialog import askopenfilename

from gramatica2 import Gramatica2,Produccion2
from automataP import AutomataP,EstadoP,TransicionP

import time


gramaticas2 = []
automatasDePila = []

pTextos = ['\nListado de gramaticas disponibles:', '\nListado de automatas disponibles:']
rutaArchivo = ''

def subirArchivo():
    Tk().withdraw()
    global rutaArchivo
    rutaArchivo = askopenfilename()
    if rutaArchivo:
        print('------------------------------')
        print('¡Archivo cargado exitosamente!')
        print('------------------------------')
        leerArchivo()
    else:
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        print('Aun no se ha cargado el archivo!')
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

def initalScreen():
    seconds = 5
    
    print('--------Gramaticas libres de contexto--------')
    print('----------Hector Ponsoy | 201807220----------')
    while seconds != 0:
        print (">>>>>>>>>>>>>>>>>>>>>", seconds,'<<<<<<<<<<<<<<<<<<<<<')
        time.sleep(1)
        seconds = seconds - 1
    print('\n\n\n\n\n\n\n\n')
    print('''
        ******************************
        ******************************
        ******************************
        **********BIENVENIDO**********
        ******************************
        ******************************
        ******************************''')
    time.sleep(2)
    print('\n\n\n\n\n\n\n\n')

lineasEnLista = []
listaParaSplitTermi = []

def leerArchivo():
    global lineasEnLista, listaParaSplitTermi
    
    leerRuta = open(rutaArchivo, 'r')
    
    for lineas in leerRuta:
        lineasEnLista.append(lineas)
    leerRuta.close()
    
    
    
    
    
    
    
    
    eliminandoSaltosDeLinea()
    eliminandoEspaciosUltimos()
    cambiandoSeparador()
    
    
    listaParaSplitTermi = lineasEnLista
    # print('********',listaParaSplitTermi,'------')
    listaDelistas()
    mandandoListas(listaTotal2)
    
    

def eliminandoSaltosDeLinea():
    for i, x in enumerate(lineasEnLista):
        if "\n" in x:
            lineasEnLista[i] = x.replace('\n', '')

def eliminandoEspaciosUltimos():
    for i in range(len(lineasEnLista)):
        lineasEnLista[i] = lineasEnLista[i].rstrip()


def cambiandoSeparador():
    for i, x in enumerate(lineasEnLista):
        if "->" in x:
            lineasEnLista[i] = x.replace('->', ' > ')

listaTotal2 = [[]]
def listaDelistas():
    global listaTotal2
    
    contador = 0

    for i in range(len(lineasEnLista)):
        if lineasEnLista[i] != "*":
            listaTotal2[contador].append(lineasEnLista[i])
        else:
               
            listaTotal2.append([])
            contador = contador + 1

       
    listaTotal2 = listaTotal2[:-1]
    




otraNoche = []

def automatizando(lista):
    global otraNoche
    
    guardadnto = lista[1].split(';') 
       

    noTer = guardadnto[0].split(',')
    siTer = guardadnto[1].split(',')
    prTer = guardadnto[2].split(',')

    newList = []
    newList.append(lista[0])
    newList.append(noTer)
    newList.append(siTer)
    newList.append(prTer)
    for i in range(2, len(lista)):
        newList.append(lista[i])
        
    otraNoche.append(lista[0])
    otraNoche.append(noTer)
    otraNoche.append(siTer)
    otraNoche.append(prTer)
    
    for i in range(2, len(lista)):
        otraNoche.append(lista[i])
    otraNoche.append('*')
    
    

    return newList


listaTotal3 = []

def mandandoListas(final):
    global listaTotal3
    
    for i in range(len(final)):
        listaTotal3.append(automatizando(final[i]))
    return listaTotal3
        


def Menu():
    opcion = 0
    while opcion != 6:
        print(" ")
        print("------------Menu Principal-------------")
        print("                                       ")
        print("1. Cargar archivo                      ")
        print("2. Mostrar información de la gramática ")
        print("3. Generar autómata de pila equivalente")
        print("4. Reporte de recorrido                ")
        print("5. Reporte en tabla                    ")
        print("0. Salir                               ")
        print("-------------------------------------- ")
        print('Opcion: ', end='' )
        opcion = input()
        
        if opcion == '1':
            subirArchivo()
            sending(listaTotal3)
            
        elif opcion == '2':
            print("\nListado de gramaticas disponibles:")

            if len(gramaticas2)==0:
                print("   Aun no existen gramaticas en el sistema\n")
            else:
                #mostrando las gramaticas disponibles
                gramatica = ""
                for valor in gramaticas2:
                    if gramatica == "":
                        gramatica = "   "+valor.nombre+"\n"
                    else:
                        gramatica += "   "+valor.nombre+"\n"
                print(gramatica)

                #captura del nombre del automata
                nombre = input("Escriba el nombre de una gramatica del listado: ")

                gramatica = None

                #verificacion del nombre del automata
                for valor in gramaticas2:
                    if valor.nombre == nombre:
                        gramatica = valor
                        break

                if gramatica == None:
                    print("El nombre ingresado no existe en el listado")
                else:
                    #-----------------------------
                    
                    
                    cont = 2
                    for i in range(len(otraNoche)):
                        if otraNoche[i] == nombre:
                            indice = i
                            break
                    
                    print('\nNombre de la gramatica tipo 2: ',nombre)
                    print('No terminales = ',otraNoche[indice + 1])
                    print('Terminales = ',otraNoche[indice + 2])
                    print('No terminal inicial = ',otraNoche[indice + 3] )
                    
                    rango = indice + 4
                    
                    for i in range(rango, len(otraNoche)):
                        if otraNoche[i] != '*':
                            print(otraNoche[i])
                        else:
                            break
                    
            
        elif opcion == '3':
            automatas()
            
        elif opcion == '4':
            pass
        elif opcion == '5':
            print(pTextos[1])

            if len(automatasDePila)==0:
                print("   Aun no existen automatas en el sistema\n")
            else:
                   
                gramatica = ['']
                for valor in automatasDePila:
                    if gramatica[0] == "":
                        gramatica[0] = "   "+valor.nombre+"\n"
                    else:
                        gramatica[0] += "   "+valor.nombre+"\n"
                print(gramatica[0])

                   
                nombre = input("Escriba el nombre de un automata del listado: ")

                automata = [None]

                   
                for valor in automatasDePila:
                    if valor.nombre == nombre:
                        automata[0] = valor
                        break

                if automata[0] == None:
                    print("El nombre ingresado no existe en el listado")
                    
                
                else:
                       
                    reporteEnTabla(automata[0], [])
        elif opcion == '6':
            opcion = 6
        else:
            print("Ingrese una opcion valida")

def datos(nombre, unaLista):
    # print(pTextos[0])
    
    gramatica = [None, []]

   

       
       

       
    for valor in gramaticas2:
        if valor.nombre == nombre:
            gramatica[0] = valor
            break

    if gramatica[0] == None:
           
        nueva_gramatica = Gramatica2(nombre,[],[],"",[])

           
        gramaticas2.append(nueva_gramatica)

        formandoGramatica(nueva_gramatica, unaLista)
           
    else:
           
        print('pasa aqui')
            

listaTotal = [
   ['Grm1', ['S', 'A', 'B', 'C'], ['a', 'b', 'z'], ['S'], 'S > A', 'A > a A a', 'A > B', 'B > b B b', 'B > C', 'C > z C', 'C > z'], 
   ['Gramatica2', ['A', 'B', 'C', 'D'], ['0', '1'], ['A'], 'A > 1 B', 'A > 0 C', 'B > 1 A', 'B > 0 D', 'C > 1 D', 'C > 0', 'D > 1 C']
]


def sending(lis):
    global pTextos
    
    for i in range(len(lis)):
        mandandoDatos(lis[i])

def mandandoDatos(unaLista):
    
    datos(unaLista[0], unaLista)
       
    
def formandoGramatica(nueva_gramatica, unaLista):
       
       
    
    longitudTerminales = len(unaLista[2])
    for x in range(longitudTerminales):
        mandandoTerminales(nueva_gramatica, unaLista[2][x])
    
    longitud = len(unaLista[1])
    for i in range(longitud):
        mandandoNoTerminales(nueva_gramatica, unaLista[1][i])
    
    
    longitudListaTotal = len(unaLista)
    for i in range(4, longitudListaTotal):
        mandandoProducciones(nueva_gramatica, unaLista[i]) 
    
    
    longitudNoTerminalInicial = len(unaLista[3])
    for i in range(longitudNoTerminalInicial):
        mandandoNoTerminalInicial(nueva_gramatica, unaLista[3][i])   
        
    
       


def mandandoNoTerminales(gramatica2, noTerminales):
       
    noTerminal = noTerminales

       
    gramatica2.crearNoTerminal(noTerminal)
       

def mandandoTerminales(gramatica2, terminales):
    
    terminal = terminales

       
    gramatica2.crearTerminal(terminal)

def mandandoNoTerminalInicial(gramatica2, noTerminalInicial):
       
    noTerminal = noTerminalInicial

       
    gramatica2.modificarInicial(noTerminal)
    
def  mandandoProducciones(gramatica2, producciones):
       
    produccion = producciones

       
    gramatica2.crearProduccion(produccion)
    

def generandoAutomatas(gramatica2, nombreAP):
    
    print(pTextos[0])

    if len(gramaticas2)==0:
        print("   Aun no existen gramaticas en el sistema\n")
    else:
           
        gramatica = ['', []]
        for valor in gramaticas2:
            if gramatica[0] == "":
                gramatica[0] = "   "+valor.nombre+"\n"
            else:
                gramatica[0] += "   "+valor.nombre+"\n"
        print(gramatica[0])

           
        nombre = nombreAP

        gramatica[0] = None

           
        for valor in gramaticas2:
            if valor.nombre == nombre:
                gramatica[0] = valor
                break

        if gramatica[0] == None:
            print("El nombre ingresado no existe en el listado")
        else:
               
            simbolos = []

               
            for valor in gramatica[0].terminales:
                simbolos.append(valor)
            for valor in gramatica[0].noTerminales:
                simbolos.append(valor)
            simbolos.append("#")

               
            nuevo_automata = AutomataP(gramatica[0].nombre,[],gramatica[0].noTerminalInicial,gramatica[0].terminales,simbolos,[])

               
            for it in range(len(automatasDePila)):
                if automatasDePila[it].nombre == gramatica[0].nombre:
                    automatasDePila.pop(it)
                    gramatica[1] = valor
                    break

            automatasDePila.append(nuevo_automata)
            nuevo_automata.crearEstados()
            print(nuevo_automata.crearTransiciones(gramatica[0]))
    


def automatas():
    print(pTextos[0])

    if len(gramaticas2)==0:
        print("   Aun no existen gramaticas en el sistema\n")
    else:
           
        gramatica = ['', []]
        for valor in gramaticas2:
            if gramatica[0] == "":
                gramatica[0] = "   "+valor.nombre+"\n"
            else:
                gramatica[0] += "   "+valor.nombre+"\n"
        print(gramatica[0])

           
        nombre = input("Escriba el nombre de una gramatica del listado: ")

        gramatica[0] = None

           
        for valor in gramaticas2:
            if valor.nombre == nombre:
                gramatica[0] = valor
                break

        if gramatica[0] == None:
            print("El nombre ingresado no existe en el listado")
        else:
               
            simbolos = []

               
            for valor in gramatica[0].terminales:
                simbolos.append(valor)
            for valor in gramatica[0].noTerminales:
                simbolos.append(valor)
            simbolos.append("#")

               
            nuevo_automata = AutomataP(gramatica[0].nombre,[],gramatica[0].noTerminalInicial,gramatica[0].terminales,simbolos,[])

               
            for it in range(len(automatasDePila)):
                if automatasDePila[it].nombre == gramatica[0].nombre:
                    automatasDePila.pop(it)
                    gramatica[1]= valor
                    break

            automatasDePila.append(nuevo_automata)
            nuevo_automata.crearEstados()
            print(nuevo_automata.crearTransiciones(gramatica[0]))
        generate(nombre)

def generate(autoAP):
    print(pTextos[1])

    if len(automatasDePila)==0:
        print("   Aun no existen automatas en el sistema\n")
    else:
           
        gramatica = ['']
        for valor in automatasDePila:
            if gramatica[0] == "":
                gramatica[0] = "   "+valor.nombre+"\n"
            else:
                gramatica[0] += "   "+valor.nombre+"\n"
        print(gramatica[0])

           
        nombre = autoAP

        automata = [None, []]

           
        for valor in automatasDePila:
            if valor.nombre == nombre:
                automata[0] = valor
                break

        if automata[0] == None:
            print("El nombre ingresado no existe en el listado")
        else:

               
            grafo = automata[0].generarGrafo()
               
            # path_dot = "C:\\Users\\hctr\\Desktop\\" + nombre +".dot"
            path_dot = nombre +".dot"
            archivo_dot = [codecs.open(path_dot,"w","utf-8")]
            archivo_dot[0].write(grafo)
            archivo_dot[0].close()

               
               
            # path_imagen = "C:\\Users\\hctr\\Desktop\\" + nombre +".png"
            path_imagen = nombre +".png"
            comando = "dot " + path_dot + " -Tpng -o " + path_imagen
            os.system(comando)
               
            
            
            
               
               
               
            
            indice = [i for i, x in enumerate(listaParaSplitTermi) if x == nombre]
            
            indiceConjunto = listaParaSplitTermi[indice[0] + 1]
            
            conjunto = indiceConjunto.split(';')
            
            # print(conjunto[1],'00000000000000000000000000000000000000')
                    
            reporte = """
            <html>
            <head>
                <title>Automata de pila</title>
                <meta charset="utf-8">
                <meta name="Author" content="https://github.com/pablorgarcia" />
                <meta name="description" content="Table Responsive" />
                <meta name="keywords" content="table, responsive" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <link href="table-responsive.css" media="screen" type="text/css" rel="stylesheet" />
            </head>
            <body>
                <h1><span class="blue"></span>AP_<span class="blue"></span> <span class="yellow">"""+nombre+"""</pan>
                </h1>
                <table class="container">
                    <thead>
                        <tr>
                            <th>No.</th>
                            <th>Terminales</th>
                            <th>Alfabeto de pila</th>
                            <th>Estados</th>
                            <th>Estado inicial</th>
                            <th>Estado de aceptacion</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>"""+conjunto[1]+"""</td>
                            <td>"""+str(automata[0].simbolosPila)+"""</td>
                            <td>i, p, q, f</td>
                            <td>i</td>
                            <td>f</td>
                        </tr>
                    </tbody>
                </table>
                <div id="imagen" align="center">
                    <img src='"""+nombre+""".png'>
                </div>
            </body>
            </html>
            """
            
            
            mensaje = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <img src='C:\\Users\\hctr\\Desktop\\"""+nombre+""".png' alt=''>
            </body>
            </html>
            """
            nombreReporte = 'AP_'+nombre+'.html'
            file = open(nombreReporte,mode='w', encoding="utf-8")
            file.write(reporte)
            file.close()
            webbrowser.open(nombreReporte)
    
    
def reporteEnTabla(automata, response):
    cadena = input("Escriba la cadena a validar: ")
    response = evaluarTexto(automata,cadena)
    # print(response[0])
    path_report = automata.nombre +".txt"
    archivo_report = codecs.open(path_report,"w","utf-8")
    archivo_report.write(response[1])
    archivo_report.close()
    
    archivoEnLista = []
    pathFile = open(path_report, 'r', encoding='utf-8')
    
    for i in pathFile:
        archivoEnLista.append(i)
    pathFile.close()
    
    for i, x in enumerate(archivoEnLista):
        if "\n" in x:
            archivoEnLista[i] = x.replace('\n', '')
    
    filas = [[]]
    contador = 0
    for valor in range(0, len(archivoEnLista)):
        
        filas[contador] = archivoEnLista[valor].split(';') 
        filas.append([])
        contador += 1

    filas = filas[:-1]
    
    col1 = []
    col2 = []
    col3 = []
    for i in range(len(filas)):
        col1.append(filas[i][0])
        col2.append(filas[i][1])
        col3.append(filas[i][2])
    
    
    
    
    texto = """
    <html>
        <head>
            <title>Reporte de errores</title>
            <meta charset="utf-8">
            <meta name="Author" content="https://github.com/pablorgarcia" />
            <meta name="description" content="Table Responsive" />
            <meta name="keywords" content="table, responsive" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <link href="table-responsive.css" media="screen" type="text/css" rel="stylesheet" />
        </head>
        <body>
        <h1><span class="blue"></span>Tabla<span class="blue"></span> <span class="yellow"> Reporte</pan></h1>
        <table class="container">
            <thead>
                <tr>
                    <th>No.</th>
                    <th>Pila</th>
                    <th>Entrada</th>
                    <th>Transicion</th>
                </tr>
            </thead>
            <tbody>"""
    numeros = 1
    for i in range(1,len(col3)):
        texto = texto + """<tr><td>"""+str(numeros)+"""</td><td>"""+col1[i]+"""</td><td>"""+col2[i]+"""</td><td>"""+col3[i]+"""</td></tr>"""
        numeros = numeros + 1
    texto2="""
                    </tbody>
                    </table>

                    </body>
                    </html>"""
    texto = texto + texto2
    file = open(automata.nombre+".html" ,mode='w', encoding='utf-8')
    file.write(texto)
    file.close()
    webbrowser.open(automata.nombre+".html")
    
    print("Se a generado el archivo HTML exitosamente")


def evaluarTexto(automata,entrada):
       
       
    alpha = "\u03BB"

       
       
       

       
    respuestas = [[]]

       
    pila = [[]]

       
    noTransiciones = [[]]

       
    pilaNoTerminales = [[]]

       
    actual = [automata.noTerminalInicial]

       
    it = 0

       
    idenTer = 0
    auxis = [True, [], []]
    idenNoTer = 1
    idenAux = 0

       
    cambio = ""

       
    entradaAux = entrada

       
    report = "PILA;ENTRADA;TRANSICION\n"

       
    pila[0].append("#")


    report += alpha+";"+entradaAux+";(i, "+alpha+", "+alpha+"; p, #)\n"

       
    pila[0].append(actual[0])

    report += "#;"+entradaAux+";(p, "+alpha+", "+alpha+"; q, "+actual[0]+")\n"

       
    for transicion in automata.transiciones:
        if transicion.lecturaPila == actual[0]:
            noTransiciones[0].append(transicion)
            
       
    if len(noTransiciones[0]) == 1:

           
        val1 = [str(pila[0]).rstrip("]")]
        val1[0] = val1[0].lstrip("[")
        val1[0] = val1[0].replace(", ","")
        val1[0] = val1[0].replace("'","")

           
        val2 = [noTransiciones[0][0].guardarEnPila.split(" ")]
        
           
        value = pila[0].pop()
           

           
        for val in reversed(val2[0]):
            pila[0].append(val)
            if val.islower() == True or val.isdigit() == True:
                   
                idenTer += 1
            else:
                pilaNoTerminales[0].append( "nt"+str(idenNoTer) )
                   
                idenNoTer += 1

        idenAux+=1

           
        val2 = [str(val2[0]).rstrip("]")]
        val2[0] = val2[0].lstrip("[")
        val2[0] = val2[0].replace(", ","")
        val2[0] = val2[0].replace("'","")
        report += val1[0]+";"+entradaAux+";"+"(q, "+alpha+", "+actual[0]+"; q,"+val2[0]+")\n"
    else:
        val1 = [str(pila[0]).rstrip("]")]
        val1[0] = val1[0].lstrip("[")
        val1[0] = val1[0].replace(", ","")
        val1[0] = val1[0].replace("'","")
        
        pila[0].pop()
        aux = []
        
        
        for valor in noTransiciones[0]:
            aux = valor.guardarEnPila.split(" ")
            if aux[0] == entrada[0]:
                auxis[0]=False
                break

            for val in reversed(valor.guardarEnPila.split(" ")):
                pila[0].append(val)
                if val.islower() == True or val.isdigit() == True:
                       
                    idenTer += 1
                else:
                       
                    pilaNoTerminales[0].append( "nt"+str(idenNoTer) )
                    idenNoTer += 1

        idenAux += 1

        val2 = [str(aux).rstrip("]")]
        val2[0] = val2[0].lstrip("[")
        val2[0] = val2[0].replace(", ","")
        val2[0] = val2[0].replace("'","")
        report += val1[0]+";"+entradaAux+";"+"(q, "+alpha+", "+actual[0]+"; q,"+val2[0]+")\n"

       
    while it < len(entrada):
        noTransiciones = [[]]

           
        actual = [pila[0][len(pila[0])-1]]

           
        if pila[0][len(pila[0])-1] != "#":

               
            if pila[0][len(pila[0])-1].islower()==True or pila[0][len(pila[0])-1].isdigit()==True:
                   
                auxis[0] = False
                   
                if pila[0][len(pila[0])-1] == entrada[it]:
                    val1 = [str(pila[0]).rstrip("]")]
                    val1[0] = val1[0].lstrip("[")
                    val1[0] = val1[0].replace(", ","")
                    val1[0] = val1[0].replace("'","")
                    report += val1[0]+";"+entradaAux+";(q, "+actual[0]+", "+actual[0]+"; q,"+alpha+")\n"
                    entradaAux = entradaAux[1:len(entradaAux)]
                    
                       
                    pila[0].pop()
                    it += 1
                else:  
                    respuestas[0].append("La cadena es invalida")
                    report +=";"+";Invalida"
                    respuestas[0].append(report) 
                       
                    return respuestas[0] 
            else:
                   
                for transicion in automata.transiciones:
                    if transicion.lecturaPila == actual[0]:
                        noTransiciones[0].append(transicion)

                if len(noTransiciones[0]) == 0:
                    respuestas[0].append("La cadena es invalida")
                    report +=";"+";Invalida"
                    respuestas[0].append(report) 
                       
                    return respuestas[0] 
                elif len(noTransiciones[0]) == 1:
                    val1 = [str(pila[0]).rstrip("]")]
                    val1[0] = val1[0].lstrip("[")
                    val1[0] = val1[0].replace(", ","")
                    val1[0] = val1[0].replace("'","")
                    val2 = [noTransiciones[0][0].guardarEnPila.split(" ")]

                    pila[0].pop()
                    cambio = pilaNoTerminales[0].pop(len(pilaNoTerminales[0])-1)

                    for val in reversed(val2[0]):
                        pila[0].append(val)
                        if val.islower() == True or val.isdigit() == True:
                               
                            idenTer += 1
                        else:
                            pilaNoTerminales[0].append("nt"+str(idenNoTer) )
                               
                            idenNoTer += 1
                
                    idenAux += 1

                    val2 = [str(val2[0]).rstrip("]")]
                    val2[0] = val2[0].lstrip("[")
                    val2[0] = val2[0].replace(", ","")
                    val2[0] = val2[0].replace("'","")
                    report += val1[0]+";"+entradaAux+";"+"(q, "+alpha+", "+actual[0]+"; q,"+val2[0]+")\n"
                else:
                    val1 = [str(pila[0]).rstrip("]")]
                    val1[0] = val1[0].lstrip("[")
                    val1[0] = val1[0].replace(", ","")
                    val1[0] = val1[0].replace("'","")

                    aux = []
                    pila[0].pop()
                    cambio = pilaNoTerminales[0].pop(len(pilaNoTerminales[0])-1)
                    for valor in noTransiciones[0]:
                        aux = valor.guardarEnPila.split(" ")
                        if aux[0] == entrada[it]:
                            auxis[0] = True
                            break
                    for val in reversed(valor.guardarEnPila.split(" ")):
                        pila[0].append(val)
                        if val.islower() == True or val.isdigit() == True:
                               
                            idenTer += 1
                        else:
                            pilaNoTerminales[0].append("nt"+str(idenNoTer))
                               
                            idenNoTer += 1
                
                    idenAux += 1

                    val2 = [str(aux).rstrip("]")]
                    val2[0] = val2[0].lstrip("[")
                    val2[0] = val2[0].replace(", ","")
                    val2[0] = val2[0].replace("'","")
                    report += val1[0]+";"+entradaAux+";"+"(q, "+alpha+", "+actual[0]+"; q,"+val2[0]+")\n"
        else:
            break

       
       
    if len(pila[0]) == 1 and it == len(entrada):
        report += "#;"+entradaAux+";(q, "+alpha+", #; f, "+alpha+")\n"
        report += ";"+";Aceptacion"
        respuestas[0].append("La cadena es valida")
        respuestas[0].append(report)
           
        return respuestas[0]
    else:
        for valor in pila[0]:
            if valor.islower() == True or valor.isdigit() == True:
                respuestas[0].append("La cadena es invalida")
                report +=";"+";Invalida"
                respuestas[0].append(report)
                   
                return respuestas[0]

        while True:
            actual = [pila[0][len(pila[0])-1]]
            noTransiciones = [[]]
            if pila[0][len(pila[0])-1] != "#":
                if pila[0][len(pila[0])-1] == "epsilon":
                    val1 = [str(pila[0]).rstrip("]")]
                    val1[0] = val1[0].lstrip("[")
                    val1[0] = val1[0].replace(", ","")
                    val1[0] = val1[0].replace("'","")
                    report += val1[0]+";"+entradaAux+";(q, "+actual[0]+", "+actual[0]+"; q,"+alpha+")\n"
                    pila[0].pop()
                else:
                    for transicion in automata.transiciones:
                        if transicion.lecturaPila == actual[0]:
                            noTransiciones[0].append(transicion)

                    if len(noTransiciones[0]) == 0:
                        respuestas[0].append("La cadena es invalida")
                        report +=";"+";Invalida"
                        respuestas[0].append(report)
                           
                        return respuestas[0]
                    else:
                        val1 = [str(pila[0]).rstrip("]")]
                        val1[0] = val1[0].lstrip("[")
                        val1[0] = val1[0].replace(", ","")
                        val1[0] = val1[0].replace("'","")
                        auxi = False
                        
                        aux = []
                        pila[0].pop()
                        cambio = pilaNoTerminales[0].pop(len(pilaNoTerminales[0])-1)

                        for valor in noTransiciones[0]:
                            aux = valor.guardarEnPila.split(" ")
                            if aux[0] == "epsilon":
                                auxis[0]= False
                                auxi = True
                                break
                        if auxi == False:
                            auxis[0]= True
                            break
                        for val in reversed(valor.guardarEnPila.split(" ")):
                            pila[0].append(val)
                            if val.islower() == True or val.isdigit() == True:
                                   
                                idenTer += 1
                            else:
                                pilaNoTerminales[0].append("nt"+str(idenNoTer))
                                   
                                idenNoTer += 1

                        idenAux += 1
                        
                        val2 = [str(aux).rstrip("]")]
                        val2[0] = val2[0].lstrip("[")
                        val2[0] = val2[0].replace(", ","")
                        val2[0] = val2[0].replace("'","")
                        report += val1[0]+";"+entradaAux+";"+"(q, "+alpha+", "+actual[0]+"; q,"+val2[0]+")\n"
            else:
                break
        
        if len(pila[0]) == 1:
            report += "#;"+entradaAux+";(q, "+alpha+", #; f, "+alpha+")\n"
            report += ";"+";Aceptacion"
            respuestas[0].append("La cadena es valida")
            respuestas[0].append(report)
               
            return respuestas[0]
        else:
            respuestas[0].append("La cadena es invalida")
            report +=";"+";Invalida"
            respuestas[0].append(report)
               
            return respuestas[0]

initalScreen()
Menu()
