# Enter your code here. Read input from STDIN. Print output to STDOUT
# First letter: S = split, C = combine
# Second letter: M = method, C = class, V = variable

def camelCase(line):
    user_input = []
    for input_values in line:
        user_input.append(input_values)
    
    word = user_input[4:]
    new_word = ''
    # print(word)

    upper = 0
    index = 0

    # First Letter
    if user_input[0] == 'S':
        for value in word:
            # print(value, type(value))
            if value == '(' or value == ')':
                continue
            elif value == value.upper() and index != 0:
                new_word+= ' '
            new_word+= value.lower()
            index += 1
        return(new_word)
            
    elif user_input[0] == 'C':
        
        for value in word:    
            if user_input[2] == 'C' and index == 0:
                new_word += user_input[4].upper()
            elif value == ' ':
                upper = 1
            elif upper == 1:
                new_word+= value.upper()
                upper = 0
            else:
                new_word+= value.lower()
            index += 1
        
        # Second Letter
        if user_input[2] == 'M':
            new_word += '()'
        return(new_word)



if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    lines = input().splitlines()
    
    for line in lines:
        if line.strip():
            print(camelCase(line))
