def match_words(words):
  c = 0

  for word in words:
    if word[0] == word[-1]:
      c+= 1
  return c

print(match_words(['abc', 'xyz', 'aba', '1221']))
