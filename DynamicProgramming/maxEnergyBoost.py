class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        
        n = len(energyDrinkA)

        dp = {}
        
        def function(i, choice):

            if (i >= n):
                return 0

            if((i, choice) in dp):
                return dp[(i, choice)]

            if(choice == "A"):

                pickA = energyDrinkA[i] + function(i + 1, "A")

                nPickA = energyDrinkA[i] + function(i + 2, "B")

                dp[(i, choice)] = max(pickA, nPickA)
                return max(pickA, nPickA)
            
            elif(choice == "B"):

                pickB = energyDrinkB[i] + function(i + 1, "B")

                nPickB = energyDrinkB[i] + function(i + 2, "A")

                dp[(i, choice)] = max(pickB, nPickB)
                return max(pickB, nPickB)
        
        return max(function(0, "A"), function(0, "B"))



