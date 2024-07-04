from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from .osaka import Osaka

from thefuzz import fuzz

__all__ = ("search",)

def search(query: str, osakas: List[Osaka]) -> List[Osaka]:
    return sorted(osakas, key=lambda x: fuzz.ratio(query, x.title), reverse=True)