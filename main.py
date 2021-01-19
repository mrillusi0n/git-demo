from formats import to_lower, to_upper, to_toggle, to_backwards

FORMATTING = {
	'caps': to_upper,
	'lower': to_lower,
	'toggle': to_toggle,
	'rev': to_backwards,
}

def main():
	text = input("Input some text to format:\n")
	format_name = input("Choose a text format: ")

	func = FORMATTING[format_name]

	result = func(text)
	print(result)


if __name__ == "__main__":
	main()
