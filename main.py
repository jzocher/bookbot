def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_char_count(text)
    create_report(book_path, num_words, num_chars)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    for t in text:
        if t.isalpha():
            t = t.lower()
            if t not in chars:
                chars[t] = 1
            else:
                chars[t] += 1
    sorted_dict = {}
    for key in sorted(chars, key=chars.get):
        sorted_dict[key] = chars[key]
    sorted_dict = dict(reversed(sorted_dict.items()))
    return sorted_dict

def create_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    for c in chars:
        print(f"The \'{c}\' character was found {chars[c]} times.")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()