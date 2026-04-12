from sys import argv
import json
import ast

class Urls_Array:

    def convert_to_json(self, array):
         
        print("\nArray recebido: \n", array)

        # converte string para dict Python
        dados = ast.literal_eval(array)

        # converte dict para JSON válido
        self.json_valido_array = json.dumps(dados)
        
        print("\nJSON válido: \n", self.json_valido_array)

        return self.json_valido_array
    

    def __init__(self, array):
        
        json_valido_array = self.convert_to_json(array) # Converte a string de array recebido para JSON válido      

        # converte JSON para lista de dicionários Python
        self.array = json.loads(json_valido_array)        

        self.urls = []

        self.i = 1


    def get_urls(self):
        for item in self.array:
            print(f"Item {self.i}\n", item)

            self.add_url(item["url"])

            self.i += 1

    def add_url(self, url):
        self.urls.append(url)

    def print_urls(self):
        print(self.urls)


if __name__ == "__main__":
    
    try:
        if len(argv) < 2:
            raise ValueError("Nenhum array recebido. Por favor, forneça um array JSON como argumento.")
        
        else:
            urls_array = Urls_Array(argv[1]) # urls_array = Urls_Array(data)

            urls_array.get_urls()
            urls_array.print_urls()

    except ValueError as e:
        print(e)