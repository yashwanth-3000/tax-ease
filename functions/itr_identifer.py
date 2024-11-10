def get_itr_form():
    print("\n=== ITR Form Determination System ===\n")
    
    # Question 1
    print("Question 1: What is your total annual income?")
    print("1) Less than Rs. 50 Lakh")
    print("2) More than Rs. 50 Lakh")
    
    while True:
        try:
            income = int(input("Enter your choice (1 or 2): "))
            if income in [1, 2]:
                break
            print("Please enter either 1 or 2")
        except ValueError:
            print("Please enter a valid number")
    
    # Question 2
    print("\nQuestion 2: What are your sources of income?")
    print("1) Only salary and one house property")
    print("2) Business/Professional income")
    print("3) Multiple sources including foreign income")
    print("4) Presumptive business income")
    
    while True:
        try:
            income_source = int(input("Enter your choice (1-4): "))
            if income_source in [1, 2, 3, 4]:
                break
            print("Please enter a number between 1 and 4")
        except ValueError:
            print("Please enter a valid number")
    
    # Question 3
    print("\nQuestion 3: Which of these best describes your status?")
    print("1) Individual resident Indian")
    print("2) Company/Corporate entity")
    print("3) Charitable/Religious trust")
    print("4) Partnership firm/LLP")
    
    while True:
        try:
            status = int(input("Enter your choice (1-4): "))
            if status in [1, 2, 3, 4]:
                break
            print("Please enter a number between 1 and 4")
        except ValueError:
            print("Please enter a valid number")

    # Determine ITR form
    itr_form = determine_itr(income, income_source, status)
    
    return itr_form

def determine_itr(income, income_source, status):
    # If status is not individual
    if status == 2:
        return "ITR-6 (For Companies)"
    elif status == 3:
        return "ITR-7 (For Charitable/Religious Trusts)"
    elif status == 4:
        return "ITR-5 (For Partnership Firms/LLPs)"
    
    # For individuals (status == 1)
    if income == 1 and income_source == 1:  # Less than 50L and salary only
        return "ITR-1 (Sahaj)"
    elif income_source == 2:  # Business/Professional income
        return "ITR-3"
    elif income_source == 3:  # Multiple sources including foreign income
        return "ITR-2"
    elif income == 1 and income_source == 4:  # Less than 50L and presumptive business
        return "ITR-4 (Sugam)"
    else:
        return "ITR-2"  # Default for other cases

def main():
    print("Welcome to ITR Form Determination System")
    
    while True:
        itr_form = get_itr_form()
        print(f"\nBased on your responses, you should file: {itr_form}")
        
        print("\nWould you like to determine ITR form for another person?")
        choice = input("Enter 'yes' to continue or any other key to exit: ").lower()
        if choice != 'yes':
            break
    
    print("\nThank you for using ITR Form Determination System!")

if __name__ == "__main__":
    main()