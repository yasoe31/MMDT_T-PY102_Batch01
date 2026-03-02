"""
Lab01.py — Linked List Lab (Auto-graded)

Covers:
- LeetCode 206: Reverse Linked List
- LeetCode 2816: Double a Number Represented as a Linked List

Lab format:
- Node classes are defined separately from LinkedList wrappers.

Student instructions:
- Do NOT change required function names/signatures.
- You MAY add helper functions/methods.
- Use pointer manipulation (don’t solve by converting the whole list to an int or Python list).
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    @classmethod
    def from_list(cls, values):
        head = None
        tail = None
        for v in values:
            node = Node(v)
            if head is None:
                head = node
                tail = node
            else:
                assert tail is not None
                tail.next = node
                tail = node
        return cls(head)

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


# ============================================================
#  REQUIRED FUNCTIONS (Implement these)
# ============================================================

def reverseList(head):
    """
    LeetCode 206 — Reverse Linked List
    Reverse a singly linked list and return the new head.
    Time: O(n), Space: O(1)
    """
    # TODO: Implement
    #raise NotImplementedError

    current_node = head

    is_first = True
    previous_node = None

    #current_node = current_node.next # start from 2nd node, since we already set the first node's next to None.

    while current_node is not None:

        next_node = current_node.next
        if is_first:
            current_node.next = None
            previous_node = current_node
            is_first = False
            current_node = next_node
        else:
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

    head = previous_node
    return head




def doubleIt(head):
    """
    LeetCode 2816 — Double a Number Represented as a Linked List

    Digits are stored in forward order (most significant digit first).
    Return the head of a new list (or reuse nodes) representing 2x the number.

    Examples:
      1 -> 8 -> 9   (189)  =>  3 -> 7 -> 8  (378)
      9 -> 9 -> 9   (999)  =>  1 -> 9 -> 9 -> 8  (1998)

    Requirements:
    - Use linked-list operations/pointer logic.
    - Avoid converting the entire list into an integer/string for the core solution.
    """

    # TODO: Implement
    #raise NotImplementedError

    # Step 1: Reverse the list to make it easier to double from the least significant digit
    reversed_head = reverseList(head)
    # Step 2: Double the digits and handle carry
    current_node = reversed_head
    carry = 0
    last_node = None
    while current_node is not None:
        value = current_node.val * 2
        value += carry
        current_node.val = value % 10
        carry = value // 10
        if current_node.next is None:
            last_node = current_node
        current_node = current_node.next

    # Step 3: If there's a carry left after processing all digits, add a new node
    if carry > 0:
        new_node = Node(carry)

        # attach the new node to the end of the reversed list, kind of dangerous because it modifies the reversed head list.
        last_node.next = new_node


    # Step 4: Reverse the list back to restore original order
    final_head = reverseList(reversed_head)
    return final_head


# ============================================================
#n1 = Node(3)

#n2 = Node(5)

#n1.next = n2

#sll = SinglyLinkedList(n1)
#print(sll.to_list())

# ============================================================

#sll = SinglyLinkedList.from_list([2,4])

#print(sll.to_list())

# ============================================================

#sll = SinglyLinkedList.from_list([2,4,6,8,10])

#reversed_list = reverseList(sll.head)

#print(SinglyLinkedList(reversed_list).to_list())

# ============================================================

#sll = SinglyLinkedList.from_list([1,8,9])

sll = SinglyLinkedList.from_list([9,9,9])

doubled_list = doubleIt(sll.head)

print(SinglyLinkedList(doubled_list).to_list())

