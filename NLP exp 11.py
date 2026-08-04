# Simple Top-Down Parser

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["John"], ["Mary"]],
    "VP": [["V", "NP"]],
    "V": [["likes"], ["sees"]]
}

sentence = input("Enter sentence: ").split()

def parse(symbol, words):
    if not words:
        return False, []

    if symbol not in grammar:
        if words[0] == symbol:
            return True, words[1:]
        return False, words

    for production in grammar[symbol]:
        remaining = words
        success = True

        for part in production:
            success, remaining = parse(part, remaining)
            if not success:
                break

        if success:
            return True, remaining

    return False, words

result, remaining = parse("S", sentence)

if result and not remaining:
    print("Sentence Accepted")
else:
    print("Sentence Rejected")