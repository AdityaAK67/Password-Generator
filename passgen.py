import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', 
    '`', '{', '|', '}', '~', '"', '\'', ',', '.', '§', '¶', '©', '®', '™', '¤', '°', '²', '³', 'µ'
]
characters = letters + numbers + symbols

# Ask user for starting characters
start_string = input("Enter the starting string for the password (can be letters, numbers, or anything else): ")

start_size = len(start_string) + 1  # 
end_size = int(input("Enter the End Size "))
print("Generated password: ")
for size in range(start_size, end_size + 1):
    # Generate all combinations of the remaining characters
    for combination in itertools.product(characters, repeat=size-len(start_string)):
        password = start_string + ''.join(combination)
    
        print(password)
