def about():
    print("\n===== ABOUT ME =====")
    print("Hello! I am Sunidhi.")
    print("I am a beginner in Data Science and Python programming.")
    print("Currently pursuing BS in Data Science and Applications from IIT Madras.")
    print("Interested in Artificial Intelligence, Machine Learning, and Data Science.")

def education():
    print("\n===== EDUCATION =====")
    print("BS in Data Science and Applications")
    print("Indian Institute of Technology Madras (IIT Madras)")

def skills():
    print("\n===== SKILLS =====")
    print("• Python")
    print("• Git & GitHub")
    print("• Basic Data Science")
    print("• Problem Solving")

def projects():
    print("\n===== PROJECTS =====")
    print("1. Student Management System")
    print("2. Portfolio Application (Python)")

def contact():
    print("\n===== CONTACT =====")
    print("Email : sunidhiguraja@gmail.com")

while True:
    print("\n===================================")
    print("      MY PORTFOLIO APPLICATION")
    print("===================================")
    print("1. About Me")
    print("2. Education")
    print("3. Skills")
    print("4. Projects")
    print("5. Contact")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        about()
    elif choice == "2":
        education()
    elif choice == "3":
        skills()
    elif choice == "4":
        projects()
    elif choice == "5":
        contact()
    elif choice == "6":
        print("\nThank you for visiting my portfolio!")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 6.")
