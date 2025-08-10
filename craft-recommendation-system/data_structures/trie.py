# data_structures/trie.py
from __future__ import annotations
from typing import List, Tuple

class Edge:
    __slots__ = ("label", "child")
    def __init__(self, label: str, child: "CTrieNode") -> None:
        self.label = label
        self.child = child

class CTrieNode:
    __slots__ = ("edges", "is_end", "score")
    def __init__(self) -> None:
        self.edges: List[Edge] = []
        self.is_end: bool = False
        self.score: float = 0.0  # relevance for suggestions

def _common_prefix(a: str, b: str) -> int:
    i = 0
    n = min(len(a), len(b))
    while i < n and a[i] == b[i]:
        i += 1
    return i

class CompressedTrie:
    """
    Insert/search over strings with path compression.
    Supports suggest(prefix, k) returning highest-score terms.
    """
    def __init__(self) -> None:
        self.root = CTrieNode()

    def insert(self, word: str, score: float = 1.0) -> None:
        node = self.root
        i = 0
        while i < len(word):
            ch = word[i]
            # find edge starting with ch
            edge = next((e for e in node.edges if e.label[0] == ch), None)
            if edge is None:
                child = CTrieNode()
                child.is_end = True if i + 1 == len(word) else False
                child.score = score if child.is_end else 0.0
                node.edges.append(Edge(word[i:], child))
                return
            # split if needed
            cp = _common_prefix(word[i:], edge.label)
            if cp == len(edge.label):
                node = edge.child
                i += cp
            else:
                # split existing edge
                old_suffix = edge.label[cp:]
                new_child = CTrieNode()
                new_child.edges.append(Edge(old_suffix, edge.child))
                new_child.is_end = False
                new_child.score = 0.0
                edge.label = edge.label[:cp]
                edge.child = new_child
                # add remaining part of new word
                remain = word[i+cp:]
                if remain:
                    leaf = CTrieNode()
                    leaf.is_end = True
                    leaf.score = score
                    new_child.edges.append(Edge(remain, leaf))
                else:
                    new_child.is_end = True
                    new_child.score = score
                return
        # reached end
        node.is_end = True
        node.score = max(node.score, score)

    def _dfs_collect(self, node: CTrieNode, prefix: str, out: List[Tuple[str, float]]) -> None:
        if node.is_end:
            out.append((prefix, node.score))
        for e in node.edges:
            self._dfs_collect(e.child, prefix + e.label, out)

    def suggest(self, prefix: str, k: int = 5) -> List[Tuple[str, float]]:
        node = self.root
        built = ""
        i = 0
        while i < len(prefix):
            ch = prefix[i]
            edge = next((e for e in node.edges if e.label[0] == ch), None)
            if not edge:
                return []
            cp = _common_prefix(prefix[i:], edge.label)
            if cp == len(edge.label):
                built += edge.label
                node = edge.child
                i += cp
            else:
                # prefix diverges before consuming edge
                return []
        results: List[Tuple[str, float]] = []
        self._dfs_collect(node, built, results)
        results.sort(key=lambda x: (-x[1], x[0]))
        return results[:k]
