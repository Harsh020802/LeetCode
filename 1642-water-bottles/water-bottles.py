class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        c=numBottles
        while(numBottles>=numExchange):
            new=(numBottles%numExchange)
            numBottles=(numBottles//numExchange)
            c+=numBottles
            numBottles+=new

        return c

    