# Flávio no Partido Missão? O que rolou?

No último dia 12 de Agosto a filiação “errônea” de Flávio Bolsonaro ao partido Missão, gerou um factóide que foi explorado por ambos grupos para gerar um ciclo notícias. Mas afinal, entendemos agora o que aconteceu com o sistema do TSE?

**Veja no canal:**
{{#embed https://youtube.com/watch?v=RMTQTMKHNkk}}

[](https://www.brasildefato.com.br/2026/08/19/pf-abre-inquerito-para-investigar-suposta-fraude-que-filiou-flavio-bolsonaro-ao-partido-missao/ (preview))

[https://noticias.uol.com.br/comprova/ultimas-noticias/2026/08/20/candidatura-tse-pl-flavio-bolsonaro-filiacao-missao.ghtm](https://noticias.uol.com.br/comprova/ultimas-noticias/2026/08/20/candidatura-tse-pl-flavio-bolsonaro-filiacao-missao.ghtm (preview))

> As postagens retratam uma situação que existia no momento em que foram publicadas, mas que foi resolvida poucas horas depois. Flávio Bolsonaro apareceu filiado ao partido Missão no sistema da Justiça Eleitoral nos dias 12 e 13 de agosto, o que impediu temporariamente o seu registro de candidatura à presidência do Brasil pela sua legenda, o PL. A filiação foi corrigida ainda em 13 de agosto e o pedido de registro foi protocolado na mesma data, dois dias antes do fim do prazo legal. O TSE também descartou a hipótese de ataque hacker ao sistema.

- Aqui, ao invés de eu colocar uma sessão sobre como vamos focar na parte técnica e é pra ignorar esse negócio de política, eu vou tirar um tempo pra falar mal da direita e principalmente do MBL:
  - Um movimento populista e demagogo que está tentando disputar o que sobrou do movimento bolsonarista
  - Renan Santos é um canalha que tenta dar um ar de “jovem e descolado” para as piores tendências da direita e acha que falar fingindo que tá brabo faz parecer que tem autoridade
  - Um livro cheio de propostas rasas para problemas difíceis pra agradar uma classe média e adolescentes sem mexer em estruturalmente nada  

- Mas agora é só com o pessoal técnico e sem política aqui, vamos continuar analisando a situação:

- O que disse o Missão:
  - Foi alguém usando o sistema filiação deles, mas não foram eles pessoalmente
  - Sistema interno de filiação ao partido Missão repassa os dados do formulário para o TSE e só consegue acusar erro nos dados depois do processo já ter sido feito
  - O cadastro de filiação do Flávio Bolsonaro no sistema do Missão teria ocorrido no dia 02/08/26. Foi mandado um email automático para o email do Flávio que eles alegam ter sido aberto (o gabinete do Flávio alegou achar que era spam)
  - Dia 12/08/26 o sistema do Missão de fato sobe o cadastro para o TSE sem que seja acusado erro ou discrepância de dados
  - O sistema do TSE não permite desfiliação (não fica claro se tentaram desfiliar o Flávio ou se é por tentar desfiliar outros pelo sistema deles)
  - Também alegaram que a equipe do Flávio estava mentindo sobre ter problema ao cadastrar a candidatura porque essa filiação não deveria ter bloqueado nada

- O que disse o Flávio Bolsonaro:

> Integrantes da campanha de Flávio Bolsonaro (PL) à Presidência disseram à coluna que a nota do partido Missão sobre a filiação fraudulenta do candidato não tem sentido e não esclarece o que ocorreu. A equipe afirma que tentou fazer o registro da candidatura presidencial de Flávio no TSE nesta manhã, mas não conseguiu porque ele foi filiado ontem ao Missão.

[https://www.facebook.com/congressoemfoco/videos/fl%C3%A1vio-bolsonaro-pl-rj-afirmou-que-sua-filia%C3%A7%C3%A3o-ao-partido-miss%C3%A3o-foi-fraudada-e/1610108730550915/](https://www.facebook.com/congressoemfoco/videos/fl%C3%A1vio-bolsonaro-pl-rj-afirmou-que-sua-filia%C3%A7%C3%A3o-ao-partido-miss%C3%A3o-foi-fraudada-e/1610108730550915/ (preview))

- O que disse o TSE:

<https://xcancel.com/TSEjusbr/status/2087969732104221035>

> O presidente  do TSE, ministro Kassio Nunes Marques, encaminhou uma representação à  PGE (Procuradoria-Geral Eleitoral) para a adoção das providências  cabíveis após a filiação fraudulenta do candidato do PL à Presidência da  República, Flávio Bolsonaro, ao partido Missão.
>
> Nunes  Marques também determinou a instauração de inquérito pela Polícia  Judiciária para apurar as circunstâncias em que o nome de Flávio foi  incluído nos registros de filiados da legenda.

- Pra resumir isso:
  - Na prática isso não vai dar em nada, mas se Missão e Flávio estão falando a verdade tem alguém que abusou do sistema do Missão pra abusar do sistema do TSE
  - Esse é um caso de abuso que chama a atenção por envolver o segundo candidato nas pesquisas, mas poderia ser muito mais danoso acontecendo com candidatos menores e mais desconhecidos

- Então, o que aconteceu realmente tecnicamente?

[](https://yaso.substack.com/p/onde-esta-a-vulnerabilidade-que-permitiu (preview))

- Em resumo: o sistema de cadastro de filiações permite que seja feito qualquer cadastro apenas por uma pessoa com acesso ao sistema, não existe um processo de identificação para saber quem pode fazer o que e no geral todos tem bastante permissão.

- Tanto que isso já aconteceu em outros ciclos eleitorais, como o Lula tendo sido cadastrado no PL por 6 meses em 2024:

[https://oglobo.globo.com/politica/noticia/2024/01/11/lula-permaneceu-filiado-ao-pl-de-bolsonaro-por-seis-meses-entenda-o-caso-e-como-funciona-o-sistema-do-tse.ghtml](https://oglobo.globo.com/politica/noticia/2024/01/11/lula-permaneceu-filiado-ao-pl-de-bolsonaro-por-seis-meses-entenda-o-caso-e-como-funciona-o-sistema-do-tse.ghtml (preview))

- Aparentemente o sistema interno de filiação do PT e outros partidos busca por pessoas politicamente expostas para impedir a “filiação troll”. Me parece que tem relação com esse tipo de caso

- Muito parecido com o caso da misantropi4 ou até o caso da injeção de prompt feita pelos advogados da Natura:
  - Muitas vezes o sistema presume que as credenciais também carregam a informação de identidade, mas isso não é verdade
  - Parece que a maneira de lidar é: “se alguém abusar das credenciais serão aplicadas sanções legais”.
  - Mas claramente esse modelo é defasado perto da importância e do uso mais difundido que esses sistemas tem no nosso dia a dia

- A conclusão que podemos chegar até agora, considerando que ainda não achamos o suposto culpado pela filiação:
  - Alguém abusou do sistema do TSE abusando do sistema do Missão
  - Flávio Bolsonaro usou isso como oportunidade para se fingir de vítima do sistema
  - Os discípulos de Marçal do MBL usaram isso como oportunidade para tentar se promover (mas ficaram com o c\* na mão, meio que de leve)
  - Não tem desculpa pro TSE ter um sistema tão rústico quando estamos lidando com um processo tão importante.
  - A ameaça de sanção legal não substitui a segurança e precauções básicas

> “Deixei a porta aberta, mas é proibido por lei invadir a minha casa”

### Referências de vídeo

{{#embed https://www.youtube.com/watch?v=17PYuzyLxOs}}

{{#embed https://www.youtube.com/watch?v=DJ6GkePul1w}}
