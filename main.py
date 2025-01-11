def count_words(text):
    
    words = text.split()
    count = len(words)
    return count


def count_characters(text):
    """Counts the number of times each character appears in the given text."""
    char_count = {} 
    text = text.lower() 

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def main():
    path_to_file = 'book/frankenstein.txt'
    try:
        with open(path_to_file, 'r') as f:
            file_contents = f.read()

        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)

        print(f"{word_count} words found in the document")

        for char, count in sorted(char_count.items()):
            print(f"The '{char}' character was found {count} times")

        print('--- End report ---')

    except FileNotFoundError:
        print(f"Error: The file '{path_to_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the main function
main()
