def main():
  path_to_file = "/home/robimgabriel/workspace/github.com/robim-gabriel/bookbot/books/frankenstein.txt"
  file_content = read_content(path_to_file)
  num_words = count_words(file_content)
  chars = count_each_letter(file_content)

def read_content(path_to_file):
  with open(path_to_file) as f:
    file_content = f.read()
  return file_content

def count_words(content_string):
  words = content_string.split()
  return len(words)

def count_each_letter(content_string):
  letters_dict = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
  lowered_string = content_string.lower()
  for letter in lowered_string:
    if letter in letters_dict:
      letters_dict[letter] += 1
  return letters_dict

main()