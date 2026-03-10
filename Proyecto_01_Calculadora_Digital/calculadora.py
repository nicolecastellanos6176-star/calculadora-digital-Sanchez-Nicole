"hola mundo"
"""
Calculadora Multifuncional Interactiva - Versión Avanzada
Proyecto de Tecnología Digital

Equipo:
- Estudiante 1: [Junior Gael] - Estructura Principal y Gestión de Datos
- Estudiante 2: [Nicole Sanchez] - Funciones Matemáticas
- Estudiante 3: [Diego Valdez] - Conversores y Sistema de Historial

Fecha: Marzo 2026
Universidad de Guadalajara - Campus GDL
"""

import os
from datetime import datetime

from pyparsing import nums

from Proyecto_01_Calculadora_Digital.agregar_al_historial import agregar_al_historial

# Variable global para almacenar historial (lista de strings)
historial = []

# ============================================
# SECCIÓN 1: FUNCIONES MATEMÁTICAS (Estudiante 2)
# ============================================

def sumar(a, b):
    return a + b


def restar(a, b):
   return a - b
    

def multiplicar(a, b):
   return a * b 


def dividir(a, b):
   if b == 0:
    print("❌ Error: no se puede dividir entre cero.")
    return None 
   return a / b 
    

def modulo(a, b):
    if b == 0:
     return None 
    return a % b 


def potencia(a, b):
   return a ** b 

# ============================================
# SECCIÓN 2: CONVERSIÓN DE SISTEMAS NUMÉRICOS (Estudiante 2)
# ============================================

def decimal_a_binario(numero):
    #caso especial: si el numero es 0 
    if numero == 0:
        return "0"
    resultado = "" 
    temp = int(numero)
    while temp > 0:
        residuo = temp % 2 
        resultado = str(residuo) + resultado 
        temp = temp // 2
    return resultado 


def decimal_a_hexadecimal(numero):
    if numero == 0: 
        return "0"
    hex_chars = "0123456789ABCDEF" 
    resultado = ""
    temp = int(numero)
    while temp > 0:
        resultado = hex_chars[temp % 16] + resultado 
        temp //= 16 
    return resultado 

def binario_a_decimal(binario):
    """
    Convierte n string binario a su valor decimal
    """
    decimal = 0
    #Convertimos a string por si acaso entra como numero
    binario_str = str(binario)
    posicion = 0
    for digito in reversed(binario_str):
        if digito == '1':
            decimal += 2 ** posicion
        posicion += 1 
    return decimal 
    
def hexadecimal_a_decimal(hexadecimal):
    try:
        return int(str(hexadecimal), 16)
    except ValueError:
        return None


# ============================================
# SECCIÓN 3: CONVERSIÓN DE UNIDADES (Estudiante 3)
# ============================================

def bytes_a_kilobytes(bytes_val):
    return bytes_val / 1024

def kilobytes_a_megabytes(kb):
    return kb / 1024

def megabytes_a_gigabytes(mb):
    return mb / 1024 

#Funciones inversas
def gygabytes_a_magabytes(gb):
    return gb * 1024
def megabytes_a_kilobytes(mb):
    return mb * 1024
def kilobyte_a_bytes(kb):
    return kb * 1024

# ============================================
# SECCIÓN 4: GESTIÓN DE HISTORIAL (Estudiante 3)
# ============================================

def agregar_al_historial(operacion, num1, num2, resultado):

    global historial
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entrada = f"{fecha_hora} | {operacion}: {num1} + {num2} = {resultado}"
    historial.append(entrada)
if len(historial)> 10:
     historial.pop(0)


def mostrar_historial():
    """
    Muestra el historial de operaciones.
    """
    global historial

print("\n" + "-"*30)
if not historial:
   print("📭 El historial está vacío.")
else:
    print("📜 HISTORIAL DE OPERACIONES:")
    for i, registro in enumerate(historial, 1):
     print(f"{i}. {registro}")
    print("-"*30)
    
def limpiar_historial():
    """
    Limpia el historial de operaciones.
    """
    global historial
    historial.clear()


# ============================================
# SECCIÓN 5: GESTIÓN DE ARCHIVOS (Estudiante 1)
# ============================================

def guardar_historial_archivo():
    """
    Guarda el historial en el archivo datos/historial.txt
    """
    global historial

    if not os.path.exists("datos"):
        os.makedirs("datos")
    try:
     with open("datos/historial.txt", "w", encoding="utf-8") as archivo:
        for registro in historial:
         archivo.write(registro + "\n")
     print("💾 Historial guardado correctamente en 'datos/historial.txt'.")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")

def cargar_historial_archivo():
    """Carga los datos del archivo .txt a la lista de historial al iniciar."""
    global historial
    ruta = "datos/historial.txt"
    
    if os.path.exists(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                # Leemos las líneas y eliminamos el salto de línea (\n) con strip()
             historial = [linea.strip() for linea in archivo.readlines()]
            print("📜 Historial cargado exitosamente.")
        except Exception as e:
            print(f"❌ Error al cargar el archivo: {e}")
    else:
        # Si el archivo no existe, inicializamos el historial como una lista vacía
        historial = []

#=============================================
# SECCIÓN 6: VALIDACIÓN (Estudiante 1)
# ============================================

def validar_numero(mensaje):
    """
    Solicita y valida un número al usuario."""
    
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("❌ Error: Ingrese un número válido.")


def validar_numero_entero(mensaje):
    """
    Solicita y valida un número entero al usuario."""
    while True:
        try: 
            numero= int(input(mensaje))
            return numero 
        except ValueError:
            print("❌ Error: Ingrese un numero entero valido (sin decimales).")

# ============================================
# SECCIÓN 7: MENÚS (Estudiante 1)
# ============================================

def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("   CALCULADORA MULTIFUNCIONAL v2.0")
    print("="*60)
    print("\nMENÚ PRINCIPAL:")
    print("1. Calculadora Básica")
    print("2. Conversor de Unidades de Datos")
    print("3. Calculadora de Sistemas Numéricos")
    print("4. Ver Historial")
    print("5. Limpiar Historial")
    print("6. Salir")
    print("-"*60)


def menu_calculadora_basica():
    """Menú y lógica de la calculadora básica"""
    print("\n--- CALCULADORA BÁSICA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo (residuo)")
    print("6. Potencia")
    print("7. Volver al menú principal")

    opcion = input("\nSeleccione operación: ")

    if opcion == "7": 
        return
        
# Solicitar números
    num1 = validar_numero("Ingrese el primer número: ")
    num2 = validar_numero("Ingrese el segundo número: ")

    resultado = None 
    operacion_nombre = "" 
    if opcion == "1":
        resultado = sumar(num1, num2)
        operacion_nombre = "Suma"
    elif opcion == "2":
        resultado = restar(num1, num2)
        operacion_nombre = "Resta"
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
        operacion_nombre = "Multiplicación"
    elif opcion == "4":
        resultado = dividir(num1, num2)
        operacion_nombre = "División"
    elif opcion == "5":
        resultado = modulo(num1, num2)
        operacion_nombre = "Módulo"
    elif opcion == "6":
        resultado = potencia(num1, num2)
        operacion_nombre = "Potencia"
    else:
        print("❌ Opción no válida.")
        return

    # Si la operación fue exitosa (especialmente por la división entre cero)
    if resultado is not None:
        print(f"\n✅ El resultado de la {operacion_nombre} es: {resultado}")
        # Guardamos en el historial
        agregar_al_historial(operacion_nombre, num1, num2, resultado)


def menu_conversor_unidades():
    """Menú y lógica del conversor de unidades"""
    print("n\--- CONVERSOR DE UNIDADES DE DATOS ---")
    print("1. Bytes a Kilobytes (KB)")
    print("2. Kylobytes (KB) a Megabytes (MB)")
    print("3. Megabytes (MB) a Gigabytes (GB)")
    print("4. Gigabytes (GB) a Megabytes (MB)")
    print("5. volver al menu principal")

    opcion = input("\nSeleccione una opcion: ")

    if opcion == "5": 
        return

    valor = validar_numero("Ingrese la cantidad a convertir: ")
    resultado = 0
    unidad_orig = ""
    unidad_dest = "" 

    if opcion == "1":
        resultado = bytes_a_kilobytes(valor)
        unidad_orig, unidad_dest = "Bytes", "KB"
    elif opcion == "2":
        resultado = kilobytes_a_megabytes(valor)
        unidad_orig, unidad_dest = "KB", "MB"
    elif opcion == "3":
        resultado = megabytes_a_gigabytes(valor)
        unidad_orig, unidad_dest = "MB", "GB"
    elif opcion == "4":
        resultado = gygabytes_a_magabytes(valor)
        unidad_orig, unidad_dest = "GB", "MB"
    else: 
      return

    print("❌ opcion no valida.")
    print(f"\n✅{valor} {unidad_orig} equivalen a {resultado:.4f} {unidad_dest}")
    agregar_al_historial(f"Conv.{unidad_orig}->{unidad_dest}", valor, 0,resultado)


def menu_sistemas_numericos():
    """Menú y lógica de conversión de sistemas numéricos"""
    print("\n--- CALCULADORA DE SISTEMAS NUMERICOS ---")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Decimal a Hexadecimal")
    print("4. Hexadecimal a Decimal")
    print("5. Volver al menu principal")

    opcion = input("\nSeleccione una opcion: ")
    if opcion == "1":
        num = validar_numero_entero("Ingrese numero decimal: ")
        res = decimal_a_binario(num)
        print(f"✅ Resultado: {res}")
        agregar_al_historial("Decimal a Binario", num, 0, res)

    elif opcion == "2":
        # Aquí pedimos un string porque el binario se maneja mejor así
        bin_str = input("Ingrese número binario (0 y 1): ")
        res = binario_a_decimal(bin_str)
        print(f"✅ Resultado: {res}")
        agregar_al_historial("Binario a Decimal", bin_str, 0, res)

    elif opcion == "3":
        num = validar_numero_entero("Ingrese número decimal: ")
        res = decimal_a_hexadecimal(num)
        print(f"✅ Resultado: {res}")
        agregar_al_historial("Decimal a Hexadecimal", num, 0, res)

    elif opcion == "4":
        hex_str = input("Ingrese número hexadecimal: ")
        res = hexadecimal_a_decimal(hex_str)
        if res is not None:
            print(f"✅ Resultado: {res}")
            agregar_al_historial("Hexadecimal a Decimal", hex_str, 0, res)
        else:
            print("❌ Error: Valor hexadecimal no válido.")
    
    else:
        print("❌ Opción inválida.")
    
        
# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del programa"""

    print("╔" + "═"*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  CALCULADORA MULTIFUNCIONAL - Versión Avanzada".center(58) + "║")
    print("║" + " "*58 + "║")
    print("║" + "  Con historial, funciones y persistencia de datos".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "═"*58 + "╝")

    # Cargar historial al iniciar
    cargar_historial_archivo()
    print("\n✅ Historial cargado desde archivo.")

    continuar = True

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            menu_calculadora_basica()

        elif opcion == "2":
            menu_conversor_unidades()

        elif opcion == "3":
            menu_sistemas_numericos()

        elif opcion == "4":
            mostrar_historial()

        elif opcion == "5":
            confirmacion = input("\n¿Está seguro de limpiar el historial? (s/n): ")
            if confirmacion.lower() == "s":
                limpiar_historial()
                print("✅ Historial limpiado.")

        elif opcion == "6":
            print("\n💾 Guardando historial...")
            guardar_historial_archivo()
            print("✅ Historial guardado en datos/historial.txt")
            print("\n¡Gracias por usar la Calculadora Multifuncional!")
            print("¡Hasta pronto! 👋")
            continuar = False

        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")

    print("\nPrograma terminado.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
