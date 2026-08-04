# Simplified Earley Parser

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["John"], ["Mary"]],
    "VP": [["likes", "NP"]]
}

sentence = input("Enter sentence: ").split()

chart = [[] for _ in range(len(sentence)+1)]

chart[0].append(("S", ["NP", "VP"], 0))

for i in range(len(sentence)):
    if sentence[i] in ["John", "Mary"]:
        chart[i+1].append(("NP", [], i))
    elif sentence[i] == "likes":
        chart[i+1].append(("VP", [], i))

print("\nChart States")

for i in range(len(chart)):
    print("Position", i)
    print(chart[i])

print("\nParsing Completed (Simplified Earley)")