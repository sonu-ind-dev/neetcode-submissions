class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitingTime = 0 # 13
        prepairingAt = customers[0][0] # 21

        for customer in customers:
            if prepairingAt < customer[0]: prepairingAt = customer[0]

            prepairingAt += customer[1]
            waitingTime += prepairingAt - customer[0]
        
        return waitingTime / len(customers)
