#Best Solution
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head  #using fast pointer and slow pointer method, slow jumps one node, fast jumps two node
        while fast and fast.next:  
            fast = fast.next.next   #incase of odd no. of elements, fast would get to last node only
            slow = slow.next
        return slow   #in case of even no. of nodes, fast will reach none
#----------------------------------------------------------------------------------------------------------------
#Basic Approach
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while head:
            length+=1
            head = head.next
        # print(length)   
        mid = length//2
        for i in range(mid):
            
            curr = curr.next
            
        return curr
