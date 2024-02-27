class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant=deque()
        dire=deque()

        for i , char in enumerate(senate):
            if char=='R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            rad_hero=radiant.popleft()
            dire_hero=dire.popleft()

            if rad_hero<dire_hero:
                radiant.append(rad_hero+len(senate))
            else:
                dire.append(dire_hero+len(senate))
        
        return 'Radiant' if len(radiant)>len(dire) else 'Dire'