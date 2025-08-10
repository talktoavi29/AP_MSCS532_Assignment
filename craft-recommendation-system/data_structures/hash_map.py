# data_structures/hash_map.py
from __future__ import annotations
from typing import Any, Optional, Tuple, List

_TOMBSTONE = object()

class OpenAddressMap:
    """
    Key -> value mapping using double hashing.
    Auto-resizes at load factor ~0.75. Supports put/get/delete.
    """
    def __init__(self, initial_capacity: int = 1024) -> None:
        cap = 1
        while cap < initial_capacity:
            cap <<= 1
        self._keys: List[Optional[Any]] = [None] * cap
        self._vals: List[Optional[Any]] = [None] * cap
        self._size = 0  # number of real entries (excludes tombstones)

    @property
    def capacity(self) -> int:
        return len(self._keys)

    def _h1(self, k: Any) -> int:
        return (hash(k) & 0x7FFFFFFF) % self.capacity

    def _h2(self, k: Any) -> int:
        # must be non-zero and co-prime with capacity (power of two => odd step works)
        return ((hash((k, 0x9E3779B97F4A7C15)) & 0x7FFFFFFF) % (self.capacity - 1)) | 1

    def _probe(self, key: Any) -> Tuple[int, bool]:
        i = 0
        first_tomb = -1
        h1 = self._h1(key)
        h2 = self._h2(key)
        while i < self.capacity:
            j = (h1 + i * h2) & (self.capacity - 1)
            k = self._keys[j]
            if k is None:
                return (first_tomb if first_tomb != -1 else j, False)
            if k is _TOMBSTONE:
                if first_tomb == -1:
                    first_tomb = j
            elif k == key:
                return (j, True)
            i += 1
        raise RuntimeError("Hashtable full (should resize earlier).")

    def _resize(self, new_cap: int) -> None:
        old_k, old_v = self._keys, self._vals
        self._keys = [None] * new_cap
        self._vals = [None] * new_cap
        self._size = 0
        for k, v in zip(old_k, old_v):
            if k is not None and k is not _TOMBSTONE:
                self.put(k, v)

    def _maybe_resize(self) -> None:
        if (self._size + 1) / self.capacity >= 0.75:
            self._resize(self.capacity << 1)

    def put(self, key: Any, value: Any) -> None:
        self._maybe_resize()
        idx, found = self._probe(key)
        if not found and (self._keys[idx] is None or self._keys[idx] is _TOMBSTONE):
            self._size += 1
        self._keys[idx] = key
        self._vals[idx] = value

    def get(self, key: Any, default: Any = None) -> Any:
        idx, found = self._probe(key)
        return self._vals[idx] if found else default

    def delete(self, key: Any) -> bool:
        idx, found = self._probe(key)
        if not found:
            return False
        self._keys[idx] = _TOMBSTONE
        self._vals[idx] = None
        self._size -= 1
        return True
