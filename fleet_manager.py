def init_database():
    """Returns 4 lists pre-populated with at least 5 Star Trek TNG characters"""
    names = ["Jean-Luc Picard", "William Riker", "Data", "Worf Rozhenko", "Beverly Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Operations", "Medical"]
    ids = [1001, 1002, 1003, 1004, 1005]
    
    return names, ranks, divs, ids


def display_menu():
    """Queries user's full name, prints options, and returns user's choice"""
    user_name = input("Enter your full name: ")
    print(f"\n--- FLEET MANAGEMENT SYSTEM ---")
    print(f"Logged in as: {user_name}")
    print("\n1. View Crew Roster")
    print("2. Add Crew Member")
    print("3. Remove Crew Member")
    print("4. Update Crew Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    
    choice = input("\nSelect option: ")
    return choice


def add_member(names, ranks, divs, ids):
    """Adds a crew member with validation for unique ID and valid rank"""
    valid_ranks = ["Ensign", "Lieutenant", "Lt. Commander", "Commander", "Captain"]
    
    new_id = input("Enter ID: ")
    
    # Validate ID is unique
    if new_id in ids:
        print("Error: ID already exists.")
        return
    
    new_rank = input("Enter rank: ")
    
    # Validate rank is valid TNG rank
    if new_rank not in valid_ranks:
        print(f"Error: Invalid rank. Valid ranks are: {', '.join(valid_ranks)}")
        return
    
    new_name = input("Enter name: ")
    new_div = input("Enter division (Command/Operations/Medical): ")
    
    # Append data to all 4 lists
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    
    print(f"Crew member {new_name} added successfully.")


def remove_member(names, ranks, divs, ids):
    """Removes a crew member by ID from all 4 lists"""
    member_id = input("Enter ID to remove: ")
    
    # Find the index
    if member_id not in ids:
        print("Error: ID not found.")
        return
    
    idx = ids.index(member_id)
    
    # Remove from all 4 lists to keep them in sync
    removed_name = names.pop(idx)
    ranks.pop(idx)
    divs.pop(idx)
    ids.pop(idx)
    
    print(f"Crew member {removed_name} (ID: {member_id}) removed.")


def update_rank(names, ranks, ids):
    """Finds a member by ID and updates their rank"""
    member_id = input("Enter ID to update: ")
    
    if member_id not in ids:
        print("Error: ID not found.")
        return
    
    valid_ranks = ["Ensign", "Lieutenant", "Lt. Commander", "Commander", "Captain"]
    new_rank = input("Enter new rank: ")
    
    if new_rank not in valid_ranks:
        print(f"Error: Invalid rank. Valid ranks are: {', '.join(valid_ranks)}")
        return
    
    idx = ids.index(member_id)
    old_rank = ranks[idx]
    ranks[idx] = new_rank
    
    print(f"{names[idx]}: {old_rank} -> {new_rank}")


def display_roster(names, ranks, divs, ids):
    """Displays a formatted table of all crew members"""
    if len(names) == 0:
        print("No crew members in database.")
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<8} {'Name':<20} {'Rank':<18} {'Division':<15}")
    print("="*70)
    
    for i in range(len(names)):
        print(f"{ids[i]:<8} {names[i]:<20} {ranks[i]:<18} {divs[i]:<15}")
    
    print("="*70)


def search_crew(names, ranks, divs, ids):
    """Searches for crew members whose name contains the search term"""
    search_term = input("Enter search term: ").lower()
    
    found = False
    for i in range(len(names)):
        if search_term in names[i].lower():
            print(f"ID: {ids[i]} | {names[i]} - {ranks[i]} ({divs[i]})")
            found = True
    
    if not found:
        print(f"No crew members found matching '{search_term}'.")


def filter_by_division(names, divs):
    """Filters and displays crew members by division"""
    valid_divisions = ["Command", "Operations", "Medical"]
    division = input(f"Enter division ({'/'.join(valid_divisions)}): ")
    
    if division not in valid_divisions:
        print(f"Error: Invalid division. Valid divisions are: {', '.join(valid_divisions)}")
        return
    
    found = False
    print(f"\n--- {division} Division ---")
    
    for i in range(len(names)):
        if divs[i] == division:
            print(f"{names[i]} - {divs[i]}")
            found = True
    
    if not found:
        print(f"No crew members found in {division} division.")


def calculate_payroll(ranks):
    """Calculates total payroll based on rank"""
    rank_credits = {
        "Ensign": 200,
        "Lieutenant": 400,
        "Lt. Commander": 600,
        "Commander": 800,
        "Captain": 1000
    }
    
    total_cost = 0
    
    for rank in ranks:
        if rank in rank_credits:
            total_cost += rank_credits[rank]
    
    print(f"\nTotal Payroll Cost: {total_cost} credits")
    return total_cost


def count_officers(ranks):
    """Counts and returns the number of Captains and Commanders"""
    count = 0
    
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count += 1
    
    print(f"High-ranking officers (Captain/Commander): {count}")
    return count


def main():
    """Main program loop"""
    print("FLEET MANAGEMENT SYSTEM - ONLINE")
    print("="*50)
    
    # Initialize database
    names, ranks, divs, ids = init_database()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            display_roster(names, ranks, divs, ids)
        elif choice == "2":
            add_member(names, ranks, divs, ids)
        elif choice == "3":
            remove_member(names, ranks, divs, ids)
        elif choice == "4":
            update_rank(names, ranks, ids)
        elif choice == "5":
            search_crew(names, ranks, divs, ids)
        elif choice == "6":
            filter_by_division(names, divs)
        elif choice == "7":
            calculate_payroll(ranks)
        elif choice == "8":
            count_officers(ranks)
        elif choice == "9":
            print("Shutting down Fleet Management System.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
