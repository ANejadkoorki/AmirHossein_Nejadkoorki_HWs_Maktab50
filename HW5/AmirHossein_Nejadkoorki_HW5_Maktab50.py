import os  # First Question

os.chdir("C:\\Users\\Amir Hossein\\Desktop")  # please put your Desktop path here!!!!
first_file = open("a.txt")
count_of_lines, count_of_words, count_of_cahracters = 0, 0, 0
for i in first_file:
    count_of_lines += 1
    count_of_words += len(i.split())
    count_of_cahracters += len(i)
print("count of lines : ", count_of_lines, "\ncount of words : ", count_of_words, "\ncount of characters : ",
      count_of_cahracters)
print("------------------------------------------------------------------")
# Second Question
second_file = open("a_copy.txt", "x")
first_file.seek(0, 0)
process = second_file.write(first_file.read())
second_file.close()
finall_copied_file = open("a_copy.txt")
print(finall_copied_file.read())
finall_copied_file.close()
print("------------------------------------------------------------------", "\n code by AmirHossein Nejadkoorki")
first_file.close()
