list=[10,40,50]
print(type(list))
print(list[2])
list.append(30)
print(list)

dict={
    "name":"mahi",
    "age":18
}
print(dict.keys())

tup=(10,20,30)
print(type(tup))
print(tup[1])
print(tup[2])

print("Hello World")
#wrd=input()
flag=False
wrd=input()
word="Hello World"
for wrd in word:
    #print(wrd)
    flag=True
    #if wrd in word:
      #  flag=True
       # break
   # else:
      # flag=False
if flag==True:
    print("Char found")
else:
    print("Char not found")        
