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
