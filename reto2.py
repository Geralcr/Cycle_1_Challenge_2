# -*- coding: utf-8 -*-
"""
Geraldine Claros Rios
"""
#Definicion funcion con argumento tipo diccionario
def prestamo(informacion: dict) -> dict:

    #Diccionario que se retorna
    dictAprobacion = dict()
    dictAprobacion['id_prestamo'] = informacion['id_prestamo']

    ingreso_deudor = informacion['ingreso_deudor']
    ingreso_codeudor = informacion['ingreso_codeudor']
    cantidad_prestamo = informacion['cantidad_prestamo']
    dependientes = informacion['dependientes']
    if dependientes == '3+':
        dependientes = 3

    if dependientes < 0:
        dependientes = 0

    if type(ingreso_codeudor) == str or ingreso_codeudor < 0:
        ingreso_codeudor = 0

    if type(ingreso_deudor) == str or ingreso_deudor < 0:
        ingreso_deudor = 0

    if type(cantidad_prestamo) == str or cantidad_prestamo < 0:
        cantidad_prestamo = 0

    # Verifica si tiene historia_credito es 1 ####
    if informacion['historia_credito'] == 1:

        #### Verifica si i_c > 0 & i_d/9 > c_p ####
        if ingreso_codeudor > 0 and ingreso_deudor / 9 > cantidad_prestamo:

            dictAprobacion['aprobado'] = True

        else:

            #### Compruebo dependiente > 2 & independiente ####
            if dependientes > 2 and informacion['independiente'] == "Si" :

                dictAprobacion['aprobado'] = ingreso_codeudor / 12 > cantidad_prestamo

            else:

                dictAprobacion['aprobado'] = cantidad_prestamo < 200

#### Verifica si tiene historia_credito es 0 ####
    elif informacion['historia_credito'] == 0:

        #### Verifico si es independiente ####
        if informacion['independiente'] == "Si":

            #### Verifico si ¬(casado & dependientes > 1) ####
            if not (informacion['casado']  == "Si" and dependientes > 1):

                #### Verifico si i_d / 10 > c_p or i_c / 10 > c_p ####
                if (ingreso_deudor / 10  > cantidad_prestamo) or (ingreso_codeudor / 10 > cantidad_prestamo):

                    dictAprobacion['aprobado'] = cantidad_prestamo < 180

                else:

                    dictAprobacion['aprobado'] = False

            else:

                dictAprobacion['aprobado'] = False

        elif informacion['independiente'] == "No":

            #### Verifico si ¬semiurbano or dependientes <2 ####
           if not (informacion['tipo_propiedad'] == "Semiurbano") and (dependientes < 2 and dependientes >= 0 ):

               #### Verifico si es graduado ####
               if informacion['educacion'] == "Graduado":

                   dictAprobacion['aprobado'] = ingreso_deudor / 11 > cantidad_prestamo and ingreso_codeudor / 11 > cantidad_prestamo

               elif informacion['educacion'] == "No Graduado":

                   dictAprobacion['aprobado'] = False

           else:

               dictAprobacion['aprobado'] = False

    return dictAprobacion


################### PRUEBAS UNITARIAS ##################
informacionReto1 ={
    'id_prestamo': 'RetoS2_001',
    'casado' : "No",
    'dependientes' : "3+",
    'educacion' : "Graduado",
    'independiente' : "Si",
    'ingreso_deudor' : 4692,
    'ingreso_codeudor' : 120,
    'cantidad_prestamo' : 106,
    'plazo_prestamo' : 360,
    'historia_credito' : 1,
    'tipo_propiedad' : "Rural"
    }


#print(int("3+"))

informacionReto2 = {
    'id_prestamo': 'RETOS2_001', 
    'casado': 'No', 
    'dependientes': 0, 
    'educacion': 'Graduado', 
    'independiente': 'Si', 
    'ingreso_deudor': 4692, 
    'ingreso_codeudor': 120, 
    'cantidad_prestamo': 106, 
    'plazo_prestamo': 360, 
    'historia_credito': 1, 
    'tipo_propiedad': 'Rural'
    }

print(prestamo(informacionReto1))
print(prestamo(informacionReto2))

print(prestamo({'id_prestamo': 'RETOS2_002', 'casado': 'Si', 'dependientes': '3+', 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 692, 'ingreso_codeudor': 150, 'cantidad_prestamo': 106, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Urbano'}))
print(prestamo({'id_prestamo': 'RETOS2_003', 'casado': 'Si', 'dependientes': '3+', 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 691, 'ingreso_codeudor': 1500, 'cantidad_prestamo': 106, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_004', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 0, 'cantidad_prestamo': 286, 'plazo_prestamo': 90, 'historia_credito': 1, 'tipo_propiedad': 'Urbano'}))
print(prestamo({'id_prestamo': 'RETOS2_005', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 0, 'cantidad_prestamo': 170, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_006', 'casado': 'No', 'dependientes': 2, 'educacion': 'No Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 1000, 'cantidad_prestamo': 86, 'plazo_prestamo': 460, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))
print(prestamo({'id_prestamo': 'RETOS2_007', 'casado': 'No', 'dependientes': 2, 'educacion': 'No Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 1000, 'cantidad_prestamo': 256, 'plazo_prestamo': 460, 'historia_credito': 0, 'tipo_propiedad': 'Semiurbano'}))
print(prestamo({'id_prestamo': 'RETOS2_008', 'casado': 'No', 'dependientes': '3+', 'educacion': 'No Graduado', 'independiente': 'Si', 'ingreso_deudor': 100, 'ingreso_codeudor': 0, 'cantidad_prestamo': 1086, 'plazo_prestamo': 160, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))
print(prestamo({'id_prestamo': 'RETOS2_009', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 11, 'ingreso_codeudor': 564, 'cantidad_prestamo': 100, 'plazo_prestamo': 189, 'historia_credito': 0, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_010', 'casado': 'No', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 11, 'ingreso_codeudor': 564, 'cantidad_prestamo': 100, 'plazo_prestamo': 189, 'historia_credito': 0, 'tipo_propiedad': 'Semiurbano'}))
print(prestamo({'id_prestamo': 'RETOS2_011', 'casado': 'No', 'dependientes': 1, 'educacion': 'No Graduado', 'independiente': 'No', 'ingreso_deudor': 11, 'ingreso_codeudor': 564, 'cantidad_prestamo': 100, 'plazo_prestamo': 189, 'historia_credito': 0, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_012', 'casado': 'No', 'dependientes': 0, 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 1111, 'ingreso_codeudor': 1111, 'cantidad_prestamo': 90, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_013', 'casado': 'No', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 11, 'ingreso_codeudor': 564, 'cantidad_prestamo': 100, 'plazo_prestamo': 189, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))

