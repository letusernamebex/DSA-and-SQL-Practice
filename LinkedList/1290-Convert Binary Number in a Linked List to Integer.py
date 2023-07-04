# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Basic Solution-------------------------------------------------------------------------------------------------
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num=0
        length=0
        curr=head
        while curr:    #calculate length of linkedlist
            length+=1
            curr=curr.next
            
        curr=head
        while curr:
            # print(curr.val)
            num = num + ((curr.val)*(2**(length-1))) #do weighted sum of binary bits multiplied by powers of 2
            # print(num)
            curr=curr.next
            length-=1
            
        return num
#--------------------------------------------------------------------------------------------------------------
#Best Solution (Bitwise Concept used)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        while head: 
            answer = 2*answer + head.val #Multiplying answer by 2 shifts that number left, then we add a bit (We can also do answer<<1, same as *2)
            head = head.next             #(Similar thing is done in decimal, multiplying by 10, then adding next digit)
        return answer    
#---------------------------------------------------------------------------------------------------------------
#recursive Solution for upper one
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def convert(ans, head):
            if head==None:
                return ans
            ans = ans*2 + head.val
            return convert(ans, head.next)
        return convert(0,head)