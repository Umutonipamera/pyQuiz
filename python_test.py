x=[100,110,120,130,140,150]
a= [item * 5 for item in x]
print(a)

def divisible_by_three(n):
	new_list= range(n,n+1)
	for a in new_list:
		if(a%3==0):
			print(a)
divisible_by_three(100)			
  

def flattens():
    x=[[1,2],[3,4],[5,6]]
    z=[b for a in x for b in a]
    print(z)
flattens()

def smallest():
    x=[3,6,8,2,4,1,5,7]
    print(min(x))
smallest()

def divisible_by_seven():
	n=[]
	for x in range(100, 200): 
	    if (x%7==0):
	        n.append(str(x))
	print (','.join(n))
        
divisible_by_seven()

x = ['a','b','a','e','d','b','c','e','f','g','h']
x=list(set(x))
print(x)


class Rectangle:

	def__init__(self,w,l):


	self.width=width

	self.length=length
	def area(self):
	return self.width*self.length	
def parameter(self):
	return self.width+self.length


students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
def greetings():
	for student in students:
		name= student["name"]
		age= student["age"]
		print(f"Hello student {name}, you were born in {2021-age}")
greetings()
