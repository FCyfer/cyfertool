#!/usr/bin/env python3
import argparse

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

def print_guids(title, guids, only_guids=False):
    if only_guids:
        for guid in guids:
            print(guid)
    else:
        print(f"\n{title} (Total: {len(guids)})")
        print("=" * 50)
        for i, guid in enumerate(guids, 1):
            print(f"{i:3}. {guid}")

def save_guids(file_path, guids):
    with open(file_path, "w") as f:
        for guid in guids:
            f.write(guid + "\n")
    print(f"\n✅ GUIDs saved to {file_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Sequential GUID Generator - useful for fuzzing predictable UUIDs"
    )
    parser.add_argument(
        "--guid", "-g", required=True,
        help="Base GUID to generate sequential GUIDs from"
    )
    parser.add_argument(
        "--count", "-c", type=int, default=50,
        help="Number of sequential GUIDs to generate (default: 50)"
    )
    parser.add_argument(
        "--title", "-t", default="Generated GUIDs",
        help="Title for printed results"
    )
    parser.add_argument(
        "--out", "-o", help="Output file to save GUIDs (optional)"
    )
    parser.add_argument(
        "--only-guids", action="store_true",
        help="Print only GUIDs (no index/title) for wordlists"
    )

    args = parser.parse_args()

    guids = generate_sequential_guids(args.guid, args.count)
    print_guids(args.title, guids, args.only_guids)

    if args.out:
        save_guids(args.out, guids)

    if not args.only_guids:
        print("\nGeneration complete!")

if __name__ == "__main__":
    main()
