# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self,val = 0, next= None):
        self.val = val
        self.next = next



def isPalindrome(head):
    rev = None
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow_next = slow.next
        slow.next = rev
        rev = slow
        slow = slow_next
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(3)
six = ListNode(2)
seven = ListNode(1)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = None

vald = isPalindrome(one)
print("Result:",vald)
