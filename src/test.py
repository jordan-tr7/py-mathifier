
import tokenize
from enum import Enum


class Modification(Enum):
    RENAME = 1
    DELETE = 2
    

FILE_NAME = 'src/example_file.py'


def get_token_list(file):
    with tokenize.open(file) as f:
        tokens = tokenize.generate_tokens(f.readline)
        tokens_list = list(tokens)

    return tokens_list
    
    
def get_modifications(tokens_list, type_condition, text_condition, mod_type):
    
    mod_dict = {}
    
    for i, token in enumerate(tokens_list):
        
        if tokens_list[i].exact_type == type_condition and tokens_list[i].string == text_condition: #1, my_var
        
            if tokens_list[i].start[0] in mod_dict.keys():
                mod_dict[tokens_list[i].start[0]].append(
                    {
                    'type': mod_type,
                    'line': tokens_list[i].start[0],
                    'start': tokens_list[i].start,
                    'start_char': tokens_list[i].start[1],
                    'end': tokens_list[i].end, 
                    'end_char': tokens_list[i].end[1], 
                    'text'
                    }
                )
            else:
                mod_dict[tokens_list[i].start[0]] = [{
                    'type': mod_type,
                    'line': tokens_list[i].start[0],
                    'start': tokens_list[i].start,
                    'start_char': tokens_list[i].start[1],
                    'end': tokens_list[i].end, 
                    'end_char': tokens_list[i].end[1]
                }]
 
    return [mod_dict[i] for i in mod_dict]
    


def process_modifications(tokens_list, modifications_list):
    
    for mod in modifications_list:
        
        line = mod[0]['line']
        mod_type = mod[0]['type']
        print(line)
        
        not_processed = True
        
        for index, token in enumerate(tokens_list):
            if token.start[0] < line:
                continue
            if token.start[0] > line:
                break 
            
            
            print("We're at the correct token")
            print(token)
       
        
    
    #for i, token in enumerate(tokens_list):
    #    if token.start[0] == modifications_list[0][0]['line']:
     #       print("We're at a line that needs to be modified")
     #       print(token)




#def get_line_tokens(tokens_list, line, start=0):
#    return [token for token in tokens_list if token.start[0] == line and token.start[1] >= start]
    
    
def update_token(tokens_list, new_string, tokens_to_verify):
    print("hi")


def main():
    
    
    tl = get_token_list(FILE_NAME)
    
    #for i in tl:
    #    print(i)
    
    ml = get_modifications(tl, 1, "my_var", Modification.RENAME)
    
    for mod in ml:
       print(mod)
    
    
    print("\n\n\n")
    print(ml[1][0]['line'])
    #print(ml)
    print("\n\n\n")
    #test = get_line_tokens(tl, ml[0][0]['line'], ml[0][0]['start_char'])
    #print(test)
    
    process_modifications(tl, ml)
    
    
    """
    
    
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

    
    print("\n\n")
    for i in changed_lines:
        print(i)
        print("\n\n")
    """
    
    
if __name__ == "__main__":
    main()
