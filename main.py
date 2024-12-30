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

  print(f"Frankenstein Wordcount: {count_words(file_contents)}")
  print(f"Frankenstein characters: {characters(file_contents)}")

if __name__ == '__main__':
  main()  # next section explains the use of sys.exit