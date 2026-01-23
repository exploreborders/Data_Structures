"""
Chapter 9: Recursion - Linked List Operations

This module demonstrates recursive operations on linked lists,
building on the linked list implementations from Chapter 7.
"""

import sys
import os

# Add the code directory from chapter 7 to the path
chapter7_code = os.path.join(os.path.dirname(__file__), '..', '..', 'chapter_7_deques_and_linked_lists', 'code')
if chapter7_code not in sys.path:
    sys.path.insert(0, chapter7_code)

# Try to import the linked list classes from Chapter 7
try:
    from doubly_linked_list import DoublyLinkedList, Node
except ImportError:
    # If not available, define simple versions for demonstration
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    class DoublyLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0

        def append(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            self.size += 1

        def __str__(self):
            result = []
            current = self.head
            while current:
                result.append(str(current.data))
                current = current.next
            return " -> ".join(result)


def length_recursive(node):
    """
    Calculate the length of a linked list recursively.

    Args:
        node: Head node of the linked list

    Returns:
        Length of the linked list

    Examples:
        >>> # Empty list
        >>> length_recursive(None)
        0
        >>> # List with elements
        >>> head = Node(1)
        >>> head.next = Node(2)
        >>> head.next.next = Node(3)
        >>> length_recursive(head)
        3
    """
    if node is None:  # Base case: empty list
        return 0
    else:  # Recursive case: 1 + length of rest
        return 1 + length_recursive(node.next)


def search_recursive(node, target):
    """
    Search for a target value in a linked list recursively.

    Args:
        node: Current node to check
        target: Value to search for

    Returns:
        True if target found, False otherwise

    Examples:
        >>> head = Node(1)
        >>> head.next = Node(2)
        >>> head.next.next = Node(3)
        >>> search_recursive(head, 2)
        True
        >>> search_recursive(head, 4)
        False
    """
    if node is None:  # Base case: end of list, not found
        return False
    elif node.data == target:  # Base case: found
        return True
    else:  # Recursive case: search rest of list
        return search_recursive(node.next, target)


def find_index_recursive(node, target, current_index=0):
    """
    Find the index of a target value in a linked list recursively.

    Args:
        node: Current node to check
        target: Value to search for
        current_index: Current position in list

    Returns:
        Index of target if found, -1 otherwise

    Examples:
        >>> head = Node(10)
        >>> head.next = Node(20)
        >>> head.next.next = Node(30)
        >>> find_index_recursive(head, 20)
        1
        >>> find_index_recursive(head, 40)
        -1
    """
    if node is None:  # Base case: end of list, not found
        return -1
    elif node.data == target:  # Base case: found
        return current_index
    else:  # Recursive case: search rest with incremented index
        return find_index_recursive(node.next, target, current_index + 1)


def reverse_list_recursive(head):
    """
    Reverse a linked list recursively.

    Args:
        head: Head node of the linked list

    Returns:
        New head of the reversed list

    Examples:
        >>> # Create list: 1 -> 2 -> 3
        >>> head = Node(1)
        >>> head.next = Node(2)
        >>> head.next.next = Node(3)
        >>> reversed_head = reverse_list_recursive(head)
        >>> # reversed_head should point to 3 -> 2 -> 1
        >>> reversed_head.data
        3
    """
    if head is None or head.next is None:  # Base case: empty or single node
        return head

    # Recursive case: reverse the rest of the list
    rest_reversed = reverse_list_recursive(head.next)

    # Make current node point to the end of the reversed rest
    head.next.next = head
    head.next = None

    return rest_reversed


def print_list_recursive(node):
    """
    Print all elements of a linked list recursively.

    Args:
        node: Head node of the linked list

    Examples:
        >>> head = Node(1)
        >>> head.next = Node(2)
        >>> head.next.next = Node(3)
        >>> print_list_recursive(head)  # Prints: 1 2 3
        1 2 3
    """
    if node is None:  # Base case: end of list
        return
    else:  # Recursive case: print current, then rest
        print(node.data, end=" ")
        print_list_recursive(node.next)


def sum_list_recursive(node):
    """
    Calculate the sum of all elements in a linked list recursively.

    Args:
        node: Head node of the linked list

    Returns:
        Sum of all elements

    Examples:
        >>> head = Node(1)
        >>> head.next = Node(2)
        >>> head.next.next = Node(3)
        >>> sum_list_recursive(head)
        6
    """
    if node is None:  # Base case: empty list
        return 0
    else:  # Recursive case: current data + sum of rest
        return node.data + sum_list_recursive(node.next)


def find_max_recursive(node):
    """
    Find the maximum value in a linked list recursively.

    Args:
        node: Head node of the linked list (assumes non-empty)

    Returns:
        Maximum value in the list

    Examples:
        >>> head = Node(3)
        >>> head.next = Node(1)
        >>> head.next.next = Node(4)
        >>> head.next.next.next = Node(2)
        >>> find_max_recursive(head)
        4
    """
    if node.next is None:  # Base case: single element
        return node.data
    else:  # Recursive case: max of current and max of rest
        max_rest = find_max_recursive(node.next)
        return max(node.data, max_rest)


def is_palindrome_recursive(node):
    """
    Check if a linked list is a palindrome recursively.
    This is a more advanced example that requires helper functions.

    Args:
        node: Head node of the linked list

    Returns:
        True if list is palindrome, False otherwise
    """
    # For palindrome check, we need to compare from both ends
    # This requires finding the length first, then comparing
    # This is complex with singly linked lists - we'll implement a simpler version

    # Convert to list for simplicity (not efficient but demonstrates concept)
    values = []
    current = node
    while current:
        values.append(current.data)
        current = current.next

    # Check if values list is palindrome
    return values == values[::-1]


# Demonstration functions
def create_sample_list():
    """Create a sample linked list for testing."""
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    return head


def demonstrate_linked_list_recursion():
    """Demonstrate recursive operations on linked lists."""
    print("Linked List Recursion Examples")
    print("=" * 40)

    # Create sample list
    head = create_sample_list()
    print("Original list: ", end="")
    print_list_recursive(head)
    print()

    # Length
    length = length_recursive(head)
    print(f"Length: {length}")

    # Search
    print(f"Contains 3: {search_recursive(head, 3)}")
    print(f"Contains 6: {search_recursive(head, 6)}")

    # Find index
    index = find_index_recursive(head, 3)
    print(f"Index of 3: {index}")

    # Sum
    total = sum_list_recursive(head)
    print(f"Sum: {total}")

    # Max
    maximum = find_max_recursive(head)
    print(f"Maximum: {maximum}")

    # Reverse
    print("\nReversing list...")
    reversed_head = reverse_list_recursive(head)
    print("Reversed list: ", end="")
    print_list_recursive(reversed_head)
    print()

    # Palindrome check
    palindrome_list = Node('r')
    palindrome_list.next = Node('a')
    palindrome_list.next.next = Node('d')
    palindrome_list.next.next.next = Node('a')
    palindrome_list.next.next.next.next = Node('r')

    print("Palindrome list: ", end="")
    print_list_recursive(palindrome_list)
    print(f"Is palindrome: {is_palindrome_recursive(palindrome_list)}")


if __name__ == '__main__':
    demonstrate_linked_list_recursion()</content>
<parameter name="filePath">chapter_9_recursion/code/linked_list_recursion.py