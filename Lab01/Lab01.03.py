"""SwapVar"""
def swap(value):
    """swap"""
    final = (value[1],value[0])
    print(final)


def convert_string_to_tuples(text_in):
  values = text_in.strip('()').split(', ')
  return tuple(map(float, values))

swap(convert_string_to_tuples(input()))