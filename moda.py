
lista1=[1,2,3,4,3,3,3,4,5,2,3,1,4,4,4,5,5,5,5,5]#lista de numeros enteros o float
"""
En esta funcion verificamos que es una lista de floats o numeros enteros
"""
def verificacion(lista1):
    if isinstance(lista1,list):
        if all(isinstance(lista1,int or float)):
            return lista1
        else:
            TypeError('tienen que ser o enteros o float los valores de la lista')
    else:
        SyntaxError('tenemos que escribir una lista')
"""
Aqui convertimos toda las listas en float para que sea mas sencillo comprobarlo
"""
def convertir_float(lista1):
    lista1=list(map(lambda x:float(x),lista1))

"""
Comprobamos si ya a sido verificado si o no o si no lo verificamos
"""
def Comprovacion(lista1):
    if verificacion(lista1)==0:
        return ValueError('tiene que ser una lista de numeros enteros o float')
    elif verificacion(lista1)==1:
        return convertir_float(lista1)
"""
Finalmente esta funcion crea un dicionario donde creamos el dicionario con clave del numero
y sus valores son las veces que aparece el numero en la lista
"""
def check_moda(lista1):
    moda={}
    for i in range(len(lista1)):
        if lista1[0] not in moda.keys():
            moda[lista1[0]]=+1
            del lista1[0]
        elif lista1[0] in moda.keys():
            moda[lista1[0]]+=1
            del lista1[0]
    mas=max(moda.values())#el valor maximo en el dicionario
    #Este for busca la clave que esta asociado el valor mas repetido
    for k,v in moda.items():
        if v==mas:
            return k
"""
Alfinal, imprimimos la moda de la lista
"""
print("La moda es: ",check_moda(lista1))
#la complejidad temporal es de big O(n) y tambien theta y omega es N. Ya que tenemos que recorer la lista de N elementos. 