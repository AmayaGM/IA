#Amaya Galaviz Maribel
#IA_Práctica 1 - IA Busqueda
from collections import deque
import numpy as np
import time

# Comienza el contador y realiza alguna tarea
start_time = time.time()
time.sleep(5)  # Espera 5 segundos
elapsed_time = time.time() - start_time

# Función para encontrar la posición de la casilla con valor 0 en la matriz
def find_zero(matrix):
    return tuple(np.where(matrix == 0))

# Función para realizar un movimiento en el rompecabezas
def move(matrix, direction):
    zero_pos = find_zero(matrix)

    if direction == 'Arriba':
        new_pos = (zero_pos[0] - 1, zero_pos[1])
    elif direction == 'Abajo':
        new_pos = (zero_pos[0] + 1, zero_pos[1])
    elif direction == 'Izquierda':
        new_pos = (zero_pos[0], zero_pos[1] - 1)
    elif direction == 'Derecha':
        new_pos = (zero_pos[0], zero_pos[1] + 1)
    else:
        raise ValueError("Dirección no válida")

    # Intercambia la posición de la casilla vacía (0) con la casilla adyacente
    matrix[zero_pos], matrix[new_pos] = matrix[new_pos], matrix[zero_pos]

# Función para imprimir el estado del rompecabezas
def imprimir(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Función para resolver el rompecabezas utilizando BFS
def solve_puzzle(initial_state, goal_state):
    initial_state = np.array(initial_state)
    goal_state = np.array(goal_state)
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if np.array_equal(current_state, goal_state):
            return path

        zero_pos = find_zero(current_state)

        for direction in ['Arriba', 'Abajo', 'Izquierda', 'Derecha']:
            new_pos = zero_pos

            if direction == 'Arriba':
                new_pos = (zero_pos[0] - 1, zero_pos[1])
            elif direction == 'Abajo':
                new_pos = (zero_pos[0] + 1, zero_pos[1])
            elif direction == 'Izquierda':
                new_pos = (zero_pos[0], zero_pos[1] - 1)
            elif direction == 'Derecha':
                new_pos = (zero_pos[0], zero_pos[1] + 1)

            # Verifica que el movimiento sea válido
            if (0 <= new_pos[0] < 3) and (0 <= new_pos[1] < 3):
                new_state = current_state.copy()
                new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]

                # Si el nuevo estado no ha sido visitado, lo agrega a la cola y al conjunto de visitados
                if tuple(map(tuple, new_state)) not in visited:
                    queue.append((new_state, path + [direction]))
                    visited.add(tuple(map(tuple, new_state)))

    return []

# Estado inicial y estado objetivo del rompecabezas
initial_state = np.array([[7, 2, 4], [5, 0, 6], [8, 3, 1]])
goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

# Imprime el estado inicial del rompecabezas
imprimir(initial_state)

# Resuelve el rompecabezas y muestra los pasos si se encuentra una solución
solution = solve_puzzle(initial_state, goal_state)

if solution:
    print("Solución encontrada:")
    for step, move_direction in enumerate(solution, 1):
        print(f"Paso {step}: Mover {move_direction}")
        move(initial_state, move_direction)
        imprimir(initial_state)
else:
    print("No se encontró una solución.")

# Imprime el tiempo transcurrido
print(f"Tiempo transcurrido: {elapsed_time} segundos")


