if __name__ == "__main__":
    package = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }
    while True:
        brackets = []
        stack = []
        words = input()
        if words == ".":
            break
        for word in words:
            if word in package.keys() or word in package.values():
                brackets.append(word)
        for bracket in brackets:
            if not stack:
                stack.append(bracket)
            elif bracket in package.keys():
                stack.append(bracket)
            elif bracket == package[stack[-1]]:
                stack.pop()
        print("no" if stack else "yes")


            
