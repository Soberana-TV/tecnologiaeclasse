# Câmera no vaso, eleição de criptólogos e zork

## Um pouco droga, um pouco salada

### UI/UX de segurança do novo

**Organização de pesquisa em criptologia cancela resultado de sua eleição anual de liderança após perder chave de descriptografia:** segundo a International Association of Cryptologic Research, os resultados estavam armazenados em um sistema que utiliza criptografia para registrar os votos. Três curadores detinham, cada um, um terço do material criptográfico da chave necessária para descriptografar os votos, mas um deles perdeu sua parte de forma irrecuperável. Ele renunciou ao cargo e foi substituído. As informações são do site Ars Technica.

<https://arstechnica.com/security/2025/11/cryptography-group-cancels-election-results-after-official-loses-secret-key/>

- Por incrível que pareça eu gosto de criptografia, sistemas de consenso, essa coisa toda...
- Segundo eles a perda da chave é um 'erro honesto, humano, porém infeliz' e é isso que eu to sempre tentando dizer. Mais que humano podemos imaginar que o erro também é material histórico e dialético (kkkkk desculpem)
- Eu acho que os pesquisadores e desenvolvedores tem que passar uma temporada perto dos usuários desses sistemas, principalmente os mais vulneráveis para repensar as suas prioridades

### Que merda hein...

**Empresa que criou câmera que encaixa na borda do vaso sanitário para analisar saúde intestinal admite que consegue descriptografar e analisar dados de usuários:**  na época em que o Dekoda, da Kohler, foi anunciado, foi dito que o  aparelho utilizava criptografia de ponta a ponta (E2EE). No entanto,  segundo um consultor de tecnologia independente, a outra “ponta” da  criptografia é a pŕopria empresa, e o que ela chama de “E2EE” é, na  verdade, criptografia HTTPS entre o aplicativo e o servidor. As  informações são do site PCMag.       

<https://techcrunch.com/2025/12/03/end-to-end-encrypted-smart-toilet-camera-is-not-actually-end-to-end-encrypted/>

> Antecipando preocupações com a privacidade, a Kohler afirmou em seu site que os sensores do Dekoda só monitoram o interior do vaso sanitário e alegou que todos os dados são protegidos com "criptografia de ponta a ponta".
>
> O uso da expressão "criptografia de ponta a ponta" pela empresa, no entanto, está incorreto, como apontou o pesquisador de segurança Simon Fondrie-Teitler em uma postagem de blog na terça-feira.
>
> Ao ler a política de privacidade da Kohler, fica claro que a empresa se refere ao tipo de criptografia que protege os dados durante a transmissão pela internet, conhecida como criptografia TLS — a mesma que alimenta os sites HTTPS.

- O produto são os seus dados! Todos esses produtos smart estão te cobrando "duas vezes" além de exporem a sua privacidade a vazamentos e atores maliciosos dentros dessas empresas.

- E tem mais, essa merda está treinando IA:

> O pesquisador de segurança também apontou que, considerando que a Kohler pode acessar os dados dos clientes em seus servidores, é possível que a empresa esteja usando fotos das tigelas dos clientes para treinar a IA. Citando outra resposta do representante da empresa, o pesquisador foi informado de que os algoritmos da Kohler são treinados apenas com dados anonimizados.
>
> ...
>
> “Se o usuário der seu consentimento (o que é opcional), a Kohler Health poderá anonimizar os dados e usá-los para treinar a IA que impulsiona nosso produto”, disse Lin. “Essa caixa de seleção de consentimento é exibida no aplicativo Kohler Health, é opcional e não vem pré-selecionada.”
>
> Após a publicação desta matéria, a Kohler atualizou seu site para remover as menções à “criptografia de ponta a ponta”. A página do produto Dekoda agora afirma que o produto utiliza “criptografia de dados em repouso e em trânsito”.

- E tudo isso pode ser seu por apenas...

> O Dekoda custa US$ 599, mais uma assinatura obrigatória de pelo menos US$ 6,99 por mês.

##### Vou aproveitar para recomendar um canal

<https://www.instagram.com/p/DSTS2yGDgvH/>

#### Os Zorks estão livres...

**Microsoft torna jogos Zork I, II e III open-source sob a licença MIT:**  os títulos foram lançados no fim dos anos 70 e início dos anos 80 para  computadores da época. A abertura do código é resultado do esforço  conjunto das equipes do Xbox, da Activision, do Escritório de Programas  de Código Aberto da Microsoft e do arquivista digital do Internet  Archive, Jason Scott. Os projetos podem ser conferidos nos repositórios  “zork1”, “zork2” e “zork3” da conta “historicalsource” no GitHub. As  informações são do site Ars Technica.

<https://github.com/historicalsource>

<https://en.wikipedia.org/wiki/Zork>

> This repository is a directory of source code for the Infocom game "Zork I", including a variety of files both used and discarded in the production of the game. It is written in ZIL (Zork Implementation Language), a refactoring of MDL (Muddle), itself a dialect of LISP created by MIT students and staff.

<https://github.com/historicalsource/zork1/blob/master/gmain.zil>

<https://app.formbricks.com/s/cmheupgol1w7jad01dqomg89g>

### Que frio...

**Norte-americanos recorrem à mineração de moedas digitais para aquecer casas no inverno:**  enquanto alguns utilizam aparelhos dedicados, como o HeatTrio de 900  dólares, outros instalam mineradores domésticos em áreas como sótãos,  redirecionando o ar quente pela ventilação. Especialistas, no entanto,  afirmam que a chance desses dispositivos minerarem um bloco de BTC são  quase nulas, funcionando apenas como aquecedores comuns. As informações  são da CNBC.

<https://www.cnbc.com/2025/11/16/bitcoin-crypto-mining-home-heating-energy-bills.html>

- Existem os haters:

> “Os dispositivos de aquecimento Bitcoin que vi parecem ser simples aquecedores que usam sua própria eletricidade para aquecer o ambiente... o que não é uma forma eficiente de aquecer uma casa”, disse ele. “Sim, a mineração de bitcoin gera muito calor, mas a única maneira de levar isso para sua casa é usando sua própria eletricidade”, disse Mohr.
>
> ...
>
> "Na minha opinião, esta não é uma oportunidade real que funcionará. Em vez disso, está aproveitando coisas de que as pessoas ouviram falar - excesso de calor da mineração de bitcoin e lucros da mineração - e está dando falsas esperanças de que existe uma maneira de um indivíduo se beneficiar disso", disse Mohr.

- Existem os fãs:

> "Imagine um cenário semelhante em que a configuração de mineração criptográfica de um complexo de apartamentos produz moeda digital e energia térmica utilizável. Isso abre a porta para a inovação em energia distribuída para uma base mais ampla de partes interessadas, uma abordagem que poderia complementar os sistemas de aquecimento existentes e as estratégias de geração renovável", disse Morris.
>
> ...
>
> Peterson aqueceu sua própria casa por dois anos e meio usando equipamentos de mineração de bitcoin e acredita que o calor fornecerá energia para quase tudo no futuro. “Você irá ao Home Depot em alguns anos e comprará um aquecedor de água com uma porta de dados e sua água será aquecida com bitcoin”, disse Peterson.
