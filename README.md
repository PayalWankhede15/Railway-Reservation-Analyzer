 I am a BCA 1st year student,


Project name: Railway Reservation Analyzer
Student: Payal Wankhede
ERP ID: RU-26-01098
Course: BCA in AI ML with Google Certification
Teacher: Mr. Satyaprakash
University: Rungta International Skills University, Bhilai, CG
Technologies: Python 3, Pandas, Matplotlib, VS Code

What the project does:
It reads a bookings CSV file (columns: PNR, Train, Class, Fare, Status) with
Pandas. It shows bookings per train, revenue per train (Confirmed tickets
only) and ticket status counts. It skips rows with an invalid fare, shows an
error if the file is missing, and draws bar charts with Matplotlib.

Menu in my program:
1. Bookings per train
2. Revenue per train (Confirmed only)
3. Tickets by status
4. Exit

My files:
- railway_analyzer.py
- bookings.csv
- test1_test4_bookings.csv, test2_single.csv, test3b_invalid_fare.csv
- screenshots folder (test case outputs and graphs)
- Project_Report.docx, Project_Presentation.pptx

Test cases:
1. Normal input: Gondwana : 4, Rajdhani : 3, Shatabdi : 3, Total bookings: 10
2. One row file: Shatabdi : Rs. 950, Total confirmed revenue: Rs. 950
3a. Missing file: Error: File 'missing.csv' not found.
3b. Invalid fare: Warning: Row with PNR 1011 skipped - invalid fare.
    Valid records analysed: 10
4. Revenue: Rajdhani : Rs. 4100, Gondwana : Rs. 2540, Shatabdi : Rs. 1900,
   Total confirmed revenue: Rs. 8540

Include these sections in Markdown: title and short description, student
details table, problem statement, features, technologies used, project
structure, input file format, how to run (pip install pandas matplotlib, then
python railway_analyzer.py), test cases table, screenshots section with image
links (screenshots/filename.png), sample output, future scope, and author.

