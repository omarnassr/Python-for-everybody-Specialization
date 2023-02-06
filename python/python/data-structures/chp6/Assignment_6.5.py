'''
 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
  Convert the extracted value to a floating point number and print it out.
  '''

text = "X-DSPAM-Confidence:    0.8475"

# finding the No part in the variable
stop_position = text.find('0')
print(stop_position)
# slicing the no part of the text
slice_text = text[stop_position:]
print(slice_text)
# turning result to float datatype
turn_into_float = float(slice_text)
print(turn_into_float)

