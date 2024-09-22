import inflect

# Create an inflect engine
p = inflect.engine()

# Function to convert number to words
def number_to_words(number):
    return p.number_to_words(number)

# Example usage
if __name__ == "__main__":
    num = 123
    words = number_to_words(num)
    print(f"{num} in words is: {words}")
