# Marcas d’água em texto de IA

A União Europeia quer que textos gerados por IA, em alguns casos, recebam uma marca d’agua que permite sua identificação. A Anthropic entregou e hoje nós vamos falar sobre.

[https://arstechnica.com/tech-policy/2026/08/claudes-new-scarlet-letter-watermark-is-invisible-for-now/](https://arstechnica.com/tech-policy/2026/08/claudes-new-scarlet-letter-watermark-is-invisible-for-now/ (preview))

![image.png](./anthropic_watermark/image.jpg)

- “Agora todo o texto satânico que vocês escreverem com esses LLMs carregará a marca da IA generativa: a marca da bosta”

- Eu imagino que parte do público acha que eu vou focar em falar mal de laboratório de IA e big tech, sempre saudável, mas no geral eu vou abrir o vídeo dizendo que isso não é uma ideia horrível.
  - Pra achar isso 100% horrível só se você é uma pessoa que depende de enganar os outros com texto de IA

- Porém existem muitas pegadinhas nessa questão, então o foco aqui vai ser entender como isso funciona e explorar as consequências de algo assim

- Anúncio da Anthropic:

[https://support.claude.com/pt/articles/16266773-como-claude-marca-conteudo-gerado-por-ia](https://support.claude.com/pt/articles/16266773-como-claude-marca-conteudo-gerado-por-ia (preview))

- Outras empresas de IA devem anunciar a mesma coisa nos próximos dias também e já existem outras técnicas como o C2PA e SynthID
  - Nesse artigo a OpenAI por exemplo indica que logo irá seguir a Anthropic https://openai.com/index/advancing-content-provenance/

### Mas como funciona?

- Modelos de geração de texto são um processo estatístico de escolha da próxima palavra.
- Grande parte das vezes uma palavra é mais provável de ocupar aquele próximo “espaço”, mas existem outras tão prováveis ou quase tão prováveis quanto

- Geralmente modelos permitem o ajuste da ‘temperatura’ que adiciona uma maior aleatoriedade a essa escolha e é percebido como uma maior ‘criatividade’ nas respostas, ao mesmo tempo que as deixa menos previsíveis e potencialmente mais longe das ideais (de acordo com o modelo)

{{#embed https://www.youtube.com/watch?v=iz9TbUdf8MQ }}

- Técnicas normais de detecção trabalham com a inserção de padrões ou caracteres que marcam o texto como sendo gerado por IA, porém isso é facilmente detectável e removível

- A ideia dessa marcação de texto da Anthropic é mudar a estatística de seleção das palavras, da mesma maneira que a temperatura já faz aleatoriamente, mas fazê-lo de maneira estatísticamente significativa usando uma chave inicial de geração

- Dessa forma para quem conhece o modelo e essa chave inicial, seria possível analisar a frequência das palavras para dizer de maneira acurada que uma IA gerou o texto

- Sim, isso quer dizer que a gente não sabe ao certo no que esse texto difere do “ideal” e nem é possível detectar ou derrotar essa marcação se não temos informação sobre a geração inicial do texto\*
  - O asterisco aqui é por que a gente sempre acha uma maneira de burlar, mas na teoria não deveria ser possível

### E existe algum problema com isso?

- Existem muitas coisas boas que vem com a habilidade de marcar textos gerados por IA, mas isso não seria um vídeo do TeClas se a gente não problematizasse um pouco…

- Esse tipo de técnica, principalmente a maneira que a Anthropic vai fazer, deixa LLMs mais inúteis ainda para trabalho de precisão onde as palavras e seu posicionamento realmente importam
  - Correção de gramática, formatação de textos, edições simples sem mudar o sentido de uma frase
  - Código também? Imagino que os comentários e nome de variáveis vão acabar sendo os mais afetados
  - O grande \* aqui é que para a maioria desses casos de uso LLMs já tem esse problema

### Pontos pra discutir:

- Ferramentas de detecção de texto de IA já existem… e no geral são basicamente um caô. Até onde me consta elas simplesmente não funcionam e temos vários casos onde os seus falsos positivos são danosos

- Existe na implementação da Anthropic e na exigência da União Europeia uma desconexão importante:
  - “Só é necessário uma watermark em textos que informam sobre o interesse público”, “Não é necessário uma watermark se foi feito uma revisão humana”
  - Isso simplesmente não dá pra fazer (ou é 1000x difícil)
  - “Não inclua a marca d’água pois eu irei revisar o texto”

- Só que ao mesmo tempo é uma boa desculpa da Anthropic (pode botar outros labs de IA aqui tb) para merdificar as suas respostas com o respaldo legal e ganhar os benefícios do texto identificado aos seus modelos
  - Não treinar modelos posteriores com conteúdo com marca d’água
  - Captura regulatória e exigências de marca d’água para competidores (modelos abertos!) 
  - Necessidade de terceiros acessarem a sua ferramenta de detecção de IA
  - …potencial exigencia de autoria ou licensiamento de textos detectados como sendo “escritos por IA”

- Algumas dessas coisas estão mais na ordem do dia do que as outras, mas é sempre necessário lembrar que a Anthropic e todos os laboratórios de IA são ferramentas do imperialismo estadunidense
  - Em primeiro lugar eles tão de olho nesse IPO, depois em agradar o Trump e muito lá depois no que é bom pra “humanidade”

- Eu sou muito a favor de regulamentar as ferramentas de IA, mas quem sabe a União Europeia não pega uma grana e começa a rodar modelos abertos e soberanos ao invés de pedir migalhas pros lacaios do mega hitler laranja?
  - As vezes dá uma preguiça…

- Só que pra concluir, isso não é ruim necessariamente e é uma decorrência natural do que vem acontecendo com IA:
  - Mas como tudo no canal TeClas, tem um DEPENDE gigante aí
