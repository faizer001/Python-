num = int (input("enter a number : "))
even_sum = 0
odd_sum = 0
i = 0
while i <= num :
  if(i%2==0):
    even_sum+=i
  else:
    odd_sum+=i
  i+=1
print("Even sum is : ",even_sum)  
print("Odd sum is : ",odd_sum)