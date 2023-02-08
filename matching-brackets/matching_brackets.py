def is_paired(input_string):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = []
    for i in input_string:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            # To check if closing bracket is after opening bracket
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                # If the brackets are balanced, then the pair is deleted from stack
                stack.pop()
            else:
                return False
    # If stack is empty, then all brackets pairs are balanced
    if len(stack) == 0:
        return True
    else:
        return False
