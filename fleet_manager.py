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


def add_member(names, ranks, divs, ids):
    valid_ranks = ["Ensign", "Lieutenant", "Lt. Commander", "Commander", "Captain"]
    
    new_id = int(input("Enter ID: "))
    
    if new_id in ids:
        print("Error: ID already exists.")
        return
    
    new_rank = input("Enter rank: ")
    
    if new_rank not in valid_ranks:
        print("Error: Invalid rank.")
        return
    
    new_name = input("Enter name: ")
    new_div = input("Enter division: ")
    
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    
    print(f"Crew member {new_name} added successfully.")


def remove_member(names, ranks, divs, ids):
    member_id = int(input("Enter ID to remove: "))
    
    if member_id not in ids:
        print("Error: ID not found.")
        return
    
    idx = ids.index(member_id)
    
    removed_name = names.pop(idx)
    ranks.pop(idx)
    divs.pop(idx)
    ids.pop(idx)
    
    print(f"Crew member {removed_name} (ID: {member_id}) removed.")


def update_rank(names, ranks, ids):
    member_id = int(input("Enter ID to update: "))
    
    if member_id not in ids:
        print("Error: ID not found.")
        return
    
    valid_ranks = ["Ensign", "Lieutenant", "Lt. Commander", "Commander", "Captain"]
    new_rank = input("Enter new rank: ")
    
    if new_rank not in valid_ranks:
        print("Error: Invalid rank.")
        return
    
    idx = ids.index(member_id)
    old_rank = ranks[idx]
    ranks[idx] = new_rank
    
    print(f"{names[idx]}: {old_rank} -> {new_rank}")


def display_roster(names, ranks, divs, ids):
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
    search_term = input("Enter search term: ").lower()
    
    found = False
    for i in range(len(names)):
        if search_term in names[i].lower():
            print(f"ID: {ids[i]} | {names[i]} - {ranks[i]} ({divs[i]})")
            found = True
    
    if not found:
        print(f"No crew members found matching '{search_term}'.")


def filter_by_division(names, divs):
    division = input("Enter division (Command/Operations/Engineering/Medical/Security): ")
    
    found = False
    print(f"\n--- {division} Division ---")
    
    for i in range(len(names)):
        if divs[i] == division:
            print(f"{names[i]} - {divs[i]}")
            found = True
    
    if not found:
        print(f"No crew members found in {division} division.")


def calculate_payroll(ranks):
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
    count = 0
    
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count += 1
    
    print(f"High-ranking officers (Captain/Commander): {count}")
    return count


def main():
    print("FLEET MANAGEMENT SYSTEM - ONLINE")
    print("="*50)
    
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
