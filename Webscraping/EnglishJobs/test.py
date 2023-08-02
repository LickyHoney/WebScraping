def mapping(f, xs):
    assert isinstance(xs, list)
    if xs == []:
        value = []
    else:
        value = [f(xs[0])]
    if len(xs) != 1:
        value += mapping(f, xs[1:])
    return value

def util_apply(f, pair):
    assert isinstance(pair, list) or isinstance(pair, tuple)
    return f(pair[0], pair[1])

pairs = [(1,3), (2,2), (3,1)]

def plus(x,y): return x+y

result = mapping(lambda pair:util_apply(plus, pair), pairs)
print(result)


sum = -1
count = 0
py_list = [1,2,3,4,5,6]
for j in py_list[::-1]:
    if(j==3 or count>=2):
        pass
    else:
        sum += j
        count +=1

print(sum)
    

def append_function(item, l1=[]):
    l1.append(item)
    return l1

list1 = append_function(11)
list1 = append_function(11)
print (list1)

tuple_1 = tuple("1,2,3,4,5",)
tuple_2 = tuple([1,2,3,4,5])
tuple_3 = tuple((1,2,3,4,5))
tuple_4 = tuple(('1','2','3','4','5'))

print(len(tuple_1) + len(tuple_2) + len(tuple_3))


principle = 300
_yield = 15
time = 3

print("Interest ={}".format(principle * _yield* time/100))

a = {(x,y) for x in range(1,5) for y in range(1,5) if x<=y}
b = {(x,y) for x in range(1,5) for y in range(1,5) if x>=y}
print(len(a&b))

# with open("value.txt", "r") as file_obj:
#     content = "test\n"
#     file_obj.writelines(content)
#     file_obj.seek(0,0)
#     body = file_obj.readlines()
#     print("read body: %s" % (body))

str = "FutureSkill"
print(str.rjust(12, '*'))


# a = [0,1,2,3,4]
# i = 1
# sum=0
# while a[i] != 0 and i != 5:
#     sum = sum + a[i]
#     i=i+1
#     print(sum)


# p = [lambda _: 1]
# for k in range(1,6):
#     p.append((lambda f: (lambda x: x * f(x))) )

a = [1,2,3,4,5]
b = [6,7,8,9,10]
i=0
i,a[i] = i+2, b[i]
print(i,a) 

a = [1,2,3,4,5]
b =[1,2,3]
a += a
print(a)
print(set(a) - set(b) - {4})

str = 'abc,abc,abc,abc,abc,abc,abc'
print(str.count('abc', -18, -1))

y =0
for i in range(0,10,2):
    y+=i
print(y)