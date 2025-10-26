
# PROJECT WITHOUT PANDAS

students = [
    {
        "NAME OF THE STUDENT":"Camila Wood",
        "GENERAL MANAGEMENT SCORE (OUT of 50)":45,
        "Domain Specific SCORE (OUT 50)":45,
        "Login IDs":"STFBCM001",
        "PASSWORDS":"CamWoo53",
        "REMARKS":""
    },
    {
        "NAME OF THE STUDENT":"Alexander Thompson",
        "GENERAL MANAGEMENT SCORE (OUT of 50)":50,
        "Domain Specific SCORE (OUT 50)":50,
        "Login IDs":"STFBCM002",
        "PASSWORDS":"alEThO93",
        "REMARKS":""
    },
    {
        "NAME OF THE STUDENT":"Liam Taylor",
        "GENERAL MANAGEMENT SCORE (OUT of 50)":36,
        "Domain Specific SCORE (OUT 50)":40,
        "Login IDs":"HRVBCM001",
        "PASSWORDS":"LIATaY41",
        "REMARKS":""
    }
]

faculty = [
    {"Name":"Mary White","LoginID":"Mwhite","password":"nrf23yma"},
    {"Name":"Dr. Elizabeth Thompson","LoginID":"Ethompson","password":"eal2br3d"},
]


def student_portal(students):
    print("\n--- Student Login ---")
    login_id = input("Enter Login ID: ")
    password = input("Enter Password: ")
    found = None
    for i in students:
        if i["Login IDs"] == login_id and i["PASSWORDS"] == password:
            found = i
            break
    if not found:
        print("Invalid Student Login ID/Passsword. Try Again!")
        return

    print(f"\nWelcome, {found["NAME OF THE STUDENT"]}!")
    print("1. Show Marks")
    print("2. Show Remarks")
    choice = int(input("Enter Choice: "))

    if choice==1:
        print("1. Show General Management Score")
        print("2. Show Domain Specific Score")
        print("3. Show Total Marks & Percentage Obtained ")
        choice = int(input("Enter Choice: "))
        gms = found["GENERAL MANAGEMENT SCORE (OUT of 50)"]
        dss = found["Domain Specific SCORE (OUT 50)"]
        if choice == 1:
            print("General Management Score:",gms)
        elif choice == 2:
            print("Domain Specific Score:",dss)
        elif choice == 3:
            total = gms + dss
            percentage = (total / 100) * 100
            print("Total Marks Obtained (Out of 200): ",total)
            print(f"Precentage Obtained: {"%.2f"%percentage} %")
        else:
            print("Invalid Choice!")
    elif choice == 2:
        remark = found["REMARKS"]
        print("Remark: ",remark)
    else:
        print("Invalid Choice!")

def faculty_portal(students,faculty):
    print("\n--- Faculty Login ---")
    login_id = input("Enter Faculty Login ID: ") 
    password = input("Enter Password: ")
    
    found = None
    for i in faculty:
        if i["LoginID"] == login_id and i["password"] == password:
            found = i
            break
    if not found:
        print("Invalid Faculty Login ID/Password. Try Again!")
        return
    
    print(f"\nWelcome, {found['Name']}!")

    while True:
        print("\n1. Upload/Update Student Marks")
        print("2. Logout")
        choice = int(input("Enter choice: "))

        if choice == 1:
            s_id = input("Enter Student Name: ")

            found_student = None
            for i in students:
                if i["NAME OF THE STUDENT"] == s_id:
                    found_student = i
                    break
            
            if not found_student:
                print("Invalid Student Name. Try Again.\n")
                continue

            gms = float(input("Enter General Management Score (OUT of 50): "))
            dss = float(input("Enter Domain Specific Score (OUT of 50): "))
            remarks = input("Enter Remarks (optional): ")

            found_student["GENERAL MANAGEMENT SCORE (OUT of 50)"] = gms
            found_student["Domain Specific SCORE (OUT 50)"] = dss
            found_student["REMARKS"] = remarks

            print("Scores and remarks updated!\n")

        elif choice == 2:
            print("Logging out...\n")
            break
        else:
            print("Invalid Choice!\n")

def main():
    global students
    global faculty
    while True:
        print("\n--- Examination Portal ---")
        print("1. Student Login")
        print("2. Faculty Login")
        print("3. Exit")
        choice = input("Enter Choice: ")
        if choice == '1':
            student_portal(students)
        elif choice == '2':
            faculty_portal(students,faculty)
        elif choice == '3':
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()  