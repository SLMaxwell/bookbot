def get_num_words(text):
  return len(text.split())

def get_num_chars(text):
  lower_case = text.lower()
  chars = {}
  for c in lower_case:
    if c not in chars:
      chars[c] = 0

    chars[c] += 1
  return chars