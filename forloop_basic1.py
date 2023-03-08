# #Basic - Print all intergers from 0 to 150
for i in range(0,151):
    print(i)

# #Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5,1000,5):
    print(i)

# #Counting, the Dojo Way - Print intergers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
for i in range(1,101):
    print(i)
    if i %5 == 0:
        print("Coding")
    if i %10 == 0: 
        print("Coding Dojo")

# #Whoa. That Sucker's Huge - Add odd intergers from 0 to 500,000 and print the final sum.
for i in range(0,500000):
    if i %2 != 0:
        i+=i
        print(i)

# #Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)

#flexible counter 
lowNum=2
highNum=9
mult=3
for i in range(lowNum, highNum+1):
    if i %mult == 0:
        print(i)