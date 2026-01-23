"""
Chapter 18: Balanced Binary Search Trees - AVL Tree Implementation

This module implements AVL trees, a self-balancing binary search tree that
maintains logarithmic height bounds through automatic rebalancing.
"""

from typing import List, Optional, Tuple, Any
import random


class AVLNode:
    """Node for AVL Tree with height tracking."""

    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height = 0  # Height of subtree rooted at this node

    def __repr__(self) -> str:
        return f"AVLNode({self.key}: {self.value}, h={self.height})"

    def get_balance_factor(self) -> int:
        """Calculate balance factor: height(right) - height(left)."""
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return right_height - left_height

    def update_height(self) -> None:
        """Update height based on children's heights."""
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = 1 + max(left_height, right_height)

    def is_leaf(self) -> bool:
        """Check if node is a leaf."""
        return self.left is None and self.right is None

    def has_one_child(self) -> bool:
        """Check if node has exactly one child."""
        return (self.left is not None) ^ (self.right is not None)

    def has_two_children(self) -> bool:
        """Check if node has two children."""
        return self.left is not None and self.right is not None


class AVLTree:
    """AVL Tree implementation maintaining balance through rotations."""

    def __init__(self):
        self.root: Optional[AVLNode] = None
        self._size = 0

    def __len__(self) -> int:
        """Return number of key-value pairs."""
        return self._size

    def is_empty(self) -> bool:
        """Check if tree is empty."""
        return self.root is None

    def put(self, key: Any, value: Any) -> None:
        """Insert or update key-value pair with rebalancing."""
        self.root = self._insert_recursive(self.root, key, value)
        self._size = self._calculate_size(self.root)

    def _insert_recursive(
        self, node: Optional[AVLNode], key: Any, value: Any
    ) -> Optional[AVLNode]:
        """Recursive insertion with rebalancing."""
        if node is None:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)
        else:
            # Key exists - update value
            node.value = value
            return node

        # Update height and rebalance
        node.update_height()
        return self._rebalance(node)

    def _rebalance(self, node: AVLNode) -> AVLNode:
        """Rebalance node if balance factor is out of range."""
        balance = node.get_balance_factor()

        # Left heavy (LL or LR case)
        if balance < -1:
            if node.left and node.left.get_balance_factor() <= 0:
                # LL case
                return self._rotate_right(node)
            else:
                # LR case
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Right heavy (RR or RL case)
        elif balance > 1:
            if node.right and node.right.get_balance_factor() >= 0:
                # RR case
                return self._rotate_left(node)
            else:
                # RL case
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """Perform left rotation."""
        right_child = node.right
        if right_child is None:
            return node

        # Perform rotation
        node.right = right_child.left
        right_child.left = node

        # Update heights
        node.update_height()
        right_child.update_height()

        return right_child

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """Perform right rotation."""
        left_child = node.left
        if left_child is None:
            return node

        # Perform rotation
        node.left = left_child.right
        left_child.right = node

        # Update heights
        node.update_height()
        left_child.update_height()

        return left_child

    def get(self, key: Any) -> Any:
        """Retrieve value for given key."""
        node = self._search_recursive(self.root, key)
        if node is None:
            raise KeyError(f"Key '{key}' not found")
        return node.value

    def _search_recursive(self, node: Optional[AVLNode], key: Any) -> Optional[AVLNode]:
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
        """Remove and return value for given key with rebalancing."""
        node = self._search_recursive(self.root, key)
        if node is None:
            raise KeyError(f"Key '{key}' not found")

        value = node.value
        self.root = self._remove_node(self.root, key)
        self._size = self._calculate_size(self.root)
        return value

    def _remove_node(self, node: Optional[AVLNode], key: Any) -> Optional[AVLNode]:
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
            node.update_height()
            node = self._rebalance(node)
        return node

    def _find_min(self, node: AVLNode) -> AVLNode:
        """Find minimum key node in subtree."""
        current = node
        while current.left:
            current = current.left
        return current

    def _calculate_size(self, node: Optional[AVLNode]) -> int:
        """Calculate size of subtree."""
        if node is None:
            return 0
        return 1 + self._calculate_size(node.left) + self._calculate_size(node.right)

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

    def get_height(self) -> int:
        """Get height of the tree."""
        return self.root.height if self.root else 0

    def inorder_traversal(self) -> List[Tuple[Any, Any]]:
        """Return inorder traversal as (key, value) pairs."""
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(
        self, node: Optional[AVLNode], result: List[Tuple[Any, Any]]
    ) -> None:
        """Inorder traversal helper."""
        if node:
            self._inorder_helper(node.left, result)
            result.append((node.key, node.value))
            self._inorder_helper(node.right, result)

    def is_valid_avl(self) -> bool:
        """Check if the tree maintains AVL properties."""
        return self._is_valid_avl_helper(self.root)

    def _is_valid_avl_helper(self, node: Optional[AVLNode]) -> bool:
        """Helper to validate AVL properties."""
        if node is None:
            return True

        # Check balance factor
        balance = node.get_balance_factor()
        if abs(balance) > 1:
            return False

        # Check BST property (assuming keys are comparable)
        if node.left and node.left.key >= node.key:
            return False
        if node.right and node.right.key <= node.key:
            return False

        # Recursively check subtrees
        return self._is_valid_avl_helper(node.left) and self._is_valid_avl_helper(
            node.right
        )

    def get_balance_factor_distribution(self) -> List[int]:
        """Get distribution of balance factors in the tree."""
        factors = []
        self._collect_balance_factors(self.root, factors)
        return factors

    def _collect_balance_factors(
        self, node: Optional[AVLNode], factors: List[int]
    ) -> None:
        """Collect balance factors for all nodes."""
        if node:
            factors.append(node.get_balance_factor())
            self._collect_balance_factors(node.left, factors)
            self._collect_balance_factors(node.right, factors)

    def visualize_tree(self) -> str:
        """Create a simple text visualization of the tree."""
        if not self.root:
            return "(empty)"

        lines = []
        self._visualize_helper(self.root, "", True, lines)
        return "\n".join(lines)

    def _visualize_helper(
        self, node: Optional[AVLNode], prefix: str, is_tail: bool, lines: List[str]
    ) -> None:
        """Helper for tree visualization."""
        if node:
            lines.append(
                f"{prefix}{('└── ' if is_tail else '├── ')}{node.key}(h={node.height},bf={node.get_balance_factor()})"
            )

            child_prefix = prefix + ("    " if is_tail else "│   ")
            if node.right:
                self._visualize_helper(node.right, child_prefix, False, lines)
            if node.left:
                self._visualize_helper(node.left, child_prefix, True, lines)
