def count_words(text):
  return len(text.split())

def characters(text):
  lower_case = text.lower()
  chars = {}
  for c in lower_case:
    if c not in chars:
      chars[c] = 0

    chars[c] += 1
  return chars

def main() -> int:
  path_to_file = "./books/frankenstein.txt"

  with open(path_to_file) as f:
    file_contents = f.read()

  print()
  print(f"--- Begin report of {path_to_file} ---")
  print(f"{count_words(file_contents)} words found in the document")
  print()
  
  chars = dict(sorted(characters(file_contents).items(), key=lambda item: item[1], reverse=True))
  for k in chars:
    if k.isalpha():
      print(f"The '{k}' character was found {chars[k]} times")
  print("--- End report ---")

if __name__ == '__main__':
  main()  # next section explains the use of sys.exit