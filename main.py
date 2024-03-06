def main():
  path_to_file = "/home/robimgabriel/workspace/github.com/robim-gabriel/bookbot/books/frankenstein.txt"
  with open(path_to_file) as f:
    file_content = f.read()
    print(file_content)

main()