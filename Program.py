Input = input("Please Introduce yourself")
WordCount = 0
CharecterCount = 0

for a in Input:
   CharecterCount = CharecterCount + 1
   if(a == ' '):
      WordCount = WordCount + 1 

print(WordCount + 1)
print(CharecterCount)