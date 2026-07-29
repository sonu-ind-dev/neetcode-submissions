class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitingTime = 0 # 13
        prepairedgAt = customers[0][0] # 21

        for customer in customers:
            arrivalTime = customer[0]
            orderTime = customer[1]

            if prepairedgAt < arrivalTime: prepairedgAt = arrivalTime

            prepairedgAt += orderTime
            waitingTime += prepairedgAt - arrivalTime
        
        return waitingTime / len(customers)
