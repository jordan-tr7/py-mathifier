
import tokenize
from enum import Enum


class Modification(Enum):
    RENAME = 1
    DELETE = 2
    

FILE_NAME = 'src/example_file.py'


def update_token(new_string, tokens_to_verify):
    print("hi")


def main():
    
    with tokenize.open(FILE_NAME) as f:
        tokens = tokenize.generate_tokens(f.readline)
        
        tokens_list = list(tokens)
        
        modifications = []
        
        # Find the string token 'hello' and change it to 'world'
        for i, token in enumerate(tokens_list):
            
            #print("General Token Info:")
            #print(f"\t{token}")
            #print(f"\tString: {token.string}")
            #print(f"\tIs String DataType: {isinstance(token.string, str)}")
            #print(f"Token Exact Type: {token.exact_type}\n")
            
            """
            
            
            new_string = "AYO"
            
            # Create a new TokenInfo with the updated string
            new_token = tokenize.TokenInfo(
                type=token.type,
                string=new_string,
                start=token.start,
                end=token.end,
                line=token.line
            )
            tokens_list[i] = new_token
            """
            
            # TODO: add logic to only add one mod / line, in case of multiple uses on one line
            if tokens_list[i].exact_type == 1 and tokens_list[i].string == "my_var": #main
                
                modifications.append(
                    {
                        'type': Modification.RENAME,
                        'line': tokens_list[i].start[0],
                        'start': tokens_list[i].start,
                        'end_char': tokens_list[i].start[1]
                    }
                )
                """
                # Create a new TokenInfo with the updated string
                new_token = tokenize.TokenInfo(
                    type=token.type,
                    string="merge_sort",
                    start=token.start,
                    end=token.end,
                    line=token.line
                )
                tokens_list[i] = new_token
                """
            
            print(tokens_list[i])

    
    token_text = [token.string for token in tokens_list]
    print(''.join(token_text))
    
    # Convert the generator to a list of (type, string) tuples
    # Only the first two elements (token type and token string) are needed for untokenize
    tokens_for_untokenize = [(token.type, token.string) for token in tokens_list]

    # Untokenize the tokens back into code
    reconstructed_code = tokenize.untokenize(tokens_for_untokenize)
    
    #print(reconstructed_code)
    #with open(FILE_NAME, "w") as file:
    #    file.write(reconstructed_code)
            
    #for mod in Modification:
    #    print(mod)
    
    #x = Modification.RENAME
    #y = Modification.DELETE
    #print(y == Modification.RENAME)
    print(modifications)
    
    changed_lines = [[token for token in tokens_list if token.start[0] == mod['line'] and token.start[1] >= mod['end_char']] for mod in modifications]
    #[[token for token in tokens_list if token.start[0] == ]    mod['line'] for mod in modifications]
    
    print("\n\n")
    for i in changed_lines:
        print(i)
        print("\n\n")

if __name__ == "__main__":
    main()
