# ---------------------------------------
# LABERINTO CON BACKTRACKING Y ENERGÍA
# ---------------------------------------

laberinto = [
    [1, 1, 1, 1, 99, 1, 1, 1, "I"],
    [1, 99, 99, 1, 99, 1, 99, 1, 99],
    [1, 1, 1, 1, 99, 1, 1, 1, 99],
    [99, 1, 99, 1, 99, 1, 99, 1, 99],
    [1, 1, 1, -1, 1, 1, 3, 1, 99],
    [-2, 99, 1, 1, 99, 99, 1, 1, 1],
    [1, 1, 99, -1, 1, 1, 1, 1, 99],
    [1, 99, 1, 99, 99, 1, 2, 1, 99],
    ["F", 1, 3, 1, 1, 1, 99, 1, 1]
]

N = 9
energia_inicial = 18

# Movimientos en orden: izquierda, abajo, arriba, derecha
movimientos = [ (0,-1), (1,0), (-1,0), (0,1) ]

# Buscar coordenadas de I y F
def encontrar(inicio):
    for i in range(N):
        for j in range(N):
            if laberinto[i][j] == inicio:
                return (i,j)

ini = encontrar("I")
fin = encontrar("F")

# Matriz para marcar camino
camino = [[0]*N for _ in range(N)]
encontrado = False

def backtracking(x, y, energia):
    global encontrado

    if encontrado:
        return True

    # Si llego al final
    if (x, y) == fin:
        encontrado = True
        return True

    # Explorar movimientos
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N:

            celda = laberinto[nx][ny]

            # Bloqueada
            if celda == 99:
                continue

            # Si ya visité esa celda en esta ruta
            if camino[nx][ny] == 1:
                continue

            # Energía a gastar / recuperar
            gasto = 0
            if isinstance(celda, int):
                gasto = celda

            nueva_energia = energia - gasto

            if nueva_energia < 0:
                continue

            # Marcar movimiento
            camino[nx][ny] = 1

            if backtracking(nx, ny, nueva_energia):
                return True

            camino[nx][ny] = 0  # Desmarcar si no funcionó

    return False


# inicio en camino
camino[ini[0]][ini[1]] = 1

# búsqueda
exito = backtracking(ini[0], ini[1], energia_inicial)

# ---------------------------------------
# RESULTADOS
# ---------------------------------------
print("\nLABERINTO ORIGINAL:")
for fila in laberinto:
    print(fila)

print("\nRESULTADO:")
if exito:
    print("✅ ¡Se encontró un camino con la energía disponible!")
else:
    print("❌ No existe un camino con 18 unidades de energía.")

print("\nCAMINO ENCONTRADO (1 = recorrido):")
for fila in camino:
    print(fila)
