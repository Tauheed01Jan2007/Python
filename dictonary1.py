# dict = {0:"mango" , 1:"banana",2:"grapes",3:[1,2,3,4,5,6]}
# print(dict[3][4])


# d1 = {
#     1 : "car",
#     34 : "fruit",
#     89 : "abcd",
#     56 : [9,8,6,{'branch':'cs','name':'rahul','marks':89},2,3],
#     'z' : 67,
#     'apple' : 45
# }
# print(d1[56][3]['name'])

dataset={
    'student' : [
        {
            'sr_no' : 1,
            'details' : {
                'name' : 'Tauheed Khan',
                'id' : 'S1001',
                'branch' : 'IT',
                'marks' : {
                    'sem_1' : [85,90,75],
                    'sem_2' : [92,79,85],
                    'sem_3' : [78,84,94],
                }
            }
        }
    ]
}

name = dataset['student'][0]['details']['name']
branch = dataset['student'][0]['details']['branch'] 
s1 = dataset['student'][0]['details']['marks']['sem_1']
s2 = dataset['student'][0]['details']['marks']['sem_2']
s3 = dataset['student'][0]['details']['marks']['sem_3']
overwall_max = max(max(s1),max(s2),max(s3))
print(name,branch,max(s1),max(s2),max(s3))
# print(name,branch,overwall_max)
