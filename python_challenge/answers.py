#0
def sayHello():
   return 'hello'
#1
def addOne(x):
   return x+1
#2
def addTwoNumbers(x,y):
   if isinstance(x,str) or isinstance(y,str):
      return 'nan'
   return x+y
#3
def sumNumbers(x):
   return sum(x)
#4
def addList(*args):
   if len(args) == 0:
      return 0
   else:
      ans=0
      for i in args:
         ans+=i
   return ans
#5
def computeRemainder(x,y):
   if y == 0:
      return float('inf')
   else:
      return x%y
#6
def ranges(x,y):
   if x>y:
      return 'First argument must be less than second'
   else:
      ans = []
      for i in range(x,y):
         ans.append(i)
      return ans
#7
def reverseUpcaseString(x):
   ans = x.upper()
   return ans[::-1]
#8
def removeEnds(x):
   if len(x) < 3:
      return ''
   else:
      return x[1:-1]
#9
def charCount(x):
   ans={}
   for i in x:
      n=0
      ans[i]=0
      while n < len(x):
         if i == x[n]:
            ans[i]+=1
         n+=1
   return ansgit 
#10
def formatWithPadding(x,y,z):
   diff,i,ans = z-len(str(x)),0,''
   if diff > 0:
      while i < diff:
         ans+=y
         i+=1
      ans+=str(x)
      return ans
   else:
      return str(x)
#11
def isPalindrome(x):
   orig = x.replace(' ','').lower()
   rev=orig[::-1]
   if orig == rev:
      return True
   else: return False
#12
def hammingDistance(x,y):
   i,ans=0,0
   while i < len(x):
      if x[i] != y[i]:
         ans+=1
      i+=1
   return ans
#13
def mumble(x):
   n,ans=1,''
   for i in x:
      a=0
      while a < n:
         ans+=str(i)
         a+=1
      ans+='-'
      n+=1
   return ans[0:-1]
#14
def fromPairs(x):
   ans={}
   for i in x:
      ans[i[0]]=i[1]
   return ans