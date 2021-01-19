
def to_upper(text):
	return text.upper()


def to_lower(text):
	return text.lower()


def to_toggle(text):
	return text.swapcase()

def to_backwards(text):
    return text[::-1]

if __name__ == '__main__':
    print(to_backwards('words'))
