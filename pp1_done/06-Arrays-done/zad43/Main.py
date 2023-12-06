import MyText

our_text = "An apple a day keeps the doctor away"

result_a = MyText.num_of_words(our_text)
result_b = MyText.ordered(our_text)
result_c = MyText.alfabetical(our_text)

if(__name__ == "__main__"):
    print("Text:", our_text)
    print("Number of words:", result_a)
    print("Words from the longest:", ",".join(map(str, result_b)))
    print("Words ordered alfabetically:",",".join(map(str, result_c)))