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
