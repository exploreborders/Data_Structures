"""
Chapter 7: Deques and Linked Lists - Dynamic Data Structures

This module implements Linked Lists, the Deque ADT, and demonstrates
the Wrapper Pattern by implementing Queue using LinkedList.
"""


class Node:
    """
    A node in a singly linked list.

    Each node contains data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data})"


class DoublyNode:
    """
    A node in a doubly linked list.

    Contains data and references to both next and previous nodes.
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"DoublyNode({self.data})"


class LinkedList:
    """
    Singly linked list implementation.

    Provides basic linked list operations with O(1) length caching.
    """

    def __init__(self):
        self.head = None
        self._size = 0  # Cache size for O(1) len()

    def append(self, data):
        """
        Add item to end of list.
        Time: O(n) - must traverse to end
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, data):
        """
        Add item to beginning of list.
        Time: O(1) - just update head
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def insert_after(self, target_data, new_data):
        """
        Insert new_data after first occurrence of target_data.
        Time: O(n) - must search for target
        """
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                self._size += 1
                return True
            current = current.next
        return False  # Target not found

    def remove(self, data):
        """
        Remove first occurrence of data.
        Time: O(n) - must search for item
        """
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def find(self, data):
        """
        Find first occurrence of data.
        Time: O(n) - must search through list
        """
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def __len__(self):
        """Return cached size. Time: O(1)"""
        return self._size

    def __str__(self):
        """String representation of the list."""
        if not self.head:
            return "LinkedList([])"

        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return f"LinkedList([{', '.join(items)}])"

    def __iter__(self):
        """Make LinkedList iterable."""
        current = self.head
        while current:
            yield current.data
            current = current.next


class DoublyLinkedList:
    """
    Doubly linked list implementation.

    Maintains both head and tail pointers for O(1) operations at both ends.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data):
        """
        Add item to end of list.
        Time: O(1) - direct tail access
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
        Add item to beginning of list.
        Time: O(1) - direct head access
        """
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def remove_first(self):
        """
        Remove and return first item.
        Time: O(1)
        """
        if not self.head:
            raise IndexError("remove_first from empty list")

        item = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1
        return item

    def remove_last(self):
        """
        Remove and return last item.
        Time: O(1)
        """
        if not self.tail:
            raise IndexError("remove_last from empty list")

        item = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return item

    def __len__(self):
        return self._size

    def __str__(self):
        if not self.head:
            return "DoublyLinkedList([])"

        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return f"DoublyLinkedList([{', '.join(items)}])"


class Deque:
    """
    Deque (Double-Ended Queue) ADT implementation.

    Supports operations at both ends efficiently using DoublyLinkedList.
    """

    def __init__(self):
        self._list = DoublyLinkedList()

    def add_first(self, item):
        """
        Add item to front of deque.
        Time: O(1)
        """
        self._list.prepend(item)

    def add_last(self, item):
        """
        Add item to back of deque.
        Time: O(1)
        """
        self._list.append(item)

    def remove_first(self):
        """
        Remove and return front item.
        Time: O(1)
        Precondition: deque is not empty
        """
        if self.is_empty():
            raise IndexError("remove_first from empty deque")
        return self._list.remove_first()

    def remove_last(self):
        """
        Remove and return back item.
        Time: O(1)
        Precondition: deque is not empty
        """
        if self.is_empty():
            raise IndexError("remove_last from empty deque")
        return self._list.remove_last()

    def first(self):
        """
        Return front item without removing it.
        Time: O(1)
        Precondition: deque is not empty
        """
        if self.is_empty():
            raise IndexError("first of empty deque")
        return self._list.head.data

    def last(self):
        """
        Return back item without removing it.
        Time: O(1)
        Precondition: deque is not empty
        """
        if self.is_empty():
            raise IndexError("last of empty deque")
        return self._list.tail.data

    def is_empty(self):
        """Check if deque is empty. Time: O(1)"""
        return len(self._list) == 0

    def size(self):
        """Return number of items in deque. Time: O(1)"""
        return len(self._list)

    def __str__(self):
        return f"Deque({str(self._list)[18:-1]})"  # Extract inner list representation

    def __len__(self):
        return self.size()


class LinkedQueue:
    """
    Queue ADT implemented using LinkedList.

    Demonstrates the Wrapper Pattern - wrapping a LinkedList to provide
    Queue interface with better performance than list-based queue.

    enqueue: O(1) - append to LinkedList
    dequeue: O(1) - remove from head (vs O(n) for list-based)
    """

    def __init__(self):
        self._list = LinkedList()

    def enqueue(self, item):
        """
        Add item to back of queue.
        Time: O(1) - LinkedList append
        """
        self._list.append(item)

    def dequeue(self):
        """
        Remove and return front item.
        Time: O(1) - direct head manipulation
        Precondition: queue is not empty
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        item = self._list.head.data
        self._list.head = self._list.head.next
        self._list._size -= 1
        return item

    def front(self):
        """
        Return front item without removing it.
        Time: O(1)
        Precondition: queue is not empty
        """
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._list.head.data

    def is_empty(self):
        """Check if queue is empty. Time: O(1)"""
        return len(self._list) == 0

    def size(self):
        """Return number of items in queue. Time: O(1)"""
        return len(self._list)

    def __str__(self):
        return f"LinkedQueue({str(self._list)[12:-1]})"  # Extract inner list

    def __len__(self):
        return self.size()


# Utility functions demonstrating practical applications


def reverse_with_deque(text):
    """
    Reverse a string using a deque.
    Demonstrates deque as stack usage.
    """
    deque = Deque()
    for char in text:
        deque.add_first(char)  # Push to front

    result = ""
    while not deque.is_empty():
        result += deque.remove_first()  # Pop from front
    return result


def sliding_window_maximum(nums, k):
    """
    Find maximum in each sliding window of size k using deque.
    Deque maintains candidates for maximum in O(n) time.
    """
    if not nums or k == 0:
        return []

    deque = Deque()
    result = []

    for i, num in enumerate(nums):
        # Remove elements outside current window
        while not deque.is_empty() and deque.first() <= i - k:
            deque.remove_first()

        # Remove smaller elements (they won't be maximum)
        while not deque.is_empty() and nums[deque.last()] <= num:
            deque.remove_last()

        deque.add_last(i)  # Add current index

        # Add maximum for current window
        if i >= k - 1:
            result.append(nums[deque.first()])

    return result


def check_palindrome(text):
    """
    Check if text is palindrome using deque.
    Compare characters from both ends.
    """
    deque = Deque()
    for char in text.lower():
        if char.isalnum():  # Only consider alphanumeric
            deque.add_last(char)

    while deque.size() > 1:
        if deque.remove_first() != deque.remove_last():
            return False
    return True


if __name__ == "__main__":
    print("=== Chapter 7: Deques and Linked Lists Demo ===\n")

    # Linked List demonstration
    print("Linked List Operations:")
    linked_list = LinkedList()
    for item in ["first", "second", "third"]:
        linked_list.append(item)
        print(f"  Append '{item}': {linked_list}")

    linked_list.prepend("zero")
    print(f"  Prepend 'zero': {linked_list}")

    linked_list.insert_after("second", "2.5")
    print(f"  Insert '2.5' after 'second': {linked_list}")

    linked_list.remove("second")
    print(f"  Remove 'second': {linked_list}")
    print()

    # Doubly Linked List demonstration
    print("Doubly Linked List (Deque Backend):")
    doubly_list = DoublyLinkedList()
    for item in [1, 2, 3]:
        doubly_list.append(item)

    print(f"  Initial: {doubly_list}")
    doubly_list.prepend(0)
    print(f"  Prepend 0: {doubly_list}")
    doubly_list.append(4)
    print(f"  Append 4: {doubly_list}")

    print(f"  Remove first: {doubly_list.remove_first()}")
    print(f"  Remove last: {doubly_list.remove_last()}")
    print(f"  Final: {doubly_list}")
    print()

    # Deque demonstration
    print("Deque Operations:")
    deque = Deque()
    deque.add_first("front")
    deque.add_last("back")
    deque.add_first("very front")

    print(f"  Deque: {deque}")
    print(f"  First: {deque.first()}")
    print(f"  Last: {deque.last()}")
    print(f"  Remove first: {deque.remove_first()}")
    print(f"  Remove last: {deque.remove_last()}")
    print(f"  Final: {deque}")
    print()

    # Queue implementations comparison
    print("Queue Implementation Comparison:")
    from chapter_6_stacks_and_queues.code.stack_queue_adts import Queue as ListQueue

    # Test with 1000 items
    items = list(range(1000))

    print("  Testing with 1000 items...")

    # List-based queue
    list_queue = ListQueue()
    for item in items:
        list_queue.enqueue(item)

    # Measure dequeue performance
    import time

    start = time.time()
    for _ in range(100):
        list_queue.dequeue()
    list_time = time.time() - start

    # LinkedList-based queue
    linked_queue = LinkedQueue()
    for item in items:
        linked_queue.enqueue(item)

    start = time.time()
    for _ in range(100):
        linked_queue.dequeue()
    linked_time = time.time() - start

    print(".4f")
    print(".4f")
    print(".1f")
    print()

    # Practical applications
    print("Practical Applications:")

    # Palindrome checking
    words = ["radar", "hello", "A man a plan a canal Panama", "racecar"]
    for word in words:
        clean_word = "".join(c.lower() for c in word if c.isalnum())
        is_pal = check_palindrome(word)
        print(f"  '{clean_word}' is palindrome: {is_pal}")

    print()

    # Sliding window maximum
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    maxima = sliding_window_maximum(nums, k)
    print(f"  Sliding window maximum (k={k}): {maxima}")

    print("\n=== Key Takeaways ===")
    print("• Linked Lists: Flexible memory, O(1) end operations")
    print("• Doubly Linked: Both ends access, bidirectional traversal")
    print("• Deque: Double-ended operations, stack/queue flexibility")
    print("• Wrapper Pattern: Adapt interfaces, hide implementation")
    print("• Length Caching: O(1) size queries are crucial")
    print("• Choose structures based on access patterns and performance needs")
