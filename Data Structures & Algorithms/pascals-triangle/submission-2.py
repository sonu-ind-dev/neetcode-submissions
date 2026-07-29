class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1, 1]] * numRows

        output[0] = [1]

        for index, value in enumerate(output):
            if index < 2:
                continue
            
            newValue = value[:]
            for i in range(0, index - 1):
                newValue.insert(i + 1, output[index - 1][i] + output[index - 1][i + 1])

            output[index] = newValue
        # while numRows != len(output):
        #     lastValue = output[len(output) - 1]
        #     newValue = [1, 1]

        #     for i in range(0, len(lastValue) - 1):
        #         newValue.insert(i+1, lastValue[i] + lastValue[i+1])
            
        #     output.append(newValue)
        
        return output
