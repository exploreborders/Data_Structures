"""
Chapter 8: Concatenating Doubly Linked Lists - Efficient List Operations

This module extends the DoublyLinkedList implementation with efficient
concatenation operations, demonstrating O(1) list merging through pointer manipulation.
"""


class DoublyNode:
    """
    A node in a doubly linked list with data and bidirectional links.
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"DoublyNode({self.data})"


class DoublyLinkedList:
    """
    Doubly linked list with head and tail pointers for O(1) end operations.

    This implementation includes efficient concatenation methods that demonstrate
    the power of pointer manipulation in linked data structures.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data):
        """
        Add item to end of list. O(1) time.
        """
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, data):
        """
        Add item to beginning of list. O(1) time.
        """
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def __len__(self):
        """Return cached size. O(1) time."""
        return self._size

    def __str__(self):
        """String representation of the list."""
        if not self.head:
            return "DoublyLinkedList([])"

        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return f"DoublyLinkedList([{', '.join(items)}])"

    def __iter__(self):
        """Make list iterable."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    # Chapter 8: Concatenation methods

    def concatenate_efficient(self, other):
        """
        Concatenate another list to this one in O(1) time.

        This method modifies this list in-place by updating pointers.
        The other list becomes empty after concatenation.

        Args:
            other: DoublyLinkedList to concatenate

        Returns:
            self: This list with other list appended

        Time: O(1)
        Space: O(1)
        """
        if not isinstance(other, DoublyLinkedList):
            raise TypeError("Can only concatenate with another DoublyLinkedList")

        # Prevent self-concatenation
        if self is other:
            raise ValueError("Cannot concatenate list with itself")

        # Case 1: This list is empty
        if not self.head:
            self.head = other.head
            self.tail = other.tail
            self._size = other._size

        # Case 2: Other list is empty (nothing to do)
        elif not other.head:
            pass  # This list stays the same

        # Case 3: Both lists have elements
        else:
            # Link the lists: this.tail -> other.head
            self.tail.next = other.head
            other.head.prev = self.tail

            # Update this list's tail
            self.tail = other.tail

            # Update size
            self._size += other._size

        # Clear the other list
        other.head = None
        other.tail = None
        other._size = 0

        return self

    def concatenate_copy(self, other):
        """
        Concatenate by creating a new list with copies of all elements.

        This method preserves both original lists and creates a new combined list.

        Args:
            other: DoublyLinkedList to concatenate

        Returns:
            DoublyLinkedList: New list containing elements from both lists

        Time: O(n + m) where n, m are list sizes
        Space: O(n + m)
        """
        if not isinstance(other, DoublyLinkedList):
            raise TypeError("Can only concatenate with another DoublyLinkedList")

        result = DoublyLinkedList()

        # Copy elements from this list
        current = self.head
        while current:
            result.append(current.data)
            current = current.next

        # Copy elements from other list
        current = other.head
        while current:
            result.append(current.data)
            current = current.next

        return result

    def concatenate_multiple(self, *others):
        """
        Concatenate multiple lists efficiently in-place.

        Args:
            *others: Variable number of DoublyLinkedList objects

        Returns:
            self: This list with all others concatenated

        Time: O(k) where k is number of lists (each concatenation is O(1))
        Space: O(1)
        """
        for other in others:
            self.concatenate_efficient(other)
        return self

    def split_at(self, index):
        """
        Split this list at the given index, returning a new list with elements after index.

        Args:
            index: Position to split at (0-based)

        Returns:
            DoublyLinkedList: New list containing elements from index onwards

        Time: O(n) in worst case, but often faster due to structure
        """
        if index < 0:
            index = max(0, self._size + index)

        if index >= self._size:
            return DoublyLinkedList()  # Return empty list

        if index == 0:
            # Split at beginning - return entire list, make this list empty
            result = DoublyLinkedList()
            result.head = self.head
            result.tail = self.tail
            result._size = self._size

            self.head = None
            self.tail = None
            self._size = 0

            return result

        # Find the node at index
        current = self.head
        for _ in range(index):
            if not current:
                break
            current = current.next

        if not current:
            return DoublyLinkedList()  # Index beyond list

        # Create new list starting from current node
        result = DoublyLinkedList()
        result.head = current
        result.tail = self.tail
        result._size = self._size - index

        # Update this list's tail and size
        if current.prev:
            current.prev.next = None
        self.tail = current.prev
        self._size = index

        # Clear prev pointer of new head
        if result.head:
            result.head.prev = None

        return result

    def insert_list_at(self, index, other):
        """
        Insert another list at the specified index in this list.

        Args:
            index: Position to insert at (0-based)
            other: DoublyLinkedList to insert

        Time: O(1) for end insertions, O(n) for middle insertions
        """
        if not isinstance(other, DoublyLinkedList) or other is self:
            raise ValueError("Invalid list for insertion")

        if index <= 0:
            # Insert at beginning - prepend all elements
            # We need to prepend in reverse order to maintain sequence
            elements = list(other)  # Get elements in order
            for element in reversed(elements):
                self.prepend(element)

        elif index >= self._size:
            # Insert at end - append all elements
            current = other.head
            while current:
                self.append(current.data)
                current = current.next

        else:
            # Insert in middle - find insertion point
            current = self.head
            for _ in range(index):
                current = current.next

            # Link other list into this list
            if other.head:
                other.tail.next = current
                if current:
                    current.prev = other.tail

                if current.prev:
                    current.prev.next = other.head
                    other.head.prev = current.prev

                self._size += other._size

            # Clear other list
            other.head = None
            other.tail = None
            other._size = 0

    def reverse_in_place(self):
        """
        Reverse this list in-place by swapping all next/prev pointers.

        Time: O(n)
        Space: O(1)
        """
        if not self.head or self._size <= 1:
            return  # Nothing to do

        current = self.head
        self.head, self.tail = self.tail, self.head  # Swap head and tail

        while current:
            # Swap next and prev for this node
            current.next, current.prev = current.prev, current.next
            current = current.prev  # Move to next (which was originally prev)

    def clone(self):
        """
        Create a deep copy of this list.

        Returns:
            DoublyLinkedList: New list with copied elements

        Time: O(n)
        Space: O(n)
        """
        result = DoublyLinkedList()
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


# Utility functions for concatenation demonstrations


def demonstrate_concatenation_performance():
    """
    Demonstrate the performance difference between concatenation methods.
    """
    import time

    # Create test lists
    list1 = DoublyLinkedList()
    list2 = DoublyLinkedList()

    # Add elements
    for i in range(1000):
        list1.append(f"list1_{i}")
        list2.append(f"list2_{i}")

    # Test efficient concatenation
    list1_copy = list1.clone()
    list2_copy = list2.clone()

    start = time.time()
    result1 = list1_copy.concatenate_efficient(list2_copy)
    efficient_time = time.time() - start

    # Test copy-based concatenation
    list1_copy2 = list1.clone()
    list2_copy2 = list2.clone()

    start = time.time()
    result2 = list1_copy2.concatenate_copy(list2_copy2)
    copy_time = time.time() - start

    print("Performance Comparison:")
    print(f"Efficient concatenation: {efficient_time:.6f} seconds")
    print(f"Copy-based concatenation: {copy_time:.6f} seconds")
    print(".1f")

    return efficient_time, copy_time


def create_sample_lists():
    """Create sample lists for demonstration."""
    list1 = DoublyLinkedList()
    list2 = DoublyLinkedList()

    # Add some data
    words1 = ["hello", "world", "from"]
    words2 = ["the", "doubly", "linked", "list"]

    for word in words1:
        list1.append(word)
    for word in words2:
        list2.append(word)

    return list1, list2


if __name__ == "__main__":
    print("=== Chapter 8: Concatenating Doubly Linked Lists ===\n")

    # Create sample lists
    list1, list2 = create_sample_lists()

    print("Original lists:")
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print()

    # Demonstrate efficient concatenation
    print("Efficient concatenation (O(1)):")
    list1_concat = list1.clone()
    list2_concat = list2.clone()

    result = list1_concat.concatenate_efficient(list2_concat)
    print(f"Result: {result}")
    print(f"List2 after concatenation: {list2_concat} (empty)")
    print()

    # Demonstrate copy-based concatenation
    print("Copy-based concatenation (O(n+m)):")
    list1_copy = list1.clone()
    list2_copy = list2.clone()

    result_copy = list1_copy.concatenate_copy(list2_copy)
    print(f"Result: {result_copy}")
    print(f"Original lists unchanged:")
    print(f"List 1: {list1_copy}")
    print(f"List 2: {list2_copy}")
    print()

    # Demonstrate multiple concatenation
    print("Multiple list concatenation:")
    lists = [DoublyLinkedList() for _ in range(3)]
    words = [["The"], ["quick", "brown"], ["fox", "jumps"]]

    for lst, word_list in zip(lists, words):
        for word in word_list:
            lst.append(word)

    base_list = lists[0].clone()
    base_list.concatenate_multiple(*[lst.clone() for lst in lists[1:]])

    print(f"Combined: {base_list}")
    print()

    # Demonstrate split operation
    print("List splitting:")
    original = DoublyLinkedList()
    for word in ["apple", "banana", "cherry", "date", "elderberry"]:
        original.append(word)

    print(f"Original: {original}")

    split_list = original.split_at(2)
    print(f"After split at index 2:")
    print(f"First part: {original}")
    print(f"Second part: {split_list}")
    print()

    # Performance demonstration
    print("Performance comparison:")
    demonstrate_concatenation_performance()

    print("\n=== Key Takeaways ===")
    print("• Efficient concatenation: O(1) with pointer manipulation")
    print("• Copy concatenation: O(n+m) but preserves originals")
    print("• Doubly linked lists enable fast end operations")
    print("• Pointer updates are the key to efficient algorithms")
    print("• Choose concatenation method based on mutation needs")
