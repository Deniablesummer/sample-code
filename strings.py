# James Ryan

# Python 3.7.1

def shorten(input, length, token="...", keep=False):
	if length == 0:
		return ""
	if length >= len(input):
		return (input)

	if keep:  # keep words whole
		words = input.split(" ")
		while len(words) != 0:
			word = words.pop(int(len(words) / 2))
			output = words

			if (len(words)) % 2 == 0:
				output.insert(int(len(words) / 2), token)
			else:
				output.insert(int((len(words) / 2) + 1), token)
			output = ' '.join(output)
			output = output.replace(" " + token + " ", token)
			output = output.replace(" " + token, token)
			output = output.replace(token + " ", token)
			if len(output) <= length:
				return output
			words.remove(token)
		return token

	else:  # don't keep words whole
		middle = int(len(input) / 2)
		overage = int(len(input) - length + len(token))
		return input.replace(
			input[int(middle - (overage / 2)):int(middle + (overage / 2))],
			token)