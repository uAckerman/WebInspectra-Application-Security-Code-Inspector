from controller import InspectionController
from sql_injection import SQLInjectionCheck

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"

    controller = InspectionController(base_url)

    controller.register_check(SQLInjectionCheck())

    results = controller.run()

    for result in results:
        print(result)
