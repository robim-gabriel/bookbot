def main(): 
  path_to_file = "books/frankenstein.txt"
  build_report(path_to_file)

def read_content(path_to_file):
  with open(path_to_file) as f:
    file_content = f.read()
  return file_content

def count_words(content_string):
  words = content_string.split()
  return len(words)

def count_each_letter(content_string):
  letters_dict = {}
  lowered_string = content_string.lower()
  for letter in lowered_string:
    if letter in letters_dict:
      letters_dict[letter] += 1
    else:
      letters_dict[letter] = 1
  return letters_dict

def convert_char_dict_to_list_of_char_dicts(dict):
  list = []
  for elem in dict:
    list.append({"char": elem, "num": dict[elem]})
  return list

def sort_on(dict):
  return dict["num"]

def build_report(path_to_file):
  print(f"===== Begin report of {path_to_file} =====")
  lower_string = read_content(path_to_file).lower()
  num_words = count_words(lower_string)
  print(f"\t{num_words} words found in the document\n")
  chars = convert_char_dict_to_list_of_char_dicts(count_each_letter(lower_string))
  chars.sort(reverse=True, key=sort_on)
  for dict in chars:
    if dict["char"].isalpha():
      print(f"\tThe {dict["char"]} character was found {dict["num"]} times")
  print("=================== End Report ===================")
main()