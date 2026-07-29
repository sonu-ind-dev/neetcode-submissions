class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        while numRows != len(output):
            lastValue = output[len(output) - 1]
            newValue = [1, 1]

            for i in range(0, len(lastValue) - 1):
                newValue.insert(i+1, lastValue[i] + lastValue[i+1])
            
            output.append(newValue)
        
        return output
