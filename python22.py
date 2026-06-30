def print_rangoli(size):
    # your code goes here
    import string

    alpha = string.ascii_lowercase
    width = 4 * size - 3
    lines = []
    
    for i in range(size - 1, -1, -1):
        
        letters_down = [alpha[j] for j in range(size - 1, i - 1, -1)]
        
        letters_up = letters_down[-2::-1]
        line_letters = letters_down + letters_up
        line = "-".join(line_letters)
        centered_line = line.center(width, '-')
        lines.append(centered_line)

    result = lines + lines[-2::-1]
    print("\n".join(result))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)