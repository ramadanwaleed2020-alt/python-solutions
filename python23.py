def solve(s): 
    words = s.split(' ')
    result = []
    for word in words:
        if word:
            word = word[0].upper() + word[1:]
        result.append(word)
    return ' '.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
