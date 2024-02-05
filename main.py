# with open("first_file.txt", "w") as test_file:
#     test_file.write("Lemon, Car, Watermelon, Wind, Mandarin, Table, Piano, Bicycle, Flower, Lantern, Scratch")
#
#
# with open("first_file.txt", "r") as test_file:
#
#     test_file_split = test_file.read().split(", ")
#
#
# with open("final_file.txt", "a") as test_final_file:
#     for word in test_file_split:
#         if len(word) >= 7:
#             test_final_file.write(word + "\n")




########################
# def count_words(text):
#     words = text.split(", ")
#     return len(words)
#
# with open("file.txt", "w") as count_len_words_file:
#     text = "Lemon, Car, Watermelon, Wind, Mandarin, Table, Piano, Bicycle, Flower, Lantern, Scratch"
#     count = count_words(text)
#     count_len_words_file.write(text)
#
# with open("file.txt", "a") as count_len_words_file:
#     count_len_words_file.write(f"\nTotal words: {count}")


# forbidden_word = input("Enter the word you want to ban: ")
#
# with open("text_file.txt", "w") as input_file:
#     text = input("Enter any text: ")
#     input_file.write(text)
#
# with open("text_file.txt", "r") as input_file:
#     text = input_file.read()
#     if forbidden_word in text:
#         text_without_banword = text.replace(forbidden_word, "*" * len(forbidden_word))
#
#         with open("modified_text_file.txt", "w") as output_file:
#             output_file.write(text_without_banword)
#
#
#         print("Modified text:")
#         print(text_without_banword)
#         print("Statistics:")
#         print(f"Replaced {text.count(forbidden_word)} occurrences of '{forbidden_word}' with '*'")
#     else:
#         print("The forbidden word was not found in the text.")

######################################




# forbidden_word = input("Enter the word you want to ban: ")
#
# with open("text_file.txt", "w") as input_file:
#     text = input("Enter any text: ")
#     input_file.write(text)
#
# with open("text_file.txt", "r") as input_file:
#     text = input_file.read()
#     if forbidden_word in text:
#         text_without_banword = text.replace(forbidden_word, "*" * len(forbidden_word))
#
#         with open("modified_text_file.txt", "w") as output_file:
#             output_file.write(text_without_banword)
#
#
#         replacements_count = text.count(forbidden_word)
#
#
#         with open("statistics.txt", "w") as stats_file:
#             stats_file.write(f"Replaced {replacements_count} occurrences of '{forbidden_word}' with '*'\n")
#
#         print("Modified text:")
#         print(text_without_banword)
#         print("Statistics:")
#         print(f"Replaced {replacements_count} occurrences of '{forbidden_word}' with '*'")
#     else:
#         print("The forbidden word was not found in the text.")



