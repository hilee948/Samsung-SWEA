n = int(input())
 
check = ['3','6','9']
 
for i in range(1,n+1):
  arr = str(i)
  temp=''
  for j in arr:
    if j in check: 
      temp += '-'
  if not temp:
    print(i,end=' ')
  else:
    print(temp,end=' ')
