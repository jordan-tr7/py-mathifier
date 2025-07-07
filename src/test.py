
import tokenize


def main():
    with tokenize.open('src/example_file.py') as f:
        tokens = tokenize.generate_tokens(f.readline)
        for token in tokens:
            print("General Token Info:")
            print(f"\t{token}")
            print(f"\tString: {token.string}")
            print(f"\tIs String DataType: {isinstance(token.string, str)}")
            print(f"Token Exact Type: {token.exact_type}\n")
            


if __name__ == "__main__":
    main()
