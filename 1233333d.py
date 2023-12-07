f=open("new.txt","w")
a=input("Enter the sentence: ")
p=a+"\n"
f.write(p)
f.close()
f=open("new.txt", "r")
l= f.read()
k=""
for i in l:
  k+=i
j=k.split()
for i in j:
  print(i)
f.close()