# - *- coding: utf- 8 - *-
import os
import time
import random
import platform



Titulo = ('///////=====================================================///////\n'
          '///////                     WELCOME TO                      ///////\n'
          '///////                                                     ///////\n'
          '///////                  THE GAME OF LIFE                   ///////\n'
          '///////=====================================================///////\n'
          '///////              Presentado por: Juanita Gomez          ///////\n'
          '///////=====================================================///////\n');

separator = ('\n///////=====================================================///////')

footer = ('Gracias por Jugar\nPara finalizar el juego oprima (ctrl + .)\nHasta la proxima\n')




if platform.system() == 'Darwin' or platform.system() == 'Linux' :
   os.system('clear')
elif platform.system() == 'win32' :
   os.system('cls')

print(Titulo)

r = input('Determine la probabilidad de que una célula inicie viva: ')
m = input('Determine el tamaño de la matriz cuadrada que desea usar: ')
if m > 35 :
   print('Tenga en cuenta que para ese tamaño de matriz puede ser necesario \nreajustar la pantalla')
   time.sleep(2)
n=0
a=str(' ◼︎')
b=str('  ')
#Creacion de matriz
matriz = [[0 for x in range(m)] for y in range(m)] 
i=0;
for i in range(0,m):
    for j in range(0,m):
        y=random.randint(0,100)
        if (y>r):
            matriz[i][j]=b
        else:
            matriz[i][j]=a
            
#Evolucion de la matriz (Ciclo infinito)
while 1>0:
    
    #Imprimir a Consola
    if platform.system() == 'Darwin' or platform.system() == 'Linux' :
       os.system('clear')
    elif platform.system() == 'win32' :
       os.system('cls')

    print (Titulo)
    
    print('Ud escogio una probabilidad inicial de vida del: ' + str(r));
    print('Ud escogio una matriz cuadrada de tamano: ' + str(m));
    
    print (separator + '\n')
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
          for row in matriz]))
    print (separator + '\n')
    print ('Ud lleva ' + str(n) + ' pasos')
    print (footer)

    n += 1
    time.sleep(20)
    
    #Cada una de las iteraciones del programa 
    for i in range(0,m):
        j=0
        for j in range(0,m):
            v=0;
            if i+1<m:
                if matriz[i+1][j]==a:
                    v=v+1
                if j+1<m:
                    if matriz[i+1][j+1]==a:
                        v=v+1
                if j-1>=0:
                    if matriz[i+1][j-1]==a:
                        v=v+1                       
            if i-1>=0:
                if matriz[i-1][j]==a:
                    v=v+1
                if j+1<m:
                    if matriz[i-1][j+1]==a:
                        v=v+1
                if j-1>=0:
                    if matriz[i-1][j-1]==a:
                        v=v+1                   
            if j+1<m:
                if matriz[i][j+1]==a:
                    v=v+1              
            if j-1>=0:
                if matriz[i][j-1]==a:
                        v=v+1

            #Encontrar celulas vivas
            if matriz[i][j]==a:

                #1Una celula viva con menos de dos vecinos vivos muere
                if v<2:
                    matriz[i][j]=b
                #2Una celula viva con 2 o 3 vecinos vivos permanece en su estado
                if (v==2 or v==3):
                    matriz[i][j]=a
                #3Una celula viva con mas de 3 vecinos muere
                if v>3:
                    matriz[i][j]=b

            #Encontrar celulas muertos
            if matriz[i][j]==b:
 
                #4Una celula muerta con exactamente 3 vecinos vivos se convierte en viva
                if v==3:
                    matriz[i][j]=a

   
    

