def solution(words):
    package = {
        "(" : ")",
        "[" : "]"
    }

    brackets = []
    stack = []

    # 괄호만 남기기
    for word in words:
        if word in package.keys() or word in package.values():
            brackets.append(word)

    # running
    for bracket in brackets:
        if bracket in package:
            stack.append(bracket)
        else:
            if not stack:
                return "no"
            else:
                if package[stack[-1]] == bracket:
                    stack.pop()
                else:
                    return "no"
    return "no" if stack else "yes"

if __name__ == "__main__":
    while True:
        words = input()
        if words == ".":
            break
        else:
            print(solution(words))