from sys import argv
import json


class Urls_Array:

    
    def __init__(self, array:list):
        
        # converte JSON para lista de dicionários Python
        self.array = json.loads(array)        

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
