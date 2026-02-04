def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "La Forge"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
    divs = ["Command", "Command", "Operations", "Security", "Engineering"]
    ids = [1001, 1002, 1003, 1004, 1005]
    return names, ranks, divs, ids


def display_menu():
    user_name = input("Enter your full name: ")
    print(f"\n--- FLEET MANAGEMENT SYSTEM ---")
    print(f"Logged in as: {user_name}")
    print("\n1. View Roster")
    print("2. Add Member")
    print("3. Remove Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    
    choice = input("\nSelect option: ")
    return choice
