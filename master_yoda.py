
def master_yoda(sentence):
    wordlist = sentence.split()
    reversed_wordlist = wordlist[::-1]
    return " ".join(reversed_wordlist)

print(master_yoda('I am home'))