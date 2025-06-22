# Count word frequency in a sentence.
# Input: "apple banana apple" → Output: {'apple': 2, 'banana': 1}

def word_frequency(sentence):
    words = sentence.split() 
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

list_1 = "apple banana apple"

count_words = word_frequency(list_1)
print("Count_words:", count_words)