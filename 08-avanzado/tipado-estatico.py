# tipado en variables
a: int = 5
print(a)

b: str = 'Hola mundo'
print(b)

c: bool = True
print(c)

# Tiapdo en funciones
def suma(a: int, b: int) -> int:
    return a + b

print(suma('1', '2'))

# tipado de estructuras de datos
from typing import Dict, List

postives: List[int] = [1, 2, 3, 4, 5]
users: Dict = {
    'colombia': 4,
    'Mexico': 1,
    'Argentina': 3
}

countries: List[Dict[str, str]] = [
    {
        'name': 'Colombia',
        'people': '450000'
    },
    {
        'name': 'Mexico',
        'people': '550000'
    },
    {
        'name': 'Argentina',
        'people': '250000'
    },
]

from typing import Tuple

numbers: Tuple[int, float, int] = (1, 0.5, 1)

# algo mas complejo
CoordinatesType = List[Dict[str, Tuple[int, int]]]
coordinates: CoordinatesType = [
    {
        'coord1': (1,2),
        'coord2': (3,2),
    },
    {
        'coord1': (0,2),
        'coord2': (3,1),
    },
]
