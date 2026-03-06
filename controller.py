from sql_injection import SQLInjectionCheck

class InspectionController:
    def __init__(self, base_url): # This function takes the target application
        self.base_url = base_url
        self.checks = []

    def register_check(self, check): # It adds different security tests 
        self.checks.append(check)

    def run(self): # Runs those tests and return results
        results = []
        for check in self.checks:
            result = check.run(self.base_url)
            results.append(result)
        return results

