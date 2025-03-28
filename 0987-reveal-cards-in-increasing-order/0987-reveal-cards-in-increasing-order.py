class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = [None] * len(deck)
        queue = []
        deck.sort()

        for i in range(len(deck)):
            queue.append(i)

        for i in range(len(deck)):
            idx = queue.pop(0)
            ans[idx] = deck[i]
            if queue:
                queue.append(queue.pop(0))

        return ans
            
        