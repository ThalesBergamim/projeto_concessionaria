import google.generativeai as genai
from django.conf import settings

def get_gemini_client(model, brand, year):
    genai.configure(api_key='AIzaSyAb89bfQDNZcsmWVi5FYz33-AbV6m21xFo')
    
    prompt = f'''
    Traga uma descrição de vendas completa para o carro {model} {brand} {year} em no maximo 250 caracteres. 
    Fale coisas especificas de cada modelo de carro como potência, velocidade maxima, etc. Gere o texto sem "*", somente a descrição de vendas. 
    '''
    
    generation_config = {
        "temperature": 2,   
        "max_output_tokens": 300,
        "response_mime_type": "text/plain",
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,)
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao gerar descrição: {str(e)}")
        return "Descrição não disponível no momento."





