# Automação de Testes - E-commerce Saucedemo

## 📋 Sobre o Projeto
Este projeto consiste em uma automação de testes para o site de e-commerce Saucedemo, desenvolvido como parte do processo de capacitação técnica. A automação foi implementada utilizando Selenium WebDriver com Python, focando em testes de compra padrão.

## 🚀 Tecnologias Utilizadas
- Python 3.9
- Selenium WebDriver
- pytest
- pytest-html
- pytest-metadata
- GitHub Actions (CI/CD)

## 🛠️ Estrutura do Projeto
```
.
├── .github/
│   └── workflows/
│       └── ci_full.yml          # Configuração do GitHub Actions
├── pages/
│   ├── base_page.py            # Classe base para páginas
│   ├── cart_page.py            # Página do carrinho
│   ├── checkout_page.py        # Página de checkout
│   ├── inventory_page.py       # Página de inventário
│   ├── login_page.py           # Página de login
│   └── product_page.py         # Página de produtos
├── test_execution/
│   └── test_execution_compra_standard.py  # Script de execução dos testes
├── conftest.py                 # Configurações do pytest
├── pytest.ini                  # Configurações do pytest
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação do projeto
```

## 🔧 Configuração do Ambiente

### Pré-requisitos
- Python 3.9 instalado
- Chrome Browser instalado
- Git instalado

### Instalação
1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Instale o ChromeDriver:
```bash
python -m pip install webdriver-manager
```

## 🧪 Execução dos Testes

### Localmente
Para executar os testes localmente:
```bash
pytest --html=relatorio_teste.html
```

### No GitHub Actions
Os testes são executados automaticamente no GitHub Actions quando:
- Um push é feito para o repositório
- Um pull request é criado

## 📊 Relatório de Testes
- O relatório é gerado automaticamente após a execução dos testes
- O título do relatório é personalizado: "DM- Teste de Capacitação Técnica - Maxwell e-commerce Saucedemo"
- O relatório é processado e disponibilizado como artefato no GitHub Actions

## 🔄 Workflow do GitHub Actions
O workflow está configurado para:
1. Configurar o ambiente Python
2. Instalar o Chrome e ChromeDriver
3. Instalar as dependências
4. Executar os testes
5. Processar e enviar o relatório como artefato

## 📝 Funcionalidades Testadas
- Login no sistema
- Navegação pelo inventário
- Adição de produtos ao carrinho
- Processo de checkout
- Finalização de compra

## 🛡️ Configurações de Segurança
- Modo headless para execução em ambiente CI
- Modo anônimo do Chrome
- Desabilitação de notificações e popups
- Configurações de segurança do Chrome

## 🤝 Contribuição
Para contribuir com o projeto:
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✉️ Contato
Maxwell - [vmaxbh@gmail.com]

---
Desenvolvido com ❤️ por Maxwell
