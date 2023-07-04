# Basic Solution

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        setA = set()
        
        while headA:
            setA.add(headA)
            headA = headA.next
            
        while headB:
            if headB in setA:
                return headB
            headB = headB.next
            
        return headB

# Optimized solution using 2 pointers and without additional data structure

# suppose A=a+c; B=b+c;
# ==> A+B=a+c+b+c
# ==> B+A=b+c+a+c
# this nullifies the difference in length of both LLs. So, on 2nd traversal, they both will coincide or miss each other
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if headA is None or headB is None:
            return None
        
        currA, currB = headA, headB
        
        while currA != currB:

            # when a node hits end, start it from head of another linked list
            
            currA = headB if currA is None else currA.next
            currB = headA if currB is None else currB.next
            
        return currA

