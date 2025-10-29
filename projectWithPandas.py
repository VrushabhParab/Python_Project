import pandas as pd

DATA_FILE = 'Private_data.csv'

def load_data():
    return pd.read_csv(DATA_FILE)

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def student_portal(df):
    print("\n--- Student Login ---")
    login_id = input("Enter Login ID: ")
    password = input("Enter Password: ")
    #student = # data from students 
    student = df[(df['NAME OF THE STUDENT'] == login_id) & (df['PASSWORD'] == password)]
    if student.empty:
        print("Invalid Student Login ID/Passsword. Try Again!")
        return
    print(f"\nWelcome, {student.iloc[0]['NAME OF THE STUDENT']}!")
    again = True 
    print("1. Show Marks")
    print("2. Show Remarks")
    print("3. Logout")
    choice=(input("Enter Choice: "))
    if choice==1:
        print("1. Show General Management Score")
        print("2. Show Domain Specific Score")
        print("3. Show Total Marks & Percentage Obtained ")
        choice=input("Enter Choice: ")
        if choice==1:
            gms = student.iloc[0].get('General Management Score (OUT of 50)', 'Not uploaded')
            print("General Management Score:",gms)
        elif choice==2:
            dss = student.iloc[0].get('Domain Specific Score (OUT of 50)', 'Not uploaded')
            print("General Management Score:",dss)
        elif choice==3:
            total=dss+gms
            print("Total Marks Obtained (Out of 200): ",total)
            percentage=(total/200)*100
            percentage1= "%.2f" % percentage
            print("Precentage Obtained: ",percentage1,"%")
        else:
            print("Invalid Choice!")
    elif choice==2:
        remarks = student.iloc[0].get('REMARKS', '')
        print("Remarks: ",remarks)
    elif choice ==3:
        print("Logging Out...\n")
        again = False
    else:
        print("Invalid Choice!")

def faculty_portal(df):
    print("\n--- Faculty Login ---")
    login_id = input("Enter Faculty Login ID: ") 
    password = input("Enter Password: ")
    #faculty = # data from faculties
    if faculty.empty:
        print("Invalid Faculty Login ID/Passsword. Try Again!")
    else:
        print("Welcome....faculty details")
    while True:
        print("1. Upload/Update Student Marks")
        print("2. Logout ")
        choice = input("Enter choice: ")
        if choice == '1':
            sid = input("Enter Student Login ID: ")
            gms = input("Enter General Management Score (OUT of 50): ")
            dss = input("Enter Domain Specific Score (OUT of 50): ")
            remarks = input("Enter Remarks (optional): ")
            if sid in df['LOGIN ID'].values:
                df.loc[df['LOGIN ID'] == sid, 'General Management Score (OUT of 50)'] = gms
                df.loc[df['LOGIN ID'] == sid, 'Domain Specific Score (OUT of 50)'] = dss
                df.loc[df['LOGIN ID'] == sid, 'REMARKS'] = remarks
                save_data(df)
                print("Scores And Remarks Updated!\n")
            else:
                print("Invalid Student Login ID. Try Again.\n")
        elif choice == '2':
            break
        else:
            print("Invalid Choice!")

def main():
    #df = load_data()  # Load data once
    while True:
        print("\n--- Examination Portal ---")
        print("1. Student Login")
        print("2. Faculty Login")
        print("3. Exit")
        choice = input("Enter Choice: ")
        if choice == '1':
            student_portal(df)
        elif choice == '2':
            faculty_portal(df)
        elif choice == '3':
            break
        else:
            print("Invalid Choice!")

main()
