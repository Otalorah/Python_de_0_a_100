# ==========================================
# EJERCICIO 1: Conversión y Constructores
# ==========================================

# 1. Convierte el texto "inf" en un número flotante especial usando float()
infinito = float("inf")

# 2. Convierte el número decimal 7.8 en un número entero utilizando int() (recuerda que trunca la parte decimal)
numero_entero = int(7.8)
print("Entero truncado:", numero_entero)


# ==========================================
# EJERCICIO 2: Operaciones
# ==========================================

a = 17
b = 5

# 3. Calcula la división entera de a entre b utilizando el operador correspondiente
resultado_division_entera = a // b

# 4. Obtiene el residuo de a entre b
residuo = a % b

# 5. Calcula la siguiente operacion matematica: (((x+y)**123) mod 23) - 72639162 + (x // b)**(x**y)**ya
valor = (((a + b) ** 123) % 23) - 72639162 + (a // b) ** (a**b) ** b
print("Resultado de la operacion:", valor)


# ==========================================
# EJERCICIO 3: Números Complejos
# ==========================================

# 6. Declara un número complejo que tenga 4 como parte real y 2 como parte imaginaria
complejo = complex(4, 2)

# 7. Extrae únicamente la parte imaginaria del número complejo anterior usando el atributo correspondiente
parte_imaginaria = complejo.imag
print("Parte imaginaria:", parte_imaginaria)

"""
GANADORES EJERCICIO ACTUAL | Ejercicio 2
====================================================
N/A. Carloss_ | Incorrecto
2. Alan     | 20252020082 | Correcto
3. Samuel Castañeda| 20262020152 | Correcto
4. Tat | 20262020136 | Correcto

GANADORES ANTERIOR EJERCICIO | Ejercicio 1
====================================================
1. Edward Hernandez | 20261020055 | Correcto
2. Uriel Ramos | 80919352 | Correcto
N/A. Yasser Camacho | Incorrecto
3. Edder | EDDeR carrion: 1018436366 |Correcto 

"""
