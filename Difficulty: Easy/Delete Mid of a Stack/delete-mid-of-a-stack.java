//{ Driver Code Starts
// Initial template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        while (t-- > 0) {
            String temp[] = sc.nextLine().trim().split(" ");
            Stack<Integer> myStack = new Stack<>();
            int n = temp.length;
            // adding elements to the stack
            for (int i = 0; i < n; i++) {
                int x = Integer.parseInt(temp[i]);
                myStack.push(x);
            }
            Solution obj = new Solution();
            obj.deleteMid(myStack);

            while (!myStack.isEmpty()) {
                System.out.print(myStack.peek() + " ");
                myStack.pop();
            }
            System.out.println();

            System.out.println("~");
        }
    }
}
// } Driver Code Ends


// User function Template for Java



class Solution {
    
    
    private void deleteEle(Stack<Integer> s, int mid, int count) {
        if (count == mid) { // Base case: remove middle element
            s.pop();
            return;
        }

        int temp = s.pop(); // Remove top element
        deleteEle(s, mid, count + 1); // Recursive call
        s.push(temp); // Restore elements after deletion
    }
    
    
    // Function to delete middle element of a stack.
    public void deleteMid(Stack<Integer> s) {
        // code here
        if (s.isEmpty()) return;

        int mid = (s.size() / 2) + 1; 
        deleteEle(s, mid-1, 0);
    }
}
