# Codexaegis-Application-Security-Code-Inspector
I built Codexaegis, a developer-focused security inspection framework designed to analyze running web applications for vulnerabilities using automated attack simulation and modular security checks, with an architecture ready for future IDE integration. 
  
***
<div align="center">
  <img src="doc/screenshots/project_flow1.png" alt="project" width="900"> 
</div>

***

# Feature
- Inspect application functions for vulnerabilities
- Automated attack simulation against running endpoints
- Detect webapp threats and logic flaws
- Modular security check system
- Vulnerable and secure demo applications
- IDE integration ready architecture

# Workflow

## Phase 1: Build the app ( [app.py](https://github.com/uAckerman/Codexaegis-Application-Security-Code-Inspector/blob/main/app.py) )

I built a simple Flask based web application to demonstrate how authentication systems work and how common security vulnerabilities can occur if secure coding practices are not followed.

The application uses **Flask** as the backend framework and **SQLite** as the database. When the app runs for the first time, it automatically initializes a database file (**database.db**) and creates a users table with fields for id, username, and password. It also inserts a default user (**admin / admin123**) for testing purposes.


***
<img src="doc/screenshots/p1.png" alt="project" width="900"> 
  
***
> I enhance the login page with some custom styling
***
<img src="doc/screenshots/p2.png" alt="project" width="700"> 

***

## Phase 2: Build the Inspection Engine Core ( [controller.py](https://github.com/uAckerman/Codexaegis-Application-Security-Code-Inspector/blob/main/controller.py) )

In this step, i create the main engine that runs security checks on a website. It manages all security checks on a website.

**What the Code Does:**

| Method | Description |
|------|-------------|
| `__init__(base_url)` | Saves the target website URL and creates an empty list to store security checks |
| `register_check(check)` | Adds a security check (like SQL Injection) to the list |
| `run()` | Runs all registered checks on the target URL and collects their results |

 ## Phase 3: Create the SQL Injection Detection Logic ( [sql_injection.py](https://github.com/uAckerman/Codexaegis-Application-Security-Code-Inspector/blob/main/sql_injection.py) )

The **SQLInjectionCheck** module is designed to test whether a web application login functionality is vulnerable to SQL Injection.   
- In the first step, the module attempts the attack by sending a crafted payload
  ```
   "username": "' OR '1'='1",  
   "password": "' OR '1'='1"
  ```  
  to the login endpoint using an HTTP POST request. This payload is commonly used to manipulate SQL queries and attempt to bypass authentication    by commenting out the rest of the query.  
- In the second step, the module tests the response from the server. It checks whether the response contains the message “**Login Successful**” If this message appears, it indicates that the SQL Injection attempt may have successfully bypassed the login mechanism, marking the system as **VULNERABLE**. If the login is not bypassed, the result is marked as **SAFE**. If any exception occurs during the request, the module returns an **ERROR** status along with the error details.

## Phase 4: Build the Main Scanner Runner ( [scanner.py](https://github.com/uAckerman/Codexaegis-Application-Security-Code-Inspector/blob/main/scanner.py) )

The Main Scanner Runner is the entry point of the security inspection engine. Its role is to start the scanning process, load the security modules, run them against the target application, and display the results.

# Testing and Verification  
  
This section demonstrates how the inspection engine is tested against the vulnerable demo application to verify that the SQL Injection detection module functions correctly.

## Step 1: Start the Vulnerable Web Application  
First, the demo application must be started so that the inspection engine has a target to analyze.

```
python .\app.py
```

***
<div align="center">
  <img src="doc/screenshots/p3.png" alt="project" width="900"> 
</div>

***

## Step 2: Verify the Login Endpoint  
Open a browser and navigate to:
```
http://127.0.0.1:5000/login
```

Test the login functionality using the default credentials stored in the database:  
```
Username: admin
Password: admin123
```

If the credentials are correct, the application should return;

***
<div align="center">
  <img src="doc/screenshots/p4.png" alt="project" width="900"> 
</div>

***
<div align="center">
  <img src="doc/screenshots/p6.png" alt="project" width="900"> 
</div>

***

**This confirms that the login system is functioning correctly before performing the security inspection.**

## Step 3: Execute the Security Scanner

Next, open a new terminal and run the inspection engine from the project root directory.

```
python .\scanner.py
```

The scanner will execute the registered security modules and attempt to detect vulnerabilities in the application.

***
<div align="center">
  <img src="doc/screenshots/p5.png" alt="project" width="900"> 
</div>

***

## Step 4: Analyze the Scanner Output  

After the scan is complete, the scanner will display the results in the terminal.

Example output:
```
{'check': 'SQL Injection Check', 'status': 'VULNERABLE'}
```
***
This output indicates that the SQL Injection detection module successfully identified a vulnerability in the login endpoint.

# Future Improvements

Add XSS detection module and other attack modules related to web  
Generate structured vulnerability reports

# Conclusion

Overall, this project serves as a practical demonstration of how automated security inspection can assist developers and security engineers in identifying potential vulnerabilities during the development and testing phases of a web application.
