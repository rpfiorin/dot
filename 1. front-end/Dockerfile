FROM cypress/included:12.5.0

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o diretorio /app da imagem
COPY . .

RUN npm install

# Comando para executar os testes em headless
CMD ["npm", "run", "npx cypress run"]