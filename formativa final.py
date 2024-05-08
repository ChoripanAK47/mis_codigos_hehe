valorTotal = 0
valorDesc = 0
valorFinal = 0
cantRoll_1 = 0
cantRoll_2 = 0
cantRoll_3 = 0
cantRoll_4 = 0
## salirSubMenu = x

## Inicio menú de selección
while True:
    print("Bienvenido a Sushi Shop")
    print("xxx_Maldito_Otaku_xxx\n")
    print("1. Pikachu Roll $4500")
    print("2. Otaku Roll $5000 ")
    print("3. Pulpo Venenoso Roll $5200")
    print("4. Anguila Eléctrica Roll $4800")
    print("5. Salir\n")
    print("Para terminar de seleccionar, presione 5")
    opcion = int(input("Ingrese el número de elemento que desea comprar: "))

## Opcion 1
    if opcion == 1:
        cantRoll_1 += 1
        valorTotal = valorTotal + 4500
        print("----------------------------------------------")
        print("Usted ha agregado 1 orden de Pikachu Roll")
        print("Pikachu Roll: ",cantRoll_1)
        print("Otaku Roll: ",cantRoll_2)
        print("Pulpo venenoso Roll: ",cantRoll_3)
        print("Anguila Eléctrica Roll: ",cantRoll_4)
        print("----------------------------------------------")

## Opcion 2        
    else:
        if opcion == 2:
            cantRoll_2 += 1
            valorTotal = valorTotal + 5000    
            print("----------------------------------------------")
            print("Usted ha agregado 1 orden de Otaku Roll")
            print("Pikachu Roll: ",cantRoll_1)
            print("Otaku Roll: ",cantRoll_2)
            print("Pulpo venenoso Roll: ",cantRoll_3)
            print("Anguila Eléctrica Roll: ",cantRoll_4)
            print("----------------------------------------------")

## Opcion 3
        else:
            if opcion == 3:
                cantRoll_3 += 1
                valorTotal = valorTotal + 5200
                print("----------------------------------------------")
                print("Usted ha agregado 1 orden de Pulpo Venenoso Roll")
                print("Pikachu Roll: ",cantRoll_1)
                print("Otaku Roll: ",cantRoll_2)
                print("Pulpo venenoso Roll: ",cantRoll_3)
                print("Anguila Eléctrica Roll: ",cantRoll_4)
                print("----------------------------------------------")

## Opcion 4
            else:
                if opcion == 4:
                    cantRoll_4 += 1
                    valorTotal = valorTotal + 4800
                    print("----------------------------------------------")
                    print("Usted ha agregado 1 orden de Anguila Eléctrica Roll")
                    print("Pikachu Roll: ",cantRoll_1)
                    print("Otaku Roll: ",cantRoll_2)
                    print("Pulpo venenoso Roll: ",cantRoll_3)
                    print("Anguila Eléctrica Roll: ",cantRoll_4)
                    print("----------------------------------------------")

## Opcion 5
                else:
                    if opcion == 5:
                        print("Se ha guardado su orden exitosamente\n")
                        print("¿Usted posee un código de descuento?")       
                        tieneDesc = input("s/n: ")

## Ingresar código de descuento
                        while True:
                                    if tieneDesc == "s":
                                        codigoDesc = input("Ingrese su código de descuento: ")
                                        if codigoDesc == "soyotaku":
                                            valorDesc = valorTotal * 0.10
                                            valorFinal = valorTotal - valorDesc
                                            print("Código de descuento válido, descuento aplicado")
                                            print("----------------------------------------------")
                                            print("Total productos ",cantRoll_1 + cantRoll_2 + cantRoll_3 + cantRoll_4)
                                            print("----------------------------------------------")
                                            print("Pikachu Roll: ",cantRoll_1)
                                            print("Otaku Roll: ",cantRoll_2)
                                            print("Pulpo venenoso Roll: ",cantRoll_3)
                                            print("Anguila Eléctrica Roll: ",cantRoll_4)
                                            print("----------------------------------------------")
                                            print("Subtotal a pagar: $",valorTotal)
                                            print("Valor del descuento: $",valorDesc)
                                            print("TOTAL: $",valorFinal)
                                            print("----------------------------------------------")
                                            print("¿Desea hacer otro pedido, o salir del programa?")
                                            print ("1. Otro pedido / 2. Salir")
                                            opcionFinal = int(input("Ingrese opcion: "))
                                            if opcionFinal == 1:
                                                break
                                            else:
                                                if opcionFinal == 2:
                                                    print("Gracias por su compra, vuelva pronto")
                                                    break
## Código de descuento inválido
                                        else: 
                                            print("Código inválido")
                                            print("Ingrese otro código o escriba 'x' para salir")
                                            codigoDesc = input()
                                            if codigoDesc == "x":
                                                print("----------------------------------------------")
                                                print("Total productos ",cantRoll_1 + cantRoll_2 + cantRoll_3 + cantRoll_4)
                                                print("----------------------------------------------")
                                                print("Pikachu Roll: ",cantRoll_1)
                                                print("Otaku Roll: ",cantRoll_2)
                                                print("Pulpo venenoso Roll: ",cantRoll_3)
                                                print("Anguila Eléctrica Roll: ",cantRoll_4)
                                                print("----------------------------------------------")
                                                print("Subtotal a pagar: $",valorTotal)
                                                print("Valor del descuento: $",valorDesc)
                                                print("TOTAL: $",valorFinal)
                                                print("----------------------------------------------")
                                                print("¿Desea hacer otro pedido, o salir del programa?")
                                                print ("1. Otro pedido / 2. Salir")
                                                opcionFinal = int(input("Ingrese opcion: "))
                                                if opcionFinal == 1:
                                                    break
                                                else:
                                                    if opcionFinal == 2:
                                                        print("Gracias por su compra, vuelva pronto")
                                                        break
## Sin código de descuento                                                                
                                    else:
                                        if tieneDesc == "n":
                                            print("----------------------------------------------")
                                            print("Total productos ",cantRoll_1 + cantRoll_2 + cantRoll_3 + cantRoll_4)
                                            print("----------------------------------------------")
                                            print("Pikachu Roll: ",cantRoll_1)
                                            print("Otaku Roll: ",cantRoll_2)
                                            print("Pulpo venenoso Roll: ",cantRoll_3)
                                            print("Anguila Eléctrica Roll: ",cantRoll_4)
                                            print("----------------------------------------------")
                                            print("Subtotal a pagar: $",valorTotal)
                                            print("Valor del descuento: $",valorDesc)
                                            print("TOTAL: $",valorFinal)
                                            print("----------------------------------------------")
                                            print("¿Desea hacer otro pedido, o salir del programa?")
                                            print ("1. Otro pedido / 2. Salir")
                                            opcionFinal = int(input("Ingrese opcion: "))
                                            if opcionFinal == 1:
                                                break
                                            else:
                                                if opcionFinal == 2:
                                                    print("Gracias por su compra, vuelva pronto")
                                                    break
                        break