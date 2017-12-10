# **botfalardepython**

Bot do [grupo](https://t.me/BoraFalarDePython) bora falar de python.

# Como ajudar a desenvolver

### Passos a seguir

1. crie um diretório para o projeto
2. mude para o novo diretório criado
3. no diretório criado, crie um virtualenv para o projeto
4. ative o virtualenv
5. inicie o git no diretório do projeto
6. adicione o repositório remoto
7. faça um pull para baixar os arquivos
8. instale os requisitos
9. crie um bot no botfather do Telegram
10. vejas as issues existentes e eleja uma para trabalhar

### Os passos de 1 a 8 podem seguir os comandos abaixo. (Linux ou MacOS)

```commandline
md botborafalar
cd botborafalar
python3 -m venv .venv
source .venv/bin/activate
git init
git remote add origin https://github.com/jlugao/botfalardepython.git
git pull origin master
pip install -r requirements-dev.txt
```

# Features:

* Até quinta feira as 12:00 pode inscrever temas após esse período
* Abre pra votação até as 20:30
* Toda semana zera a votação
* Fica registrado um histórico de lives
* Lembrete de votação agendado
* Um voto por usuário apenas
* Lista de votação

# Comandos 

## **/add**
```
/add <nome-da-live>
```
   * #### Exemplo:
```
/add Live de testes
```
   * #### Retorna:
```
Live de testes adicionada para votação
```

## **/list**
```
/list
```
   * #### Retorna:
```
3 - Live de testes - @jlugao - votos: 5
2 - bot do grupo - @user1 - votos:2
4 - live sobre wagtail - @user2 votos: 1
1 - live sobre programação funcional - @user2 votos: 0
```

## **/vote**
```
/vote <id-da-live>
```
   * #### Exemplo:
```
/vote 1
```
   * #### Retorna:
```
@fulano votou na live "live sobre programação funcional"
```

## **/history**
```
/history
```
   * #### Retorna:
```
26/08/2017 - Live sobre programação funcional - https://youtu.be/21321344231
```
