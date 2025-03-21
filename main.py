import sys
from stats import count_words, count_characters, char_dict_to_sorted_list

def	get_book_text(filepath):
	
	with open(filepath,'r') as f:
		file_contents = f.read()
	return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    
    # Get character counts
    char_counts = count_characters(book_text)
    
    # Convert the character counts dictionary to a sorted list
    # Make sure to import this function from stats.py
    sorted_chars = char_dict_to_sorted_list(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    # Print character count section
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]

        # Only print if the character is alphabetic
        if char.isalpha():
            print(f"{char}: {count}")
    
    # Print footer
    print("============= END ===============")

if __name__ == "__main__":
	main()


