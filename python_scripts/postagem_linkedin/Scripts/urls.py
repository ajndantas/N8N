from sys import argv
from re import sub
import json


class Urls_Array:


    def __init__(self, array: str):
        
        self.i = 1
        
        raw = " ".join(array) # Concatena os elementos do array em uma única string
        
        self.array = json.loads(array) # Converte a string JSON em um objeto Python

        print("Array tratado para python: ", self.array, "Tipo do array tratado: ", type(self.array))
        
        self.urls = []


    def get_urls(self):

        for item in self.array:
                        
            print(f"Item {self.i}: ", item, "Tipo do item: ", type(item))

            self.add_url(item["url"])

            self.i += 1


    def add_url(self, url:str):
        self.urls.append(url)


    def print_urls(self) -> str:
        print(self.urls)


if __name__ == "__main__":
    
    try:
        if len(argv) < 2:
            raise ValueError("Nenhum array recebido. Por favor, forneça um array JSON como argumento.")
        
        else:
            urls_array = Urls_Array(argv[1:])

            urls_array.get_urls()
            urls_array.print_urls()

    except ValueError as e:
        print(e)