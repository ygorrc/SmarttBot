# SmarttBot
 
 ## Instalação
 
 - Requisitos: Docker, docker-compose
 - Para executar:
   - `docker-compose up`.
   - `docker-compose exec backend sh`.
   - `python manage.py migrate`.
   
 ## Descrição do Desafio`
Dados os preços de execução (cotações) de uma criptomoeda reportados em tempo real
através de uma API pública, você deve criar um sistema que irá processar estas cotações,
agregá-las em candlesticks (com os dados de abertura, máxima, mínima e fechamento - saiba
mais nesse link ) e salvar estes candles em um banco de dados.
Você deve construir os candles de 1min, 5min e 10min. Os candles só precisam ser salvos no
banco de dados uma vez que estejam completos (não precisam ser atualizados no banco de
dados em tempo real). Por exemplo, a cada um minuto, o sistema irá salvar no banco de dados
o último candle de 1min finalizado.
A API a ser consumida é obrigatoriamente a Poloniex Public API (mais especificamente o
comando returnTicker ou o canal websocket Ticker Data ). Assim, não utilize clientes de
terceiros para consumir a API Poloniex, pois invalidará o seu teste. Você deverá desenvolver o
seu próprio cliente.
 
 ## App
 
 A aplicação backend está dividida duas seções principais: SmartBot e candles, Abaixo é mostrado uma breve introdução do funcionamento de cada.
 
 ### SmarttBot
 
A parte mais importante desta seção foi as chamadas das tarefas assicronas que estão no arquivo setings.py, onde são realizadas a cada 1 min, 5min ,10min de acordo com a tarefa assicrona que são realizadas na seção Candles

### Candles

Foi dividido em varias partes importantes

- model.py: onde foi feita a tabela candle do banco de dados 
- tasks.py: onde está sendo feito maior parte do projeto, esta parte è:
  - 3 tasks que cada uma corresponde a um candle(1 min, 5 min, 10 min), onde faz a chamada da api poloniex(cada chamada é realiazada a cada 1 s, na doc da api fala que o limite são 6 chamadas por segundos mais opitei por 1 por segundo). Depois de todo procesamento as informações são salvas no banco de dados).
 
 
 
 ## Ferramentas e Tecnologias utilizadas
 
 - django
 - redis
 - flower
 - mysql
 - celery
 - celery-beat
 - poloniex
 
 ## Versionamento do codigo
 
 Não cheguei usar o git , pois uso um proprio visionamento no meu pc.
 
 ## Programação web
 
 Utilizei o framework django com a linguagem de programação python para fazer o backend, e o front não cheguei a mexer muito por este motivo não esta funcionando a parte do frontend. Mas cheguei a fazer os view para futura implementação do frontend.
 
 ## Programação Banco de dados
 
 Foi utilizado o mysql que foi gerenciado pelo django
 
 ## Docker
 
 O docker permitiu a criação de uma aplicação multi-container que separou o projeto em 6 partes:
 
 - A primeira parte foi o django que é a propria aplicação.
 - A segunda parte foi o mysql que é o banco de dados.
 - A terceira parte foi o redis que é o agente de mensagens.
 - A quarta parte foi o celery que é o que realiza as tarefas assicronas.
 - A quinta parte foi o celery-beat que automatiza as tarefas assicronas.
 - A sexta parte foi o flower que gerencia e monitora as tarefas assicronas.
 
 ## Desafios e Dificuldades
 
 Primeiro desafio que eu encontrei foi que sempre implementei backend nos frameworks Spring na liguagem programação java e Nodejs na linguagem de programação JavaScript, então o framework django foi tudo novo para mim.
 
 Segundo desafio foi achar uma maneira de executar as tarefas assicronas e automaticas, que são os candles. Depois de pesquisar muito sobre isto achei o framework celery junto com a automatização dele, que foi feito pelo celery-beat. Ainda tinha o framework redis que trabalha com as trocas de mensagens.
 
 Terceiro desafio foi as versões de cada um,pois como tinha muito framework sempre dava conflito. Então isto gastei muito tempo vendo qual versão era compativel com todos.
 
 Ultimo desafio foi o flower, que monitora e gerencia cluster do aipo. Esta parte não consegui debugar ainda , espero que mais para frente eu consiga
 
 ## Melhorias
 
 Consegui fazer o que foi pedido em partes, pois não fiz a parte dos teste. Então é uma parte que está faltando e futuramente irei fazer.

Uma coisa acho bem importante e estarei desenvolvendo é a parte do frontend.
 
 
 
 
