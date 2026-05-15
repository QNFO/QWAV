from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Node:
    value: int = 0
    depth: int = 0
    children: List = field(default_factory=list)
    parent: Optional['Node'] = None
    @property
    def is_leaf(self): return len(self.children) == 0

root = Node(depth=0)
print("Node created OK, is_leaf:", root.is_leaf)
