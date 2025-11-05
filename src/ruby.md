# Ruby on Rails fora dos trilhos

O Rubygems sofreu uma "mudança de direção" forçada por intervenção de empresas influentes no ecossistema Ruby, porém isso ficou em segundo plano quando o criador do Ruby on Rails novamente se envolveu numa "polêmica" por suas opiniões políticas merdas.

- Tudo começou no dia 22/09/25 com:

<https://github.com/Plan-Vert/open-letter>

- Em resumo: um abaixo assinado de pessoas da comunidade Ruby e Ruby on Rails que estão pedindo que a equipe do RoR se retire do projeto e crie um fork (fora da alçada de David Heinemeier Hansson)
- Essa não é a primeira controvérsia que o DHH e o Basecamp se envolvem (vamos falar mais pra frente). Qual foi o evento recente que deflagrou mais essa crise?

### Qual a problema´tica com o DHH?

<https://web.archive.org/web/20250920061923/https://world.hey.com/dhh/as-i-remember-london-e7d38e64>

- Essa postagem faz uma boa crítica do texto: <https://paulbjensen.co.uk/2025/09/17/on-dhhs-as-i-remember-london.html>
- Esse também: <https://tekin.co.uk/2025/09/the-ruby-community-has-a-dhh-problem>

### Ou será que foi mesmo?

- De certa maneira a carta não faz um bom trabalho de explicar para quem está de fora as dinâmicas de poder da comunidade Ruby on Rails
- Quando uma dessas coisas 'explode' e é noticiada pela mídia mais geral de tecnologia geralmente tem algumas história do passado:

#### How Ruby went off the Rails

de 404media.co

<https://archive.is/G1Alk>

> Em 19 de setembro, a Ruby Central, uma organização sem fins lucrativos que administra o RubyGems.org, uma plataforma para compartilhamento de código e bibliotecas Ruby, assumiu o controle de vários repositórios do GitHub para Ruby Gems, bem como de outros projetos críticos de código aberto Ruby dos quais o restante da comunidade de desenvolvimento Ruby depende. Um grupo de desenvolvedores de código aberto que contribuiu para esses projetos e os manteve por anos teve suas permissões revogadas repentinamente. Quando esses desenvolvedores anunciaram nas redes sociais que seu acesso havia sido retirado, muitos desenvolvedores Ruby viram a decisão como uma traição às suas contribuições de anos para o ecossistema Ruby e para os princípios do código aberto em geral. Outros acusaram a Ruby Central de ceder à pressão corporativa de empresas como a Shopify, que, segundo eles, queriam mais controle sobre o projeto.

###

> O RubyGems.org e outras ferramentas essenciais do Ruby não foram interrompidos durante essa transição até o momento, mas o incidente revela uma verdade fundamental sobre a internet e o desenvolvimento de código aberto: grande parte da tecnologia que usamos diariamente e que consideramos garantida é mantida por um pequeno número de desenvolvedores que não são remunerados por esse trabalho ou recebem salários muito baixos em comparação com os das grandes empresas de tecnologia. O desenvolvimento de código aberto continua a viabilizar grande parte da internet, mas, à medida que algumas dessas ferramentas se tornam mais importantes e valiosas financeiramente, elas ficam sujeitas a maior escrutínio e pressão da comunidade, das organizações e das empresas que dependem delas.

- Um lado da questão:

> A controvérsia atual surgiu nas redes sociais em 19 de setembro, quando Ellen Dash, uma das colaboradoras dos projetos de código aberto RubyGems e Bundler no GitHub, anunciou que Haught, Diretor de Código Aberto da Ruby Central, revogou a participação na organização do GitHub de todos os administradores das equipes de manutenção do RubyGems, Bundler e RubyGems.org. Naquele momento, suas permissões e acesso à organização do GitHub foram revogados, o que significa que eles não podiam mais fazer alterações ou contribuições ao código, e Haught, representando a Ruby Central, assumiu o controle.
>
> “Não vou usar meias palavras: isso foi uma tomada de poder hostil”, disse Dash em uma carta pública de “despedida” que compartilhou online. “Considero o comportamento da Ruby Central uma ameaça para a comunidade Ruby como um todo. A remoção forçada daqueles que mantiveram o RubyGems e o Bundler por mais de uma década é inerentemente uma ação hostil. A Ruby Central ultrapassou os limites ao fazer isso.”

- E o outro:

> A Ruby Central, por sua vez, descreve a mudança como centrada na segurança.
> "Com o recente aumento de ataques à cadeia de suprimentos de software, estamos tomando medidas proativas para proteger o ecossistema de gems Ruby de ponta a ponta", disse a Ruby Central em uma explicação sobre sua decisão. "Para fortalecer a segurança da cadeia de suprimentos, estamos tomando medidas importantes para garantir que o acesso administrativo ao RubyGems.org, RubyGems e Bundler seja gerenciado com segurança. Isso inclui nossos sistemas de produção e repositórios do GitHub. No curto prazo, suspenderemos temporariamente o acesso administrativo a esses projetos enquanto finalizamos novas políticas que limitam os direitos de acesso de commit e organização. Essa decisão foi tomada e aprovada pelo Conselho da Ruby Central como parte de nossa responsabilidade fiduciária. Enquanto isso, temos um forte sistema de plantão para garantir a continuidade e a confiabilidade enquanto avançamos com esse trabalho. Essas mudanças visam proteger a infraestrutura crítica que alimenta o ecossistema Ruby, seja você um desenvolvedor baixando gems para sua máquina local [ou] uma equipe pequena ou grande que depende da segurança e disponibilidade dessas ferramentas."

- O DHH está envolvido nisso por causa de um detalhe importante:

> Em uma mensagem de vídeo de 22 de setembro em resposta às críticas sobre sua decisão de remover mantenedores, a diretora executiva da Ruby Central, Shan Cureton, descreveu uma dinâmica semelhante. Ela disse que "patrocinadores e empresas que dependem de ferramentas Ruby nos procuraram com preocupações sobre a cadeia de suprimentos" e que "nosso financiamento e patrocínios estão diretamente ligados à nossa capacidade de demonstrar fortes padrões operacionais. Sem esses padrões em vigor, fica mais difícil garantir o apoio necessário para manter os mantenedores pagos, organizar eventos e fornecer recursos para desenvolvedores em todas as etapas de sua jornada."
>
>
> Como a Shopify é uma das principais patrocinadoras e financiadoras da Ruby Central, isso levou alguns na comunidade Ruby a acreditarem que a Shopify estava pressionando a Ruby Central a fazer essa mudança.

> “Literalmente, só existe uma empresa que está fornecendo o dinheiro que mantém a Ruby Central funcionando, e é a Shopify”, Arko me disse. “Então, eu simplesmente não acho que haja outra explicação plausível além de a Shopify ter exigido isso.” Quando perguntei a Arko por que ele achava que a Ruby Central o removeu, se não fosse por motivos de segurança, Arko disse: “uma especulação totalmente impossível de provar é que o CEO da Shopify é o melhor amigo do DHH, que me odeia.” DHH também é membro do conselho da Shopify.

#### "Não vamos falar de política no trabalho"

####

<https://www.theverge.com/2021/4/27/22406673/basecamp-political-speech-policy-controversy>

- O Basecamp, empresa do DHH, tinha uma piada interna problemática de guardar 'nomes engraçados' de pessoas que se registravam no seu serviço
- Pessoas que trabalhavam lá dentro e tentaram levantar essa problemática foram rechaçadas e ficou um grande climão.
- O que resultou numa proibição de "falar de política" dentro da empresa...
- Eu não deveria ter que explicar a problemática disso, mas lá vai. A existência de minoriais sociais e os problemas que elas enfrentam dentro e fora do ambiente de trabalho são "políticos"

- Versão do DHH:

  <https://world.hey.com/dhh/let-it-all-out-78485e8e>

#### Flertes com o público anti woke:

<https://world.hey.com/dhh/the-waning-days-of-dei-s-dominance-9a5b656c>

- Eu já não faço mais parte da comunidade Ruby e RoR faz um tempinho. A imagem que eu tinha do DHH é de um cara "chato", mas "genial". Ele é tecnicamente muito bom, MAS...
- Lembra vocês de alguém? Cada país tem o Elon Musk que merece não é mesmo?

  {{#embed https://www.youtube.com/watch?v=qO7BI0UAj8c }}

#### Conclusão

- O esforço de um fork provavelmente está fadado ao fracasso, uma análise muito parecida com a que eu faço da Godot. Porém os nomes apoiando essa cisão são muito mais pesados e essa crise não é algo menor... pode estourar de novo mais pra frente
- Fica a reflexão novamente sobre a dificuldade de conciliar um projeto de software livre (ou até mesmo aberto) e as pressões do mercado e políticas ditatoriais dos seus "donos"
- Esse caso como o da Godot, Wordpress e muitos outros fica dormente por enquanto, mas ficaremos de olho
