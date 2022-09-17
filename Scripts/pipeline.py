import sys
import os

sys.path.append(os.path.abspath(os.path.join("./Scripts/")))


class PromptPipeline():
    

    def extract_values(self, data):
        """
            extract the values from each json dictionaries and put in prompt format

        """
        s: str = ''
        try:
            for d in data:
                s+='Job Description: '
                s+=d['document']
                s+='\n'
                """
                    Extract entities from tokens
                    to conver them to the following 
                        DIPLOMA: ...
                        DIPLOMA_MAJOR: ....
                        EXPERIENCE: ...
                        SKILLS: ....
                """
                token_dict = {}
                for token in d['tokens']:
                    entity_label = token['entityLabel']
                    if entity_label in token_dict.keys():
                        token_dict[entity_label] += f",{token['text']}"
                    else:
                        token_dict[entity_label] = f"{token['text']}"
                dict_str = ''
                for key,value in token_dict.items():
                    dict_str+=f"{key}: {value}\n"
                s+=dict_str
                s+='\n--\n'
            return s
        except Exception:
            print("--> failed...")
    



