#User function Template for python3
class Solution:
    def insertAtBottom(self,st,x):
        # code here
        
        if len(st) == 0:
            st.append(x)
            return
        temp = st.pop()
        self.insertAtBottom(st,x)
        st.append(temp)
        return st
        


#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        n,x = map(int,input().split())
        stack = list(map(int,input().split()))
        obj = Solution()
        ans = obj.insertAtBottom(stack,x)
        for e in ans:
            print(e,end=" ")
        print()
        
        
        
        print("~")
# } Driver Code Ends