# Finance Dashboard — receita e despesa fictícias

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51.0-FF4B4B?logo=streamlit&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.3.3-150458?logo=pandas&logoColor=white)

Painel Streamlit com seis meses de receita e despesa escritos direto em `app.py`. A barra lateral filtra os meses; a página soma receita, despesa e saldo e plota as duas séries. Não lê arquivo, banco nem API. Não é análise financeira.

## Stack

- Python 3.10, fixado no workflow
- Streamlit 1.51.0 e pandas 2.3.3, usados na página
- NumPy 2.3.4 está no `requirements.txt` e não é importado
- gráfico via `st.line_chart`

## Estrutura

```
.
├── app.py                                # dados fixos, filtro e métricas
├── requirements.txt                       # streamlit, pandas, numpy
└── .github/workflows/python-app.yml      # Python 3.10, flake8 e pytest
```

Os meses são Jan–Jun. Receita: 5000, 6200, 5800, 7100, 6500, 8000. Despesas: 3000, 3200, 3100, 3500, 3400, 4000. Sem mês selecionado, a página só mostra o aviso.

## Como rodar

```bash
git clone https://github.com/gabrielteramae/finance-dashboard.git
cd finance-dashboard
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Testes realizados

Não há arquivo de teste. O workflow chama `pytest` depois do flake8, então essa etapa falha enquanto não existir suíte (pytest encerra com código 5 quando não coleta nada).

---

© 2026 Gabriel Teramae Chan
