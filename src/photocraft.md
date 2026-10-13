# Artcraft, decompilação, recompilação e engenharia reversa com LLMs

As comunidades de hacking, engenharia reversa, emulação e retrogaming estão completamente eufóricas nos últimos meses com as possibilidades de usar LLMs para acelerar o seu trabalho. Hoje vamos comentar sobre

- Este desenvolvedor finalmente coringou com a Adobe e resolveu “vibecodar” uma cópia das ferramentas da suite Adobe em Rust e disponibilizar elas como software aberto

[https://getartcraft.com/apps](https://getartcraft.com/apps (preview))

- Ninguém odeia mais a Adobe do que os próprios usuários da Adobe. E faz duas semanas (exatamente 01/10/26) que a comunidade está em polvorosa com esse projeto.

- Em teoria, com uma versão aberta e gratuita das ferramentas Adobe designers podem simplesmente trabalhar num computador local sem conexão à internet e sem mensalidades (ou taxas de cancelamento) 

- Como isso foi possível? Nós temos algumas hipóteses, porém a descrição do processo foi “vibecoded”
  - Será que ele usou uma especificação de cada funcionalidade para reimplementar?
  - Uma análise do código binário?
  - Acesso ao código do Photoshop original (pode ter algo nas LLMs) ou um reaproveitamento de código aberto dos clones de produtos da Adobe?

- Cada uma dessas hipóteses vai lidar com diferentes consequências legais…

[https://www.heise.de/en/news/Open-Source-Guru-Raymond-AI-Ends-Closed-Source-Software-11480690.html](https://www.heise.de/en/news/Open-Source-Guru-Raymond-AI-Ends-Closed-Source-Software-11480690.html (preview))

- E nós já temos alguns anúncios do fim do software proprietário, como por exemplo o Eric S. Raymond

### Mas os programas funcionam mesmo?

[https://au.lifehacker.com/software/119843/i-tried-photocraft-the-ai-clone-of-photoshop-and-its-almost-exactly-like-the-real-thing](https://au.lifehacker.com/software/119843/i-tried-photocraft-the-ai-clone-of-photoshop-and-its-almost-exactly-like-the-real-thing (preview))

- O consenso parece ser “mais ou menos”, eu pedi pro meu editor de thumbs testar e ele imediatamente não conseguiu fazer funcionar algumas coisas que ele usa todo dia
  - Mas todo mundo dizendo: “olha tá 90% ali”

- Eu não pude deixar de pensar nessa frase:

> The first 90 percent of the code accounts for the first 90 percent of the development time. The remaining 10 percent of the code accounts for the other 90 percent of the development time.

Tom Cargill, Bell Labs

### As recompilações / decompilações + a mistureba

{{#embed https://www.youtube.com/watch?v=mYZPHdKKMaI }}

- Já faz algum tempo que a moda na comunidade de retro gaming / emulação são as recompilação / descompilações dos jogos:
  - Emulação: simular o processador e o hardware de um videogame num ambiente virtual para rodar exatamente o mesmo código do jogo em uma arquitetura de hardware diferente. Ex.: ZSNES + uma rom de Super Mario World
  - Descompilação: engenharia reversa do código binário de um jogo que gera um código em linguagem de alto nível e documentada, mas que compila de volta para o exato mesmo código binário. Ex.: descompilação do SSMB https://decomp.dev/doldecomp/melee
  - Recompilação: uma reimplementação da mesma lógica do jogo de uma maneira independente e que compila para outra arquitetura computador e frequentemente inclui melhorias. Basicamente um ‘port’ nativo. Ex.: A recompilação do Bloodborne para PC https://github.com/Supermedo/bloodborne_pc 
- Todos esses tipos de coisas se confundem entre si e compartilham códigos e técnicas. Muitas vezes um decomp é a base para um recomp e/ou são o mesmo projeto e/ou misturam os nomes e conceitos. O importante é tentar entender MAIS OU MENOS o que tá rolando

[https://knowyourmeme.com/memes/cultures/ai-video-game-merging](https://knowyourmeme.com/memes/cultures/ai-video-game-merging (preview))

- E isso tudo leva à tendência de pessoas misturando código e mods desses diferentes projetos para criar mashups entre diferentes jogos e postar um videozinho no X pra ganhar pontos de internet com a sua comunidade

- O ponto principal aqui é que esse é o cenário perfeito para o uso de LLMs de código e sistemas de agente:
  - Um ambiente de escopo bem definido (engines de jogos, engines gráficas, física, som e etc…)
  - Material open source abundante (jogos, demos, emuladores, código em geral)
  - Uma especificação em texto (o próprio código binário) e uma especificação de testes (o comportamento do jogo original) 

- Esse é o tipo de problema que pode literalmente ser resolvido com algumas centenas de milhares de dólares e uma assinatura de IA

### Isso tudo é legal?

- Eu acho super legal, mas do ponto de vista da lei isso é um DEPENDE gigante…

- A minha opinião sobre o que as LLMs são não mudou, elas literalmente são o aglomerado de trabalho criativo, direitos autorais, artes, textos e etc… de milhões de pessoas sendo regurgitados 

- O que é especialmente interessante agora é que essa violação de direitos autorais tem acontecido contra empresas bilionárias e que todos nós odiamos e isso é belo e moral
  - O contrário não é belo e moral e essa é uma posição 100% congruente da minha parte

- As repercussões legais, no momento, não estão conseguindo correr rápido o suficiente para dar conta da velocidade que esses projetos estão sendo criados
  - Um decomp do SSBM que demoraria anos pra fazer tem que valer muito a pena, por isso ninguém vai botar muito esforço no decomp de Chameleon Twist 2 sabendo que eventualmente a Nintendo pode vir arruinar a tua vida igual.
  - Com um LLM é só ter tempo e dinheiro

- Como se já não bastasse agora temos projetos que são feitos exatamente para facilitar esse processo:

[https://rea.tools/](https://rea.tools/ (preview))

- Nós ainda não entendemos as repercussões legais disso e isso pode obrigar os tribunais lá na gringolandia a finalmente levarem a sério a questão porque agora é IA vs Bigtech… será?

### Mas isso é bom mesmo ou tem uma pegadinha?

- Eu não gosto de ser o chatão e botar defeito numa coisa que tem tanta gente animada, mas aqui vão alguns pontos negativos:
  - Hoje isso me parece um pesadelo de segurança, tanto por termos milhares de entusiastas rodando código vibecodado e aleatório da internet quanto pelas possibilidades de engenharia de todos sistemas que usamos
  - Isso pode ensejar a criação de bloqueios de software na nuvem e patentes mais agressivos ainda
  - A dependência nesse tipo de prática ao invés da criação de um ecossistema aberto pode nos deixar ainda mais na mão dos modelos proprietários de IA. Será que isso é um psyop do Jensen Huang, Sam Altman e Dario Amodei?

- Qualidade de software, software livre, aprendizado, comunidade, reuso de código é importante e pra uma coisa assim dar bons frutos a comunidade precisa ser direcionada por pessoas que se preocupem com isso:
  - Esses projetos precisam de um controle de qualidade, reuso de componentes, precisam funcionar em ambientes sem acesso a LLMs (ou LLMs poderosos)
  - É preciso fomentar o aprendizado, o software livre e o senso de comunidade mesmo que essas ferramentas façam parecer que não precisamos
  - As comunidades tem que encontrar maneiras de se proteger legalmente e de maneira prática dos ataques que irão aparecer baseado nisso

- Eu queria MUITO que isso fosse o fim do código fechado, a falência da Adobe e a criação de um ecossistema de video games gratuitos e abertos. Mas…
  - Ainda vivemos num sistema que depende do nosso trabalho pra botar comida na mesa
  - Essas empresas e bilionários ainda tem o poder pra dispor sobre o nosso trabalho
  - O nosso acesso “quase gratuito” a esses modelos e ao hardware não está garantido

- Por isso ainda não estamos no paraíso do software livre, mas fica cada vez mais claro o que está nos impedindo de chegar lá.

### Recomendação de vídeo

{{#embed https://www.youtube.com/watch?v=VBhtzgXMdtM}}
