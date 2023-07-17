import os
import core
import random
from datetime import datetime
diccReportes = {}

def LoadInfoReportes():
    global diccReportes
    if(core.checkfile('reportes.json') == True):
        diccReportes=core.LoadInfo('reportes.json')
    else:
        diccReportes=core.CrearInfo('reportes.json',diccReportes)

def MainMenu():
    diccReportes = core.LoadInfo('reportes.json')
    os.system('cls') and os.system('clear')
    isAddReporte=True
    print("+","-"*55,"+")
    print("|{:^19}{}{:^19}|".format("","GESTION DE REPORTES",""))
    print("+","-"*55,"+")
    print("1. Agregar reporte\n2. Buscar reporte.\n3. Editar reporte.\n4. Eliminar reporte.\n5. Menú principal")
    opcion=int(input("Ingresa opcion: "))
    if(opcion==1):
        os.system('cls') and os.system('clear')
        print("+","-"*55,"+")
        print("|{:^20}{}{:^19}|".format("","AGREGAR DE REPORTE",""))
        print("+","-"*55,"+")
        reporteNumero = str(len(diccReportes)+1)
        idTrainer = str(random.randint(1,10000)).zfill(5)
        nombreTrainer=input('Ingresar nombre trainer: ').upper()
        emailPersonal = input("Ingresar email personal: ")
        emailCorporativo = input("Ingresar email corporativo: ")
        telefonoMovil = input("Ingresar telefono movil: ")
        telefonoResidencia = input("Ingresar telefono de la residencia: ")
        telefonoEmpresa = input("Ingresar telefono de la empresa: ")
        os.system('cls') and os.system('clear')
        print('DETALLE DEL REPORTE')
        print('Categoria del daño:','1. Hardware','2. Software',sep='\n')
        isSearch = True
        while isSearch:
            try:
                opcion = int(input("Ingresa la categoría del daño: "))
                if opcion == 1:
                    categoria = 'HARDWARE'
                    isSearch=False
                elif opcion == 2:
                    categoria = 'SOFTWARE'
                    isSearch=False
                else:
                    print("Opción incorrecta... Ingresa una nuevamente.")
            except Exception:
                print('Opción incorrecta... Ingresa una nuevamente.')
                isSearch=True
        print('Tipo de insidencia:','1. Leve','2. Moderado','3. Critico',sep='\n')
        isSearch = True
        while isSearch:
            try:
                opcion=int(input('Tipo de insidencia: '))
                if (opcion==1):
                    insidencia='LEVE'
                    isSearch=False
                elif(opcion==2):
                    insidencia='MODERADO'
                    isSearch=False
                elif (opcion==3):
                    insidencia='CRITICO'
                    isSearch=False
                else:
                    print("Opción incorrecta... Ingresa una nuevamente.")
            except Exception:
                print('Opción incorrecta... Ingresa una nuevamente.')
                isSearch=True
        print('Elemento Afectado','1. Computadores','2. Teclados','3. Mouse','4. Diademas','5. Otro: ',sep='\n')
        isSearch = True
        while isSearch:
            try:
                opcion=int(input('Tipo de insidencia: '))
                if (opcion==1):
                    elementoAfectado='COMPUTADORES'
                    isSearch=False
                elif(opcion==2):
                    elementoAfectado='TECLADOS'
                    isSearch=False
                elif (opcion==3):
                    elementoAfectado='MOUSE'
                    isSearch=False
                elif(opcion==4):
                    elementoAfectado='DIADEMAS'
                    isSearch=False
                elif (opcion==5):
                    elementoAfectado= input('Ingresa el nombre del elemento afectado: ')
                    isSearch=False
                else:
                    print("Opción incorrecta... Ingresa una nuevamente.")
            except Exception:
                print('Opción incorrecta... Ingresa una nuevamente.')
                isSearch=True
        descripcion = input('Ingresa una breve descripcion: ').upper()
        fecha= datetime.now().strftime("%H:%M:%S %d-%m-%Y")        
        os.system('cls') and os.system('clear')
        print('LUGAR DE AFECTACIÓN','1. Area Training','2. Area Review 1','3. Area Review 3','4. Otro: ',sep='\n')
        isSearch = True
        while isSearch:
            try:
                opcion=int(input("Ingrese opción: "))
                if (opcion==1):
                    area='AREA TRAINING'
                    print('1. APOLO','2. ARTEMIS','3. SPUTNIK','4. SKYLAB',sep='\n')
                    opcionSalon=int(input("Ingresa salon:"))
                    if(opcionSalon==1):
                        salon='APOLO'
                        isSearch=False
                    elif(opcionSalon==2):
                        salon='ARTEMIS'
                        isSearch=False
                    elif(opcionSalon==3):
                        salon='SPUTNIK'
                        isSearch=False
                    elif(opcionSalon==4):
                        salon='SKYLAB'
                        isSearch=False
                elif(opcion==2):
                    area='AREA REVIEW 1'
                    salon='CORVUS'
                    isSearch=False
                elif (opcion==3):
                    area='AREA REVIEW 2'
                    salon='ENDOR'
                    isSearch=False
                elif(opcion==4):
                    area=input('Ingresa el nombre del area: ')
                    salon="Area Comun"
                    isSearch=False
                else:
                    print("Opción incorrecta... Ingresa una nuevamente.")
                    isSearch=True
            except Exception:
                print('Opción incorrecta... Ingresa una nuevamente.')
                isSearch=True
        idEquipo=input('Ingresa el Id del equipo afectado: ')
        reporte = {
            'reporteNumero':reporteNumero,
            'fecha':fecha,
            'idTrainer':idTrainer,
            'nombreTrainer':nombreTrainer,
            'emailPersonal':emailPersonal,
            'emailCorporativo':emailCorporativo,
            'telefonoMovil':telefonoMovil,
            'telefonoResidencia':telefonoResidencia,
            'telefonoEmpresa':telefonoEmpresa,
            'detalleReporte':{
                'categoria':categoria,
                'insidencia':insidencia,
                'elementoAfectado':elementoAfectado,
                'descripcion':descripcion
            },
            'lugarReporte':{
                'area':area,
                'salon':salon,
                'idEquipo':idEquipo
            }
        }
        diccReportes.update({f"{reporteNumero}":reporte})
        core.CrearInfo('reportes.json',diccReportes)
        os.system('pause')
        MainMenu()
    if(opcion==2):
        os.system('cls') and os.system('clear')
        print("+","-"*55,"+")
        print("|{:^19}{}{:^19}|".format("","BUSCAR REPORTE",""))
        print("+","-"*55,"+")
        print("Busca y selecciona el numero de reporte que necesitas editar: ")
        for i in diccReportes:
            print(f"Reporte #:{i} {diccReportes[i]}")
        numeroReporte=input("Ingresa el numero del reporte: ")
        print(f"La información del reporte es:\n{diccReportes[numeroReporte]}")
        os.system('pause')
    if(opcion==3):
        os.system('cls') and os.system('clear')
        print("+","-"*55,"+")
        print("|{:^19}{}{:^19}|".format("","EDITAR REPORTE",""))
        print("+","-"*55,"+")
        print("Busca y selecciona el numero de reporte que necesitas editar: ")
        for i in diccReportes:
            print(f"Reporte #:{i} {diccReportes[i]}")
        numeroReporte=input("Ingresa el numero del reporte: ")
        if numeroReporte in diccReportes:
            nombreTrainer = input("Ingresa el nuevo nombre or Enter para continuar: ").upper() or diccReportes[numeroReporte].get('nombreTrainer')
            emailPersonal = input("Ingresa el email personal or Enter para continuar: ") or diccReportes[numeroReporte].get('emailPersonal')
            emailCorporativo = input("Ingresa el nuevo email corporativo or Enter para continuar: ") or diccReportes[numeroReporte].get('emailCorporativo')
            telefonoMovil = input("Ingresa el nuevo telefono movil or Enter para continuar: ") or diccReportes[numeroReporte].get('telefonoMovil')
            telefonoResidencia = input("Ingresa el nuevo telefono de residencia or Enter para continuar: ") or diccReportes[numeroReporte].get('telefonoResidencia')
            telefonoEmpresa = input("Ingresa el nuevo telefono de la empresa or Enter para continuar: ").upper() or diccReportes[numeroReporte].get('telefonoEmpresa')
            # nombreTrainer = input("Ingresa el nuevo nombre or Enter para continuar: ").upper() or diccReportes[numeroReporte].get('nombreTrainer')
            # nombreTrainer = input("Ingresa el nuevo nombre or Enter para continuar: ").upper() or diccReportes[numeroReporte].get('nombreTrainer')
        else:
            print("Ingresaste un valor incorrecto.")
        reporte = {
            'reporteNumero':diccReportes[numeroReporte].get('reporteNumero'),
            'fecha':diccReportes[numeroReporte].get('fecha'),
            'idTrainer':diccReportes[numeroReporte].get('idTrainer'),
            'nombreTrainer':nombreTrainer,
            'emailPersonal':emailPersonal,
            'emailCorporativo':emailCorporativo,
            'telefonoMovil':telefonoMovil,
            'telefonoResidencia':telefonoResidencia,
            'telefonoEmpresa':telefonoEmpresa,
            'detalleReporte':{
                'categoria':diccReportes[numeroReporte]['detalleReporte'].get('categoria'),
                'insidencia':diccReportes[numeroReporte]['detalleReporte'].get('insidencia'),
                'elementoAfectado':diccReportes[numeroReporte]['detalleReporte'].get('elementoAfectado'),
                'descripcion':diccReportes[numeroReporte]['detalleReporte'].get('descripcion')
            },
            'lugarReporte':{
                'area':diccReportes[numeroReporte]['lugarReporte'].get('area'),
                'salon':diccReportes[numeroReporte]['lugarReporte'].get('salon'),
                'idEquipo':diccReportes[numeroReporte]['lugarReporte'].get('idEquipo')
            }
        }
        diccReportes.update({f"{numeroReporte}":reporte})
        core.CrearInfo('reportes.json',diccReportes)
    if(opcion==4):
        os.system('cls') and os.system('clear')
        print("+","-"*55,"+")
        print("|{:^19}{}{:^19}|".format("","EDITAR REPORTE",""))
        print("+","-"*55,"+")
        print("Busca y selecciona el numero de reporte que necesitas editar: ")
        for i in diccReportes:
            print(f"Reporte #:{i} {diccReportes[i]}")
        numeroReporte=input("Ingresa el numero del reporte a eliminar: ")
        diccReportes.pop(numeroReporte)
        core.EditInfo('reportes.json',diccReportes)
        os.system('pause')
        MainMenu()
    if(opcion==5):
        isAddReporte=False
    if (isAddReporte):
        MainMenu()