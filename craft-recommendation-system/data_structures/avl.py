# data_structures/avl.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Iterable, List, Optional, Tuple

@dataclass
class _Node:
    key: float
    value: Any
    left: Optional["_Node"] = None
    right: Optional["_Node"] = None
    height: int = 1

def _h(n: Optional[_Node]) -> int:
    return n.height if n else 0

def _bf(n: Optional[_Node]) -> int:
    return _h(n.left) - _h(n.right) if n else 0

def _rotate_left(z: _Node) -> _Node:
    y = z.right
    T2 = y.left if y else None
    y.left = z
    z.right = T2
    z.height = 1 + max(_h(z.left), _h(z.right))
    y.height = 1 + max(_h(y.left), _h(y.right))
    return y

def _rotate_right(z: _Node) -> _Node:
    y = z.left
    T3 = y.right if y else None
    y.right = z
    z.left = T3
    z.height = 1 + max(_h(z.left), _h(z.right))
    y.height = 1 + max(_h(y.left), _h(y.right))
    return y

class AVLTree:
    """
    Stores (key -> value). Keys are ratings by default (float).
    Provides insert/update, get, and range/ordered queries.
    """
    def __init__(self, compare: Optional[Callable[[float, float], int]] = None) -> None:
        self._root: Optional[_Node] = None
        self._compare = compare

    def _cmp(self, a: float, b: float) -> int:
        if self._compare:
            return self._compare(a, b)
        return (a > b) - (a < b)

    def insert(self, key: float, value: Any) -> None:
        def _insert(n: Optional[_Node], k: float, v: Any) -> _Node:
            if not n:
                return _Node(k, v)
            if self._cmp(k, n.key) < 0:
                n.left = _insert(n.left, k, v)
            elif self._cmp(k, n.key) > 0:
                n.right = _insert(n.right, k, v)
            else:
                # update on key collision
                n.value = v
                return n

            n.height = 1 + max(_h(n.left), _h(n.right))
            bf = _bf(n)

            # LL
            if bf > 1 and self._cmp(k, n.left.key) < 0:
                return _rotate_right(n)
            # RR
            if bf < -1 and self._cmp(k, n.right.key) > 0:
                return _rotate_left(n)
            # LR
            if bf > 1 and self._cmp(k, n.left.key) > 0:
                n.left = _rotate_left(n.left)
                return _rotate_right(n)
            # RL
            if bf < -1 and self._cmp(k, n.right.key) < 0:
                n.right = _rotate_right(n.right)
                return _rotate_left(n)
            return n

        self._root = _insert(self._root, key, value)

    def get(self, key: float) -> Optional[Any]:
        n = self._root
        while n:
            c = self._cmp(key, n.key)
            if c == 0:
                return n.value
            n = n.left if c < 0 else n.right
        return None

    def inorder(self, reverse: bool = False) -> Iterable[Tuple[float, Any]]:
        stack: List[_Node] = []
        n = self._root
        while stack or n:
            while n:
                stack.append(n)
                n = n.right if reverse else n.left
            n = stack.pop()
            yield (n.key, n.value)
            n = n.left if reverse else n.right

    def top_k(self, k: int) -> List[Tuple[float, Any]]:
        # highest keys first
        out: List[Tuple[float, Any]] = []
        for key, val in self.inorder(reverse=True):
            out.append((key, val))
            if len(out) == k:
                break
        return out