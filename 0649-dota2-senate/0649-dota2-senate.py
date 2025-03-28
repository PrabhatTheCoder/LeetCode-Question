class Solution:
    def predictPartyVictory(self, s: str) -> str:
        n = len(s)
        radiant = []
        dire = []
        for i, c in enumerate(s):
            if c == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
                dire.pop(0)
                radiant.pop(0)
            else:
                dire.append(dire[0] + n)
                radiant.pop(0)
                dire.pop(0)

        return "Radiant" if radiant else "Dire"