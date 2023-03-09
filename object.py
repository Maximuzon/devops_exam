from dataclasses import dataclass
from typing import Optional


@dataclass
class Object:
    name: int
    capacity: int
    amount_of_people: int
    is_full: int = 0
    top_level : int = 0
    likes: int = 0
    id: Optional[int] = None