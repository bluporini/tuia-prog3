"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def minimax_max(tateti: Tateti, estado: List[List[str]]) -> int:
    """
    Estrategia minimax-max: Calcula recursivamente el valor minimax en un nodo MAX

    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero

    Returns:
        int: Valor minimax en un nodo MAX

    """

    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)
    valor = -1

    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = max(valor, minimax_min(tateti, sucesor))

    return valor

def minimax_min(tateti: Tateti, estado: List[List[str]]) -> int:
    """
    Estrategia minimax-min:  Calcula recursivamente el valor minimax en un nodo MIN

    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero

    Returns:
        int: Valor minimax en un nodo MIN
    """

    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)
    valor = 2 # No hay utilidad mayor o igual a 2

    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = min(valor, minimax_max(tateti, sucesor))

    return valor


def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    """

    
    if tateti.jugador(estado) == JUGADOR_MAX:
        sucesor = {}
        for accion in tateti.acciones(estado):
            sucesor[accion] = minimax_min(tateti, tateti.resultado(estado, accion))

        return max(sucesor, key=sucesor.get)
    
    if tateti.jugador(estado) == JUGADOR_MIN:
        sucesor = {}
        for accion in tateti.acciones(estado):
            sucesor[accion] = minimax_max(tateti, tateti.resultado(estado, accion))

        return min(sucesor, key=sucesor.get)

    raise NotImplementedError(
        "\n" + "="*60 +
        "\n🚫 ALGORITMO MINIMAX NO IMPLEMENTADO" +
        "\n" + "="*60 +
        "\n\nPara usar la estrategia Minimax debe implementarla primero." +
        "\n\nInstrucciones:" +
        "\n1. Abra el archivo 'estrategias.py'" +
        "\n2. Busque la función 'estrategia_minimax()'" +
        "\n3. Elimine la línea 'raise NotImplementedError(...)'" +
        "\n4. Implemente el algoritmo minimax" +
        "\n\nMientras tanto, use la 'Estrategia Aleatoria'." +
        "\n" + "="*60
    )
