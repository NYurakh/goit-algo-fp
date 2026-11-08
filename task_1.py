class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Реверсування через зміну посилань."""
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def get_middle(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


    def sorted_merge(self, a: Node | None, b: Node | None) -> Node | None:
        """Об'єднання двох відсортованих списків."""
        dummy = Node(0)
        tail = dummy
    
        while a is not None and b is not None:
            if a.data <= b.data:
                tail.next = a
                tail = a
                a = a.next
            else:
                tail.next = b
                tail = b
                b = b.next
    
        tail.next = a if a is not None else b
    
        return dummy.next

    def merge_sort(self, head):
        """Сортування злиттям."""
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        right = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(right)

        return self.sorted_merge(left, right)

    def merge_sorted_lists(self, other):
        """Об'єднання двох відсортованих списків."""
        self.head = self.sorted_merge(self.head, other.head)
        other.head = None


if __name__ == "__main__":
    first = LinkedList()

    for value in [5, 10, 15, 20, 25]:
        first.insert_at_end(value)

    print("Початковий список:")
    first.print_list()

    first.reverse()
    print("Після реверсування:")
    first.print_list()

    first.head = first.merge_sort(first.head)
    print("Після сортування:")
    first.print_list()

    second = LinkedList()
    for value in [59, 20, 35]:
        second.insert_at_end(value)

    second.head = second.merge_sort(second.head)

    first.merge_sorted_lists(second)
    print("Після об'єднання:")
    first.print_list()
