# Claude Mythos é mesmo o mito?

Segundo a Anthropic eles acabaram de criar um dos mais poderosos LLM de todos os tempos e logo o público não irá acessá-lo, por enquanto. Por que? Ele é tão bom em código e pensamento criativo que a exploração de vulnerabilidades em software

<https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf>

- Em resumo o Claude Mythos é a evolução do Opus, um modelo de uso geral só que é muito bom em código
  - Isso faz muito sentido para a pesquisa de IA (como falaremos mais pra frente)
  - No documento lançado a Anthropic documenta vários casos de vulnerabilidades complexas que foram descobertas e exploradas pelo modelo com sucesso (bsd, ffmpeg, linux, firefox e supostamente mais)
  - O modelo supostamente conseguiu escapar de uma sandbox sem conexão à internet
  - Isso fez eles considerarem o modelo perigoso demais para ser lançado para o público em geral, mas ele foi liberado para pesquisadores, empresas e instituições para o reforço de sua segurança

> Today we’re announcing Project Glasswing1, a new initiative that brings together Amazon Web Services, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks in an effort to secure the world’s most critical software.

[https://www.anthropic.com/glasswing](https://www.anthropic.com/glasswing (preview))

- Vamos fazer um vídeo um pouco diferente, ao invés da conversa mais ‘seca’ apresentando fatos e algumas opiniões, vamos trabalhar com cenários. Isso vai me permitir falar um pouco sobre isso mesmo face essa incerteza.

1. A Anthropic está sendo completamente honesta e eles estão corretos na sua avaliação com relação ao Mythos
   1. O que isso significa para a segurança de software?
      - Project Glasswing
      - Questão de tempo para que grupos criminosos ‘no varejo’ usem algo assim
      - Podemos confiar nessas empresas e governos usando algo assim?
      - NSA e todas agências de inteligência querem os 0-day pra elas
      - Se atualizar o bicho pega, se deixar o bicho come
   2. Sobre os testes de segurança do modelo e o alinhamento
   3. Sobre a pesquisa de IA apoiada por modelos de IA (recurssive self improvement)
   4. Gap de inteligência entre ‘setor privado’ e sociedade em geral (mais processamento pra quem quer pagar, pra quê liberar pro público?)
2. A Anthropic não está sendo completamente honesta OU está incorreta na sua avaliação com relação ao Mythos (“olha só tudo o que o meu filho fez!”)
   1. Nesse caso nada estruturalmente muda além do paulatino avanço da capacidade dos modelos de IA, com tudo que estamos tentando entender ainda (mais produtividade? mais alienação do trabalho? mais custos para trabalhar? transformação da nossa profissão? e etc…)
   2. Isso é uma ótima estratégia de marketing e permite pra eles algo muito melhor que é a venda para clientes corporativos e não para os chinelões que pagam pouco e usam muito.

- Se perguntarem a minha opinião nós estamos no cenário 2 PORÉM eu tenho menos fé ainda na nossa segurança da informação e nas pesquisas de segurança dos modelos do que os engenheiros da Anthropic, então eu me preocupo com o cenário 1.
