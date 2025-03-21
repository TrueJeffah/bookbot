def count_words(text):
        words = text.split()
        return len(words)

def count_characters(text):
	char_counts = {}
	text = text.lower()

	for char in text:
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts


def char_dict_to_sorted_list(char_counts):
	char_list = []

	for char, count in char_counts.items():
		char_dict = {"char": char, "count": count}
		char_list.append(char_dict)

	def sort_on(dict):
 	   	return dict["count"]

	char_list.sort(reverse=True, key=sort_on)
	
	return char_list



