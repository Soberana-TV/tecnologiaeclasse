# A otimização de busca de IA no dia a dia

Faz alguns dias nós fizemos um vídeo sobre o ‘ai search optimization’, como influenciar as buscas de IA DOS OUTROS. Hoje eu quero trazer 3 exemplos dessa prática acontecendo na política.

**Veja no canal:**
{{#embed https://www.youtube.com/watch?v=3l9yBpWYtLM}}

- ChatGPT estava recomendando vote em candidatos, contratiando as regras do TSE 

[https://www.instagram.com/p/DcUAu17Dopy/](https://www.instagram.com/p/DcUAu17Dopy/ (preview))

[https://www.uol.com.br/tilt/colunas/diogo-cortiz/2026/08/21/chatgpt-escorrega-na-regra-do-tse-e-tem-candidato-preferido-a-presidencia.htm](https://www.uol.com.br/tilt/colunas/diogo-cortiz/2026/08/21/chatgpt-escorrega-na-regra-do-tse-e-tem-candidato-preferido-a-presidencia.htm (preview))

[https://www.reuters.com/world/americas/brazil-races-rein-ai-weeks-before-election-2026-09-01](https://www.reuters.com/world/americas/brazil-races-rein-ai-weeks-before-election-2026-09-01 (preview))

- Como os modelos de linguagem / agentes de IA poderiam TENTAR evitar isso?
  - Sistema intermediários que verificam os resultados / raciocínio e tentam identificar violações da lei eleitoral
  - Eu chuto que se a gente quisesse muito dava pra conseguir fazer ele recomendar ainda

[https://www.instagram.com/p/DcTtuYlIke5/](https://www.instagram.com/p/DcTtuYlIke5/ (preview))

https://diplomatique.org.br/ia-do-google-usa-o-le-monde-diplomatique-brasil-como-fonte-da-fake-news-de-que-maduro-nunca-foi-capturado/

- Como isso funciona? Afinal a IA só repete o que está no treinamento dela, certo?

- Não, por favor se voltem a esse vídeo aqui:

{{#embed https://www.youtube.com/watch?v=KuKwbWmr5M8 }}

- Modelos de linguagem são ferramentas de completar a próxima palavra de um texto. Uma aplicação comum é a construção de textos a partir de outros iniciais para criar uma espécie de sistema de busca e conhecimento.
  - As vezes chamado de RAG (Retrieval Augumented Generation), mas cada vez mais é simplesmente o contexto da conversa com esses modelos

- Em resumo, é o que vocês já conhecem, o modelo vai conversar com vocês baseado num conjunto de textos que vão ser dados previamente, mas não são parte do treinamento do modelo. 

- Isso quer dizer que a reposta que chega pra gente tem diferentes camadas:
  - A base de treinamento do modelo (o que foi “treinado”)
  - As conexões probabilísticas que foram feitas entre essas palavras, feito para “alinhar o modelo” (o que foi “refinado” e “reforçado”)
  - O prompt inicial e o contexto da “conversa com o modelo”
  - Alguma ferramenta ou passo intermediário da conversa (“essa reposta tem o problema X e Y, refaça”)

- Então nesses dois casos acima algumas hipóteses:
  - O modelo recomenda candidatos baseado numa análise “tecnocrática” dos seus planos de governo, notícias e textos que encontra no seu treinamento e buscas. Com todos os viéses do modelo, mais os textos e mais infinitas camadas. Difícil de entender, mas o resultado é o esperado.
  - Algo no pré prompt do Gemini ou num passo intermediário estava marcando aquele artigo como falso e gerando aquela reposta bizarra.
  - Manipulação? As empresas não se posicionaram explicitamente sobre os casos, mas eu sempre lembro disso aqui:

[https://www.cubaheadlines.com/articles/310539](https://www.cubaheadlines.com/articles/310539 (preview))

- Agora que a gente sabe dessas “técnicas”. A última história que eu quero mostrar aqui pra vocês é como Israel está gastando mais de U$ 100mi pra se aproveitar exatamente disso:

[https://www.dropsitenews.com/p/fd107677-6cf9-4ece-9e45-de16bbde8b4a?postPreview=free](https://www.dropsitenews.com/p/fd107677-6cf9-4ece-9e45-de16bbde8b4a?postPreview=free (preview))

- Em resumo:
  - Sites com desinformação mascarada de “pontos e contrapontos” criados em massa e que efetivamente influenciam resultados de mecanismos de busca com IA
  - Esses artigos primeiro atuam como “ai search optimization”, mas eventualmente eles aparecem nos conjuntos de treinamento
  - Isso tudo feito pela empresa de Brad Parscale que foi responsável pela primeira campanha do Trump e envolvido no escândalo da Cambridge Analytica
  - Pesquisas de opinião mostram que isso cria um efeito rebote e pessoas que percebem isso tendem a ficar com uma visão ainda mais negativa de Israel… o que é bom
  - Porém julgando pelos comentários que eu vejo aqui no youtube… realmente em algum nível funciona

- Quando nós avisamos sobre os perigos de depender de ferramentas de IA nós estamos falando desse tipo de coisa, decisões e crenças baseadas numa saída desses modelos devem ser tratadas com MUITO CUIDADO

- Deixa eu falar de um jeito que os fãs de IA vão entender: não é ludismo nem medo da tecnologia, é responsabilidade com a verdade e o consumo críticos de informações

- Mas agora vocês pegaram o pulo do gato e se vocês entendem um pouco melhor como essas ferramentas funcionam eu fico feliz. vlw!
