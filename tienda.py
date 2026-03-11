print(" SISTEMA DE TIENDA ")

MONTO_COMPRA_DESCUENTO = 1000
monto = float(input("Ingresa el monto consumido: "))
es_miembro = input("Eres miembro de la tienda (Si/No): ")

descuento = 0

#Verificar dato
if monto >= MONTO_COMPRA_DESCUENTO and es_miembro.strip().lower() == "si":
    descuento = 0.1 #Descuento del 10 %
elif es_miembro.strip().lower() == "si":
    
