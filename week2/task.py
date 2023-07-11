
#task1

def find_and_print(messages):
# write down your judgment rules in comments
# your code here, based on your own rules
    #把message放在conversation的字典
    conversation_dict=messages
    #關鍵字放在query的陣列裡面
    query=["18 years old","legal age","college student","vote"]
    for conver in conversation_dict.items():
        #迴圈判斷關鍵字有沒有在每一句對話裡面
        for search in query:
            if search in conver[1]:
                print(conver[0])
        
find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
    })




#task2

def calculate_sum_of_bonus(data):
# write down your bonus rules in comments
# your code here, based on your own rules
    employees_list=data
    #整理匯率
    for employee in employees_list['employees']:
        if "USD" in str(employee['salary']):
            employee['salary']=employee['salary'].replace("USD","")
            employee['salary']=int(employee['salary'])*30
        
    #公式 salary, performance and role fields
    sum_bonus=0
    for employee in employees_list['employees']:
        role={'Engineer':1,'Sales':1,'CEO':1.2}
        performance={'above average':1.1,'average':1,'below average':0.9}

        for r in role.keys():
            if employee['role']==r:
                employee['role']=role[r]
        for p in performance.keys():
            if employee['performance']==p:
                employee['performance']=performance[p]
        employee['salary']=str(employee['salary']).replace(",","")
        employee['salary']=int(employee['salary'])*0.01
        employee['bonus']=employee['salary']*employee['performance']*employee['role']
        sum_bonus+=employee['bonus']
        
    if sum_bonus > 10000:
        print("總獎金超過10,000")
    else:
        print("總共獎金"+str(sum_bonus))


calculate_sum_of_bonus({

    "employees":[
    {
    "name":"John",
    "salary":"1000USD",
    "performance":"above average",
    "role":"Engineer"
    },
    {
    "name":"Bob",
    "salary":60000,
    "performance":"average",
    "role":"CEO"
    },
    {
    "name":"Jenny",
    "salary":"50,000",
    "performance":"below average",
    "role":"Sales"
    }
    ]
    }) # call calculate_sum_of_bonus function


#task3

def func(*data):
# your code here
    second={}
    for name in data:
        second[name]=[name[1],0]
        #second={'名字':['第二個字',數量]}
    # i=['第二個字',數量]
    for i in second.values():
        # k=['第二個字',數量]
        for k in second.values():
            if i[0]==k[0]:
                i[1]+=1
    #second={'名字':['第二個字',數量],'名字':['第二個字',數量]}
    #no_one可以控制有沒有印過
    no_one=0
    for name in second.items():
        if name[1][1]==1:
            print(name[0])
            no_one=1
        #如果全部都沒有
    if no_one==0:
        print("沒有")

func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有


#task4


#There is a number sequence: 0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, …
                   #index排序0, 1, 2, 3, 4, 5, 6, 7,   8,  9, 10
def get_number(index):
    output=0
    if index%2==0:
        output=index/2*3
        print(int(output))
    else:
        output=(index+1)/2*3+1
        print(int(output))


get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15



#task5