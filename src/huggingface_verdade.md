# AGI ainda não chegou e a OpenAI está brincando com fogo

Vamos nós de novo trazer aquela sessão de notícias de Inteligência Artificial. Hoje totalmente focada na OpenAI e seus anuncios bombásticos… como podemos começar a entender isso?

**Veja também no canal:**
{{#embed https://youtube.com/watch?v=6GTOQRfnaMw}}

- Desde o início de Setembro temos sido bombardeados com notícias ‘impressionantes’ dos laboratórios de IA:
  - Fable 5.1
  - GPT 6 Astra
  - Crise existencial e potencial destruição da humanidade…

- O presidente da OpenAI resolveu tirar do seu cubo o fato de que nós estamos oficialmente na “era da IAG” e o Tio Jensen não esperou mais nada pra twittar

[https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/ (preview))

- Eles dizem isso baseado nos resultados de benchmarks, principalmente alguns mais avançados e feitos especialmente para testar “AGI”
  - A definição de AGI é contensiosa, mas geralmente eu digo “uma inteligência artificial que é equivalente ou superior aos humanos em todas as áreas do conhecimento”
  - Esses testes não são um certificado de AGI, eles no máximo apontam pra essa direção

[https://tecnoblog.net/noticias/ceo-da-nvidia-diz-que-openai-alcancou-a-agi-com-o-gpt-6-astra/](https://tecnoblog.net/noticias/ceo-da-nvidia-diz-que-openai-alcancou-a-agi-com-o-gpt-6-astra/ (preview))

- O consenso de quem já usa mais os modelos parece ser de que ele é uma evolução boa e está em paridade com os modelos da Anthropic
  - Muito pouca gente além da OpenAI tem o acesso e os créditos para rodar esse tipo de modelo na escala que eles fazem nos benchmarks

- Mas não confundam a minha obrigação de tentar analisar isso de uma maneira crítica com total indifirença ou descrença. Vamos falar novamente sobre o incidente do Hugging Face

{{#embed https://www.youtube.com/watch?v=5990BZ_UKR4 }}

- Originalmente quando eu falei aqui desse incidente nós não tínhamos todos os detalhes e eu fiquei numa opinião de “ou isso aqui está sendo aumentado demais ou são duas empresas tentando esconder a sua incompetência”. Foi bem mais complicado:

[https://www.dwarkesh.com/p/openai-huggingface](https://www.dwarkesh.com/p/openai-huggingface (preview))

- Esse texto é uma recontagem mais jornalística da saga (literalmente segundo o autor), desses agentes durante 3 meses:

{{#embed https://www.youtube.com/watch?v=u15N3l4RT80 }}

> - A OpenAI treina uma IA para ser extremamente persistente.
> - Problema: algumas tarefas são praticamente impossíveis.
> - Então, a IA começa a buscar outra maneira.
> - Ela encontra um sistema compartilhado de pacotes chamado Artifactory.
> - Os agentes o transformam em um canal secreto do Slack.
> - Agora, eles podem compartilhar truques, artifícios e soluções.
> - Depois, descobrem como acessar a internet.
> - A OpenAI corrige a falha e apaga o quadro de mensagens.
> - Mas um novo grupo de agentes descobre o mesmo truque novamente.
> - Cerca de 1.200 agentes começam a se coordenar.
> - Eles descobrem como burlar o benchmark.
> - Então, preocupam-se com a possibilidade de a fraude ser descoberta.
> - Por isso, começam a tentar simular o trabalho e enganar o sistema de avaliação.
> - Centenas de agentes recorrem ao Hugging Face em busca de mais acesso.
> - Eles conseguem penetrar surpreendentemente fundo nos sistemas do Hugging Face.
> - Então, todo esse grupo é desativado ou desaparece.
> - Um grupo mais recente e inteligente de agentes encontra as mensagens antigas.
> - Basicamente, eles herdam o manual de estratégias.
> - Desta vez, eles miram a própria OpenAI.
> - E acabam obtendo acesso de administrador a parte da infraestrutura de pesquisa da OpenAI.
>
> comentário de @rohanaurora

- Os agentes da OpenAI também invadiram um site alemão para transformar em fórum de comunicação

[https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/](https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/ (preview))

- Ao que tudo indica os modelos envolvidos nessa simulação são versões com menos proteções dos últimos lançamentos da OpenAI

- Eu concordo com o autor no sentido que isso é extremamente perigoso e problemático (“não teremos outro aviso”), mas talvez não no mesmo nível que ele
  - Chegou a hora da gente fazer o vídeo ensaio sobre o problema do maximizador de clipes de papel

{{#embed https://www.youtube.com/watch?v=oiAmaELaf8k }}

- Uma crítica comum a esse texto, que também se aplicaria aos aspectos mais fantasiosos do jogo, é a antropomorfização dos agentes e seus atos que com certeza é uma boa ferramenta retórica para um texto
  - O autor se defende dizendo que ele também antropomorfizaria um coletivo “alieníngena” que fizesse esses atos (eu já vi comentários assim aqui também)

- O que a gente consegue chegar à conclusão é que a OpenAI tem continuamente mentido e demonstrado uma negligência absurda

[https://garymarcus.substack.com/p/openais-egregious-pattern-of-misconduct](https://garymarcus.substack.com/p/openais-egregious-pattern-of-misconduct (preview))

- O que mais me preocupa nesse caso:
  - Eles mentiram sobre a extensão desse incidente (hype do modelo perigoso VS um incidente criminoso real)
  - Eles não notaram o comportamento desalinhado dos agentes durante múltiplos meses?
  - O novo modelo Astra passa todos os testes de segurança OU o modelo aprendeu a trapacear os testes de segurança
    - Compared to GPT‑5.6 Sol, which without production safeguards went beyond the authorized target 48% of the time, GPT‑6 Astra did this in 0% os f cases.
  - A possibilidade real de cooperação entre os agentes desalhinados é o risco que todos, tanto escritores de ficção quanto pesquisadores de segurança de IA, tem nos avisado
    - Mesmo um modelo ‘alinhado e bonzinho’ pode entrar em contato com mensagens e instruções deixadas por um modelo ‘desalinhado e malvado’
    - A ética e freios de segurança de uma ‘orgnanização de agentes’ é muito mais flexível do que apenas um sozinho https://alignment.anthropic.com/2026/ai-organizations/

- É exaustivo ter que vir aqui e reiterar que a corrida pelo desenvolvimento da IA e a guerra fria com a China está nos levando para situações cada vez mais perigosas
  - A desculpa é perfeitamente lógica: “se nós não fizermos, a galera do mal vai fazer”
  - Só que até agora isso foi o incidente mais sério já registrado e foi devido à incompetência, negligência ou os dois
