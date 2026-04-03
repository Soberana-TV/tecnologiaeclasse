# Anthropic libera o código do Claude Code... sem querer

Isso não é uma piada de primeiro de Abril. A Anthropic, responsável pelo Claude Code vazou acidentalmente todo o código da ferramenta... de novo. Vamos falar sobre o que isso significa.

- O Claude Code é um assistente de programação que roda direto no terminal. Ela edita arquivos, executa comandos, gerencia git, faz tudo que um dev faria, só que com um modelo de IA. É o que a Anthropic chama do seu 'molho secreto', embora existam ferramentas dos concorrentes como o Codex da OpenAI e diversas alternativas abertas
- Importante entender que o 'Claude Code' não é o LLM desenvolvido pela Anthropic, ele é o que geralmente nós chamamos de 'harness' (arreios / sela).
  - Uma ferramenta que deixa o modelo 'nos trilhos' de um comportamento específico
  - Provê contexto e dados que serão úteis para essa tarefa
  - Provê acesso a ferramentas fora do modelo que podem ajudar nessa tarefa

- Esse é o 'molho' da Anthropic e foi isso que vazou. Vocês já devem estar vendo o código por aí... tem uma chance de 50% que o código esteja no meu HD aqui agora.

::: warn
**Aviso Legal**

Não hospedem os forks desse código no seu github. Não deem motivos para advogados do vale do silício testarem novas doutrinas legais com vocês

:::

::: error
**Aviso de Segurança**

Não rode o código do Claude Code localmente se não sabe o que está fazendo.

Podem existir versões maliciosas do código por aí, mas também o código original tem dependências internas às quais não temos acesso nos repositórios.

Quando você rodar `npm install` já vai estar baixando pacotes diferentes que foram `squatted` por atores maliciosos

:::

::: success
**Aviso de amigo**

Se inscreva no canal, deixe like, deixa hype, apoiase, pix, pega um cafézinho e vamos falar mais sobre essa situação

:::

- No dia 31 de março de 2026, a Anthropic subiu pro npm o Claude Code versão 2.1.88. Só que junto com o pacote, foi também um **source map** de 59,8 MB chamado `cli.js.map`
- Source map é um arquivo de debug que mapeia código minificado de volta pro código original. Serve pra desenvolvedor debugar erros em produção, mesmo com o código minificado e obfuscado.
  - Isso não deveria ter ido parar lá, duuuh

<https://xcancel.com/Fried_rice/status/2038894956459290963>

- Foi erro humano? Foi um erro dos agentes de IA? Foi um bug do Bun? Não sabemos ao certo, a Anthropic disse que foi um erro humano (estão protegendo o produto deles). Mas isso aqui foi engraçado:

<https://github.com/oven-sh/bun/issues/28001>

- Não é a primeira vez que isso acontece com a Anthropic. Em fevereiro de 2025, um early version do Claude Code já tinha vazado do mesmo jeito
- Na época eles tiraram do ar, apagaram, mandaram DMCA pra deus e o mundo e prometeram que não ia acontecer de novo. Pois, estamos aqui de novo ...

- O que foi vazado é um total de aproximadamente 500 mil linhas de código contendo alguns segredos de negócio, os prompts e skills internos, medidas de segurança e o código no geral, comentários e nomes de variáveis e tudo mais.

- O primeiro repositório a fazer um 'mirror' do código ganhou 60k estrelas no Github em poucas horas, se tornando o repositório mais rápido a chegar nesse ponto de todos os tempos.

- A Anthropic passou o dia 01/04 mandando DMCAs e tentando tirar os repositórios do ar, mas parece que agora resolveu parar com a estratégia.

- Outra coisa que começou a acontecer foram as reescritas 'clean room' do código. Traduções por LLM do código para outras linguagens. Não é divertido quando fazem com vocês né gurizada?

- A última coisa que temos que pensar é... será que foi uma grande jogada de marketing? Até agora eu acho que não, o que nós encontramos no código me sugere isso.

- Então agora vamos para a parte interessante, falar sobre coisas que chamam atenção dentro do código. Esse chinês aqui fez um relatório gigante estudando, mas eu vou falar de algumas coisas que chamaram mais atenção:

<https://github.com/ComeOnOliver/claude-code-analysis>

- **BUDDY**:  um sistema de bichinho virtual tipo Tamagotchi que aparece na interface  do Claude Code. Tem 18 espécies - pato, dragão, axolote, capivara,  cogumelo, até fantasma. Cada bichinho tem raridade, atributos (debug,  paciência, caos, sabedoria, sarcasmo), nome e personalidade gerados na  primeira vez que você usa. Teria sido lançado pro 01/04.
- **KAIROS**: um "Claude sempre ativo". Funciona em segundo plano, guarda memória em pastas privadas, literalmente sonha, reorganizando informações durante a madrugada, e pode iniciar tarefas sozinho sem esperar comando do usuário. É uma forma de  agente autônomo que roda 24/7 no seu computador.
- **ULTRAPLAN**: planejamento remoto em nuvem, com um Claude coordenando vários agentes de IA ao mesmo tempo.
- **Undercover Mode**:  o modo "à paisana". Quando o Claude Code contribui com código em  repositórios open source, ele recebe instrução explícita no system  prompt pra **não revelar que é IA**.  Nada de "Co-Authored-By: AI" nos commits. Nada de mencionar Anthropic.
  - Não preciso dizer que isso é paia. É mentir de propósito pra passar  despercebido em projetos que, muitas vezes, explicitamente vetam contribuição automatizada de IA.
  - Anthropic porque você tem vergonha do seu filho?
- **Medidas antidestilação:** Se  detecta que alguém tá fazendo scraping das respostas pra treinar um  concorrente, o Claude Code injeta definições falsas de ferramentas nas requisições da API, contaminando o dataset do adversário.
  - O vazamento do código agora ajuda muito quem está construindo modelos destilados :)

- Também chamou atenção que o código todo foi escrito usando IA (isso já se sabia) e algumas gambiarras e padrões de qualidade de código
  - Eu vou defender eles nesse sentido: só quem trabalha com desenvolvimento em projetos tão grandes assim sabe o espagueti que fica.
  - É um trauma compartilhado da comunidade dev. Sabemos que criamos monstros, mas é rir pra não chorar

- Exemplos disso abundam pela internet, mas um dos mas engraçados pra mim:
  - os termos ofensivos hardcoded pra impedir a geração de ids, por exemplo 'cum' e 'shit'
  - uma expressão regular que procura palavras de frustração como 'shit', 'fuck' e 'damn' para marcar aquela conversa como 'frustrante' para o usuário

<https://neuromatch.social/@jonny/116324676116121930>

- Outras coisas interessantes:
  - Agora todas falhas de segurança da Anthropic são open source
  - bugs na cache e maneiras de gerenciar o contexto criavam sessões mais caras do que o necessário

### Conclusões

- "o problema da programação já está resolvido". Só que fazer um projeto lôngevo e de sucesso com essas ferramentas, não.
- Eu não sei quantas vezes eu tenho que repetir e ficar lendo comentário de: "eu fiz um sistema em 1 mês que demoraria um ano, com uma equipe de 3 pessoas usando IA"

- O ritmo que a gente está desenvolvendo tecnologia em 2026 é uma máquina de bugs, exploits e dívida técnica. O momento da colheita está chegando.

- E eu entendo que é 'impossível' parar isso. O Zézinho da esquina vai continuar fazendo o seu SaaS com IA, você vai continuar tendo que entregar código cada vez mais rápido, o coach de IA continua lá vendendo curso do último hype e a gente vai continuar nesse ritmo por um tempo.

- Quanto à Anthropic. O código já tá por aí. Os concorrentes já estão copiando, os chineses já estão destilando. E a gente fica aqui só olhando e dizendo: "que legal, como shippa rápido esses produtos da Anthropic!" kkkkkk

- Será que isso interfere na valorazação da empresa? Nos lançamentos futuros de modelos ou da ferramenta? No IPO? Será que eles vão resolver lançar a ferramenta como open source a aproveitarem o marketing de graça? Sei lá :)
