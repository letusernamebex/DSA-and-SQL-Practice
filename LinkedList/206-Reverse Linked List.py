# Using Stack--------------------------------------------------------------------------------------------------------------
# We will iterate through the list once, pushing all the nodes into the stack
# After pushing all nodes, we will start popping and changing the pointer

# Reversing using Iterative method------------------------------------------------------------------------------------------    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None

        while curr:
            temp = curr.next   # we will store the next node before breaking the connection
            curr.next = prev   # we will move the pointer to previous node
            prev = curr        # moving pointers
            curr = temp
            
        return prev            # prev will be at the new head and curr will be at None after prev
#---------------------------------------------------------------------------------------------------------------------------------
# Reversing using Recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head, prev):
            if head == None:  #Base case when head reaches None, we would return "prev" node, recursion stack will start popping
                return prev
            else:
                next = head.next   #following iterative approach
                head.next = prev
            return rev(next, head)
        return rev(head, None)
