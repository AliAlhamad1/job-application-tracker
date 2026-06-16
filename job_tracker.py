import json
from datetime import datetime
FILE_NAME = 'applications.json'

def saveApplications(applications):
    with open(FILE_NAME, 'w') as file:
        json.dump(applications, file, indent=4)

def loadApplications():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

applications = loadApplications()


def chooseStatus():
    print("Choose status:")
    print("1. Applied")
    print("2. Interview")
    print("3. Rejected")
    print("4. Offer")
    print("5. Saved")
    print()
    choice = input("Choose an option: ")

    if choice == '1':
        return "Applied"
    elif choice == '2':
        return "Interview"
    elif choice == '3':
        return "Rejected"
    elif choice == '4':
        return "Offer"
    elif choice == '5':
        return "Saved"
    else:
        return "Applied"

def addApplication(applications):
    company = input("Enter company name: ")
    role = input("Enter role: ")
    status = chooseStatus()
    date_applied = getDateInput()
    link = input("Enter the application link: ")
    notes = input("Enter any additional notes: ")

    application = {
        "company": company,
        "role": role,
        "status": status,
        "date_applied": date_applied,
        "link": link,
        "notes": notes

    }

    applications.append(application)
    saveApplications(applications)
    print()
    print("Application saved")
    print()

def printApplications(applications):
        if len(applications) == 0:
            print("No applications found.")
        else:
            print("View by:")
            print("1. Original order")
            print("2. Company name A-Z")
            print("3. Status")
            print("4. Date applied")

            choice = input("Choose an option: ")

            if choice == '1':
                applicationsToPrint = applications
            elif choice == '2':
                applicationsToPrint = sorted(applications, key=lambda app: app["company"].lower())
            elif choice == '3':
                applicationsToPrint = sorted(applications, key=lambda app: app["status"].lower())
            elif choice == '4':
                applicationsToPrint = sorted(applications, key=lambda app: app["date_applied"])
            else:
                print("Invalid view option.")
                return

            print("All Applications:")
            for index, app in enumerate(applicationsToPrint, start=1):
                print()
                print("Application #" + str(index))
                print()
                print("Company: " + app["company"])
                print("Role: " + app["role"])
                print("Status: " + app["status"])
                print("Date Applied: " + app["date_applied"])
                print("Application Link: " + app["link"])
                print("Notes: " + app["notes"])
                print()

def updateApplications(applications):
        if len(applications) == 0:
            print("No applications found.")
        else:
            try:
                updateNum = int(input("Which application number would you like to update: "))
                index = updateNum - 1

                if index >= 0 and index < len(applications):
                    applications[index]['status'] = chooseStatus()
                    print()
                    print("Updated successfully")
                    print()
                    saveApplications(applications)
                else:
                    print("Invalid application number.")
            except ValueError:
                print("Please enter a valid number.")


def deleteApplications(applications):
        if len(applications) == 0:
            print("No applications found")
        else:
            try:
                deleteNum = int(input("Which application would you like to delete: "))
                print()
                index = deleteNum - 1

                if index >= 0 and index < len(applications):
                    applications.pop(index)
                    print("Deleted successfully")
                    print()
                    saveApplications(applications)
                else:
                    print("Invalid application number")
            except ValueError:
                print("Please enter a valid number.")



def searchApplications(applications):
        if len(applications) == 0:
            print("No applications found")

        else:
            print("Search by:")
            print("1. Company")
            print("2. Status")

            choice = input("Choose an option: ")

            found = False
            if choice == '1':
                companyString = input("Enter the company name to search for the application: ")
                companyString = companyString.lower()

                for app in applications:
                    if companyString in app["company"].lower():
                        print()
                        print("Company: " + app["company"])
                        print("Role: " + app["role"])
                        print("Status: " + app["status"])
                        print("Date Applied: " + app["date_applied"])
                        print("Application Link: " + app["link"])
                        print("Notes: " + app["notes"])
                        found = True
            elif choice == '2':
                status = chooseStatus()
                for app in applications:
                    if app["status"] == status:
                        print()
                        print("Company: " + app["company"])
                        print("Role: " + app["role"])
                        print("Status: " + app["status"])
                        print("Date Applied: " + app["date_applied"])
                        print("Link: " + app["link"])
                        print("Notes: " + app["notes"])
                        found = True

            else:
                print("Invalid search option.")
                return

            if found == False:
                print("No matching applications found.")

def viewStats(applications):
    if len(applications) == 0:
        print("No applications found.")
    else:
        applied = 0
        interview = 0
        rejected = 0
        offer = 0
        saved = 0
        for app in applications:
            if app["status"] == "Applied":
                applied += 1
            elif app["status"] == "Interview":
                interview += 1
            elif app["status"] == "Rejected":
                rejected += 1
            elif app["status"] == "Offer":
                offer += 1
            elif app["status"] == "Saved":
                saved += 1

        print("Application Stats:")
        print("Total applications: " + str(len(applications)))
        print("Applied: " + str(applied))
        print("Interview: " + str(interview))
        print("Rejected: " + str(rejected))
        print("Offer: " + str(offer))
        print("Saved: " + str(saved))

def editApplication(applications):
    if len(applications) == 0:
        print("No applications found.")
    else:
        try:
            editNum = int(input("Which application number would you like to edit: "))
            index = editNum - 1

            if index >= 0 and index < len(applications):
                print("What would you like to edit?")
                print("1. Company")
                print("2. Role")
                print("3. Status")
                print("4. Date applied")
                print("5. Link")
                print("6. Notes")

                choice = input("Choose an option: ")

                if choice == '1':
                    applications[index]["company"] = input("Enter new company: ")
                elif choice == '2':
                    applications[index]["role"] = input("Enter new role: ")
                elif choice == '3':
                    applications[index]["status"] = chooseStatus()
                elif choice == '4':
                    applications[index]["date_applied"] = getDateInput()
                elif choice == '5':
                    applications[index]["link"] = input("Enter new link: ")
                elif choice == '6':
                    applications[index]["notes"] = input("Enter new notes: ")
                else:
                    print("Invalid edit option.")
                    return

                saveApplications(applications)
                print("Application updated successfully.")

            else:
                print("Invalid application number.")

        except ValueError:
            print("Please enter a valid number.")

def getDateInput():
    while True:
        date_applied = input("Enter the date applied YYYY-MM-DD: ")

        try:
            datetime.strptime(date_applied, "%Y-%m-%d")
            return date_applied
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")



while True:


    print("1. Add application")
    print("2. View applications")
    print("3. Update status")
    print("4. Edit application")
    print("5. Delete an application")
    print("6. Search an application")
    print("7. View stats")
    print("8. Exit")
    print()
    choice = input("Choose an option: ")
    print()
    if choice == '1':
        addApplication(applications)
    elif choice == '2':
        printApplications(applications)
    elif choice == '3':
        updateApplications(applications)
    elif choice == '4':
        editApplication(applications)
    elif choice == '5':
        deleteApplications(applications)
    elif choice == '6':
        searchApplications(applications)
    elif choice == '7':
        viewStats(applications)
    elif choice == '8':
        print("Exiting")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, 5, 6, 7, or 8.")




