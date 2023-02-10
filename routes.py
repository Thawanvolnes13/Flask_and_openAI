#import webbrowser
from flask import Flask, render_template as rd, request

import openai as ia

app = Flask(__name__)



@app.route('/')
def inicio():
    print("hello")
    return rd('index.html')

@app.route('/search', methods=['POST'])
def search():
    
    search_variable=request.form['name-search']
    
    
        
    try:    
        ia.api_key= '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'
        response = ia.Image.create(
            prompt = str(search_variable),
            n = 1,
            size='1024x1024'
        )
        image_url = response['data'][0]['url']
#        webbrowser.open_new_tab(image_url)
        print(f'URL da imagem gerada: {image_url}')
    except:
        print("Não encontramos o que você procura")
        return rd('index.html', erro_search="block")
        
    return rd('index.html', erro_search="none", link_url=image_url)
    
if __name__ == '__main__':
    app.run()