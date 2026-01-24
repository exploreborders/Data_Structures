"""
Chapter 14: Trees - Hierarchical Data Structures

This module implements various tree data structures and algorithms,
including binary trees, binary search trees, AVL trees, and heaps.
"""

from typing import List, Optional, Any, Tuple, Callable
import collections


class TreeNode:
    """Basic binary tree node."""

    def __init__(self, value: Any):
        self.value = value
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None
        self.height = 1  # Used for AVL trees

    def __repr__(self) -> str:
        return f"TreeNode({self.value})"

    def is_leaf(self) -> bool:
        """Check if node is a leaf (no children)."""
        return self.left is None and self.right is None

    def get_height(self) -> int:
        """Calculate height of subtree rooted at this node."""
        if self.is_leaf():
            return 0

        left_height = self.left.get_height() if self.left else -1
        right_height = self.right.get_height() if self.right else -1
        return 1 + max(left_height, right_height)

    def get_balance_factor(self) -> int:
        """Calculate balance factor for AVL trees."""
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return left_height - right_height


class BinaryTree:
    """Basic binary tree with traversal methods."""

    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root

    def is_empty(self) -> bool:
        """Check if tree is empty."""
        return self.root is None

    def get_height(self) -> int:
        """Get height of the tree."""
        return self.root.get_height() if self.root else 0

    def inorder_traversal(self) -> List[Any]:
        """Inorder traversal: Left -> Root -> Right."""
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper for inorder traversal."""
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def preorder_traversal(self) -> List[Any]:
        """Preorder traversal: Root -> Left -> Right."""
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper for preorder traversal."""
        if node:
            result.append(node.value)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def postorder_traversal(self) -> List[Any]:
        """Postorder traversal: Left -> Right -> Root."""
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper for postorder traversal."""
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.value)

    def level_order_traversal(self) -> List[Any]:
        """Level order (breadth-first) traversal."""
        if not self.root:
            return []

        result = []
        queue = collections.deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def inorder_iterative(self) -> List[Any]:
        """Iterative inorder traversal using stack."""
        result = []
        stack = []
        current = self.root

        while current or stack:
            # Reach the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Current is None, pop from stack
            current = stack.pop()
            result.append(current.value)
            current = current.right

        return result

    def preorder_iterative(self) -> List[Any]:
        """Iterative preorder traversal using stack."""
        if not self.root:
            return []

        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(node.value)

            # Push right first, then left (so left is processed first)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def count_nodes(self) -> int:
        """Count total number of nodes in the tree."""
        return self._count_nodes_helper(self.root)

    def _count_nodes_helper(self, node: Optional[TreeNode]) -> int:
        """Helper for counting nodes."""
        if not node:
            return 0
        return (
            1
            + self._count_nodes_helper(node.left)
            + self._count_nodes_helper(node.right)
        )

    def count_leaves(self) -> int:
        """Count number of leaf nodes."""
        return self._count_leaves_helper(self.root)

    def _count_leaves_helper(self, node: Optional[TreeNode]) -> int:
        """Helper for counting leaves."""
        if not node:
            return 0
        if node.is_leaf():
            return 1
        return self._count_leaves_helper(node.left) + self._count_leaves_helper(
            node.right
        )

    def is_complete(self) -> bool:
        """
        Check if the tree is complete (all levels filled except possibly the last,
        and all nodes as left as possible).
        """
        if not self.root:
            return True

        from collections import deque

        queue = deque([self.root])
        found_none = False

        while queue:
            node = queue.popleft()

            if node is None:
                found_none = True
                continue

            if found_none:
                # If we've seen a None and now see a non-None, it's not complete
                return False

            queue.append(node.left)
            queue.append(node.right)

        return True

    def is_full(self) -> bool:
        """
        Check if the tree is full (every node has either 0 or 2 children).
        """
        return self._is_full_helper(self.root)

    def _is_full_helper(self, node: Optional[TreeNode]) -> bool:
        """Helper for checking if tree is full."""
        if not node:
            return True

        # If node has one child but not the other, it's not full
        if (node.left is None) != (node.right is None):
            return False

        # Recursively check subtrees
        return self._is_full_helper(node.left) and self._is_full_helper(node.right)

    def is_balanced(self) -> bool:
        """
        Check if the tree is height-balanced (difference in height of left and right
        subtrees is at most 1 for every node).
        """

        def check_balance(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                return True, 0

            left_balanced, left_height = check_balance(node.left)
            right_balanced, right_height = check_balance(node.right)

            balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )
            height = 1 + max(left_height, right_height)

            return balanced, height

        balanced, _ = check_balance(self.root)
        return balanced

    def find_max(self) -> Any:
        """Find maximum value in the tree."""
        if not self.root:
            raise ValueError("Tree is empty")

        return self._find_max_helper(self.root)

    def _find_max_helper(self, node: TreeNode) -> Any:
        """Helper for finding maximum."""
        max_val = node.value
        if node.left:
            max_val = max(max_val, self._find_max_helper(node.left))
        if node.right:
            max_val = max(max_val, self._find_max_helper(node.right))
        return max_val

    def mirror(self) -> None:
        """Mirror the tree (swap left and right subtrees)."""
        self._mirror_helper(self.root)

    def _mirror_helper(self, node: Optional[TreeNode]) -> None:
        """Helper for mirroring tree."""
        if not node:
            return

        # Swap left and right
        node.left, node.right = node.right, node.left

        # Recurse
        self._mirror_helper(node.left)
        self._mirror_helper(node.right)


class BinarySearchTree(BinaryTree):
    """Binary Search Tree implementation."""

    def __init__(self):
        super().__init__()

    def search(self, value: Any) -> bool:
        """Search for a value in the BST."""
        return self._search_helper(self.root, value) is not None

    def search_with_path(self, value: Any) -> tuple[bool, List[Any]]:
        """
        Search for a value and return both found status and search path.

        Args:
            value: Value to search for

        Returns:
            Tuple of (found: bool, path: List of node values visited)
        """
        path = []
        found = self._search_with_path_helper(self.root, value, path)
        return found, path

    def _search_with_path_helper(
        self, node: Optional[TreeNode], value: Any, path: List[Any]
    ) -> bool:
        """Helper for search with path tracking."""
        if not node:
            return False

        path.append(node.value)

        if node.value == value:
            return True
        elif value < node.value:
            return self._search_with_path_helper(node.left, value, path)
        else:
            return self._search_with_path_helper(node.right, value, path)

    def _search_helper(
        self, node: Optional[TreeNode], value: Any
    ) -> Optional[TreeNode]:
        """Helper for searching."""
        if not node or node.value == value:
            return node

        if value < node.value:
            return self._search_helper(node.left, value)
        else:
            return self._search_helper(node.right, value)

    def insert(self, value: Any) -> None:
        """Insert a value into the BST."""
        self.root = self._insert_helper(self.root, value)

    def _insert_helper(self, node: Optional[TreeNode], value: Any) -> TreeNode:
        """Helper for insertion."""
        if not node:
            return TreeNode(value)

        if value < node.value:
            node.left = self._insert_helper(node.left, value)
        elif value > node.value:
            node.right = self._insert_helper(node.right, value)
        # Ignore duplicates for simplicity

        return node

    def delete(self, value: Any) -> None:
        """Delete a value from the BST."""
        self.root = self._delete_helper(self.root, value)

    def _delete_helper(
        self, node: Optional[TreeNode], value: Any
    ) -> Optional[TreeNode]:
        """Helper for deletion."""
        if not node:
            return None

        if value < node.value:
            node.left = self._delete_helper(node.left, value)
        elif value > node.value:
            node.right = self._delete_helper(node.right, value)
        else:
            # Node found - handle deletion
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children - find inorder successor
            successor = self._find_min(node.right)
            node.value = successor.value
            node.right = self._delete_helper(node.right, successor.value)

        return node

    def _find_min(self, node: TreeNode) -> TreeNode:
        """Find minimum value node in subtree."""
        current = node
        while current.left:
            current = current.left
        return current

    def find_min(self) -> Any:
        """Find minimum value in the BST."""
        if not self.root:
            raise ValueError("Tree is empty")
        return self._find_min(self.root).value

    def find_max(self) -> Any:
        """Find maximum value in the BST."""
        if not self.root:
            raise ValueError("Tree is empty")

        current = self.root
        while current.right:
            current = current.right
        return current.value

    def is_valid_bst(self) -> bool:
        """Check if the tree is a valid BST."""
        return self._is_valid_bst_helper(self.root, float("-inf"), float("inf"))

    def _is_valid_bst_helper(
        self, node: Optional[TreeNode], min_val: Any, max_val: Any
    ) -> bool:
        """Helper for BST validation."""
        if not node:
            return True

        if not (min_val < node.value < max_val):
            return False

        return self._is_valid_bst_helper(
            node.left, min_val, node.value
        ) and self._is_valid_bst_helper(node.right, node.value, max_val)

    def copy(self) -> "BinarySearchTree":
        """
        Create a deep copy of the BST.

        Returns:
            New BinarySearchTree with copied structure
        """
        new_tree = BinarySearchTree()
        if self.root:
            new_tree.root = self._copy_helper(self.root)
        return new_tree

    def _copy_helper(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """Helper for deep copying tree nodes."""
        if not node:
            return None

        new_node = TreeNode(node.value)
        new_node.left = self._copy_helper(node.left)
        new_node.right = self._copy_helper(node.right)
        new_node.height = node.height  # Copy height for AVL trees
        return new_node


class AVLTree(BinarySearchTree):
    """AVL Tree - Self-balancing BST."""

    def _insert_helper(self, node: Optional[TreeNode], value: Any) -> TreeNode:
        """AVL insert with balancing."""
        # Standard BST insert
        if not node:
            return TreeNode(value)

        if value < node.value:
            node.left = self._insert_helper(node.left, value)
        elif value > node.value:
            node.right = self._insert_helper(node.right, value)
        else:
            return node  # Duplicate, ignore

        # Update height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Get balance factor
        balance = self._get_balance(node)

        # Balance the tree
        # Left Left Case
        if balance > 1 and value < node.left.value:
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _delete_helper(
        self, node: Optional[TreeNode], value: Any
    ) -> Optional[TreeNode]:
        """AVL delete with balancing."""
        # Standard BST delete
        if not node:
            return None

        if value < node.value:
            node.left = self._delete_helper(node.left, value)
        elif value > node.value:
            node.right = self._delete_helper(node.right, value)
        else:
            # Node found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Two children - get inorder successor
            successor = self._find_min(node.right)
            node.value = successor.value
            node.right = self._delete_helper(node.right, successor.value)

        if not node:
            return None

        # Update height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Get balance
        balance = self._get_balance(node)

        # Balance the tree
        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _get_height(self, node: Optional[TreeNode]) -> int:
        """Get height of node."""
        return node.height if node else 0

    def _get_balance(self, node: Optional[TreeNode]) -> int:
        """Get balance factor."""
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _right_rotate(self, y: TreeNode) -> TreeNode:
        """Right rotation."""
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _left_rotate(self, x: TreeNode) -> TreeNode:
        """Left rotation."""
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y


class Heap:
    """Binary heap implementation (max-heap by default)."""

    def __init__(self, max_heap: bool = True):
        self.heap: List[Any] = []
        self.max_heap = max_heap

    def _compare(self, a: Any, b: Any) -> bool:
        """Compare elements based on heap type."""
        return a > b if self.max_heap else a < b

    def _parent(self, i: int) -> int:
        """Get parent index."""
        return (i - 1) // 2

    def _left_child(self, i: int) -> int:
        """Get left child index."""
        return 2 * i + 1

    def _right_child(self, i: int) -> int:
        """Get right child index."""
        return 2 * i + 2

    def insert(self, value: Any) -> None:
        """Insert value into heap."""
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, i: int) -> None:
        """Bubble up element to maintain heap property."""
        while i > 0 and self._compare(self.heap[i], self.heap[self._parent(i)]):
            # Swap with parent
            self.heap[i], self.heap[self._parent(i)] = (
                self.heap[self._parent(i)],
                self.heap[i],
            )
            i = self._parent(i)

    def extract_top(self) -> Any:
        """Extract and return the top element (max/min)."""
        if not self.heap:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap root with last element
        top = self.heap[0]
        self.heap[0] = self.heap.pop()

        # Bubble down from root
        self._bubble_down(0)

        return top

    def _bubble_down(self, i: int) -> None:
        """Bubble down element to maintain heap property."""
        size = len(self.heap)

        while True:
            left = self._left_child(i)
            right = self._right_child(i)
            largest = i

            # Find the largest/smallest among i, left, right
            if left < size and self._compare(self.heap[left], self.heap[largest]):
                largest = left
            if right < size and self._compare(self.heap[right], self.heap[largest]):
                largest = right

            if largest == i:
                break

            # Swap and continue
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    def peek(self) -> Any:
        """Return the top element without removing it."""
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self) -> int:
        """Return the number of elements in the heap."""
        return len(self.heap)

    def is_empty(self) -> bool:
        """Check if heap is empty."""
        return len(self.heap) == 0

    @classmethod
    def heapify(cls, arr: List[Any], max_heap: bool = True) -> "Heap":
        """Build heap from array in O(n) time."""
        heap = cls(max_heap)
        heap.heap = arr.copy()

        # Start from the last non-leaf node and bubble down
        for i in range(len(arr) // 2 - 1, -1, -1):
            heap._bubble_down(i)

        return heap

    @classmethod
    def heap_sort(cls, arr: List[Any], ascending: bool = True) -> List[Any]:
        """Sort array using heap sort."""
        if ascending:
            # Use max-heap, extract max repeatedly
            heap = cls.heapify(arr, max_heap=True)
            result = []
            while not heap.is_empty():
                result.append(heap.extract_top())
            return result
        else:
            # Use min-heap, extract min repeatedly
            heap = cls.heapify(arr, max_heap=False)
            result = []
            while not heap.is_empty():
                result.append(heap.extract_top())
            return result


class TreeAnalysis:
    """Tools for analyzing tree structures and performance."""

    @staticmethod
    def is_balanced_bst(root: Optional[TreeNode]) -> bool:
        """Check if BST is height-balanced."""

        def check_balance(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                return True, 0

            left_balanced, left_height = check_balance(node.left)
            right_balanced, right_height = check_balance(node.right)

            balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )
            height = 1 + max(left_height, right_height)

            return balanced, height

        balanced, _ = check_balance(root)
        return balanced

    @staticmethod
    def tree_diameter(root: Optional[TreeNode]) -> int:
        """Find the diameter of the tree (longest path between any two nodes)."""

        def diameter_helper(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0

            left_diam, left_height = diameter_helper(node.left)
            right_diam, right_height = diameter_helper(node.right)

            # Diameter through current node
            current_diam = left_height + right_height

            # Overall diameter
            diameter = max(left_diam, right_diam, current_diam)
            height = 1 + max(left_height, right_height)

            return diameter, height

        diameter, _ = diameter_helper(root)
        return diameter

    @staticmethod
    def lowest_common_ancestor(
        root: Optional[TreeNode], p: Any, q: Any
    ) -> Optional[TreeNode]:
        """Find lowest common ancestor of two nodes."""
        if not root:
            return None

        # For BST, we can optimize
        if hasattr(root, "left") and hasattr(root, "right"):  # Assume BST
            if p > root.value and q > root.value:
                return TreeAnalysis.lowest_common_ancestor(root.right, p, q)
            elif p < root.value and q < root.value:
                return TreeAnalysis.lowest_common_ancestor(root.left, p, q)
            else:
                return root

        # General binary tree approach (more complex)
        # This is a simplified version - full implementation would need parent pointers
        # or two traversals
        return None

    @staticmethod
    def build_tree_from_traversals(
        inorder: List[Any], preorder: List[Any]
    ) -> Optional[TreeNode]:
        """Build binary tree from inorder and preorder traversals."""
        if not inorder or not preorder:
            return None

        # Root is first element in preorder
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find root in inorder
        root_index = inorder.index(root_val)

        # Recursively build left and right subtrees
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1 :]

        left_preorder = preorder[1 : 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder) :]

        root.left = TreeAnalysis.build_tree_from_traversals(left_inorder, left_preorder)
        root.right = TreeAnalysis.build_tree_from_traversals(
            right_inorder, right_preorder
        )
