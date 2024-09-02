# string


# s = str()#empty
# s1 = ''#empty
# s2 ='wertyuERDFGVHb234567#$%^&'
# s3 ="wertyuERDFGVHb234567#$%^&"
# s4 ='''wertyuERDFGVHb234567#$%^&'''
# s5="""wertyuERDFGVHb234567#$%^&"""
# print(type(s5))
#
# var = (10,9.9,9+9j,True,[89,90],'ertyuijh',10,10)
# print(type(var))

# se = {10,8+9j,True,'56789',10,10,True,True,(89,90)}
# print(se)
# print(type(se))

#Type Casting


# a = [45,89,67,81,83,255,256]
# a = bytearray(a)
# print(a)
# print(type(a))

# range(1,11)

var = 'qwerty'
print(type(var))
print(dir(var))

#Captilize
# print(var.capitalize())

#upper and lower
# var = 'QgjTTghgv'
# print(var.upper())
# print(var.lower())

# startswith() and endswith()
# st ='yes i have'
# # print(st.startswith('y'))
# print(st.endswith('e'))

#swapcase
# st = 'gvhyFYVyhvhv'
# print(st.swapcase())

#count
# st = 'i love india, india ia best'
# print(st.count(' '))
# print(len(st))

#replace
# st = 'Ji Jacky'
# print(st.replace('Ji','Hi'))

# isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier(','
# islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper'

#strip.split.join,format(f string)

#strip :- rstrip.lstrip

# st = '           kjhjk             '
# print(st.rstrip())

#split

# st = 'Ramesh,Suresh,Vibesh,Vignesh,Mahesh,Lokesh'
# print(st.split(','))

#join
# li = ['Ramesh', 'Suresh', 'Vibesh', 'Vignesh', 'Mahesh', 'Lokesh']
# print(' '.join(li))

#format(f string)
a = 10
b = 20

result = a+b

print(f'addition {a} and {b} the result is :- {result}')