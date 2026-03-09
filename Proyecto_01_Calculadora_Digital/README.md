# 💻 Proyecto 1: Calculadora Multifuncional Interactiva

## 🎯 Objetivo del Proyecto

Crear una calculadora de línea de comandos con múltiples funcionalidades que incluya operaciones matemáticas básicas, conversiones de unidades, y calculadoras especializadas para tecnología digital.

**Carrera:** Tecnología Digital
**Duración:** 2 semanas
**Equipo:** 3 estudiantes

## 📚 Conceptos de Python Utilizados

- Variables y tipos de datos (int, float, str)
- Operadores aritméticos (+, -, *, /, //, %, **)
- Operadores de comparación y lógicos
- Condicionales (if/elif/else)
- Loops (while para menú principal, for para conversiones)
- **Listas** para almacenar historial de operaciones
- **Funciones** definidas con parámetros y return
- **Archivos de texto** para guardar/cargar historial
- Conversión de tipos (int(), float(), str())
- Formateo de strings (f-strings)

## 🎓 Competencias a Desarrollar

1. Diseñar interfaces de usuario basadas en menús
2. Validar entradas del usuario
3. Implementar lógica condicional compleja
4. Trabajar con sistemas numéricos (decimal, binario, hexadecimal)
5. Realizar conversiones de unidades

## 📋 Requisitos Funcionales

### ✅ Requisitos Mínimos (Obligatorios)

1. **Menú Principal Interactivo**
   - Mostrar opciones numeradas claramente
   - Permitir al usuario seleccionar operaciones
   - Opción para salir del programa
   - Loop continuo hasta que el usuario decida salir

2. **Calculadora Básica con Funciones** (6 operaciones)
   - Suma, Resta, Multiplicación, División, Módulo, Potencia
   - **Cada operación debe ser una función** (ej: `def sumar(a, b)`)
   - División con validación de división por cero
   - Funciones deben retornar resultados

3. **Conversor de Unidades de Datos**
   - Bytes ↔ Kilobytes ↔ Megabytes ↔ Gigabytes
   - Al menos 6 conversiones implementadas como funciones
   - Usar funciones con parámetros y return

4. **Calculadora de Sistemas Numéricos**
   - Decimal → Binario (función con algoritmo manual)
   - Decimal → Hexadecimal
   - Binario → Decimal
   - Hexadecimal → Decimal

5. **Historial de Operaciones (Listas)**
   - Almacenar las últimas 10 operaciones en una lista
   - Opción de menú para ver historial
   - Cada entrada: operación, números, resultado
   - Opción para limpiar historial

6. **Persistencia de Datos (Archivos)**
   - Guardar historial en archivo `datos/historial.txt` al salir
   - Cargar historial al iniciar (si existe)
   - Formato: fecha, operación, resultado

7. **Validación de Entrada**
   - Función `validar_numero()` para verificar entradas
   - Manejar opciones inválidas del menú
   - Mensajes de error claros

### 🌟 Características Opcionales (Extra)

- Exportar historial a CSV con formato: `fecha,operacion,num1,num2,resultado`
- Calculadora científica (funciones trigonométricas aproximadas)
- Estadísticas del historial (operación más usada, promedio de resultados)
- Búsqueda en historial por tipo de operación
- Conversor de temperaturas (Celsius, Fahrenheit, Kelvin)
- Gráfico ASCII de frecuencia de operaciones
- Modo batch: cargar operaciones desde archivo de texto
- Colores en la terminal (usando códigos ANSI)

## 👥 Distribución de Trabajo Sugerida

### Estudiante 1: Estructura Principal y Gestión de Datos
- Crear el loop principal del programa
- Implementar el sistema de menús
- **Funciones de gestión de archivos** (cargar/guardar historial)
- **Funciones de validación** de entrada
- Integrar todos los módulos

### Estudiante 2: Calculadoras Matemáticas (Funciones)
- **6 funciones matemáticas** (sumar, restar, multiplicar, dividir, modulo, potencia)
- **4 funciones de conversión numérica** (dec2bin, dec2hex, bin2dec, hex2dec)
- Validación de división por cero
- Funciones con parámetros y return

### Estudiante 3: Conversores y Sistema de Historial
- **6 funciones de conversión de unidades** (bytes, KB, MB, GB)
- **Sistema de historial con listas** (agregar, ver, limpiar)
- **Función para mostrar historial** formateado
- Características adicionales opcionales

## 📊 Ejemplo de Ejecución

```
╔════════════════════════════════════════════╗
║   CALCULADORA MULTIFUNCIONAL v1.0          ║
║   Equipo: [Nombres de los estudiantes]    ║
╚════════════════════════════════════════════╝

MENÚ PRINCIPAL
1. Calculadora Básica
2. Conversor de Unidades de Datos
3. Calculadora de Sistemas Numéricos
4. Salir

Seleccione una opción: 1

--- CALCULADORA BÁSICA ---
1. Suma
2. Resta
3. Multiplicación
4. División
5. Módulo (residuo)
6. Potencia
7. Volver al menú principal

Seleccione operación: 6

Ingrese la base: 2
Ingrese el exponente: 10

Resultado: 2^10 = 1024

¿Desea realizar otra operación? (s/n): s

[El programa continúa...]
```

## 📝 Rúbrica de Evaluación (100 puntos)

### Funcionalidad (40 puntos)
- [ ] Menú principal funciona correctamente (5 pts)
- [ ] Calculadora básica completa (10 pts)
- [ ] Conversor de unidades completo (10 pts)
- [ ] Calculadora de sistemas numéricos completa (10 pts)
- [ ] El programa no se cierra inesperadamente (5 pts)

### Código (30 puntos)
- [ ] Uso correcto de variables (5 pts)
- [ ] Uso apropiado de condicionales (8 pts)
- [ ] Uso apropiado de loops (8 pts)
- [ ] Código bien organizado y legible (5 pts)
- [ ] Nombres de variables descriptivos (4 pts)

### Validación y Robustez (15 puntos)
- [ ] Validación de entradas numéricas (5 pts)
- [ ] Manejo de división por cero (3 pts)
- [ ] Manejo de opciones inválidas (4 pts)
- [ ] Mensajes de error claros (3 pts)

### Documentación y Presentación (15 puntos)
- [ ] Comentarios en el código explicando secciones (5 pts)
- [ ] README del equipo con instrucciones (5 pts)
- [ ] Presentación clara en pantalla (3 pts)
- [ ] Características adicionales creativas (2 pts bonus)

## 🚀 Entregables

### Repositorio GitHub (Obligatorio)
1. **Crear repositorio público** en GitHub: `calculadora-digital-[apellidos]`
2. **Estructura del repositorio:**
   ```
   calculadora-digital-apellidos/
   ├── README.md                    # Documentación principal
   ├── calculadora.py               # Código principal
   ├── datos/                       # Carpeta para datos
   │   ├── historial.txt           # Historial guardado
   │   └── .gitkeep                # Para mantener carpeta en Git
   ├── .gitignore                   # Ignorar __pycache__, etc.
   └── ejemplos/                    # Screenshots opcionales
   ```

3. **README.md del repositorio** debe incluir:
   - Título y descripción del proyecto
   - Nombres de los integrantes y roles
   - Características implementadas
   - Instrucciones de instalación y uso
   - Ejemplos de ejecución (con screenshots opcionales)
   - Tecnologías usadas (Python 3.x)
   - Licencia (MIT recomendada)

4. **Commits**:
   - Mínimo 15 commits distribuidos entre los 3 integrantes
   - Mensajes descriptivos en español
   - Ejemplo: "Agregar función de suma" o "Implementar historial de operaciones"

5. **Archivo .gitignore** debe incluir:
   ```
   __pycache__/
   *.pyc
   .DS_Store
   *.txt.bak
   ```

6. **Comentarios y docstrings** en todas las funciones:
   ```python
   def sumar(a, b):
       """
       Suma dos números.

       Args:
           a (float): Primer número
           b (float): Segundo número

       Returns:
           float: Resultado de la suma
       """
       return a + b
   ```

## 💡 Consejos

1. **Comiencen simple:** Primero hagan funcionar el menú principal, luego añadan características
2. **Prueben frecuentemente:** Ejecuten el programa después de cada cambio
3. **Usen comentarios:** Ayudan a entender el código de sus compañeros
4. **División clara:** Cada estudiante trabaja en su parte, luego integran
5. **Validación es clave:** Un programa robusto maneja errores del usuario
6. **Conversión de tipos:** Recuerden que input() siempre devuelve string

## 🔗 Recursos Útiles

- **Conversión binaria:** Usen el algoritmo de división sucesiva entre 2
- **Conversión hexadecimal:** Recuerden que 10=A, 11=B, 12=C, 13=D, 14=E, 15=F
- **Unidades de datos:** 1 KB = 1024 bytes, 1 MB = 1024 KB, etc.
- **Códigos ANSI (opcional):** `\033[1;32m` para texto verde, `\033[0m` para resetear

## 📅 Cronograma Sugerido

### Semana 1
- **Día 1-2:** Reunión de equipo, dividir tareas, crear estructura básica
- **Día 3-4:** Cada estudiante desarrolla su módulo
- **Día 5-6:** Primera integración, pruebas básicas
- **Día 7:** Corrección de errores de integración

### Semana 2
- **Día 1-2:** Añadir validaciones y mejoras
- **Día 3-4:** Implementar características opcionales
- **Día 5-6:** Documentación y comentarios finales
- **Día 7:** Pruebas finales y preparación de entrega

---

**¡Éxito con su proyecto!** 🎉

Si tienen dudas, consulten los notebooks de los Módulos 1-6 o pregunten al instructor.
