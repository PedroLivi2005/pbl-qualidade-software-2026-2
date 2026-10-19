# Projeto do aluno - Aula 11

## 1. Preparar o ambiente

Confira o Python:

```bash
python --version
```

Instale as dependencias:

```bash
python -m pip install -r requirements.txt
```

Confira o pytest:

```bash
python -m pytest --version
```

Execute a suite:

```bash
python -m pytest -q
```

## 2. Exercicio formativo

Implemente, usando TDD:

```python
calcular_total_com_desconto(itens, percentual_desconto)
```

Regras:

1. calcular o total dos itens;
2. aplicar desconto entre 0 e 30 por cento;
3. desconto menor que 0 deve gerar `ValueError`;
4. desconto maior que 30 deve gerar `ValueError`;
5. lista vazia deve retornar zero;
6. todos os testes anteriores devem continuar aprovados.

## 3. Cenários mínimos

- total 100 e desconto 10 por cento: resultado 90;
- total 100 e desconto zero: resultado 100;
- total 100 e desconto 30 por cento: resultado 70;
- desconto 31 por cento: `ValueError`;
- lista vazia: resultado zero.

## 4. Processo esperado

Para cada comportamento:

1. escreva o teste;
2. execute e confirme a falha (Red);
3. implemente o mínimo necessário (Green);
4. execute toda a suíte;
5. melhore a estrutura sem alterar o comportamento (Refactor);
6. execute toda a suíte novamente.

## 5. Registro do ciclo

Use o arquivo `REGISTRO_TDD.md`.

## Observacao sobre venv

Na proxima aula sera utilizado `venv`, um ambiente virtual isolado que mantem os pacotes do projeto separados dos demais projetos Python.
