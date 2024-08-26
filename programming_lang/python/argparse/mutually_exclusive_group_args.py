import argparse

def main():
    parser = argparse.ArgumentParser(description="Example script that requires one of two arguments.")

    # Create a mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)

    # Add arguments to the group
    group.add_argument('--option1', type=str, help="First option")
    group.add_argument('--option2', type=str, help="Second option")

    # Parse the arguments
    args = parser.parse_args()

    # Your logic here
    if args.option1:
        print(f"Option 1 provided: {args.option1}")
    elif args.option2:
        print(f"Option 2 provided: {args.option2}")

if __name__ == "__main__":
    main()
