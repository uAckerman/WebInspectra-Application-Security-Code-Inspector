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

 
