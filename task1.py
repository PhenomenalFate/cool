print("word frequency")
a= input("enter the sentence")
a=a.lower()
a=a.split()
freq=[]
word=[]
b=0
for i in a:
    word.append(i)

    b=(a.count(i))
    freq.append(b)
  
    
print(type(word))
print(type(freq))
print(word)
print(freq)
d={k:v for k,v in zip(word,freq)}
print(d)
