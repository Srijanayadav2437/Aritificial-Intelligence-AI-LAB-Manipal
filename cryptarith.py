import itertools

def get_value(word, substitution):
    """Convert a word into its corresponding numeric value based on the substitution mapping."""
    value = 0
    factor = 1
    for letter in reversed(word):
        value += factor * substitution[letter]
        factor *= 10
    return value

def solve(equation):
    """Solve the cryptarithmetic puzzle defined by the equation."""
    # Split the equation into left and right parts
    left, right = equation.lower().replace(' ', '').split('=')
    left = left.split('+')
    
    # Create a set of unique letters used in the equation
    letters = set(right)
    for word in left:
        letters.update(word)

    letters = list(letters)  # Convert to a list
    digits = range(10)

    # Generate all possible digit assignments for the letters
    for perm in itertools.permutations(digits, len(letters)):
        substitution = dict(zip(letters, perm))
        
        # Ensure no leading zeros for the first letters of any word
        if any(substitution[word[0]] == 0 for word in left + [right]):
            continue
        
        # Calculate the sum of the left side and compare it with the right side
        if sum(get_value(word, substitution) for word in left) == get_value(right, substitution):
            print(' + '.join(str(get_value(word, substitution)) for word in left) + " = {} (mapping: {})".format(get_value(right, substitution), substitution))
            return substitution  # Return the first valid substitution found

    print("No solution found")
    return None

if __name__ == "__main__":
    equation = input("Enter a cryptarithmetic equation (format: WORD1 + WORD2 = RESULT): ")
    solve(equation)
