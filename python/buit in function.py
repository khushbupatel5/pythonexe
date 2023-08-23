# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:22:00 2023

@author: khushbu vora
"""

print("hello")
print(abs(-7))
print(abs(-1))
print(all({'*','',''}))
print(all([' ',' ',' ']))
print(any((1,0,0)))
print(any((0,0,0,)))
print(ascii('10'))
print(ascii('usor'))
print(ascii(['s','$']))
print(bin(7))
#print(bin(7.0))

print(bool(0.5))
print(bool(''))
print(bool(True))
a=bytearray(3)
print(a,'n/')
a.append(1)
print(a,'/n')
a[0]=2
print(a)
print(a[0])
print('/n',bytearray([1,2,3,4]))
print(bytes(5))
print(bytes([1,2,3,4,5]))
print(bytes('hello','utf-8'))
print(callable([1,2,3]))
print(callable(callable))
print(callable(False))
print(callable(list))
print(chr(65))
print(chr(97))
print(chr(89))
print(chr(48))

'''
class fruit:
     def sayhi(self):
         print("Hi,i am a fruit")
fruit.sayhi=classmethod(fruit.sayhi) 
fruit.sayhi()        
exec(compile('a=5\nb=7\nprint(a+b)','','exec'))
print(complex(3))
print(complex(3.5))
print(complex(3+5j))
class fruit:
     size=7
orange=fruit()
print(orange.size)
delattr(fruit,'size')
#print(orange.size)     
print(dict())
print(dict([(1,2),(3,4)]))
class fruit:
            size=7
            shape='round'
orange=fruit()


print(dir(orange)) 
print(divmod(3,7))
print(divmod(7,3))  
for i in enumerate (['a','b','c']):
     print(i)  
exec('a=2;b=3;print(a+b)') 
exec(input ("Enter your program"))
a=list(filter(lambda x:x%2==0,[1,2,0,False]))
print(a) 
print(float(2))
print(float('3'))
print(float('5'))
#print(float(False))
#print(float(4.7))

a,b=2,3
print("a={0} and b={1}".format(a,b))
print("a={a} and b={b}".format (a=3,b=4) )

class fruit:
     size=7
     price=50
orange=fruit()
orange.size
orange.price

print(getattr(orange,'size'))
print(getattr(orange,'price'))
print(globals()) 
print(hasattr(orange,'size'))
print(hasattr(orange,'shape'))
print(hasattr(orange,'color'))
print(hash(orange))
print(hash(True))
print(hash(0))
print(hash(3.7))
print(hash (hash))
print(help())
print(hex(16))
print(hex(False))
print(int('7'))
print(input("Enter a number"))
print(int(input("/nEnter a name"))) 
print(isinstance(0,str))
print(isinstance(orange,fruit))'''
for i in iter([1,2,3]):
    print(i)
print(len([1,2,3]))
print(list({1,3,2,2}))
print(locals())
print(list(map(lambda x:x%2==0,[1,2,3,4,5])))
print(max(2,3,4))
print(max([3,4,5]))
print(max('hello','Hello'))
print(max("hello","world"))
a=bytes(4)
print(memoryview(a))
for i in memoryview(a):
    print(i)
print(min(3,5,1))
print(min(True,False))  
O=object()
print(type(O)) 
print(dir(O)) 
print(oct(7))
print(oct(8))
print(oct(True)) 
print(pow(3,4)) 
print("okay,next fuction please")
for i in range(7,2,-2):
    print(i)
print(repr("hello"))
print(repr(7))
print(repr(False))    
a=reversed([3,4,5,])
print(a)
for i in a:
    print(i)
print(round(3.777,2))
print(round(3.7,3))
print(set([2,2,1,3]))
print(slice(2,7,2))
print('python'[slice(1,5,2)])
print('hello world'[slice(2,9,3)])
print(sorted('python'))
print(sorted([1,2,3,]))
print(sum([3,4,5],3))
print(tuple([1,2,3]))
print(tuple({1:'a',2:'b'}))
print(type({}))
print(type(set()))
print(type(()))
print(type((1)))
print(type((1,)))



