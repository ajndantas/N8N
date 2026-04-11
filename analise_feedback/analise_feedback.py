import json

class analise_feedback:
    
    def __init__(self):

        with open("analise_feedback.json", "r",encoding="utf-8") as f:
            
            self.__json_feedback = json.load(f)[0]['JSON'][0]
            print(self.__json_feedback)


if __name__ == "__main__":
    analise_feedback()
    