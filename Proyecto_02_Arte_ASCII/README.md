# 🎨 Proyecto 2: Generador de Arte ASCII Animado

## 🎯 Objetivo del Proyecto

Crear un programa que genere arte ASCII y animaciones simples en la terminal, utilizando loops, strings y control de tiempo. Los estudiantes aprenderán a crear visualizaciones creativas usando solo caracteres de texto.

**Carrera:** Animación
**Duración:** 2 semanas
**Equipo:** 3 estudiantes

## 📚 Conceptos de Python Utilizados

- Variables y strings
- Operadores de concatenación y repetición de strings (* y +)
- Loops anidados (for dentro de for)
- Range() con diferentes parámetros
- Condicionales para patrones
- **Listas** para almacenar galería de arte
- **Funciones** para generar cada patrón/animación
- **Archivos de texto** para guardar/cargar arte ASCII
- Caracteres especiales (\n, \t, espacios)
- Formateo avanzado de strings

## 🎓 Competencias a Desarrollar

1. Visualización y pensamiento espacial
2. Creación de patrones usando loops
3. Manipulación avanzada de strings
4. Diseño de interfaces visuales basadas en texto
5. Simulación de movimiento en la terminal
6. Creatividad en programación

## 📋 Requisitos Funcionales

### ✅ Requisitos Mínimos (Obligatorios)

1. **Menú de Galería Interactivo**
   - Mostrar al menos 6 opciones de arte/animación
   - Permitir al usuario seleccionar qué ver
   - Opción para regresar al menú
   - Loop continuo hasta que el usuario decida salir

2. **Tres Funciones de Patrones Geométricos**
   - `generar_triangulo(altura)` - Triángulo de caracteres
   - `generar_cuadrado(lado)` - Cuadrado con bordes
   - `generar_piramide(altura)` - Pirámide centrada
   - Cada función debe recibir parámetros y retornar el string del arte

3. **Dos Funciones de Texto Artístico**
   - `generar_banner(texto)` - Banner con nombre del usuario
   - `generar_marco(texto, estilo)` - Marco decorativo
   - Al menos 2 estilos diferentes de decoración

4. **Dos Funciones de Animación**
   - `animar_barra_progreso()` - Barra de progreso animada
   - `animar_texto_movil(texto)` - Texto moviéndose
   - Usar loops para crear la ilusión de movimiento

5. **Función de Tabla de Multiplicar Visual**
   - `generar_tabla(numero)` - Tabla decorada del 1-10
   - Formato organizado y alineado

6. **Galería con Listas**
   - Almacenar las creaciones del usuario en una lista
   - Función para ver galería guardada
   - Opción para limpiar galería

7. **Persistencia de Arte (Archivos)**
   - Guardar arte creado en archivos `.txt` en carpeta `datos/`
   - Cargar galería al iniciar
   - Exportar arte individual a archivo

### 🌟 Características Opcionales (Extra)

- Galería con categorías (geométrico, artístico, animaciones)
- Exportar múltiples artes a un solo archivo con separadores
- Importar arte desde archivo externo
- Estadísticas de la galería (patrones más creados, total de arte)
- Búsqueda en galería por palabra clave
- Animación de "lluvia" de caracteres (estilo Matrix)
- Arte generativo guardado automáticamente
- Sistema de "favoritos" con archivo separado
- Historial de parámetros usados (altura, ancho, estilo)

## 👥 Distribución de Trabajo Sugerida

### Estudiante 1: Menú y Patrones Geométricos
- Estructura del menú principal
- Triángulo de caracteres
- Cuadrado/rectángulo con bordes
- Pirámide o rombo

### Estudiante 2: Generadores de Texto Artístico
- Banner con nombre del usuario
- Marco decorativo alrededor de texto
- Diferentes estilos de decoración
- Tabla de multiplicar visual

### Estudiante 3: Animaciones
- Barra de progreso animada
- Segunda animación (pelota, texto móvil)
- Funciones de retraso/pausa
- Características adicionales opcionales

## 📊 Ejemplo de Ejecución

```
╔═══════════════════════════════════════════════╗
║     🎨 GALERÍA DE ARTE ASCII v1.0 🎨         ║
║     Creado por: [Equipo de Animación]        ║
╚═══════════════════════════════════════════════╝

GALERÍA:
1. Patrones Geométricos
2. Generador de Banner
3. Marcos Decorativos
4. Animaciones
5. Tabla de Multiplicar Visual
6. Salir

Seleccione una opción: 1

--- PATRONES GEOMÉTRICOS ---
1. Triángulo
2. Cuadrado
3. Pirámide
4. Volver

Seleccione un patrón: 3

¿Qué altura desea la pirámide? (3-15): 5

    *
   ***
  *****
 *******
*********

¿Ver otro patrón? (s/n): n

[Volver al menú principal...]
```

**Ejemplo de Animación (Barra de Progreso):**
```
Procesando...
[■■■■■■■■■■----------] 50%
[■■■■■■■■■■■■■■■■----] 80%
[■■■■■■■■■■■■■■■■■■■■] 100% ¡Completo!
```

## 📝 Rúbrica de Evaluación (100 puntos)

### Funcionalidad (40 puntos)
- [ ] Menú principal funciona correctamente (5 pts)
- [ ] Tres patrones geométricos funcionan (12 pts)
- [ ] Dos generadores de texto artístico funcionan (8 pts)
- [ ] Al menos una animación funciona (10 pts)
- [ ] Tabla de multiplicar visual funciona (5 pts)

### Código (30 puntos)
- [ ] Uso correcto de loops anidados (10 pts)
- [ ] Manipulación efectiva de strings (8 pts)
- [ ] Uso apropiado de condicionales (5 pts)
- [ ] Código organizado y legible (4 pts)
- [ ] Variables con nombres descriptivos (3 pts)

### Creatividad y Estética (15 puntos)
- [ ] Patrones visualmente atractivos (5 pts)
- [ ] Diseño creativo de arte ASCII (5 pts)
- [ ] Características adicionales únicas (5 pts)

### Documentación y Presentación (15 puntos)
- [ ] Comentarios explicando el código (5 pts)
- [ ] README del equipo con instrucciones (5 pts)
- [ ] Presentación clara y organizada (3 pts)
- [ ] Screenshots o ejemplos visuales (2 pts bonus)

## 🚀 Entregables

1. **Archivo:** `arte_ascii_equipo_[nombres].py`
2. **README del equipo:** `README_EQUIPO.md` con:
   - Nombres de los integrantes y roles
   - Descripción de cada patrón/animación
   - Instrucciones de uso
   - Screenshots (capturas de pantalla) del output
3. **Ejemplos visuales:** Archivo de texto con ejemplos de salidas
4. **Comentarios** en el código

## 💡 Consejos y Técnicas

### 1. Creación de Patrones con Loops
```python
# Triángulo simple
altura = 5
for i in range(1, altura + 1):
    print("*" * i)

# Salida:
# *
# **
# ***
# ****
# *****
```

### 2. Centrar Patrones
```python
# Pirámide centrada
altura = 5
for i in range(1, altura + 1):
    espacios = " " * (altura - i)
    estrellas = "*" * (2 * i - 1)
    print(espacios + estrellas)

# Salida:
#     *
#    ***
#   *****
#  *******
# *********
```

### 3. Bordes y Marcos
```python
ancho = 20
print("╔" + "═" * ancho + "╗")
print("║" + " " * ancho + "║")
print("╚" + "═" * ancho + "╝")
```

### 4. Simular Animación (sin módulos externos)
```python
# Usar loops vacíos para crear retrasos
for _ in range(100000000):
    pass  # Retraso simple

# O limpiar la línea anterior
print("Cargando...", end="\r")
for i in range(100):
    # Actualizar el mismo lugar
    print(f"Progreso: {i}%", end="\r")
```

### 5. Caracteres Útiles para Arte ASCII
```
Bordes: ═ ║ ╔ ╗ ╚ ╝ ─ │ ┌ ┐ └ ┘
Relleno: █ ▀ ▄ ▌ ▐ ░ ▒ ▓
Decorativos: ★ ☆ ♥ ♦ ♣ ♠ • ◦ ○ ● ◘ ◙
Flechas: ← → ↑ ↓ ↔ ↕
Densidad: . : ; + * # @
```

## 📖 Inspiración y Referencias

### Ejemplo 1: Letra Grande (A)
```
  AAA
 A   A
AAAAAAA
A     A
A     A
```

### Ejemplo 2: Corazón
```
 ♥♥   ♥♥
♥  ♥ ♥  ♥
♥   ♥   ♥
 ♥     ♥
  ♥   ♥
   ♥ ♥
    ♥
```

### Ejemplo 3: Tabla Decorada
```
╔════════════════════════╗
║  TABLA DEL 5           ║
╠════════════════════════╣
║  5 x  1 =  5           ║
║  5 x  2 = 10           ║
║  5 x  3 = 15           ║
║  ...                   ║
╚════════════════════════╝
```

## 📅 Cronograma Sugerido

### Semana 1
- **Día 1-2:** Planificación, experimentar con patrones simples
- **Día 3-4:** Desarrollo de patrones geométricos y texto artístico
- **Día 5-6:** Desarrollo de animaciones básicas
- **Día 7:** Primera integración y pruebas

### Semana 2
- **Día 1-2:** Refinamiento de patrones, mejorar estética
- **Día 3-4:** Añadir características opcionales creativas
- **Día 5:** Documentación, capturas de pantalla
- **Día 6-7:** Pulir detalles finales y preparar presentación

## 🎨 Desafío Creativo

El equipo que cree el arte ASCII más impresionante o la animación más creativa usando **solo** los conceptos de Módulos 1-6 recibirá puntos extra.

Ideas para destacar:
- Arte ASCII de un objeto complejo (computadora, animal, edificio)
- Animación que cuente una pequeña historia
- Efecto visual sorprendente (ej: texto que "explota" o "se construye")
- Generador que permita al usuario crear su propio arte

---

**¡Liberen su creatividad con código!** 🎨✨

Recuerden: Las limitaciones fomentan la creatividad. Usando solo loops, strings y condicionales, pueden crear cosas asombrosas.
