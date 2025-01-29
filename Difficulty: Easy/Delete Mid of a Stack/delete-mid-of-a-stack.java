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
    // Helper function to delete the middle element
    private void deleteEle(Stack<Integer> s, int mid) {
        if (mid == 0) { // Base case: when mid index is reached
            s.pop();
            return;
        }

        if (s.size() == 1) { // Base case: if only one element remains, do nothing
            return;
        }

        int temp = s.pop(); // Remove top element
        deleteEle(s, mid-1); // Recursive call
        s.push(temp); // Restore elements after deletion
    }

    // Function to delete the middle element of a stack.
    public void deleteMid(Stack<Integer> s) {
        if (s.isEmpty()) return;

        int mid = (s.size() / 2); // 1-based mid index
        deleteEle(s, mid); // Start recursion
    }

}
