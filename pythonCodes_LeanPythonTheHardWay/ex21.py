
def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a + b
	
def subtract(a,b):
    print "Subtracting %d - %d" % (a,b)
    return a - b
	
def multiply(a,b):
    print "Multiplying %d * %d" % (a,b)
    return a * b
	
def divide(a,b):
    print "Dividing %d / %d" % (a,b)
    return a / b
	
print "Doing math with just functions"

age = add(20,5)
height = subtract(189,4)
weight = multiply(150,2)
iq = divide(140,2)

print "Age %d, Height %d, Weight %d, IQ %d" % (age, height, weight, iq)

# A puzzle for I don't know what
print " Here's a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes:",what,"Can you do it by hand?"