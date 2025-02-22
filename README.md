# Capstone-01
AT Project 1

System Description
The OrangeHRM System is a web based manages employee photos. Employees can add or change their own photos and Human Resources can add or change everyones photos. The system produces list of photos by different selection criteria. Its photos will be used by many other systems in the company. The Photos are stored in a configurable file structure and the photo location is pointed to by a file system. This release only includes employee photos and name and address and social security information and not any of the other information planned for later.

Test Cases dealing with login (create all positive and negative Scenarios)

Please fetch the error message for invalid logins from web page

Test case ID: TC_Login_01

Test Objective:
Successful Employee login to OrangeHRM portal

Precondition:
1 A valid ESS-User account to login to be available.
2 Orange HRM 3.0 site is launched on a compatible browser

Steps:
1. In the Login panel, enter the username (Test Data: "Admin")
2. Enter the Password for the ESS-User account in the password filed (Test data: "admin123")
3. Click "Login" button

Expected Result:
The user is logged in successfully.

Test case ID: TC_Login_02

Test objective:
	Invalid Employee login to OrangeHRM portal

Precondition:
	1. A valid ESS-User account to login to be available
2. Orange HRM 3.o site is launched on a compatible browser

Steps:
1. In the login Panel, enter the username (Test Data: "Admin")
2. Enter the Password for the ESS-User account in the password field (Test data: "Invalid password")
3. Click "Login" button

Expected Result:
A valid error message for invalid credentials is displayed.

Test Cases dealing with the PIM

Test case ID: TC_PIM_01

Test objective:
Add a new employee in the PIM module

Precondition:
1. A valid ESSS-User account to login to the available
2. Orange HRM 3.0 site is launched on a compatible browser

Steps:
1. Go to PIM module from the left pane in the web page
2. Click on Add and add new employee details in the page.
3. Fill in all the personal details of the employee and click save.

Expected Result:
The user should be able to add a new employee in the PIM and should see a message for successful employee addition.

Test case ID: TC_PIM_02

Test objective:
Edit an existing employee in the module.

Precondition:
1. A valid ESSS-User account to login to the available
2. Orange HRM 3.0 site is launched on a compatible browser

Steps:
1. Go to PIM module from the left pane in the web page
2. From the existing list of employe in the PIM Module, edit the employee information of employee and save it.

Expected Result:
The user should be able to edit an existing employee information in the PIM and should see a message for successful employee details addition.

Test case ID: TC_PIM_03

Test objective:
Deleting an existing employee in the PIM module.

1. A valid ESS-User account to login to be available
2. Orange HRM 3.0 site is launched on a compatible browser

Steps:
1. Go to PIM module from the left pane in the web page
2. From the existing list of employee in PIM module; delete an existing employee.

Expected Result:
The user should be able to delete an existing employee information in the PIM and should see a message for successful deletion.
