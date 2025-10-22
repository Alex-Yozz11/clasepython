#try:
#   #codigo quepuede causa el error
#except:
#   #codigo que se ejecuta si ocurre un error

#ZeroDivisionError
try:
    numero = int(input("Ingrese un numero: "))
    resultado = 10 / numero
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")

#ValueError
try:
    edad = int(input("Ingrese su edad: "))
    print("Su edad es:", edad)
except ValueError:
    print("Error: Debe ingresa un numero entero valido")

#multiples exceptions
try:
    a = int(input("Ingrese el numerador: "))
    b = int(input("Ingrese el denominador: "))
    resultado = a / b
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except ValueError:
    print("Error: Debe ingresar un numero entero valido")

# else y finally

try:
    numero = int(input("Ingrese un numero positivo: "))
    if numero < 0:
        raise ValueError("El numero debe ser positivo")
except ValueError as e:
    print("Error:", e)
else:
    print("No hubo errores")
finally:
    print("Fin del programa")