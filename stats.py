import sys

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_content = f.read()
    return file_content
  
def get_word_count(text):
  words = text.split()
  count = len(words)
  return count

def get_characters_count(text):
  char_dict = {}
  text = text.lower()
  for char in text:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  return char_dict

def print_report(word_count, char_dict, path):
  def sort_on(char_count):
    return char_count[1]
  sorted_char_dict = sorted(char_dict.items(), key=sort_on, reverse=True)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  
  for char, coutn in sorted_char_dict:
    if char.isalpha():
      print(f"{char}: {coutn}")

  print("============= END ===============")

def main():
  if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
  path_to_book = sys.argv[1]
  text = get_book_text(path_to_book)
  word_count = get_word_count(text)
  characters_count = get_characters_count(text)
  print_report(word_count, characters_count, path_to_book)

main()
