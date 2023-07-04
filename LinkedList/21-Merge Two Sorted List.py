# Similar to merging two sorted lists.     
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        curr = dummy = ListNode()   # We will initialize curr and dummy nodes.
                                    # We will compare nodes in list1 and list2, and add in LL starting with curr node
        
        while list1 and list2:
            if list1.val<=list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
                
            curr = curr.next
            
        # if list1:
        #     curr.next = list1
        
        # elif list2:
        #     curr.next = list2
        curr.next = list1 or list2 
            
        return dummy.next   # Since curr will reach end of the LL, that is why we are using dummy, to return start of that LLs
#-----------------------------------------------------------------------------------------------------------------------------
# Using Recursion

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merger(list1,list2):
            # if list1 == None:
            #     return list2
            # if list2 == None:
            #     return list1
            if not list1 or list2:
                return list1 or list2
            
            if list1.val<=list2.val:
                list1.next = merger(list1.next, list2)
                return list1
            else:
                list2.next = merger(list1, list2.next)
                return list2
                
        return merger(list1, list2)

# Recursive Solution 2

    def mergeTwoLists(self, list1, list2):
        if list1 and list2:
            if list1.val > list2.val:  # here we are first comparing first node of both, if list1 has larger value node, then we swap
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2) # we will build whole LL fter list1 node
        return list1 or list2
