import sys
# You may change this function parameters
def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    # Participants code will be here
    profit = 0
    j=0
    for i in range(1, len(predictedSharePrices)):
        if predictedSharePrices[i - 1] > predictedSharePrices[i]:
            j = i

        if predictedSharePrices[i - 1] <= predictedSharePrices[i] and (i + 1 == len(predictedSharePrices) or predictedSharePrices[i] > predictedSharePrices[i + 1]):
            profit += (predictedSharePrices[i] - predictedSharePrices[j])
    return profit


def main():
    predictedSharePrices=[]
    numOfPredictedDay=int(input("enter no. of days:"))
    #line = input().split()
    for x in range(1,numOfPredictedDay+1):
        ele = int(input()) 
        predictedSharePrices.append(ele) # adding the element 
      
    print("predicted Share Prices are:",predictedSharePrices) 
    
    
    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)
    print("maximum profit is:")
    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()
