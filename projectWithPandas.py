import pandas as pd

def load_data_student():
    return pd.read_csv("student_data.csv")


def load_data_faculty():
    return pd.read_csv("faculty_data.csv")


def save_data(df1,df2):
    df1.to_csv("faculty_data.csv", index=False)
    df2.to_csv("student_data.csv", index=False)


def student_portal(df):
    print("\n--- Student Login ---")
    login_id = input("Enter Login ID: ")
    password = input("Enter Password: ")
    student = df[(df['Login IDs'] == login_id) & (df['PASSWORDS'] == password)]
    if student.empty:
        print("Invalid Student Login ID/Passsword. Try Again!")
        return
    print(f"\nWelcome, {student.iloc[0]['NAME OF THE STUDENT']}!")
    print("1. Show Marks")
    print("2. Show Remarks")
    choice = int(input("Enter Choice: "))
    if choice==1:
        print("1. Show General Management Score")
        print("2. Show Domain Specific Score")
        print("3. Show Total Marks & Percentage Obtained ")
        choice = int(input("Enter Choice: "))
        gms = student.iloc[0].get('GENERAL MANAGEMENT SCORE (OUT of 50)', 'Not uploaded')
        dss = student.iloc[0].get('Domain Specific SCORE (OUT 50)', 'Not uploaded')
        if choice==1:
            print("General Management Score:",gms)
        elif choice==2:
            print("Domain Specific Score:",dss)
        elif choice==3:
            total=dss+gms
            print("Total Marks Obtained (Out of 200): ",total)
            percentage=(total/100)*100
            print(f"Precentage Obtained: {"%.2f"%percentage} %")
        else:
            print("Invalid Choice!")
    elif choice==2:
        remarks = student.iloc[0].get('REMARKS', '')
        print("Remarks: ",remarks)
    else:
        print("Invalid Choice!")


def faculty_portal(df1, df2):
    print("\n--- Faculty Login ---")
    login_id = input("Enter Faculty Login ID: ") 
    password = input("Enter Password: ")
    
    faculty = df1[(df1['LoginID'] == login_id) & (df1['password'] == password)]
    if faculty.empty:
        print("Invalid Faculty Login ID/Password. Try Again!")
        return
    
    print(f"\nWelcome, {faculty.iloc[0]['Name']}!")
    
    while True:
        print("\n1. Upload/Update Student Marks")
        print("2. Logout")
        choice = input("Enter choice: ")
        
        if choice == '1':
            sid = input("Enter Student Name: ")
            
            if sid not in df2['NAME OF THE STUDENT'].values:
                print("Invalid Student Name. Try Again.\n")
                continue
            
            try:
                gms = float(input("Enter General Management Score (OUT of 50): "))
                dss = float(input("Enter Domain Specific Score (OUT of 50): "))
            except ValueError:
                print("Invalid score! Please enter numeric values.\n")
                continue
            
            remarks = input("Enter Remarks (optional): ")
            
            for col, val in [('GENERAL MANAGEMENT SCORE (OUT of 50)', gms),
                             ('Domain Specific SCORE (OUT 50)', dss),
                             ('REMARKS', remarks)]:
                if col in df2.columns:
                    df2.loc[df2['NAME OF THE STUDENT'] == sid, col] = val
                else:
                    df2[col] = None
                    df2.loc[df2['NAME OF THE STUDENT'] == sid, col] = val
            
            save_data(df1, df2)
            print("Scores and remarks updated!\n")
        
        elif choice == '2':
            print("Logging out...\n")
            break
        else:
            print("Invalid Choice!\n")

def main():
    df2 = load_data_student()
    df1 = load_data_faculty()  
    while True:
        print("\n--- Examination Portal ---")
        print("1. Student Login")
        print("2. Faculty Login")
        print("3. Exit")
        choice = input("Enter Choice: ")
        if choice == '1':
            student_portal(df2)
        elif choice == '2':
            faculty_portal(df1,df2)
        elif choice == '3':
            break
        else:
            print("Invalid Choice!")


main()
