# =====================================================================
# CURSO: FUNDAMENTOS DE PROGRAMACIÓN (213022)
# FASE 5: EVALUACIÓN FINAL POA
# PROBLEMA 1: EVALUACIÓN DE COMPROMISO DE SESIONES DE CLIENTES
# PROGRAMA: INGENIERÍA DE SISTEMAS - ECBTI
# =====================================================================

# MÓDULO (FUNCIÓN): Calcular la clasificación de compromiso de una sesión
def calcular_clasificacion_compromiso(duracion, clics):
    """
    Evalúa el nivel de compromiso basado en la duración y cantidad de clics.
    Lógica de negocio:
    - "Alto": Duración > 180s Y Clics > 8
    - "Bajo": Duración < 60s O Clics < 3
    - "Medio": En cualquier otro caso
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# PROCEDIMIENTO PRINCIPAL: Controla el flujo de la aplicación
def main():
    print("=========================================================")
    print("      INFORME DE EVALUACIÓN DE COMPROMISO DE CLIENTES     ")
    print("=========================================================\n")
    
    # REQUISITO: Matriz con al menos 5 filas de datos [ID Cliente, Duración(s), Clics]
    matriz_sesiones = [
        ["CLI-101", 240, 12],  # Cumple Duracion > 180 y Clics > 8 -> Alto
        ["CLI-102", 45, 5],    # Cumple Duracion < 60 -> Bajo
        ["CLI-103", 120, 6],   # No cumple extremos -> Medio
        ["CLI-104", 200, 2],   # Cumple Clics < 3 -> Bajo
        ["CLI-105", 150, 9]    # No cumple extremos -> Medio
    ]
    
    # Encabezado estético de la salida en consola
    print(f"{'ID CLIENTE':<15}{'DURACIÓN (s)':<15}{'CLICS':<12}{'CLASIFICACIÓN'}")
    print("-" * 55)
    
    # REQUISITO: Procesar la matriz utilizando estructuras repetitivas (Ciclo For)
    for sesion in matriz_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        
        # Llamada al módulo que procesa la lógica de negocio
        clasificacion = calcular_clasificacion_compromiso(duracion, clics)
        
        # Impresión formateada de los resultados
        print(f"{id_cliente:<15}{duracion:<15}{clics:<12}{clasificacion}")

    print("-" * 55)
    print("Proceso de auditoría finalizado con éxito.")

# Punto de entrada estándar de Python para ejecutar el programa
if __name__ == "__main__":
    main()