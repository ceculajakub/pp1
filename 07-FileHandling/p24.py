import re

message = "To be, or not to be, that is the question"
result_sentence = re.findall("[aeiouy]", message)
print(len(result_sentence))
