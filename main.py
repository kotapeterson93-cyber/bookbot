import sys
if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
else:


	def get_book_text(filepath):

		with open(filepath) as f:
			file_contents = f.read()
			return(file_contents)

	from stats import find_words
	from stats import letter_count
	from stats import convert


	def main():
		book_contents = get_book_text(sys.argv[1])

		print("============ BOOKBOT ============")
		print("Analyzing book found at books/frankenstein.txt...")
		print("----------- Word Count ----------")
	
		num_words = find_words(book_contents)
		print(f"Found {num_words} total words")


		print("--------- Character Count -------")
		chars = letter_count(book_contents)
		sorted_chars = convert(chars)
		for char in sorted_chars:
			if char["char"].isalpha():
				print(f"{char['char']}: {char['num']}")
		print("============= END ===============")


main()
