import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_car_ai_bio(model, brand, year):
    """
    Gera uma descrição de venda para um carro usando a API de Chat da OpenAI.
    """
    if not openai.api_key:
        print("ERRO CRÍTICO: Chave da API da OpenAI não encontrada. Verifique seu arquivo .env")
        return "Erro na configuração: Chave da API não encontrada."
    
    prompt = f"Crie uma descrição de venda curta e atrativa (máx 250 caracteres) para o carro {brand} {model} {year}.Destaque características específicas e populares desse modelo.**Importante: não inclua preços ou qualquer símbolo de moeda (como R$).**"

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": "Você é um especialista em marketing de carros."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=70,
            temperature=0.7
        )
    
        texto_gerado = response.choices[0].message.content.strip()

        if texto_gerado.startswith('R$ '):
            return texto_gerado[3:]  # Remove os 3 primeiros caracteres ('R', '$', ' ')
        elif texto_gerado.startswith('R$'):
            return texto_gerado[2:]  # Remove os 2 primeiros caracteres ('R', '$')
        else:
            return texto_gerado  # Retorna o texto original se não começar com R$
    
    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API da OpenAI: {e}")
        return "Não foi possível gerar a descrição do carro no momento."