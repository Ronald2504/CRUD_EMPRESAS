import os

ANCHO = 20

dic_empresas = {}

def verificar_y_crear_archivo(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            file.write("123456789,PEDRITO SAC,pedro_sac@gmail.com\n")
        print(f"Archivo '{file_name}' creado automáticamente.")

def cargar_empresas(file_name):
    verificar_y_crear_archivo(file_name)
    file = open(file_name,'r')
    str_empresas = file.read()
    file.close()
    lista_empresas = str_empresas.splitlines()
    for str_fila in lista_empresas:
        lista_fila = str_fila.split(',')
        dic_fila = {
            'razon_social':lista_fila[1],
            'direccion':lista_fila[2]
        }
        dic_nueva_empresa = {
            lista_fila[0]: dic_fila
        }
        dic_empresas.update(dic_nueva_empresa)
        
def grabar_empresas(file_name):
    str_empresas = ""
    for empresa_clave, empresa_valor in dic_empresas.items():
        str_empresas += empresa_clave
        for registro_clave, registro_valor in empresa_valor.items():
            str_empresas += ',' + registro_valor
            if registro_clave == 'direccion':
                str_empresas += '\n'

    
    fsalida = open(file_name,'w')
    fsalida.write(str_empresas)
    fsalida.close()
    



def mostrar_mensaje(texto):
    print("*" * ANCHO + "*" * ANCHO)
    if texto != " ":
        print(" " * 10 + texto)
        print("*" * ANCHO + "*" * ANCHO)

def menu():
    mostrar_mensaje("GESTIÓN DE EMPRESAS")
    print("""
          [1] REGISTRAR EMPRESA
          [2] MOSTRAR EMPRESA
          [3] ACTUALIZAR EMPRESA
          [4] ELIMINAR EMPRESA
          [5] SALIR
          """)
    mostrar_mensaje(" ")

def registrar():
    mostrar_mensaje("[1] REGISTRAR EMPRESA")
    ruc = input("RUC          : ")
    razon_social = input("RAZON SOCIAL : ")
    direccion = input("DIRECCION    : ")
    dic_nueva_empresa = {
        ruc: {
            'razon_social': razon_social,
            'direccion': direccion,
        }
    }
    dic_empresas.update(dic_nueva_empresa)

def mostrar():
    mostrar_mensaje("[2] MOSTRAR EMPRESAS")
    for ruc, datos in dic_empresas.items():
        print(f"RUC          : {ruc}")
        print(f"Razon Social : {datos['razon_social']}")
        print(f"Direccion    : {datos['direccion']}")
        mostrar_mensaje(" ")

def actualizar():
    mostrar_mensaje("[3] ACTUALIZAR EMPRESA")
    ruc = input("INGRESE RUC DE LA EMPRESA A ACTUALIZAR: ")
    if ruc in dic_empresas:
        print(f"EMPRESA A ACTUALIZAR: {dic_empresas[ruc]['razon_social']}")
        nueva_razon_social = input('RAZON SOCIAL : ')
        nueva_direccion = input('DIRECCION    : ')
        dic_nueva_empresa = {
            ruc: {
                'razon_social': nueva_razon_social,
                'direccion': nueva_direccion,
                }
            }
        dic_empresas.update(dic_nueva_empresa)
        print("EMPRESA ACTUALIZADA CON EXITO")

def eliminar():
    mostrar_mensaje("[4] ELIMINAR EMPRESA")
    ruc = input("INGRES EL RUC DE LA EMPRESA A ELIMINAR : ")
    if ruc in dic_empresas:
        dic_empresas.pop(ruc)
        print("EMPRESA ELIMINADO")
    else:
        print("NO SE ENCONTRO LA EMPRESA")