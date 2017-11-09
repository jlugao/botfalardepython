# **botfalardepython**

Bot do [grupo](https://t.me/BoraFalarDePython) bora falar de python.

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