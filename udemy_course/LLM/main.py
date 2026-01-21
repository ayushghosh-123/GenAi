import tiktoken

enc = tiktoken.encoding_for_model('gpt-4o')
text = "Hey There! My name is Ayush Ghosh"

tokens = enc.encode(text)
print("Tokens", tokens)


decode = enc.decode([25216, 3274, 0, 3673, 1308, 382, 21918, 1776, 499, 10729, 71])
print("Decoded",decode)

