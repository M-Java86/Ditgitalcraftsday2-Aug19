text = ("What is your message?")
  letter_to_convert = ['A,''E','G,''I','O,' 'S', 'T']
numbers = [4,3,6,1,0,5,7]

uppercase_text = text.upper()
translation = ""
index = 0
while index < len(text):
#print(uppercase_text[index])
index_inner_loop = 0
letter_to_add_to_translation = ""
while index_inner_loop < len(letter_to_convert):
if uppercase_text[index]== letter_to_convert[index_inner_loop]:
# print("WE HAVE A MATCH!!")
#print(numbers[index_inner_loop])
letter_to_add_to_translation = str (numbers[index_inner_loop])
#[index_inner_loop]:
else:
#print("NO MATCHES! Sad face emoji")
letter_to_add_to_translation = uppercase_text [index]
index_inner_loop +=1
index += 1
translation = translation + letter_to_add_to_translation

print(translation)