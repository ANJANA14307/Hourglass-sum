#!/bin/python3
def hourglassSum(arr):
    max_sum=-63
    for i in range(4):
        for j in range(4):
            top=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            mid=arr[i+1][j+1]
            bot=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            hourglass=top+mid+bot
            max_sum=max(max_sum,hourglass) 
    return max_sum 
if __name__=='__main__':
    arr=[]
    for i in range(6):
        row=list(map(int,input().split()))
        if len(row)!=6:
            exit() 
        arr.append(row) 
res=hourglassSum(arr) 
print(res
