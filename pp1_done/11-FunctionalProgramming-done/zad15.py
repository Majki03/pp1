text = "I completely agree with you"

words = text.split()

letter_counts = list(map(lambda word: len(word), words))

print(f"Text: {text}\n"
      f"No. of letters in words: {letter_counts}")