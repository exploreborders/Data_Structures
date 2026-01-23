"""
Chapter 15: Binary Search Trees - Ordered Mapping Implementation

This module implements Binary Search Trees (BSTs) providing an efficient
ordered mapping ADT with logarithmic-time operations.
"""

from typing import List, Optional, Tuple, Any, Callable
import random


class BSTNode:
    """Node for Binary Search Tree."""

    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.left: Optional["BSTNode"] = None
        self.right: Optional["BSTNode"] = None
        self.parent: Optional["BSTNode"] = None  # Optional parent pointer
        self.size = 1  # Size of subtree (for advanced operations)

    def __repr__(self) -> str:
        return f"BSTNode({self.key}: {self.value})"

    def update_size(self) -> None:
        """Update the size of this subtree."""
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size

    def get_height(self) -> int:
        """Get height of subtree rooted at this node."""
        if not self.left and not self.right:
            return 0

        left_height = self.left.get_height() if self.left else -1
        right_height = self.right.get_height() if self.right else -1
        return 1 + max(left_height, right_height)

    def is_leaf(self) -> bool:
        """Check if node is a leaf."""
        return self.left is None and self.right is None

    def has_one_child(self) -> bool:
        """Check if node has exactly one child."""
        return (self.left is not None) ^ (self.right is not None)

    def has_two_children(self) -> bool:
        """Check if node has two children."""
        return self.left is not None and self.right is not None


class BinarySearchTree:
    """Binary Search Tree implementation of Ordered Mapping ADT."""

    def __init__(self):
        self.root: Optional[BSTNode] = None
        self._size = 0

    def __len__(self) -> int:
        """Return number of key-value pairs."""
        return self._size

    def is_empty(self) -> bool:
        """Check if tree is empty."""
        return self.root is None

    def put(self, key: Any, value: Any) -> None:
        """Insert or update key-value pair."""
        if self.root is None:
            self.root = BSTNode(key, value)
            self._size = 1
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node: BSTNode, key: Any, value: Any) -> None:
        """Recursive helper for insertion."""
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, value)
                self._size += 1
            else:
                self._insert_recursive(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, value)
                self._size += 1
            else:
                self._insert_recursive(node.right, key, value)
        else:
            # Key exists - update value
            node.value = value

        node.update_size()

    def get(self, key: Any) -> Any:
        """Retrieve value for given key."""
        node = self._search_recursive(self.root, key)
        if node is None:
            raise KeyError(f"Key '{key}' not found")
        return node.value

    def _search_recursive(self, node: Optional[BSTNode], key: Any) -> Optional[BSTNode]:
        """Recursive search helper."""
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def contains(self, key: Any) -> bool:
        """Check if key exists in the tree."""
        return self._search_recursive(self.root, key) is not None

    def remove(self, key: Any) -> Any:
        """Remove and return value for given key."""
        node = self._search_recursive(self.root, key)
        if node is None:
            raise KeyError(f"Key '{key}' not found")

        value = node.value
        self.root = self._remove_node(self.root, key)
        self._size -= 1
        return value

    def _remove_node(self, node: BSTNode, key: Any) -> Optional[BSTNode]:
        """Remove node with given key and return new subtree root."""
        if node is None:
            return None

        if key < node.key:
            node.left = self._remove_node(node.left, key)
        elif key > node.key:
            node.right = self._remove_node(node.right, key)
        else:
            # Node found - handle removal
            if node.is_leaf():
                # Case 1: Leaf node
                return None
            elif node.has_one_child():
                # Case 2: One child
                return node.left if node.left else node.right
            else:
                # Case 3: Two children - find inorder successor
                successor = self._find_min(node.right)
                # Copy successor's data to current node
                node.key = successor.key
                node.value = successor.value
                # Remove successor from right subtree
                node.right = self._remove_node(node.right, successor.key)

        if node:
            node.update_size()
        return node

    def _find_min(self, node: BSTNode) -> BSTNode:
        """Find minimum key node in subtree."""
        current = node
        while current.left:
            current = current.left
        return current

    def min_key(self) -> Any:
        """Return minimum key in the tree."""
        if self.is_empty():
            raise ValueError("Tree is empty")
        return self._find_min(self.root).key

    def max_key(self) -> Any:
        """Return maximum key in the tree."""
        if self.is_empty():
            raise ValueError("Tree is empty")

        current = self.root
        while current.right:
            current = current.right
        return current.key

    def successor(self, key: Any) -> Optional[Any]:
        """Find inorder successor of given key."""
        node = self._search_recursive(self.root, key)
        if node is None:
            return None

        # Case 1: Node has right subtree
        if node.right:
            return self._find_min(node.right).key

        # Case 2: No right subtree - go up to find ancestor
        successor = None
        current = self.root
        while current:
            if key < current.key:
                successor = current.key
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                break

        return successor

    def predecessor(self, key: Any) -> Optional[Any]:
        """Find inorder predecessor of given key."""
        node = self._search_recursive(self.root, key)
        if node is None:
            return None

        # Case 1: Node has left subtree
        if node.left:
            current = node.left
            while current.right:
                current = current.right
            return current.key

        # Case 2: No left subtree - go up to find ancestor
        predecessor = None
        current = self.root
        while current:
            if key > current.key:
                predecessor = current.key
                current = current.right
            elif key < current.key:
                current = current.left
            else:
                break

        return predecessor

    def floor(self, key: Any) -> Optional[Any]:
        """Find largest key ≤ given key."""
        node = self.root
        floor = None

        while node:
            if node.key == key:
                return node.key
            elif node.key < key:
                floor = node.key
                node = node.right
            else:
                node = node.left

        return floor

    def ceiling(self, key: Any) -> Optional[Any]:
        """Find smallest key ≥ given key."""
        node = self.root
        ceiling = None

        while node:
            if node.key == key:
                return node.key
            elif node.key > key:
                ceiling = node.key
                node = node.left
            else:
                node = node.right

        return ceiling

    def keys_in_range(self, low: Any, high: Any) -> List[Any]:
        """Return all keys in the range [low, high]."""
        result = []
        self._collect_keys_in_range(self.root, low, high, result)
        return result

    def _collect_keys_in_range(
        self, node: Optional[BSTNode], low: Any, high: Any, result: List[Any]
    ) -> None:
        """Helper to collect keys in range."""
        if node is None:
            return

        if low <= node.key <= high:
            result.append(node.key)

        if node.key > low:
            self._collect_keys_in_range(node.left, low, high, result)
        if node.key < high:
            self._collect_keys_in_range(node.right, low, high, result)

    def values_in_range(self, low: Any, high: Any) -> List[Any]:
        """Return all values for keys in the range [low, high]."""
        result = []
        self._collect_values_in_range(self.root, low, high, result)
        return result

    def _collect_values_in_range(
        self, node: Optional[BSTNode], low: Any, high: Any, result: List[Any]
    ) -> None:
        """Helper to collect values in range."""
        if node is None:
            return

        if low <= node.key <= high:
            result.append(node.value)

        if node.key > low:
            self._collect_values_in_range(node.left, low, high, result)
        if node.key < high:
            self._collect_values_in_range(node.right, low, high, result)

    def inorder_traversal(self) -> List[Tuple[Any, Any]]:
        """Return inorder traversal as (key, value) pairs."""
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(
        self, node: Optional[BSTNode], result: List[Tuple[Any, Any]]
    ) -> None:
        """Inorder traversal helper."""
        if node:
            self._inorder_helper(node.left, result)
            result.append((node.key, node.value))
            self._inorder_helper(node.right, result)

    def preorder_traversal(self) -> List[Tuple[Any, Any]]:
        """Return preorder traversal as (key, value) pairs."""
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(
        self, node: Optional[BSTNode], result: List[Tuple[Any, Any]]
    ) -> None:
        """Preorder traversal helper."""
        if node:
            result.append((node.key, node.value))
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def postorder_traversal(self) -> List[Tuple[Any, Any]]:
        """Return postorder traversal as (key, value) pairs."""
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(
        self, node: Optional[BSTNode], result: List[Tuple[Any, Any]]
    ) -> None:
        """Postorder traversal helper."""
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append((node.key, node.value))

    def level_order_traversal(self) -> List[Tuple[Any, Any]]:
        """Return level-order traversal as (key, value) pairs."""
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            result.append((node.key, node.value))

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def is_valid_bst(self) -> bool:
        """Check if the tree maintains BST properties."""
        return self._is_valid_bst_helper(self.root, float("-inf"), float("inf"))

    def _is_valid_bst_helper(
        self, node: Optional[BSTNode], min_val: Any, max_val: Any
    ) -> bool:
        """Helper to validate BST properties."""
        if node is None:
            return True

        if not (min_val < node.key < max_val):
            return False

        return self._is_valid_bst_helper(
            node.left, min_val, node.key
        ) and self._is_valid_bst_helper(node.right, node.key, max_val)

    def get_height(self) -> int:
        """Get height of the tree."""
        return self.root.get_height() if self.root else 0

    def get_balance_factor_distribution(self) -> List[int]:
        """Get distribution of balance factors in the tree."""
        factors = []
        self._collect_balance_factors(self.root, factors)
        return factors

    def _collect_balance_factors(
        self, node: Optional[BSTNode], factors: List[int]
    ) -> None:
        """Collect balance factors for all nodes."""
        if node:
            left_height = node.left.get_height() if node.left else 0
            right_height = node.right.get_height() if node.right else 0
            factors.append(left_height - right_height)

            self._collect_balance_factors(node.left, factors)
            self._collect_balance_factors(node.right, factors)


class BSTAnalysis:
    """Tools for analyzing BST performance and structure."""

    @staticmethod
    def generate_worst_case_bst(n: int) -> BinarySearchTree:
        """Generate a worst-case BST (completely unbalanced)."""
        bst = BinarySearchTree()
        for i in range(n):
            bst.put(i, f"value{i}")
        return bst

    @staticmethod
    def generate_best_case_bst(n: int) -> BinarySearchTree:
        """Generate a best-case BST (balanced)."""
        bst = BinarySearchTree()

        def insert_balanced(low: int, high: int) -> None:
            if low > high:
                return
            mid = (low + high) // 2
            bst.put(mid, f"value{mid}")
            insert_balanced(low, mid - 1)
            insert_balanced(mid + 1, high)

        insert_balanced(0, n - 1)
        return bst

    @staticmethod
    def generate_random_bst(n: int, seed: int = 42) -> BinarySearchTree:
        """Generate a BST with random insertions."""
        random.seed(seed)
        bst = BinarySearchTree()
        keys = list(range(n))
        random.shuffle(keys)

        for key in keys:
            bst.put(key, f"value{key}")

        return bst

    @staticmethod
    def benchmark_bst_operations(
        bst: BinarySearchTree, num_operations: int = 1000
    ) -> Dict[str, float]:
        """Benchmark BST operations."""
        import time

        # Generate random keys for operations
        keys = list(range(len(bst)))
        random.shuffle(keys)

        # Benchmark search
        start_time = time.time()
        for key in keys[:num_operations]:
            bst.contains(key)
        search_time = time.time() - start_time

        # Benchmark insertion (on copy)
        bst_copy = BinarySearchTree()
        for key, value in bst.inorder_traversal():
            bst_copy.put(key, value)

        start_time = time.time()
        for i in range(num_operations):
            bst_copy.put(len(bst) + i, f"new_value{i}")
        insert_time = time.time() - start_time

        return {
            "search_time": search_time,
            "insert_time": insert_time,
            "height": bst.get_height(),
            "size": len(bst),
            "balance_factors": bst.get_balance_factor_distribution(),
        }

    @staticmethod
    def analyze_bst_shape(bst: BinarySearchTree) -> Dict[str, Any]:
        """Analyze the shape and properties of a BST."""
        height = bst.get_height()
        size = len(bst)

        # Calculate balance factors
        balance_factors = bst.get_balance_factor_distribution()
        avg_balance = (
            sum(abs(bf) for bf in balance_factors) / len(balance_factors)
            if balance_factors
            else 0
        )

        # Check if balanced
        is_balanced = all(abs(bf) <= 1 for bf in balance_factors)

        # Calculate theoretical heights
        import math

        min_height = math.ceil(math.log2(size + 1)) - 1 if size > 0 else 0
        max_height = size - 1 if size > 0 else 0

        return {
            "height": height,
            "size": size,
            "min_possible_height": min_height,
            "max_possible_height": max_height,
            "balance_factor_avg": avg_balance,
            "is_balanced": is_balanced,
            "height_ratio": height / max_height if max_height > 0 else 0,
        }
