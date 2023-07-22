def is_balanced_bracket(input_string):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_map[char]:
                return "NO"
            stack.pop()
    
    return "YES" if not stack else "NO"

def main():
    sample_inputs = [
        "{[()]}",
        "{[(])}",
        "{(([])[])[]}"
    ]

    for input_string in sample_inputs:
        result = is_balanced_bracket(input_string)
        print(f"Input: {input_string}\nOutput: {result}\n")

if __name__ == "__main__":
    main()
