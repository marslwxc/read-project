def reverseKGroup(self, head, k):
        if(head==None):return head 
        N=head
        i=0
        while(N.next!=None and i<k):
            i=i+1
            N=N.next
        if(k-1>i):return head
        i=0
        a=head
        b=head.next
        while(i<k-1):
            c=b.next
            b.next=a
            a=b
            b=c
            i=i+1
        head.next=self.reverseKGroup(b,k)  
        return a