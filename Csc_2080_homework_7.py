# Chapter 8 Discussion Question.
#Compare and contrast the following pairs of terms
#a)definite loop vs. indefinite loop
# both the definite loop and indefinite loop are ways you can loop part of the program in pyhton.
# For the definite loop to work you must first tell it how many times it will loop,
# but the indefinite loop can be told to run on a condition and will stop once that condition is met.

#b)for loop vs. while loop.
# Both the for loop and the while loop will loop the body of the program that is indented.
# The for loop you have to set a variable first then it will run that many times, then it will stop.
# The while loop you set a condition and after loop the program will see if the condition is fulfilled,
# if it's fulfilled it will stop lopping, but if is not fulfilled the program will continue to loop.

#c)interactive loop vs. sentinel loop.
# Both the interactive loop and sentinel loop are ways to implement loops that change how many times the loop is ran
# depending on the imput of the user. The interactive loop will ask ever loop if their is
# more data and if yes then it will loop again. But the sentinel loop will continue to loop untill
# the user imputs the sentinel value that will stop the loop. 


#d)sentinel loop vs. end-of-file loop
# The end-of-file loop is a type of sentinel loop, but the major difference between the two is that
# end-of-file loop allows the user to input their data in a separate file, then the loop will look thought
# the file until it reaches the end and then return a "" which would be the sentinel value that will stop the loop.

# Chapter 8 Discussion Question 2
# Give a truth table that shows the Boolean value of each of the following Boolean
# expressions, for every possible combination of "input" values.

#a) not (P and Q)
#  P|Q| P and Q |not (P and Q)|
#  T|T|    T    |       F     |
#  T|F|    F    |       T     |
#  F|T|    F    |       T     |
#  F|F|    F    |       T     |

#b) (not P) and Q
#  P|Q|   not P |(not P) and Q)|
#  T|T|    F    |       F      |
#  T|F|    F    |       F      |
#  F|T|    T    |       T      |
#  F|F|    T    |       F      |

#c) (not P) or (not Q)
#  P|Q|   not P |   not Q |(not P) or (not Q)
#  T|T|    F    |     F   |   F
#  T|F|    F    |     T   |   T
#  F|T|    T    |     F   |   T
#  F|F|    T    |     T   |   T

#d) (P and Q) or R
#  P|Q|R| (P and Q) |   R  |(P and Q) or R
#  T|T|T|    T      |   T  |   T
#  T|T|F|    T      |   F  |   T
#  T|F|T|    F      |   T  |   T
#  T|F|F|    F      |   F  |   F
#  F|T|T|    F      |   T  |   T
#  F|T|F|    F      |   F  |   F
#  F|F|T|    F      |   T  |   T
#  F|F|F|    F      |   F  |   F

#e) (P or R) and (Q or R)
#  P|Q|R| (P or R)  |(Q or R)|(P or R) and (Q or R)
#  T|T|T|    T      |   T   |   T
#  T|T|F|    T      |   T   |   T
#  T|F|T|    T      |   T   |   T
#  T|F|F|    T      |   F   |   F
#  F|T|T|    T      |   T   |   T
#  F|T|F|    F      |   T   |   F
#  F|F|T|    T      |   T   |   T
#  F|F|F|    F      |   F   |   F
# Chapter 8 Discussion Question 3.
#Write a while loop fragment that calculates the following values:
#a)Sum of the first n counting numbers: 1 + 2 + 3 + . . . + n
def main():
    print("This progam sums the first n counting numbers.")
    n=int(input("please enter a value fo n:"))
    i = 0
    while i<n:
       i = i + 1
       print(i)
        
main()

#c)Sum of a series of numbers entered by the user until the value 999 is
#entered. Note: 999 should not be part of the sum.

def main():
    print("This progam sums a series of numbers up untill the value is grater then or equal to 999.")
    sum_n = 0
    while sum_n<=999:
        n=eval(input("Enter a number that will be added:"))
        sum_n = sum_n + n
        
    print("this is the sum of the numbers is:", sum_n)

main()
          
# Chapter 8  Programming Exercise 1.
#The Fibonacci sequence starts 1, 1, 2, 3, 5, 8, . . .. Each number in the se
#quence (after the first two) is the sum of the previous two. Write a pro
#gram that computes and outputs the nth Fibonacci number, where n is a
#value entered by the user.

def main():
    n = int(input("Enter how many numbers do you want from the fibonacci sequence:"))

    a = 0
    b = 1
    c = 1

    for i in range(n):
            print(c,"", end="")
            c = a + b
            a = b
            b = c

main()

# Chapter 8  Programming Exercise 4.
# Write a program that gets a starting value from the user and then prints
# the Syracuse sequence for that starting value.
def s_sequence(x):

    r = [x]

    while x != 1:

        if x % 2 == 0.0:

            x = x / 2

            r. append(int(x))

        else:

            x = 3 * x + 1

            r. append(int(x))

    return(r)

def main():
    
    x = int(input("Enter the number that the syracuse sequence starts with:"))

    print("The syracuse sequence the starts with",x,"equals:",s_sequence(x))

    s_sequence(x)

main()
    
