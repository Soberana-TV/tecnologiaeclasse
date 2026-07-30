# Lá vem Kimi K3 torando tudo 

No dia 17/07/26 a Moonshot AI lançou a nova versão dos seus modelos de pesos abertos ‘Kimi’. O Kimi K3 já chegou abalando nos benchmarks encostadinho nos últimos modelos da OpenAI e Anthropic e é claro que isso estremece a bolha.

**Assista no canal:**
{{#embed https://www.youtube.com/watch?v=5990BZ_UKR4 }}

[https://www.poder360.com.br/poder-china/moonshot-ai-lanca-kimi-k3-maior-modelo-de-ia-da-china/](https://www.poder360.com.br/poder-china/moonshot-ai-lanca-kimi-k3-maior-modelo-de-ia-da-china/ (preview))

- O modelo foi bem em diversos benchmarks, principalmente nos que mais importam para o momento que a gente está agora que são programação e tarefas de agente:
  - Os benchmarks internos foram rodados com um harness customizado pela Moonshot
  - Porém ficou no topo também em vários benchmarks independentes como Artificial Analysis (terceiro) e LM Arena Frontend Coding (em primeiro)
  - Os pesos abertos ainda não podem ser baixados, ficou para o dia 27/07/26

- O hype foi tanto que a empresa não conseguiu atender todos usuários contratando o modelo e teve que limitar as inscrições na plataforma

- O custo dele no momento é US$ 3 entrada e U$ 15 saída, o que é 3x menor que o Fable e um pouco menos que 2x menor que GPT Sol.
  - Porém os testes iniciais mostram que ele usa mais tokens no raciocínio então o custo é um pouco maior do que uma comparação direta sugere.

- Pra não dizer que a China nunca fez nada pra você: no dia 20 de Julho a Anthropic anunciou que agora o Fable ficaria definitivamente nos planos Max e Team. Eles já estavam nessa dança com o Fable, mas agora a água bateu na bunda

### Uma coisa sobre os benchmarks

{{#embed https://www.youtube.com/watch?v=enk4w5mRjQY }}

- Esse vídeo explica de forma magistral como essas empresas manipulam benchmarks e faz isso de uma maneira só um pouquinho mais escrachada

- Embora a métrica de ‘trust me bro’ também seja uma porcaria, muitas vezes só dá pra entender a qualidade de um modelo no uso específico e contínuo que se faz dele.

### Enquanto isso no GLM 5.2

{{#embed https://www.youtube.com/watch?v=19xCOJxWU0A }}

[https://justvugg.github.io/colibri/](https://justvugg.github.io/colibri/ (preview))

### A OpenAI “invadiu” o Huggingface

{{#embed https://www.youtube.com/watch?v=MrI4VcJtFFs }}

- Durante um teste interno de segurança o GPT 5.6 Sol e um outro modelo ainda não liberado teriam decidido escapar da “sandbox” do teste e tentar roubar as respostas do teste do site Huggingface

- Usando uma vulnerabilidade no Huggingface o agente teria hackeado o site por inferir que lá ele poderia encontrar respostas para o teste que estava lhe sendo proposto
  - Era um teste de invasão chamdo ‘ExploitGym’, se foi isso mesmo ele passou no teste
  - Não ficou super claro o exploit usado, mas pareceu meio idiota… o Huggingface aceita dados + prompts para manipular eles e foi feita uma prompt injection aí

[https://openai.com/pt-BR/index/hugging-face-model-evaluation-security-incident/](https://openai.com/pt-BR/index/hugging-face-model-evaluation-security-incident/ (preview))

- Aparentemente a Huggingface percebendo o ataque tentou ligar os modelos dos EUA (Anthropic e OpenAI) pra se defender e eles disseram que era perigoso demais… aí eles meteram um GLM 5.2 pra ajudar 

- A gente tem que ser um pouco cético com essa história porque foram 2 empresas lançando um press release sobre uma situação meio constrangerdora e tentando sair como as fodonas
  - OpenAI não sabe fazer uma sandbox → Modelo poderoso demais, somos foda
  - Segurança da Huggingface tinha uma falha idiota → Usamos nossos modelos para detectar esse ataque perigosíssimo

- Eu devo ter falado nos últimos 2 vídeos nesse estilo que a OpenAI está meio desesperada pra fazer um momento igual o do Mythos

### O Xi na “World AI Conference”

- Maior evento de IA da China e um dos maiores do mundo. Aconteceu de 17 a 20 de Julho de 2026.

[https://www.dw.com/en/us-china-ai-rivalry-heats-up-as-chinese-models-gain-ground/a-77899558](https://www.dw.com/en/us-china-ai-rivalry-heats-up-as-chinese-models-gain-ground/a-77899558 (preview))

- Obviamente o Kimi K3 chamou muita atenção, mas a China também tem diversos outros players de IA no mercado, pra citar mais alguns tem a zAI, MinMax, Deepseek, Alibaba.

- Rolou a apresentação do Atlas 950 SuperPoD, cluster de IA da Huawei para treinamento de modelos de grande porte

- A China posicionou o open source e open weights como sua principal estratégia para competir com os EUA, argumentando que modelos abertos aceleram a adoção global e reduzem a dependência tecnológica.

- Durante sua fala de abertura do evento, Xi Jinping, defendeu: modelos abertos, cooperação global para o desenvolvimento seguro da IA, inclusão do sul global na economia de IA, entre outras coisas gostosas,

{{#embed https://www.youtube.com/watch?v=0Pbv5_7t1GQ }}

- Mais pro fim do discurso anunciou o World Artificial Intelligence Cooperation Organization (WAICO) que contará com 29 países fundadores (inclusive o Brasil) . Além disso também prometeu:
  - 5.000 vagas de treinamento em IA para países em desenvolvimento nos próximos cinco anos;
  - centros de cooperação em IA com ASEAN, BRICS, União Africana, Liga Árabe, CELAC e Organização para Cooperação de Xangai;
  - disponibilização do sistema chinês de previsão meteorológica com IA (MAZU) para 30 países.

[https://en.wikipedia.org/wiki/World_Artificial_Intelligence_Cooperation_Organization#Member_states](https://en.wikipedia.org/wiki/World_Artificial_Intelligence_Cooperation_Organization#Member_states (preview))

### Conclusões

- Obviamente a China não defende IA aberta apenas porque é boazinha, mas estando atrás e lidando com um competidor que está tentando bloqueá-la de chegar ao resto do mundo, essa estratégia tem sido a mais proveitosa (e pra nós também)

- Os modelos abertos não precisam chegar no nível dos mais poderosos modelos fechados dos EUA. Se der pra rodar é dentro e ninguém nunca mais vai ter motivo pra pagar 1 centavo pra laboratório de fronteira dos EUA
  - Anthropic e OpenAI sabem disso e o seu modelo de negócios não vai dar certo por causa dessa ‘race to the bottom’
  - Valeu por mais essa China 👍 

- Os medos do estouro da bolha começam a aumentar novamente, explicando temos 3 partes da economia de IA lá nos EUA
  - Pesquisa em laboratórios de fronteira
  - SaaS que faz uso de modelos de IA
  - Infraestrutura

- Modelos abertos tecnicamente são ótimos para os pontos 2 (redução de custos e mais possibilidades) e 3 (usar a infra para construir com modelos abertos) MAAAAAS
  - A alavancagem e dívida intercruzada entre todas essas empresas é o risco que existe (Oracle já sofreu um ‘downgrade’ de crédito essa semana por ex.)

- E por isso nós vemos cada vez mais um aumento do discurso chauvinista e patriota nos EUA. “Defender laboratórios de IA é defender a nação”

- Além disso eu vou falar de novo, a tentativa de banimento dos modelos abertos vem aí. O que vai criar toda uma série de problemas para as empresas que dependem dos ótimos modelos, por exemplo os qwen da Alibaba, no seu dia a dia.

- Para derrotar a China precisamos de OpenAI e Anthropic fortes → Não pode usar modelo da China → OpenAI e Anthropic quebram a tua empresa de serviços porque ela ficou dependente de IA → Crise vem → Maldita China!

- Será que eu estou certo? Só o tempo dirá, flw
