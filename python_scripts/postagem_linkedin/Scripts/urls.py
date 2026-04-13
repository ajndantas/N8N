from sys import argv
import json
import ast


class Urls_Array:

    
    def convert_to_json(self, array:str) -> str:
         
        print("\nArray recebido: \n", array)

        # converte string para dict Python
        dados = ast.literal_eval(array)

        # converte dict para JSON válido
        self.json_valido_array = json.dumps(dados)
        
        print("\nJSON válido: \n", self.json_valido_array)

        return self.json_valido_array
    
    
    def __init__(self, array:str):
        
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

    def add_url(self, url:str):
        self.urls.append(url)

    def print_urls(self) -> str:
        print(self.urls)


if __name__ == "__main__":
    
    try:
        if len(argv) < 2: # Quantos args foram passados para o script? Se for menor que 2, 
                          # significa que nenhum argumento foi fornecido (o primeiro argumento é sempre o nome do script)

            raise ValueError("Nenhum argumento fornecido. Por favor, forneça um array de URLs como argumento.")
        
        else:
            urls_array = Urls_Array(argv[1]) # Quem é argv[1] ? O argv[1] é o primeiro argumento passado para o script, que é o array de URLs.

            urls_array.get_urls()
            urls_array.print_urls()

    except ValueError as e:
        print(e)
