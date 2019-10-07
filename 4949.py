package = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }

def solution(words):
    brackets = []
    stack = []
    words = input()
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

        if stack:
            return "no"
        else:
            return "yes"



if __name__ == "__main__":
    while True:
        words = input()
        if words == ".":
            break
        print(solution(words))
                
