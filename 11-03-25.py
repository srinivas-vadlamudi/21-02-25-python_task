# sum of elements in nested list
list1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]] 
sum=0
for i in list1:
    for j in i:
            sum += j

print("sum of all nested list is",sum)

# min and max value in nested list
list2=[[-8,2,3,-2],[5,6,7,8,99],[9,10,11,12,-4],[50]] 

min_value = [0][0]
max_value = list2[0][0]

for i in list2:
    for value in i:
            if value < min_value:
                  min_value = value
            elif value > max_value:
                  max_value = value    

print("min value in nested list",min_value) 
print("max value in nested list",max_value)                 



        
            
           
         
            

        


