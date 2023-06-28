import numpy as np
import random

tipo=[]
patente=[]
marca=[]
precio=[]
multa_monto=[]
multa_fecha=[]
fecha_registro=[]
nombre_duenio=[]



def menu():
  print("1: Grabar datos")
  print("2: Buscar datos")
  print("3: Imprimir certificado")
  print("4: Si desea salir ")

bandera=True
convalidador=True
convalidador2=True
convalidador3=True
a=0
b=0
i=0
aumento=0


while (bandera==True):
  menu()
  opcion=int(input("INGRESE LA OPCIÓN QUE DESEA: "))    
  if opcion==1:

    tipo.append(input("Ingrese el tipo de vehiculo: "))

    while convalidador==True:
      patente.append(input("Ingrese la patente del vehiculo: "))
      if (len(patente[a])==6):
        convalidador=False
      else:
        print("\n\n\nVuelva a ingresar la patente, tiene que ser de 6 digitos")  

    while convalidador2==True:
      marca.append(input("Ingrese la marca del vehiculo: "))
      if(len(marca[a])>=2 and len(marca[a])<15):
        convalidador2=False
      else:
        print("\n\n\nPorfavor, vuelva a ingresar la marca del vehiculo")  
 
    while convalidador3==True:
      precio.append(int(input("Ingrese el valor del vehiculo(debe de ser mayor a 5 millones): ")))
      if (precio[a]>=5000000):
        convalidador3=False
      else:
        print("\n\n\nVuelva a ingresar el precio, recuerde que debe de ser superior a 5 millones: ")

    multa_monto.append(int(input("Ingrese el monto de la multa, y si no tiene ponga 0: " )))
    multa_fecha.append(input('Ingrese la fecha de la multa con "" y si no tiene multa ingrese 0: '))
    fecha_registro.append(input("Ingrese la fecha de registro del vehiculo: "))
    nombre_duenio.append(input("Ingrese el nombre del dueño del vehiculo: "))
    a=+1

  if opcion==2:
    buscar=input("INGRESE LA PATENTE DEL VEHICULO QUE DESEA BUSCAR: ")
    for i in patente:
      if i==buscar:
        print("TIPO DE VEHICULO: ", tipo[b])
        print("PATENTE: ", patente[b])
        print("MARCA: ", marca[b])
        print("VALOR: ", precio[b])

        if(multa_monto[b]==0 and multa_fecha[b]==0):
          print("No presenta multas")
        else:
          print("VALOR MULTA: ", multa_monto[b])
          print("FECHA MULTA: ", multa_fecha[b])
        print("FECHA REGISTRO: ", fecha_registro[b])
        print("REPRESENTANTE LEGAL: ", nombre_duenio[b])
      else:
        print("no se encuentra registro de ese vehiculo/matricula")
        b+=1
        break
        
    else:
      c=+1

    
  if opcion==3:
    certificados = ["Emisión de contaminantes", "Anotaciones vigentes", "Multas"]
    certificado = random.choice(certificados)
    for i in range(len(patente)):
        certificado = random.choice(certificados)
        monto_aleatorio = random.randint(1500, 3500)
        print("Certificado:", certificado)
        print("PATENTE:", patente[i])
        print("NOMBRE DUEÑO:", nombre_duenio[i])
        print("MONTO:", monto_aleatorio)
        print("-----------------------------------")


  if opcion==4:
    print("PROGRAMA HECHO POR CAMILA MANCILLA VERSION 99999, (porque no me ejecutaba)")
    bandera=False
  