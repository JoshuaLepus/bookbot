def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    letters = count_letter(text)
    letter = []
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in document.")
    for n in letters:
        letter.append(n)
        letter.sort()
    for l in letter:
        if l.isalpha():
            print(f"The {l} character was found {letters[l]} times.")
    print("--- End of report ---")

# Opens the file from path and returns the file as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
# Takes a string as an input and iterates count with each word
def count_words(string):
    count = 0
    words = string.split()
    for word in words:
        if word != "":
            count += 1
    return count

# Takes a string as imput converts to lover case counts the letter
def count_letter(string):
    letters_dict = {}
    for word in string:
        # .lower function works on strings not lists do not split a string before .lower
        l = word.lower()
        if l in letters_dict:
            letters_dict[l] += 1
        else:
            letters_dict[l] = 1
    return letters_dict




main()