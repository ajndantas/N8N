from sys import argv

class Urls_Array:

    
    # data = [  
    #             { 
    #                 "url": "https://businessweek.com.br/2026/04/03/inteligencia-artificial-reposiciona-rh-e-amplia-o-papel-humano-na-tomada-de-decisao/",
    #                 "id": 1,
    #                 "createdAt": "2026-04-10T18:25:54.525Z", 
    #                 "updatedAt": "2026-04-10T18:25:54.525Z"
    #             }
    #       ]

    def __init__(self,array):
        
        self.array = array

        self.urls = []       


    def get_urls(self):

        for url in self.array:
            self.add_url(url['url'])
    

    def add_url(self,url):

        self.urls.append(url)
    

    def print_urls(self):
        print(self.urls)
    

if __name__ == "__main__":

    urls_array = Urls_Array(argv[1]) # argv[1] é o argumento passado na linha de comando, que deve ser um array de URLs no formato JSON
    
    urls_array.get_urls()
    print(urls_array.urls)

    