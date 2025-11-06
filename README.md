# University/Examination portal admin/client access management

This project is a Python-based Examination Management System that allows students to view their scores and remarks, and enables faculty to update, add, remove, and sort student records using both Pandas and SQL (SQLite) operations.

The portal uses CSV files for persistent data storage and dynamically syncs data to a local SQLite database for faculty operations.

## Features
👩‍🎓 Student Login

-Secure login using Login ID and Password

-View:

    General Management Score (out of 50)

    Domain Specific Score (out of 50)

    Total Score and Percentage

    Remarks from Faculty

👨‍🏫 Faculty Login

-Secure faculty authentication

-Functionality Provided:

    Upload / Update student marks and remarks

    Sort students using SQL queries:

        By Name

        By Total Score

        By General Management Score

        By Domain Specific Score

        Add new student record (stored in both CSV and SQLite DB)
  
        Remove student record

-Auto-sync between student_data.csv and SQLite database

## Project Structure
        |-- examination.db              # SQLite Database
        |-- student_data.csv            # Student Records
        |-- faculty_data.csv            # Faculty Login Records
        |-- examination_portal.py       # Main Python Script

## Technologies Used

| Component            | Technology           |
| -------------------- | -------------------- |
| Programming Language | Python 3             |
| Data Handling        | Pandas               |
| Database             | SQLite (via sqlite3) |
| Data Storage         | CSV Files            |
| Delay                | time module          |

## License
This project is for educational purposes and can be modified and reused freely.
