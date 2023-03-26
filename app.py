def new_word():

    oldWord = "This has been pretty cool"
    replaced_word = input("enter word to replace: ")
    replaced_with = input("word to replace with: ")

    re_sentenced = oldWord.replace(replaced_word, replaced_with)
    print(re_sentenced)

new_word()