def main():
  path_to_file = "/home/robimgabriel/workspace/github.com/robim-gabriel/bookbot/books/frankenstein.txt"
  file_content = read_content(path_to_file)
  words = count_words(file_content)
  print(words)

def read_content(path_to_file):
  with open(path_to_file) as f:
    file_content = f.read()
  return file_content

def count_words(content_string):
  words = content_string.split()
  return len(words)


main()