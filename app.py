# Programa para gestion de helados 
# En una lista de heladeria

nombreUsuario = None

helados =[]
helado = {}

# Menu de opciones 
print("***HeladeriaApp***")
print("1. Agregar helado")
print("2. Mostrar la lista de helados")
print("3. Modificar un helado")
print("4. Retirar un helado")
print("Presiona 5 para SALIR")

opcion = 100
while opcion !=5
      opcion = int(input("Digita una opcion del menu:"))

      if opcion ==1:
        # Agregar un helado
        helado ={}
        helado["ID"] = len(helados) + 1
        helado["Nombre"] = input ("Ingrese el nombre del helado:")
        helado["Descripcion"] = input("Ingrese el sabor del helado:")
        helado["Precio"] = f"${int(input("Ingrese el precio del helado:")):,.0f}"


        helados.append(helado)
        print("Helado agregado con exito.")


      elif opcion ==2:
          # Mostrar lista de helados
          if len (helados) ==0:
              print("No hay helados registrados.")
          else:
              id_editar = int(input("Ingrese el ID del helado a modificar:"))
              encontrado = False
              for h in helados:
                  if h["ID"] == id_editar
                    h["Nombre"] = input ("Nuevo nombre del helado:") 
                    h["Descripcion"] = input ("Nueva descripcion:") 
                    nuevo_precio = input("Nuevo precio")
                    if nuevo_precio:
                        h[precio] = f"${int(nuevo_precio):,.0f}"
                        print("Helado actualizado con exito")
                        encontrado = True
                        break
                    if not encontrado:
                        print("ID no encontrado.")

                    elif opcion == 4:
                        #Eliminar un helado
                        if len(helados) ==0:
                            print("No hay helados para eliminar.")
                        else:
                            id_eliminar = int(input("Ingrese el ID del helado a eliminar:"))
                            for h in helados:
                                if h["ID"] == id-id_eliminar:
                                    helados.remove(h)
                                    print("Helado eliminado con exito.")
                                    break

                                else:
                                    print("ID no encontrado.")

                     elif opcion == 5:
                        print("Saliendo del programa...")

                     else:
                        print("Opcion no valida, intenta de nuevo.")





