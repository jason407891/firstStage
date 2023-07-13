def find_index_of_car(seats, status, number):
    # your code here
    #seats=array
    #status=array
    #number=int
    avalible_seat=seats
    ans=-1
    nowmin=100
    for i in range(0,len(seats)):
        if status[i]==0:
            avalible_seat[i]=0
        #avalible_seat實際上可載人的空位，並減掉乘客數量，大於等於零的最小值為最適合的解
        avalible_seat[i]-=number  
        #如果是正數，又比現在最小的數字小，ans的位子就會被取代  
        if avalible_seat[i]>-1 and avalible_seat[i]<nowmin:
            nowmin=avalible_seat[i]
            ans=i
    print(ans)
    
        
find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2