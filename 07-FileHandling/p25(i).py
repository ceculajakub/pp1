import re

message = "To be, or not to be, that is the question"
result_sentence = re.findall(r"\b\w+\b", message)
print(len(result_sentence))