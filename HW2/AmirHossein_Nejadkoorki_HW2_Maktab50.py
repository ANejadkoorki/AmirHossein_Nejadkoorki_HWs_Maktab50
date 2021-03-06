#Question1
print("Question 1 : ")
for i in range(1,5):
    if i == 3:
        #when we want to put  \ or " into a string we should write \ before it .
        print("\"\\\"\"bla bla bla")
        continue
    print("bla bla bla")

print("-----------------------------------------------------------------------")

#Question2
print("Qestion 2 : ")
User_input = input("Please enter a sequence of space-seprated numbers :  ")
a = User_input.split(" ")
print("the list is : ",a)
print("the tuple is : ",tuple(a))

print("-----------------------------------------------------------------------")


#Question3
print("Question 3 : ")
User_input_2 = input("say the sequence of the numbers you want to check : ")
l1  = User_input_2.split(" ")
for i in range(len(l1)):
    l1[i] = int(l1[i])
print("the maximum is : ",max(l1))
print("the minimum is : ",min(l1))
print("the sum is : ",sum(l1))

print("-----------------------------------------------------------------------")
print("code by Amirhossein Nejadkoorki")












