# 1. Imagem base com Python 3.14
FROM python:3.14-slim

# 2. Pasta de trabalho
WORKDIR /app

# 3. Copia e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia o código e as pastas (bronze, silver, gold)
COPY . .

# 5. Comando para rodar
CMD ["python", "main.py"]


