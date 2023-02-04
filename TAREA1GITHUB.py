#PUNTO 1
mat = [[11, 23, 76, 34, 11],
       [14, 30, 92, 30, 101],
       [12, 45, 58, 92,22],
       [74, 56, 49, 56, 100],
       [99, 5, 28, 47, 99]]

def verificarDiagonales(matriz):
  DiagonalPrincipal = 0
  DiagonalOpuesta = -1
  for i in matriz:
    if i[DiagonalPrincipal] != i[DiagonalOpuesta]:
      return False
    DiagonalPrincipal += 1
    DiagonalOpuesta -= 1
  return True

#PUNTO 2
def esCapicua(lista):
  ubicacionPrincipal = 0
  ubicacionOpuesta = -1
  for i in lista:
    if lista[ubicacionPrincipal] != lista[ubicacionOpuesta]: return False
    ubicacionPrincipal += 1
    ubicacionOpuesta -= 1
  return True

#PUNTO 3
def diferenciaListas(listaA, listaB):
  listaResultado = []
  for i in listaA:
    if i in listaB:
      listaB.remove(i)
      continue
    listaResultado.append(i)
  return listaResultado


def leerImprimir():
  procesar = int(input())
  for e in range(procesar):
    inputA = list(input().split())
    inputB = list(input().split())
    listaNuevaA = []
    for i in range(1, int(inputA[0])+1):
      listaNuevaA.append(int(inputA[i]))
    listaNuevaB = []
    for j in range(1, int(inputB[0])+1):
      listaNuevaB.append(int(inputB[j]))
    
    listaResultado = diferenciaListas(listaNuevaA, listaNuevaB)
    datosAImprimir = ', '.join(str(dato) for dato in listaResultado)
    print(datosAImprimir)

leerImprimir()


#PUNTO 4
def funcionAuxiliar(n):
  return 0 if n == 0 else int(n % 10) + funcionAuxiliar(int(n / 10))

def mostrarPrimos(N):
  listaPrimos = []
  print(f"ESTOS SON LOS NUMEROS PRIMOS ENTRE 1 Y {N}:")
  for i in range(1, N):
    if i > 1:
      for j in range(2, int(i/2)+1):
        if (i % j) == 0:
          break
      else:
        listaPrimos.append(i)
  for k in listaPrimos:
    print(f"--> {k}")

  SumaPrimos = []
  print(f"NUMEROS ENTRE 1 Y {N} DONDE SU RESULTADO TAMBIEN ES PRIMO:")
  for i in listaPrimos:
    ejecutable = funcionAuxiliar(i)
    for j in range(2, int(ejecutable/2)+1):
      if (ejecutable % j) == 0:
        break
    else:
      SumaPrimos.append(i)
  Imprimir = ', '.join(str(dato) for dato in SumaPrimos)
  print(Imprimir)

mostrarPrimos(100)

#PUNTO 5


matriz = [[1, 0, 0, 0, 0, 4, 0, 5],
          [0, 0, 0, 0, 0, 0, 4, 7],
          [2, 2, 0, 0, 9, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 8, 1, 0, 7, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [3, 0, 0, 0, 0, 6, 0, 2],
          [4, 4, 7, 0, 0, 0, 0, 0],
          [0, 9, 0, 8, 0, 7, 0, 6]]
disp = {0 : [(0, 1), (5, 4), (7, 5)],
        1 : [(6, 4), (7, 7)],
        2 : [(0, 2), (1, 2), (4, 9), (6, 1)],
        4 : [(2, 8), (3, 1), (5, 7)],
        6 : [(0, 3), (5, 6), (7, 2)],
        7 : [(0, 4), (1, 4), (2, 7)],
        8 : [(1, 9), (3, 8), (5, 7), (7, 6)]}


def sumarValoresMatriz(matrizDisp, listaParejas):
  Acumulado = 0
  for i in listaParejas:
    clave = i[0]
    ubicacion = i[1]
    if clave in matrizDisp:
      estructura = matrizDisp[clave]
      for j in estructura:
        if j[0] == ubicacion:
          Acumulado += j[1]
    else:
      Acumulado += 0
  return Acumulado
  