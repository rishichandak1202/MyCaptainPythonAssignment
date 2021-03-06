import csv

def write_csv(info):

    with open('Student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
    
    if csv_file.readlines()==0:
        writer.writerow(["Name","Age","Contact Number","Email ID","Blood Group","DOB"])    
      
    else:
        writer.writerow(info)
    
    
if __name__=='__main__':

    condition=True
    stu_no=1

    while(condition):
        student_info=input("Enter some student info for student #{} in the following format (Name, Age, Contact Number, Email ID, Blood Group, DOB)  : ".format(stu_no))  
  
        student_list = student_info.split(' ')
    
        print("\nEntered info is : \nName : {}\nAge = {}\nContact Number = {}\nEmail ID = {}\nBlood Group = {}\nDOB = {}\n".format(student_list[0],student_list[1],student_list[2],student_list[3],student_list[4],student_list[5]))
    
        choice=input("Is the entered info correct?(y/n) : ")
    
        if choice=="y":
            write_csv(student_list)
    
            condition_check=input("Enter (y/n) if you want to enter info of another student : ")
  
            if condition_check=="y" :
                condition=True
                stu_no+=1
            else:
                condition=False
        
        else:
            print("Please re-enter the correct info : ")
