import pandas as pd
import time

def load_data_students():
    return pd.read_csv("student_data.csv")

def load_data_faculty():
    return pd.read_csv("faculty_data.csv")

def student_login():
    df = pd.read_csv("student_data.csv")
    print("----STUDENT LOGIN----")
    loginId = input("Enter your loginId: ")
    password = input("Enter password: ")
    student = df[(df["Login IDs"] == loginId) & (df["PASSWORDS"] == password)]
    student = student.reset_index()
    # print(student)
    if student.empty:
        print("Invalid Credentials. Try Again!")
        return
    print("Loading....")
    time.sleep(1)
    print(f"Welcome!! {student.loc[0]["NAME OF THE STUDENT"]}")
    while True:
        print("1. Show Marks")
        print("2. Show Remarks")
        print("3. Logout")
        choice = int(input("Enter choice: "))
        time.sleep(0.5)
        if choice == 1:
            print("Loading....")
            print("1. General Management Score (OUT of 50)")
            print("2. Domain Specific Score (OUT of 50)")
            print("3. Total Score and Percentage")
            choice1 = int(input("Enter your choice: "))
            gms = student.loc[0]["GENERAL MANAGEMENT SCORE (OUT of 50)"]
            dss = student.loc[0]["DOMAIN SPECIFIC SCORE (OUT 50)"]
            if choice1 == 1:
                print("Loading....")
                time.sleep(0.5)
                print("Your score is:",gms)
            elif choice1 == 2:
                print("Loading....")
                time.sleep(0.5)
                print("Your score is:",dss)
            elif choice1 == 3:
                print("Loading....")
                time.sleep(0.5)
                totalScore = gms + dss
                print("Your Total Score:",totalScore)
                percentage = (totalScore/100) * 100
                print("Percentage obtained:",percentage,"%")
            else:
                print("Invalid choice!")
        elif choice == 2:
            print("Loading....")
            time.sleep(0.5)
            print(student.loc[0]["REMARKS"])
        elif choice == 3:
            print("Logging out...")
            time.sleep(0.5)
            break
        else:
            print("Invalid Choice")


def faculty_login():
    df1 = pd.read_csv("student_data.csv")
    df2 = pd.read_csv("faculty_data.csv")
    print("----FACULTY LOGIN----")
    t_id = input("Enter login ID: ")
    password = input("Enter password: ")
    faculty = df2[(df2["LoginID"] == t_id) & (df2["password"] == password)]
    faculty = faculty.reset_index()
    # print(faculty)
    if faculty.empty:
        print("Invalid credentials. Try again")
        return
    print("Loading....")
    time.sleep(1)
    print(f"Welcome!! {faculty.iloc[0]['Name']}")
    while True:
        print("1. Upload/Update Student Marks")
        # print("2. Sort Students")
        # print("3. Add Student")
        # print("4. Remove Student")      # SQL SQL SQL SQL SQL SQL SQL SQL
        print("5. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            student_id = input("Enter student ID: ")
            # print(list(df1["Login IDs"]))
            print("Loading....")
            time.sleep(0.5)
            if student_id not in list(df1["Login IDs"]):
                print("Student not found")
            else:
                print(f"Update marks of {df1.loc[df1['Login IDs'] == student_id,'NAME OF THE STUDENT'].values[0]}")
                gms = float(input("Enter General Management Score (OUT of 50): "))
                dss = float(input("Enter Domain Specific Score (OUT of 50): "))
                remark = input("Enter remark: ")
                total = gms + dss
                df1.loc[df1['Login IDs'] == student_id, 'GENERAL MANAGEMENT SCORE (OUT of 50)'] = gms
                df1.loc[df1['Login IDs'] == student_id, 'DOMAIN SPECIFIC SCORE (OUT 50)'] = dss
                df1.loc[df1['Login IDs'] == student_id, 'TOTAL SCORE (OUT of 100)'] = total
                df1.loc[df1['Login IDs'] == student_id, 'REMARKS'] = remark
                df1.to_csv("student_data.csv", index=False)
                print("Marks/Remark updated successfully!")
        elif choice == 5:
            print("Logging out...\n")
            break

        


def main():
    # df1 = load_data_students()
    # df2 = load_data_faculty()
    while True:
        print("\n--- Examination Portal ---")
        print("1. Student Login")
        print("2. Faculty Login")
        print("3. Exit")
        choice = input("Enter Choice: ")
        if choice == '1':
            student_login()
        elif choice == '2':
            faculty_login()
        elif choice == '3':
            break
        else:
            print("Invalid Choice!")


main()