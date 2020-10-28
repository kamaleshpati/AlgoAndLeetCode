class Solution:
    def bestTeamScore(self, scores , ages) -> int:
        best = 0
        for i in range(len(scores)):
            conflictPos = self.hasConflict(scores,ages)

            if len(conflictPos) == 0:
                best += scores[i]
            else:
                if len(conflictPos) == 1:
                    best+=scores[i]
                
        return best



    def hasConflict(self , scores , ages):
        conflictPos = []
        for i in range(len(scores)):
            for j in range(len(scores)):
                if ages[i] < ages[j] and scores[i] > scores[j]:
                    conflictPos.append(j)
        
        return conflictPos


print(Solution().bestTeamScore([1,2,3,4],[8,9,10,1]))