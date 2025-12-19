t = [
    ["vacía", "blanco", "vacía", "vacía", "vacía", "negro", "vacía", "blanco"],
    ["blanco", "vacía", "vacía", "negro", "vacía", "vacía", "negro", "vacía"],
    ["vacía", "blanco", "vacía", "vacía", "blanco", "vacía", "vacía", "vacía"],
    ["vacía", "vacía", "blanco", "vacía", "vacía", "negro", "vacía", "blanco"],
    ["vacía", "vacía", "vacía", "blanco", "vacía", "vacía", "vacía", "vacía"],
    ["vacía", "negro", "vacía", "vacía", "blanco", "vacía", "blanco", "vacía"],
    ["negro", "vacía", "vacía", "vacía", "vacía", "negro", "vacía", "blanco"],
    ["vacía", "blanco", "vacía", "negro", "vacía", "vacía", "vacía", "vacía"]
]


# Inicializar contadores
n_blancas = 0
n_negras = 0

# Inicializar fila y columna
fila = 0
col = 0

# Bucle externo: recorrer filas
while fila < 8:
    # Inicializar columna para cada nueva fila
    col = 0

    # Bucle interno: recorrer columnas
    while col < 8:
        # Comprobar si la casilla está ocupada
        if t[fila][col] != "vacía":
            # Identificar el tipo de ficha
            if t[fila][col] == "blanco":
                print(f"(fila: {fila}, columna: {col}) - Ocupada: blanco")
                n_blancas += 1
            else:  # negro
                print(f"(fila: {fila}, columna: {col}) - Ocupada: negro")
                n_negras += 1

        # Incrementar columna
        col = col + 1

    # Incrementar fila
    fila = fila + 1

# Determinar quién va ganando
print("\n--- GANADOR ---")
if n_blancas > n_negras:
    print(f"¡Ganan las fichas blancas! (B: {n_blancas} - N: {n_negras})")
elif n_negras > n_blancas:
    print(f"¡Ganan las fichas negras! (B: {n_blancas} - N: {n_negras})")
else:
    print("¡Empate! Ambos jugadores tienen el mismo número de fichas")