# Distribuições

Para subir o pacote, criar uma distribuição binária ou distribuição de código fonte.
As versões mais recentes do pip instalam primeiramente a binária e usam a distribuição de código fonte, apenas se necessário.
De qualquer forma, iremos criar ambas distribuições.

## Passos para gerar as distribuições
1. Acessar a raiz do projeto;
2. Comando de instalação;
3. Comando para a distribuição.

## Comandos de instalação
```
	python -m pip install --upgrade pip

```

``` 
	python -m pip install --user twine

```

``` 
	python -m pip install --user setuptools

```

## Comandos para criar distribuições

``` 
	python setup.py sdist bdist_wheel
	
```

