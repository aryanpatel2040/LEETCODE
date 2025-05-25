# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #If list is empty or has only one node then simply return the head
        if head == None or head.next == None:
            return head

        #Else odd will be the first node in the list and even w'd be the seccond
        odd = head
        even = head.next 
        even_head = even #This contains the reference to even list

        #Iterate till current even or next even won't equals to None
        while even!=None and even.next!=None: 
            odd.next = even.next #Jumping onto the next odd
            odd = odd.next
            even.next = odd.next #Jumppin onto the next even
            even = even.next
        odd.next = even_head #Joining the odd followed by even indices
        return head

