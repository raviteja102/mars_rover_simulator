import argparse

def main():
    parser = argparse.ArgumentParser(description="Mars Rover Simulator") 
    parser.add_argument("--file", type=str, required=True, help="Path to input file")
    args = parser.parse_args()
    
    print(f"Read commands from a file: {args.file}")
    
    try: 
        with open(args.file, 'r' ) as f :
            commands = f.readlines()
        print("Commands in file ")
        for command in commands:
            print (command.strip())
    except FileNotFoundError:
        print(f"Error: {args.file} is not found")        
        
if __name__ == "__main__":
    main()