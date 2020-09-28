class Solution:
    def minOperations(self, logs: [str]):

        count = 0
        for i in logs:
            if i == "../":
                if count != 0:
                    count= count -1
            elif i == "./":
                count= count
            else:
                count= count+1
        return count
    

print(Solution().minOperations(["d1/","d2/","./","d3/","../","d31/"]))