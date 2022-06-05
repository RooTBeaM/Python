# print fucnction
print(0,1,2,3,4) # spacebar
print(0,1,2,3,4,sep="") # no spacebar
print(0,1,2,3,4,end="***") # spacebar
print("new print") # no a new line


# a is int
a = 12315465.21585668
b = -2313.215

# all printed is string
print("{}".format(a))
print("{:.2f}".format(a))
print("{:,.3f}".format(a))
print("{:,}".format(a))

print("--"*20)

# align rignt   
print("{:20}".format(a))
print("{:20.2f}".format(a))
print("{:20,.3f}".format(a))
print("{:20,}".format(a))
# minus
print("{:20}".format(b))
print("{:=20.2f}".format(b))

# padding 
text_a = "th",'Thailand'

print(f'{text_a[0]} |{text_a[1]}|')
print(f'{text_a[0]:5} |{text_a[1]:15}|') #align left
print(f'{text_a[0]:<5} |{text_a[1]:*<15}|') # align left
print(f'{text_a[0]:>5} |{text_a[1]:>15}|') # align right
print(f'{text_a[0]:*>5} |{text_a[1]:*>15}|') # align right with *
print(f'{text_a[0]:^5} |{text_a[1]:^15}|') # align center

# dict print
dict_a = {"name" : "sing",
          "price": 40}
print(f"{dict_a['name']} = {dict_a['price']}")
print("{name} = {price}".format(**dict_a))

# ascii_table + Number System
for i in range(65,128):
    print(f"{i:3}",end="...")
    # 10 2 4 8 8 ascii
    print("{0:3} {0:#08b} {0:04o} {0:#x} {0:#X} {0:c}".format(i))

