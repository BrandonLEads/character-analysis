#Programming Exercise 8-7
def main():
    # Local variables
    num_upper = 0
    num_lower = 0
    num_space = 0
    num_digits = 0
    data = ''
    # Open file text.txt for reading
    infile = open('C:\Users\brand\OneDrive\Documents\Coding\Code posted to github\Python\character analysis\text.txt', 'r')
    # Read in data from the file.
    data = infile.read()
    # Step through each character in the file.
    # Determine if the character is uppercase,
    # Lowercase, a digit, or space, and keep a
    # running total of each.
    for ch in data:
        if ch.isupper():
            num_upper = num_upper + 1
        if ch.islower():
            num_lower = num_lower + 1
        if ch.isdigit():
            num_digits = num_digits + 1
        if ch.isspace():
            num_space = num_space + 1
    # Close the file.
    infile.close()
    # Display the totals.
    print('The number of uppercase letters in the file:', num_upper)
    print('The number of lowercase letters in the file:', num_lower)
    print('The number of digits in the file:', num_digits)
    print('The number of whitespace in the file:', num_space)
# Call the main function.
main()