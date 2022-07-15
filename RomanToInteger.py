romanDict= {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
s=input()
valueArray=[]
decimalValue=0
for i in s:
    valueArray.append(romanDict[i])
for i in range(0,len(valueArray)-1):
    if (valueArray[i]*5==valueArray[i+1]) or (valueArray[i]*10==valueArray[i+1]):
        valueArray[i]*=-1
print(sum(valueArray))
