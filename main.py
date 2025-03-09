#from stats import *
import sys
sys.dont_write_bytecode = True

# NOTE:
#   Python will create a __pycache__ folder that contains the
#   precompiled binaries of all locally imported files.
#
#   This action can be suppressed a couple ways:
#     1. Before running the python code, export an ENV variable:
#        ex.: export PYTHONDONTWRITEBYTECODE=1
#     2. import sys then set the dont_write_bytecode flag to True.
#        ex.: import sys
#             sys.dont_write_bytecode = True
#        This must be listed before any other imports.

from stats import *

def get_book_text(file_path):
  file_contents = ""
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

def output_report(path_to_file):
  file_contents = get_book_text(path_to_file)
  word_count = get_num_words(file_contents)
  chars_count = get_num_chars(file_contents)

  print()
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path_to_file}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  
  chars = dict(sorted(chars_count.items(), key=lambda item: item[1], reverse=True))
  for k in chars:
    if k.isalpha():
      print(f"{k}: {chars[k]}")

  print("============= END ===============")

def main() -> int:
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  path_to_file = sys.argv[1]
  output_report(path_to_file)

if __name__ == '__main__':
  main()  # next section explains the use of sys.exit