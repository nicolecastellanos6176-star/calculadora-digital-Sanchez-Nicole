# Ejemplos de Ejecución Extendidos - Calculadora Multifuncional

## 📋 Casos de Prueba Completos

### 1. Funciones Matemáticas

#### Prueba: suma(10, 5)
```python
>>> sumar(10, 5)
15.0
```

#### Prueba: restar(20, 8)
```python
>>> restar(20, 8)
12.0
```

#### Prueba: multiplicar(7, 6)
```python
>>> multiplicar(7, 6)
42.0
```

#### Prueba: dividir(100, 4)
```python
>>> dividir(100, 4)
25.0
```

#### Prueba: dividir(10, 0)
```python
>>> dividir(10, 0)
None
# Debe manejar división por cero
```

#### Prueba: modulo(17, 5)
```python
>>> modulo(17, 5)
2.0
```

#### Prueba: potencia(2, 10)
```python
>>> potencia(2, 10)
1024.0
```

#### Prueba: potencia(3, 3)
```python
>>> potencia(3, 3)
27.0
```

---

### 2. Conversión de Sistemas Numéricos

#### Prueba: decimal_a_binario(42)
```python
>>> decimal_a_binario(42)
'101010'
```

#### Prueba: decimal_a_binario(255)
```python
>>> decimal_a_binario(255)
'11111111'
```

#### Prueba: decimal_a_binario(0)
```python
>>> decimal_a_binario(0)
'0'
```

#### Prueba: decimal_a_hexadecimal(255)
```python
>>> decimal_a_hexadecimal(255)
'FF'
```

#### Prueba: decimal_a_hexadecimal(4096)
```python
>>> decimal_a_hexadecimal(4096)
'1000'
```

#### Prueba: binario_a_decimal('1010')
```python
>>> binario_a_decimal('1010')
10
```

#### Prueba: binario_a_decimal('11111111')
```python
>>> binario_a_decimal('11111111')
255
```

#### Prueba: hexadecimal_a_decimal('FF')
```python
>>> hexadecimal_a_decimal('FF')
255
```

#### Prueba: hexadecimal_a_decimal('A0')
```python
>>> hexadecimal_a_decimal('A0')
160
```

---

### 3. Conversión de Unidades de Datos

#### Prueba: bytes_a_kilobytes(1024)
```python
>>> bytes_a_kilobytes(1024)
1.0
```

#### Prueba: bytes_a_kilobytes(2048)
```python
>>> bytes_a_kilobytes(2048)
2.0
```

#### Prueba: kilobytes_a_megabytes(1024)
```python
>>> kilobytes_a_megabytes(1024)
1.0
```

#### Prueba: kilobytes_a_megabytes(2560)
```python
>>> kilobytes_a_megabytes(2560)
2.5
```

#### Prueba: megabytes_a_gigabytes(1024)
```python
>>> megabytes_a_gigabytes(1024)
1.0
```

#### Prueba: megabytes_a_gigabytes(512)
```python
>>> megabytes_a_gigabytes(512)
0.5
```

---

### 4. Sistema de Historial (Listas)

#### Ejemplo de historial después de varias operaciones:
```
HISTORIAL DE OPERACIONES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 2026-02-17 10:23:15 | Suma: 10 + 5 = 15
2. 2026-02-17 10:23:42 | División: 100 / 4 = 25.0
3. 2026-02-17 10:24:05 | Potencia: 2 ^ 10 = 1024
4. 2026-02-17 10:24:30 | Conversión: 42 (decimal) = 101010 (binario)
5. 2026-02-17 10:25:10 | Conversión: 1024 MB = 1.0 GB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 5. Persistencia en Archivos

#### Contenido de `datos/historial.txt`:
```
2026-02-17 10:23:15 | Suma: 10 + 5 = 15
2026-02-17 10:23:42 | División: 100 / 4 = 25.0
2026-02-17 10:24:05 | Potencia: 2 ^ 10 = 1024
2026-02-17 10:24:30 | Conversión: 42 (decimal) = 101010 (binario)
2026-02-17 10:25:10 | Conversión: 1024 MB = 1.0 GB
2026-02-17 10:25:45 | Multiplicación: 7 × 6 = 42
2026-02-17 10:26:10 | Conversión: FF (hex) = 255 (decimal)
```

---

## 🎯 Casos de Prueba por Característica

### Test Suite 1: Operaciones Básicas
```
✓ sumar(15, 27) = 42
✓ restar(100, 45) = 55
✓ multiplicar(12, 8) = 96
✓ dividir(100, 4) = 25.0
✓ dividir(10, 0) = None (manejo de error)
✓ modulo(17, 5) = 2
✓ potencia(3, 4) = 81
```

### Test Suite 2: Conversiones Numéricas
```
✓ decimal_a_binario(10) = "1010"
✓ decimal_a_binario(255) = "11111111"
✓ decimal_a_hexadecimal(255) = "FF"
✓ decimal_a_hexadecimal(4096) = "1000"
✓ binario_a_decimal("1111") = 15
✓ hexadecimal_a_decimal("A") = 10
```

### Test Suite 3: Conversiones de Unidades
```
✓ bytes_a_kilobytes(1024) = 1.0
✓ bytes_a_kilobytes(2048) = 2.0
✓ kilobytes_a_megabytes(1024) = 1.0
✓ kilobytes_a_megabytes(2560) = 2.5
✓ megabytes_a_gigabytes(1024) = 1.0
✓ megabytes_a_gigabytes(512) = 0.5
✓ gigabytes_a_megabytes(2) = 2048
✓ megabytes_a_kilobytes(5) = 5120
✓ kilobytes_a_bytes(1) = 1024
```

### Test Suite 4: Gestión de Historial
```
✓ Agregar operación al historial
✓ Mostrar historial cuando está vacío
✓ Mostrar historial con 5 operaciones
✓ Mostrar historial con más de 10 operaciones (solo últimas 10)
✓ Limpiar historial
✓ Verificar que historial está vacío después de limpiar
```

### Test Suite 5: Persistencia de Archivos
```
✓ Guardar historial vacío
✓ Guardar historial con 5 operaciones
✓ Cargar historial de archivo existente
✓ Cargar cuando no existe archivo (no error)
✓ Verificar formato correcto en archivo
✓ Verificar que se crea carpeta "datos" si no existe
```

### Test Suite 6: Validación de Entrada
```
✓ validar_numero() rechaza texto
✓ validar_numero() acepta enteros
✓ validar_numero() acepta decimales
✓ validar_numero() acepta negativos
✓ Menú rechaza opciones inválidas
✓ Mensajes de error son claros
```

---

## 📊 Matriz de Pruebas Completa

| Función | Input | Expected Output | Status |
|---------|-------|----------------|--------|
| `sumar(10, 5)` | 10, 5 | 15.0 | ✓ |
| `sumar(-5, 3)` | -5, 3 | -2.0 | ✓ |
| `restar(20, 8)` | 20, 8 | 12.0 | ✓ |
| `multiplicar(7, 6)` | 7, 6 | 42.0 | ✓ |
| `dividir(100, 4)` | 100, 4 | 25.0 | ✓ |
| `dividir(10, 0)` | 10, 0 | None | ✓ |
| `modulo(17, 5)` | 17, 5 | 2.0 | ✓ |
| `potencia(2, 10)` | 2, 10 | 1024.0 | ✓ |
| `decimal_a_binario(42)` | 42 | "101010" | ✓ |
| `decimal_a_binario(255)` | 255 | "11111111" | ✓ |
| `decimal_a_hexadecimal(255)` | 255 | "FF" | ✓ |
| `binario_a_decimal("1010")` | "1010" | 10 | ✓ |
| `hexadecimal_a_decimal("FF")` | "FF" | 255 | ✓ |
| `bytes_a_kilobytes(2048)` | 2048 | 2.0 | ✓ |
| `kilobytes_a_megabytes(1024)` | 1024 | 1.0 | ✓ |
| `megabytes_a_gigabytes(512)` | 512 | 0.5 | ✓ |

---

## 🎬 Ejemplo de Sesión Completa

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  CALCULADORA MULTIFUNCIONAL - Versión Avanzada          ║
║                                                          ║
║  Con historial, funciones y persistencia de datos       ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

✅ Historial cargado desde archivo.

============================================================
   CALCULADORA MULTIFUNCIONAL v2.0
============================================================

MENÚ PRINCIPAL:
1. Calculadora Básica
2. Conversor de Unidades de Datos
3. Calculadora de Sistemas Numéricos
4. Ver Historial
5. Limpiar Historial
6. Salir
------------------------------------------------------------

Seleccione una opción (1-6): 1

--- CALCULADORA BÁSICA ---
1. Suma
2. Resta
3. Multiplicación
4. División
5. Módulo (residuo)
6. Potencia
7. Volver al menú principal

Seleccione operación: 6

Ingrese el primer número: 2
Ingrese el segundo número: 10

━━━━━━━━━━━━━━━━━━━━━━
  RESULTADO
━━━━━━━━━━━━━━━━━━━━━━
2 ^ 10 = 1024.0
━━━━━━━━━━━━━━━━━━━━━━

✅ Operación agregada al historial.

Presione Enter para continuar...

[Volver al menú]

Seleccione una opción (1-6): 4

HISTORIAL DE OPERACIONES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 2026-02-17 10:23:15 | Suma: 10 + 5 = 15
2. 2026-02-17 10:23:42 | División: 100 / 4 = 25.0
3. 2026-02-17 10:24:05 | Potencia: 2 ^ 10 = 1024
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Presione Enter para continuar...

Seleccione una opción (1-6): 6

💾 Guardando historial...
✅ Historial guardado en datos/historial.txt

¡Gracias por usar la Calculadora Multifuncional!
¡Hasta pronto! 👋

Programa terminado.
```

---

## 📁 Estructura de Datos Esperada

### Archivo: datos/historial.txt
```
2026-02-17 10:23:15 | Suma: 10 + 5 = 15
2026-02-17 10:23:42 | División: 100 / 4 = 25.0
2026-02-17 10:24:05 | Potencia: 2 ^ 10 = 1024
```

### Archivo: .gitignore
```
__pycache__/
*.pyc
.DS_Store
*.txt.bak
datos/*.txt.bak
```

---

## ✅ Checklist de Verificación

### Funcionalidad Básica
- [ ] Las 6 operaciones matemáticas funcionan
- [ ] División por cero está manejada
- [ ] 4 conversiones de sistemas numéricos funcionan
- [ ] 6 conversiones de unidades funcionan

### Sistema de Historial
- [ ] Se puede agregar al historial
- [ ] Se puede ver el historial
- [ ] Se puede limpiar el historial
- [ ] Límite de 10 operaciones funciona

### Persistencia
- [ ] Historial se guarda al salir
- [ ] Historial se carga al iniciar
- [ ] Carpeta "datos" se crea automáticamente
- [ ] Formato del archivo es correcto

### Código
- [ ] Todas las funciones tienen docstrings
- [ ] Variables tienen nombres descriptivos
- [ ] Código está comentado
- [ ] No hay código repetido

### Git/GitHub
- [ ] Repositorio está en GitHub
- [ ] README.md está completo
- [ ] .gitignore está configurado
- [ ] Mínimo 15 commits de 3 personas
- [ ] Mensajes de commit son descriptivos

---

## 🔍 Casos de Prueba Edge

### Números Especiales
```python
# Cero
sumar(0, 0) → 0
dividir(0, 5) → 0.0

# Negativos
sumar(-5, -3) → -8
multiplicar(-2, 3) → -6
potencia(-2, 3) → -8

# Decimales
sumar(3.5, 2.7) → 6.2
dividir(7, 3) → 2.333...
```

### Strings en Conversiones
```python
# Binario inválido
binario_a_decimal("102") → Error o manejo especial

# Hexadecimal con minúsculas
hexadecimal_a_decimal("ff") → 255 (debe aceptar)
hexadecimal_a_decimal("FF") → 255
```

### Límites del Sistema
```python
# Números muy grandes
potencia(10, 100) → 10000000000...
decimal_a_binario(1000000) → String largo

# Historial al límite
Agregar 15 operaciones → Solo últimas 10 se guardan
```

---

**Nota:** Use estos casos de prueba para verificar que su calculadora funciona correctamente en todos los escenarios.
