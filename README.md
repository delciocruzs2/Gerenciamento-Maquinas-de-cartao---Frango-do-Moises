**Gerenciamento de Máquinas de cartão - Frango do Moisés**
Guia de instalação rápida para o servidor ou máquina local utilizando Docker.



🛠️ **Instalação e Execução**

**1. Obter o Código (Escolha uma opção)**
**- Opção A (Via Git): Clone o repositório diretamente:**

        (Bash)
        git clone https://github.com/delciocruz2/Gerenciamento-Maquinas-de-cartao---Frango-do-Moises.git
        cd Gerenciamento-Maquinas-de-cartao---Frango-do-Moises

**- Opção B (Via Release/Lançamento):**
B.1. Vá na aba Lançamentos (Releases) do repositório.
B.2. Em Ativos, baixe o arquivo Código-fonte (zip).
B.3. Descompacte o arquivo na pasta desejada.


**2. Abrir o Terminal**
Abra o CMD ou PowerShell dentro da pasta onde o projeto foi clonado ou descompactado.


**3. Subir o Sistema (Docker)**
Com o Docker rodando, execute o comando para construir e iniciar os containers:

        (Bash)
        docker-compose up -d --build

        

**🌐 Como Acessar o serviço:**
O sistema estará disponível imediatamente em:
👉 Link: http://localhost:4200
👉 Link: http://nome_da_maquina.local:4200
