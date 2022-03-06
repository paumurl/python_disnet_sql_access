# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 11:54:32 2020

@author: paula
"""
import sys
from tabulate import tabulate #para imprimir tablas
import os #para limpiar la pantalla
import mysql.connector #para acceder a mysql
from mysql.connector import errorcode #para gestión de errores

def limpiar_pantalla(): #función para limpiar la pantalla, ya sea Windows o Linux
    os.system("cls||clear")
    print("\n")

def menu_inicial(): #imprimimmos el menu principal
    limpiar_pantalla()
    print("=============================================================================================\n\nBienvenid@. Está usted conectad@ a la Base de Datos DISNET_DRUGSLAYER.\nSeleccione una de las siguientes opciones:\n=============================================================================================\n")
    print("\t1: Información general de la Base de Datos")
    print("\t2: Información de los fármacos")
    print("\t3: Información de las enfermedades")
    print("\t4: Información de los efectos fenotípicos")
    print("\t5: Información de los targets")
    print("\t6: Borrados")
    print("\t7: Inserciones")
    print("\t8: Modificaciones")
    print("\t9: Salir")
    opcion=input("\nIntroduzca el número de la opción que desea realizar >> ") #pedimos qué opción para luego redirigir
    
    if opcion=="1": #inicializamos el menú que corresponda con el número con funciones
        while True: #para que repite y nos muestre el mismo menú por si el usuario quiere hacer otro apartado
            menu_1() #si no, podrá volver al menú inicial pulsando 0 (más adelante)
    elif opcion=="2":
        while True:
            menu_2()
    elif opcion=="3":
        while True:
            menu_3()
    elif opcion=="4":
        while True:
            menu_4() 
    elif opcion=="5":
        while True:
            menu_5()
    elif opcion=="6":
        while True:
            menu_6()
    elif opcion=="7":
        while True:
            menu_7()
    elif opcion=="8":
        while True:
            menu_8()
    elif opcion=="9":
        db.close()
        print("\n\n\\\\\\\\\ CONEXIÓN CERRADA.") 
        sys.exit()
        
    else: #si no se introducen los números adecuados
        limpiar_pantalla() 
        print("INPUT NO VÁLIDO. FINALIZACIÓN DEL PROGRAMA.")
        db.close()
        print("\n\n\\\\\\\\\ CONEXIÓN CERRADA.") 
        sys.exit()
        

def menu_1(): #definimos las funciones de los menús, en este caso el 1
    limpiar_pantalla() #limpiamos la pantalla e imprimimos el menu 1
    print("Ha seleccionado => Información general de la base de datos\n")
    print("a: Número total de cada uno")
    print("b: Primeras 10 instancias de cada uno")
    print("0: Volver atrás")
    opcion=input("\nIntroduzca el número/letra de la opción que desea realizar >> ")
    
    if opcion=="a":
        limpiar_pantalla()
        print("Ha seleccionado => Número total de cada uno\n")
        try: #probamos a obtener del número de instancias en cada una de las tablas en única tabla mediante subconsulta, hacemos tmb gestión de errores
            queryconteo="SELECT  (SELECT COUNT(*) FROM drug) AS NumDrugs,(SELECT COUNT(*) FROM disease) AS NumDiseases, (SELECT COUNT(*) FROM phenotype_effect) AS PhenoEff, (SELECT COUNT(*) FROM target) AS NumTargets"
            cursor.execute(queryconteo)                             
            headerconteo=[]
            for cd in cursor.description: #para guardar el header y mostrarlo luego en tabla
                headerconteo.append(cd[0])
            
            dataconteo = cursor.fetchall()
            print(tabulate(dataconteo, headerconteo, tablefmt='simple')) #impresión de la tabla
            input("\nPulse cualquier tecla para continuar >> ")
        
        except mysql.connector.Error as err: #gestión de errores en caso de que vaya algo mal
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")
        
        
    elif opcion=="b":        
        limpiar_pantalla()
        print("Ha seleccionado => Primeras 10 instancias de cada uno\n")
        try: #imprimimos las 10 primeras instancias de cada entidad por separado con las columnas que nos piden para facilitar la lectura
            print("DRUGS\n")
            querydrogas="select drug_id,drug_name,molecular_type,chemical_structure,inchi_key from drug where drug_id is not null and drug_name is not null and molecular_type is not null and chemical_structure is not null limit 10"
            cursor.execute(querydrogas)
            headerdrogas=[]
            for cd in cursor.description:
                headerdrogas.append(cd[0])
            datadrogas = cursor.fetchall()
            print(tabulate(datadrogas, headerdrogas, tablefmt='simple'))
            
            print("\n")
            print("DISEASES\n")
            queryenfermedades="select disease_id,disease_name from disease where disease_id is not null and disease_name is not null limit 10"
            cursor.execute(queryenfermedades)  
            headerenfermedades=[]
            for cd in cursor.description:
                headerenfermedades.append(cd[0])
            dataenfermedades = cursor.fetchall()
            print(tabulate(dataenfermedades, headerenfermedades, tablefmt='simple'))
            
            print("\n")
            print("PHENOTYPE EFFECTS\n")
            queryfenotipos="select phenotype_id,phenotype_name from phenotype_effect where phenotype_id is not null and phenotype_name is not null limit 10"
            cursor.execute(queryfenotipos)  
            headerfenotipos=[]
            for cd in cursor.description:
                headerfenotipos.append(cd[0])
            datafenotipos = cursor.fetchall()
            print(tabulate(datafenotipos, headerfenotipos, tablefmt='simple'))
            
            print("\n")
            print("TARGETS\n")
            querytargets="select target_id,target_name_pref,target_type,target_organism from target where target_id is not null and target_name_pref is not null and target_type is not null and target_organism is not null limit 10"
            cursor.execute(querytargets)  
            headertargets=[]
            for cd in cursor.description:
                headertargets.append(cd[0])
            datatargets = cursor.fetchall()
            print(tabulate(datatargets, headertargets, tablefmt='simple'))
            input("\nPulse cualquier tecla para continuar >> ")
        
        except mysql.connector.Error as err:
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")
    
        
    elif opcion=="0": #volvemos al menu inicial si el usuarios nos pide volver
        menu_inicial()

    else: #no es un input válido
        limpiar_pantalla() 
        print("INPUT NO VÁLIDO. FINALIZACIÓN DEL PROGRAMA.")
       
def menu_2():
    limpiar_pantalla()
    print("Ha seleccionado => Información de los fármacos\n")
    print("a: Información de un fármaco dado")
    print("b: Sinónimos de un fármaco dado")
    print("c: Código ATC de un fármaco dado")
    print("0: Volver atrás")
    opcion=input("\nIntroduzca el número/letra de la opción que desea realizar >> ")
    
    if opcion=="a":
        limpiar_pantalla()
        print("Ha seleccionado => Información de un fármaco dado\n")
        try: # nos da la información asociada a un código CHEMBL de un fármaco
            codigofarmaco=input("\nIntroduzca el código CHEMBL del fármaco del que quiere conocer más >> ")
            queryinfofarmaco="select drug_name,molecular_type,chemical_structure,inchi_key from drug where drug_id=%s"
            cursor.execute(queryinfofarmaco,(codigofarmaco,))                         
            headerinfofarmaco=[]
            for cd in cursor.description:
                headerinfofarmaco.append(cd[0]) #nuevamente guardamos la info del header 
            datainfofarmaco = cursor.fetchall()
            
            if cursor.rowcount==0: #si nos devuelve resultados vacíos
                print("\nLa Base de Datos no tiene almacenada ninguna información de dicho fármaco.")
                input("\nPulse cualquier tecla para continuar >> ")
            else: #imprimos la tabla si hay información
                print("\n")
                print(tabulate(datainfofarmaco, headerinfofarmaco, tablefmt='simple'))
                input("\nPulse cualquier tecla para continuar >> ")
               
        
        except mysql.connector.Error as err: #si algo va mal hacemos gestión de errores para imprimir el error
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")
    
        
    elif opcion=="b":
        limpiar_pantalla()
        print("Ha seleccionado => Sinónimos de un fármaco dado\n")
        try: #nombres sinónimos de un codigo chembl
            nombrefarmaco=input("\nIntroduzca el nombre del fármaco del que quiere conocer sus sinónimos >> ")
            querysinonimos="select synonymous.synonymous_name from synonymous,drug where drug.drug_name=%s and synonymous.drug_id=drug.drug_id"
            cursor.execute(querysinonimos,(nombrefarmaco,))                               
            datasinonimos = cursor.fetchall()
            if cursor.rowcount==0: #si el rowcount es 0 es que la consulta nos da resultados vacíos
                print("\nLa Base de Datos no tiene almacenada ninguna información de dicho fármaco.")
                input("\nPulse cualquier tecla para continuar >> ")
            else: #si hay información imprimimos
                print(tabulate(datasinonimos, tablefmt='simple'))
                print("\nSe han obtenido %s resultado(s).\n" %cursor.rowcount)
                input("Pulse cualquier tecla para continuar >> ")
        
        except mysql.connector.Error as err:
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")
    
   
    elif opcion=="c":
        limpiar_pantalla()
        print("Ha seleccionado => Código ATC de un fármaco dado\n")
        try: #para conocer el código ATC a partir del código CHEMBL del fármaco
            codigofarmaco=input("\nIntroduzca el código CHEMBL del fármaco del que quiere conocer su código ATC >> ")
            queryATC="select ATC_code_id from ATC_code where drug_id=%s"
            cursor.execute(queryATC,(codigofarmaco,))                               
            dataATC = cursor.fetchall()   
            if cursor.rowcount==0:
                print("\nLa Base de Datos no tiene almacenado ningún código ATC para dicho fármaco.")
                input("\nPulse cualquier tecla para continuar >> ")
            else:
                print(tabulate(dataATC, tablefmt='simple'))
                print("\nSe han obtenido %s resultado(s).\n" %cursor.rowcount)
                input("Pulse cualquier tecla para continuar >> ")
        
        except mysql.connector.Error as err:
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")
    
        
    elif opcion=="0":
        menu_inicial()
    
    else:
        limpiar_pantalla()
        print("INPUT NO VÁLIDO. FINALIZACIÓN DEL PROGRAMA.")
    
def menu_3():
    limpiar_pantalla()
    print("Ha seleccionado => Información de las enfermedades\n")
    print("a: Fármacos para una enfermedad")
    print("b: Fármaco y enfermedad con el mayor score de asociación")
    print("0: Volver atrás")
    opcion=input("\nIntroduzca el número/letra de la opción que desea realizar: ")
    
    if opcion=="a":
        limpiar_pantalla()
        print("Ha seleccionado => Fármacos para una enfermedad\n")
        try: #nos da los tratamientos para el nombre de una enfermedad
            nomenfermedad=input("\nIntroduzca el nombre de la enfermedad para mostrar sus fármacos >> ")
            querytratamiento="select drug.drug_id, drug.drug_name from drug,disease,drug_disease where disease.disease_name=%s and drug_disease.drug_id=drug.drug_id and disease.disease_id=drug_disease.disease_id"
            cursor.execute(querytratamiento,(nomenfermedad,))                         
            headertratamiento=[]
            for cd in cursor.description:
                headertratamiento.append(cd[0])       
            datatratamiento = cursor.fetchall()    
           
            if cursor.rowcount==0:
                print("\nLa Base de Datos no tiene almacenada ninguna información de dicho enfermedad.")
                input("\nPulse cualquier tecla para continuar >> ")
            
            else:
                print("\n")
                print(tabulate(datatratamiento, headertratamiento, tablefmt='simple'))
                print("\nSe han obtenido %s resultado(s).\n" %cursor.rowcount)
                input("Pulse cualquier tecla para continuar >> ")
        
        except mysql.connector.Error as err:
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")
    
    
    elif opcion=="b":
        limpiar_pantalla()
        print("Ha seleccionado => Fármaco y enfermedad con el mayor score de asociación\n")
        try: #seleccionamos la enfermedad con el mayor score
            querymaxasociacion="SELECT disease_name,drug_name,inferred_score FROM drug_disease,drug,disease WHERE drug_disease.disease_id=disease.disease_id AND drug_disease.drug_id=drug.drug_id ORDER BY inferred_score DESC LIMIT 1"
            cursor.execute(querymaxasociacion)
            headermaxasociacion=[]
            for cd in cursor.description:
                headermaxasociacion.append(cd[0])       
            datamaxasociacion = cursor.fetchall()    
            print(tabulate(datamaxasociacion, headermaxasociacion, tablefmt='simple')) #impresión de la tabla
            print("\n")
            input("Pulse cualquier tecla para continuar >> ")
        
        except mysql.connector.Error as err:
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")
    
    
    elif opcion=="0": #para volver al menu inicial
        menu_inicial()
    
    else:
        limpiar_pantalla()
        print("INPUT NO VÁLIDO. FINALIZACIÓN DEL PROGRAMA.")
        
    
def menu_4():
    limpiar_pantalla()
    print("Ha seleccionado => Información de los efectos fenotípicos\n")
    print("a: Indicaciones de un fármaco dado")
    print("b: Efectos secundarios de un fármaco dado")
    print("0: Volver atrás")
    opcion=input("\nIntroduzca el número/letra de la opción que desea realizar >> ")
    
    if opcion=="a":
        limpiar_pantalla()
        print("Ha seleccionado => Indicaciones de un fármaco dado")
        try: #hallamos los efectos secundarios metiendo el string INDICATION en execute
            codigofarmaco=input("\nIntroduzca el código CHEMBL del fáramaco del que se quieren conocer los efectos fenotípicos para los que se indica >> ")
            queryindicaciones="select phenotype_effect.phenotype_id,phenotype_effect.phenotype_name from phenotype_effect,drug_phenotype_effect where drug_phenotype_effect.drug_id=%s and drug_phenotype_effect.phenotype_type=%s and phenotype_effect.phenotype_id=drug_phenotype_effect.phenotype_id"
            cursor.execute(queryindicaciones,(codigofarmaco,"INDICATION",))
            headerindicaciones=[]
            for cd in cursor.description:
                headerindicaciones.append(cd[0])       
            dataindicaciones = cursor.fetchall()    
           
            if cursor.rowcount==0: #resultados vacíos
                print("\nLa Base de Datos no tiene almacenada ninguna información de dicho fármaco.")
                input("\nPulse cualquier tecla para continuar >> ")
            else:
                print("\n")
                print(tabulate(dataindicaciones, headerindicaciones, tablefmt='simple'))
                print("\nSe han obtenido %s resultado(s).\n" %cursor.rowcount)
                input("Pulse cualquier tecla para continuar >> ")
        
        except mysql.connector.Error as err:
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")
    
    elif opcion=="b":
        limpiar_pantalla()
        print("Ha seleccionado => Efectos secundarios de un fármaco dado\n")
        try: #hallamos los efectos secundarios metiendo el string SIDE EFFECT en execute
            codigofarmaco=input("\nIntroduzca el código CHEMBL del fáramaco del que se quieren conocer sus efectos secundarios >> ")
            querysecundarios="select phenotype_effect.phenotype_id,phenotype_effect.phenotype_name from phenotype_effect,drug_phenotype_effect where drug_phenotype_effect.drug_id=%s and drug_phenotype_effect.phenotype_type=%s and phenotype_effect.phenotype_id=drug_phenotype_effect.phenotype_id order by drug_phenotype_effect.score desc"
            cursor.execute(querysecundarios,(codigofarmaco,"SIDE EFFECT",))
            headersecundarios=[]
            for cd in cursor.description:
                headersecundarios.append(cd[0])       
            datasecundarios = cursor.fetchall() 
            
            if cursor.rowcount==0:
                print("\nLa Base de Datos no tiene almacenada ninguna información de dicho fármaco.")
                input("\nPulse cualquier tecla para continuar >> ")
            else:
                print("\n")
                print(tabulate(datasecundarios, headersecundarios, tablefmt='simple')) #imprimimos la tabla
                print("\nSe han obtenido %s resultado(s).\n" %cursor.rowcount)
                input("Pulse cualquier tecla para continuar >> ")
            
        except mysql.connector.Error as err:
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")

    elif opcion=="0":
        menu_inicial()
    
    else:
        limpiar_pantalla()
        print("INPUT NO VÁLIDO. FINALIZACIÓN DEL PROGRAMA")        
        
def menu_5():
    limpiar_pantalla()
    print("Ha seleccionado => Información de los targets\n")
    print("a: Nombre de las 20 primeras dianas de un tipo dado")
    print("b: Organismo al cual se asocian mayor número de dianas")
    print("0: Volver atrás")
    opcion=input("\nIntroduzca el número/letra de la opción que desea realizar >> ")
    
    if opcion=="a":
        limpiar_pantalla()
        print("Ha seleccionado => Nombre de las 20 primeras dianas de un tipo dado\n")
        try:
            tipotarget=input("\nIntroduzca el nombre del tipo de la diana >> ")
            query20dianas="select target_name_pref from target where target_type=%s order by target_name_pref asc limit 20"
            cursor.execute(query20dianas,(tipotarget,))    
            data20dianas = cursor.fetchall()   
            
            if cursor.rowcount==0: #si los resultados son vacíos
                print("\nLa Base de Datos no tiene almacenada ninguna información de dicha diana.")
                input("\nPulse cualquier tecla para continuar >> ")
            else:
                print(tabulate(data20dianas, tablefmt='simple')) #imprimos tabla
                print("\nSe han obtenido %s resultado(s).\n" %cursor.rowcount)
                input("Pulse cualquier tecla para continuar >> ")
        
        except mysql.connector.Error as err:
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")

    elif opcion=="b":
        limpiar_pantalla()
        print("Ha seleccionado => Organismo al cual se asocian mayor número de dianas\n")
        try: #seleccionamos el organismo con mayor count de targets agrupando por organismos
            querymaxtargets="select target_organism,count(target_id) as num_targets from target group by target_organism order by count(target_id) desc limit 1"
            cursor.execute(querymaxtargets)
            headermaxtargets=[]
            for cd in cursor.description:
                headermaxtargets.append(cd[0])       
            datamaxtargets = cursor.fetchall()    
            print(tabulate(datamaxtargets, headermaxtargets, tablefmt='simple')) #imprimimos la tabla
            print("\n")
            input("Pulse cualquier tecla para continuar >> ")
        
        except mysql.connector.Error as err:
            print("ALGO FUE MAL: {}".format(err))
            input("\nPulse cualquier tecla para continuar >> ")
      
    elif opcion=="0": #para volver al menú inicial
        menu_inicial()
    
    else:
        limpiar_pantalla()
        print("INPUT NO VÁLIDO. FINALIZACIÓN DEL PROGRAMA.")
      
def menu_6():
    limpiar_pantalla()
    input("Ha seleccionado => Borrados \nPulse cualquier tecla para continuar >> ")
    print("\n")
    try: #se muestran las 10 interacciones fármaco-enfermedad con menor score
        print("A continuación se muestran las 10 interacciones fármaco-enfermedad con menor score. De entre estas seleccione aquella que desee borrar: ")
        querybajainteraccion="select drug_disease.inferred_score,drug.drug_name,disease.disease_name from drug_disease,drug,disease where drug_disease.disease_id=disease.disease_id and drug_disease.drug_id=drug.drug_id and drug_disease.inferred_score is not null order by drug_disease.inferred_score asc limit 10"
        cursor.execute(querybajainteraccion)
        headerbajainteraccion=[] #header de la tabla 
        for cd in cursor.description:
            headerbajainteraccion.append(cd[0])       
        databajainteraccion = cursor.fetchall()    
        print(tabulate(databajainteraccion, headerbajainteraccion, tablefmt='simple')) #impresión de la tabla
        #borramos a partir de los nombres que nos muestran en la tabla haciendo subconsulta con una tabla temporal pepito, la he tenido que crear porque me daba error 1093
        farmaco1=input("\nIntroduzca el nombre del fármaco de la interacción que desee borrar >> ") 
        farmaco2=input("\nIntroduzca el nombre de la enfermedad de la interacción que desee borrar >> ")
        borradointeraccion="delete from drug_disease where (drug_disease.drug_id,drug_disease.disease_id) in (select * from (select drug_disease.drug_id, drug_disease.disease_id from drug,disease,drug_disease where drug.drug_name=%s and disease.disease_name=%s and drug_disease.drug_id=drug.drug_id and drug_disease.disease_id=disease.disease_id) pepito)"
        cursor.execute(borradointeraccion,(farmaco1,farmaco2,))
        
        if cursor.rowcount==0:
            print("\nLa Base de Datos no tiene constancia de dicha interacción.\n")
            input("Pulse cualquier tecla para continuar >> ")
        
        else:
            print("\nElección borrada.\n")
            input("Pulse cualquier tecla para continuar >> ")
        
        menu_inicial()
     
    except mysql.connector.Error as err:
        print("ALGO FUE MAL: {}".format(err))
        input("\nPulse cualquier tecla para continuar >> ")

def menu_7():
    limpiar_pantalla()
    input("Ha seleccionado => Inserciones \nPulse cualquier tecla para continuar >> ")
    print("\n")
    try: #vamos a proceder a la insercion de una interaccion farmaco-enfermedad de un fármacon que ya existe
        print("Se va a proceder a la inserción de una interacción fármaco-enfermedad de un fármaco ya existente con una nueva enfermedad.")
        codigosource=input("Antes de introducir el código de la enfermedad, por favor indique el número de su fuente, 72 (OMIM) o 75 (MESH) >> ")
        if codigosource=="72" or codigosource=="75": #son las únicas source disponibles
            codigoenfermedad=input("\nPor favor, introduzca el código de la enfermedad >> ")
            nombreenfermedad=input("\nPor favor, introduzca el nombre de la enfermedad >> ")
            nombrefarmaco=input("\nPor favor, introduzca el nombre del fármaco >> ")
            
            queryexistedroga="select * from drug where drug.drug_name=%s" #comprobamos que la droga esté en la BD
            cursor.execute(queryexistedroga,(nombrefarmaco,))
            data=cursor.fetchall()
            
            if cursor.rowcount!=0: #si existe el fármaco
                insertenfermedad="insert into disease values (%s,%s,%s)" #hacemos insercion de la nueva enfermedas
                cursor.execute(insertenfermedad,(int(codigosource),codigoenfermedad,nombreenfermedad,))
                #ahora hacemos inserción de la interacción
                insertinteraccion="insert into drug_disease(select %s,drug.drug_id,3,NULL,NULL from drug where drug.drug_name=%s)"
                cursor.execute(insertinteraccion,(codigoenfermedad,nombrefarmaco,))

                print("\nInserción realizada.\n")
                input("Pulse cualquier tecla para continuar >> ")
        
            else:
                print("\nNo se produjo la inseción.\n")
                input("Pulse cualquier tecla para continuar >> ")
        else:
            print("Número de fuente no correcto.\n")
            input("Pulse cualquier tecla para continuar >> ")
        menu_inicial()

    except mysql.connector.Error as err:
        print("ALGO FUE MAL: {}".format(err))
        input("\nPulse cualquier tecla para continuar >> ")

def menu_8():
    limpiar_pantalla()
    input("Ha seleccionado => Modificaciones \nPulse cualquier tecla para continuar >> ")
    print("\n")
    try: #vamos a modificar el valor de score de las asociaciones del farmaco con efectos secundarios
        print("Se va a proceder a la actualización del score de asociaciones fármaco-efecto secundario.")
        opcionscore=input("\nIntroduzca el número que quiera considerar de score, aquellos score menores al valor introducido pasarán a tener un valor 0 >> ")
        querymodificacion="update drug_phenotype_effect set score=0 where phenotype_type=%s and score<%s"
        cursor.execute(querymodificacion,("SIDE EFFECT",float(opcionscore),))
        print("\nModificación realizada.\n")
        input("Pulse cualquier tecla para continuar >> ")
        menu_inicial() 
                
    except mysql.connector.Error as err:
        print("ALGO FUE MAL: {}".format(err))
        input("\nPulse cualquier tecla para continuar >> ")
        
        
try: #establecemos la conexión con la base de datos con gestión de errores
    db=mysql.connector.connect(host="localhost",
                                  user="drugslayer",
                                  password="drugslayer_pwd",
                                  db="disnet_drugslayer",
                                  autocommit=True)
    cursor=db.cursor()
    menu_inicial()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n\\\\\\\\\ HAY ALGO MAL CON TU USUARIO O CONTRASEÑA.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n\\\\\\\\\ NO EXISTE LA BASE DE DATOS.")
    else:
        print(err)
        
else:
    db.close()
    print("\n\n\\\\\\\\\ CONEXIÓN CERRADA.") 