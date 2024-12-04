import random
import json

# Sample questions for two topics
questions = {
    "Python": [
    {"question": "What is the correct file extension for Python files?", "options": [".py", ".python", ".pt", ".pyt"], "answer": ".py"},
    {"question": "Which of the following is a mutable data type in Python?", "options": ["List", "Tuple", "String", "Integer"], "answer": "List"},
    {"question": "What keyword is used to create a function in Python?", "options": ["def", "func", "function", "lambda"], "answer": "def"},
    {"question": "What is the output of 3 * 2 ** 3 in Python?", "options": ["24", "48", "16", "64"], "answer": "24"},
    {"question": "Which of the following is NOT a valid Python data type?", "options": ["Set", "Dictionary", "Array", "Tuple"], "answer": "Array"},
    {"question": "What does the len() function do in Python?", "options": ["Returns the length of a string", "Adds elements", "Counts items in a list", "Both A and C"], "answer": "Both A and C"},
    {"question": "What is used to handle exceptions in Python?", "options": ["try-except", "if-else", "for-while", "None"], "answer": "try-except"},
    {"question": "Which operator is used to check equality in Python?", "options": ["==", "=", "eq", "!="], "answer": "=="},
    {"question": "What is the output of type(10)?", "options": ["<class 'str'>", "<class 'int'>", "<class 'float'>", "<class 'list'>"], "answer": "<class 'int'>"},
    {"question": "Which method is used to add elements to a list?", "options": ["add()", "insert()", "append()", "push()"], "answer": "append()"},
    {"question": "How do you start a comment in Python?", "options": ["//", "#", "/*", "--"], "answer": "#"},
    {"question": "What is a lambda function?", "options": ["Named function", "Anonymous function", "Recursive function", "Class method"], "answer": "Anonymous function"},
    {"question": "What does the range() function return?", "options": ["List", "Tuple", "Generator object", "Integer"], "answer": "Generator object"},
    {"question": "Which Python keyword is used to create a class?", "options": ["class", "struct", "def", "object"], "answer": "class"},
    {"question": "What is the default encoding in Python 3?", "options": ["UTF-8", "ASCII", "UTF-16", "ISO-8859-1"], "answer": "UTF-8"},
    {"question": "What is the output of 5 // 2 in Python?", "options": ["2.5", "2", "3", "Error"], "answer": "2"},
    {"question": "Which method can convert a string to all lowercase in Python?", "options": ["lowercase()", "lower()", "toLowerCase()", "convert()"], "answer": "lower()"},
    {"question": "What does pip stand for in Python?", "options": ["Python Integrated Package", "Pip Installs Packages", "Package Indexing Protocol", "None of the above"], "answer": "Pip Installs Packages"},
    {"question": "What does Python's pass statement do?", "options": ["Exits a loop", "Skips an iteration", "Does nothing", "Terminates a function"], "answer": "Does nothing"},
    {"question": "Which of the following is a built-in Python module?", "options": ["numpy", "math", "pandas", "scikit"], "answer": "math"}
    ],
    "DBMS": [
    {"question": "What does DBMS stand for?", "options": ["Data Built Management System", "Database Management System", "Data Base Manipulation System", "Database Maintenance System"], "answer": "Database Management System"},
    {"question": "Which of the following is NOT a type of database?", "options": ["Hierarchical", "Relational", "Flat File", "Tree-based"], "answer": "Tree-based"},
    {"question": "Which language is used to query a database?", "options": ["SQL", "Python", "C++", "HTML"], "answer": "SQL"},
    {"question": "What is a primary key?", "options": ["Unique identifier for records", "Used to establish foreign keys", "Used to duplicate data", "None of the above"], "answer": "Unique identifier for records"},
    {"question": "What does ACID stand for in DBMS?", "options": ["Atomicity, Consistency, Isolation, Durability", "Access, Control, Integrity, Data", "Authentication, Commit, Isolation, Durability", "Atomicity, Control, Isolation, Database"], "answer": "Atomicity, Consistency, Isolation, Durability"},
    {"question": "What is a foreign key?", "options": ["Key in another table", "Duplicate key", "Unique key", "None of the above"], "answer": "Key in another table"},
    {"question": "Which command is used to delete all records in a table?", "options": ["TRUNCATE", "DELETE", "DROP", "REMOVE"], "answer": "TRUNCATE"},
    {"question": "What is a transaction in DBMS?", "options": ["Set of operations", "Single operation", "Query execution", "Error handling"], "answer": "Set of operations"},
    {"question": "What is normalization?", "options": ["Eliminating redundancy", "Increasing redundancy", "Enhancing queries", "None of the above"], "answer": "Eliminating redundancy"},
    {"question": "Which SQL command is used to retrieve data?", "options": ["SELECT", "GET", "FETCH", "RETRIEVE"], "answer": "SELECT"},
    {"question": "What is a view in a database?", "options": ["A virtual table", "A stored procedure", "Physical storage", "Temporary data"], "answer": "A virtual table"},
    {"question": "What does DML stand for?", "options": ["Data Manipulation Language", "Database Management Language", "Data Maintenance Language", "Database Mapping Language"], "answer": "Data Manipulation Language"},
    {"question": "Which clause is used to filter records in SQL?", "options": ["WHERE", "GROUP BY", "ORDER BY", "FILTER"], "answer": "WHERE"},
    {"question": "What is the full form of ER in ER Diagram?", "options": ["Entity Relationship", "Entity Row", "Event Resource", "Entity Record"], "answer": "Entity Relationship"},
    {"question": "What is a composite key?", "options": ["Combination of two or more columns", "Duplicate of the primary key", "Foreign key with duplicates", "None of the above"], "answer": "Combination of two or more columns"},
    {"question": "Which function is used to find the number of rows in SQL?", "options": ["COUNT()", "SUM()", "ROWS()", "LENGTH()"], "answer": "COUNT()"},
    {"question": "What is a schema in DBMS?", "options": ["Structure of a database", "Database user", "Query command", "None of the above"], "answer": "Structure of a database"},
    {"question": "Which operation is NOT part of DDL?", "options": ["SELECT", "CREATE", "ALTER", "DROP"], "answer": "SELECT"},
    {"question": "Which of the following is an example of a NoSQL database?", "options": ["MongoDB", "MySQL", "PostgreSQL", "Oracle"], "answer": "MongoDB"},
    {"question": "What is the use of indexes in a database?", "options": ["Improves query performance", "Adds redundancy", "Joins tables", "Stores metadata"], "answer": "Improves query performance"}
    ],
    "Networking": [
    {"question": "What does IP stand for in networking?", "options": ["Internet Protocol", "Internal Process", "Internet Process", "Interface Protocol"], "answer": "Internet Protocol"},
    {"question": "Which layer of the OSI model is responsible for routing?", "options": ["Network Layer", "Data Link Layer", "Transport Layer", "Session Layer"], "answer": "Network Layer"},
    {"question": "What is the default port for HTTP?", "options": ["80", "443", "25", "21"], "answer": "80"},
    {"question": "What device is used to connect multiple networks?", "options": ["Router", "Switch", "Hub", "Modem"], "answer": "Router"},
    {"question": "What does DNS stand for?", "options": ["Domain Name System", "Dynamic Network System", "Data Name System", "Domain Network Server"], "answer": "Domain Name System"},
    {"question": "Which protocol is used to transfer files over the internet?", "options": ["FTP", "HTTP", "TCP", "SMTP"], "answer": "FTP"},
    {"question": "What is the primary purpose of a firewall?", "options": ["Prevent unauthorized access", "Boost internet speed", "Control email traffic", "Perform network diagnostics"], "answer": "Prevent unauthorized access"},
    {"question": "Which IP address version uses 128-bit addressing?", "options": ["IPv4", "IPv6", "IPv5", "IPv7"], "answer": "IPv6"},
    {"question": "What is the maximum length of a MAC address?", "options": ["6 bytes", "12 bytes", "4 bytes", "8 bytes"], "answer": "6 bytes"},
    {"question": "Which protocol ensures error-free delivery of data?", "options": ["TCP", "UDP", "ICMP", "ARP"], "answer": "TCP"},
    {"question": "What does NAT stand for?", "options": ["Network Address Translation", "Network Access Transmission", "Node Allocation Table", "Network Allocation Transfer"], "answer": "Network Address Translation"},
    {"question": "What is the primary function of ARP?", "options": ["Resolve IP addresses to MAC addresses", "Route packets", "Secure network communication", "Translate URLs"], "answer": "Resolve IP addresses to MAC addresses"},
    {"question": "Which topology uses a central hub?", "options": ["Star", "Ring", "Mesh", "Bus"], "answer": "Star"},
    {"question": "What is the size of an IPv4 address?", "options": ["32 bits", "64 bits", "128 bits", "16 bits"], "answer": "32 bits"},
    {"question": "Which protocol is used for sending emails?", "options": ["SMTP", "POP3", "IMAP", "FTP"], "answer": "SMTP"},
    {"question": "What does DHCP stand for?", "options": ["Dynamic Host Configuration Protocol", "Direct Host Connection Protocol", "Data Host Communication Protocol", "Dynamic Home Communication Protocol"], "answer": "Dynamic Host Configuration Protocol"},
    {"question": "Which layer of the OSI model is responsible for error detection and correction?", "options": ["Data Link Layer", "Transport Layer", "Network Layer", "Session Layer"], "answer": "Data Link Layer"},
    {"question": "What type of network connects devices within a limited area, like a home or office?", "options": ["LAN", "WAN", "MAN", "PAN"], "answer": "LAN"},
    {"question": "Which port is commonly used for secure HTTPS traffic?", "options": ["443", "80", "22", "25"], "answer": "443"},
    {"question": "What is the purpose of a VPN?", "options": ["To create a secure connection over the internet", "To increase browsing speed", "To block ads", "To resolve DNS queries"], "answer": "To create a secure connection over the internet"}
    ]
}

# User data storage
users = {}


# Load/save user data
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file)


# Register function
def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists! Try logging in.")
        return None
    password = input("Enter a password: ")
    users[username] = {"password": password, "score": 0}
    save_users()
    print("Registration successful!")
    return username


# Login function
def login():
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found! Try registering.")
        return None
    password = input("Enter your password: ")
    if users[username]["password"] == password:
        print("Login successful!")
        return username
    else:
        print("Incorrect password!")
        return None


# Quiz function
# Quiz function with numbered topic selection
def take_quiz(username):
    # Display topics with numbers
    print("Topics available:")
    topics = list(questions.keys())
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic}")

    # Prompt the user to select a topic by number
    try:
        topic_choice = int(input("Choose a topic by entering the number: "))
        if topic_choice < 1 or topic_choice > len(topics):
            print("Invalid choice! Please try again.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Get the chosen topic
    chosen_topic = topics[topic_choice - 1]
    print(f"\nYou selected: {chosen_topic}")

    # Fetch and randomize questions for the chosen topic
    quiz_questions = random.sample(questions[chosen_topic], 5)
    score = 0

    # Display questions and validate answers
    for i, q in enumerate(quiz_questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for idx, option in enumerate(q["options"], 1):
            print(f"{idx}. {option}")
        try:
            answer = int(input("Enter the option number: "))
            if answer < 1 or answer > len(q["options"]):
                print("Invalid choice! Skipping question.")
                continue
        except ValueError:
            print("Invalid input! Skipping question.")
            continue

        if q["options"][answer - 1] == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is: {q['answer']}")

    # Display the score and save it
    print(f"\nYour score: {score}/5")
    users[username]["score"] = score
    save_users()

    if chosen_topic not in questions:
        print("Invalid topic selected!")
        return

    print(f"\nYou selected: {chosen_topic}")
    quiz_questions = random.sample(questions[chosen_topic], 5)
    score = 0

    for i, q in enumerate(quiz_questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for idx, option in enumerate(q["options"], 1):
            print(f"{idx}. {option}")
        answer = input("Enter the option number: ")
        if q["options"][int(answer) - 1] == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is: {q['answer']}")

    print(f"\nYour score: {score}/5")
    users[username]["score"] = score
    save_users()


# Main loop
def main():
    global users
    users = load_users()

    print("Welcome to the Quiz Application!")
    username = None
    while not username:
        action = input("Do you want to (1) Register or (2) Login? Enter 1 or 2: ")
        if action == "1":
            username = register()
        elif action == "2":
            username = login()
        else:
            print("Invalid choice!")

    while True:
        take_quiz(username)
        choice = input("Do you want to (1) Reattempt the quiz or (2) Exit? Enter 1 or 2: ")
        if choice == "2":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()