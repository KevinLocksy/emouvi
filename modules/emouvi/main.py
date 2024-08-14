def print_happy_emoji():
  weirdInput = "hello \\ud83d\\ude04".encode("latin_1")
  backLatin = True

  output = (weirdInput
    .decode("raw_unicode_escape")
    .encode('utf-16', 'surrogatepass')
    .decode('utf-16')
  )

  if backLatin:
    output = (output
      .encode("raw_unicode_escape")
      .decode("latin_1")
    )
    
  print(output)
#end print_happy_emoji()