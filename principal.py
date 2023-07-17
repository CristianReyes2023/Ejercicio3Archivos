import os
import reportes

if __name__=="__main__":
    isAddPrincipal=True
    while(isAddPrincipal):
        print("+","-"*55,"+")
        print("|{:^16}{}{:^15}|".format("","MENU PRINCIPAL DE REPORTES",""))
        print("+","-"*55,"+")
        print("1. Gestion de reportes\n2. Salir.")
        opcion=int(input("Ingresa opcion: "))
        if(opcion==1):
            reportes.LoadInfoReportes()
            reportes.MainMenu()
        if(opcion==2):
            pass
        else:
            print("Opción no valida, ingresa nuevamente una opción")
            os.system('pause')
            os.system('cls')