def abbrev_name(name):
  split_words = name.split(' ')
  abbreviate_name = lambda x: x[0].upper()
  abbreviates = list(map(abbreviate_name, split_words))
  abbreviates.insert(1, '.')
  result = ''.join(abbreviates)
  return result
