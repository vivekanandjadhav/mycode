v=int(input("enter the number of students"))
lis=[]
s=[]
for i in range(v):
    name =input()
    score =float(input())
    lis.append([name,score])
    s.append(score)
#print(lis)
#print(s)
s=sorted(set(s))
print(s[1])
a=s[1]
name=[]
for i in lis:
  if a==i[1]: #here we comparing the sorted list index 1==list of ith positions of 1 index which is name
     name.append(i[0])
name.sort()
for i in name:
    print(i)



