

source = 0x1355b6767988295e00000000000300347e581e360000000000000000
mask =   0x1111111111111111000000000000000000000000000000000000000

print(source&mask)

destination = 0x0000000000030034

print(destination)

verification = 0x1355b6767988295e0000000000030034

print(verification)



#challenge 2
tag = 0x0019
length =  0x0006
hello = 0x48656C6C6F

NewTag = 0x0424 
print(bin(NewTag));    #encoded

#length of sms
Value = "Hello Natujenge Σ!" #18 plus spaces
value_length = 18
print("Length = "+hex(value_length))


print("Length bytes = "+bin(value_length))#0001 0010
(ord(" "))
(ord("N"))
(ord("a"))
(ord("t")) #convers characters to ascii DECIMAL
(ord("u"))
(ord("j"))
(ord("e"))
(ord("n"))
(ord("g"))
(ord("e"))

#CONVERT ALL THE DATA TO HEXADECIMAL
#GET A SINGLE HEX DIGIT WHICH IS 4 BITS 
value_of_sms = {0x4,0x8,0x6,0x5,0x6,0xC,0x6,0xC,0x6F,}#array of bytes 4 bits one octet

#last part

print(bin(NewTag)+value_length+value_of_sms)