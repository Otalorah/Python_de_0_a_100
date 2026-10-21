problema = """
OBJETIVO:
Construir un módulo de monedero digital que aplique los conceptos centrales de
Testing_Errores.ipynb: jerarquía y creación de excepciones personalizadas, enriquecimiento
con .add_note(), control try-except-else-finally, persistencia segura con pathlib + json (UTF-8)
y pruebas unitarias automatizadas con unittest en directorios aislados (tempfile).


1. EXCEPCIÓN PERSONALIZADA:
   - Define la clase `FondosInsuficientesError`, la cual debe heredar de `ValueError`.

2. FUNCIÓN DE PROCESAMIENTO:
   - Firma requerida:
     `procesar_transaccion(ruta_json: Path, usuario: str, monto: float | int, operacion: str) -> float`

   - Validaciones de entrada:
     * Si `usuario` no es string o está vacío tras quitar espacios (.strip()), lanzar `ValueError`.
     * Si `monto` es booleano (`isinstance(monto, bool)`) o no es numérico (`int` o `float`), lanzar `TypeError`.
     * Si `monto <= 0`, lanzar `ValueError("El monto debe ser estrictamente positivo.")`.
     * Si `operacion` no es "deposito" ni "retiro", lanzar `ValueError(f"Operación no permitida: {operacion}")`.

   - Persistencia Segura (pathlib.Path + json):
     * Cargar el archivo de cuentas indicado en `ruta_json` usando `encoding="utf-8"`.
     * Si el archivo aún no existe (`FileNotFoundError`), inicializar el diccionario de cuentas vacío `{}`.
     * Si la operación es "deposito":
       - Incrementar el saldo actual del usuario (si es usuario nuevo, empieza en 0.0).
     * Si la operación es "retiro":
       - Si el saldo actual es menor que el monto a retirar, crear una instancia de
         `FondosInsuficientesError("Saldo no disponible para retiro.")`.
       - ANTES de lanzar la excepción, agregar una nota con `.add_note()` indicando:
         f"Detalle: Usuario '{usuario}' tiene saldo ${saldo_actual:.2f} e intentó retirar ${float(monto):.2f}"
       - Lanzar la excepción.
       - Si hay saldo suficiente, descontar el monto.
     * Guardar el diccionario de cuentas actualizado en `ruta_json` con `indent=4` y `ensure_ascii=False`.
     * Retornar el saldo final del usuario.

   - Control de Flujo (try - except - else - finally):
     * Incluir la cláusula `finally` para registrar en consola una bitácora de auditoría:
       f" Transacción concluida para usuario: '{usuario}'."

3. SUITE DE PRUEBAS UNITARIAS (unittest):
   - Crear una clase `TestMonederoDigital(unittest.TestCase)` que use `tempfile.TemporaryDirectory`
     en `setUp()` para no ensuciar el disco real, y limpiarlo en `tearDown()`.
   - Debe implementar las siguientes pruebas:
     a) `test_deposito_exitoso`: Verifica que el saldo aumente y se guarde en disco con `assertEqual`.
     b) `test_retiro_con_fondos_insuficientes`: Verifica con `assertRaises(FondosInsuficientesError)`
        que se lance la excepción correcta y que el atributo `__notes__` contenga la nota explicativa.
     c) `test_monto_negativo_o_cero_invalido`: Verifica con `assertRaises(ValueError)` que se rechacen montos <= 0.
     d) `test_tipo_monto_invalido`: Verifica con `assertRaises(TypeError)` al enviar textos o booleanos como monto.
"""
