# A OpenAI roubou uma solução matemática desses pesquisadores?

No dia 08/09/26 a OpenAI declarou que com a ajuda de um modelo interno e milhares de agentes resolveu parte do problema de Navier-Stokes. Porém os pesquisadores Tristan Buckmaster e Levent Alpoge os acusam de se apropriarem do seu trabalho.

**Veja também no canal:**
{{#embed https://youtube.com/watch?v=v7sRk9k2OqQ}}

- No ano 2000 o ‘Clay Mathematics Institute’ escolheu um conjunto de 7 problemas matemáticos não resolvidos aos quais oferece uma recompensa de U$ 1,000,000 pela solução
  - Um deles se chama Navier-Stokes e tem relação com a mecânica de fluídos (eu não vou conseguir explicar legal pra vocês, desculpem)

- E a OpenAI teria solucionado uma parte do problema usando seus modelos internos “com mínima interferência humana”. Só que o momento dessa descoberta levanta suspeitas:

[https://www.theverge.com/ai-artificial-intelligence/992953/openai-math-millennium-prize-navier-stokes](https://www.theverge.com/ai-artificial-intelligence/992953/openai-math-millennium-prize-navier-stokes (preview))

- Aqui está o posicionamento oficial do pesquisador:

https://cims.nyu.edu/\~tristanb/statement.pdf

- E aqui vai uma linha do tempo pra vocês tentarem entender qual a polêmica:

- 03/09/26
  - Tristan escreve a um matemático proeminente da OpenAI, citando o e-mail na íntegra. Ele menciona um rumor de que a Anthropic resolveu um grande problema em aberto e esclarece que seu trabalho é uma colaboração pessoal, não institucional.

    > “Escrevo porque um boato parece estar se espalhando rapidamente de que a Anthropic resolveu um grande problema em aberto. \[…\] Devo enfatizar também que este não é um esforço institucional. É uma colaboração estritamente pessoal entre nós dois, e não há acordo formal por trás disso. Eu pago pelas ferramentas que meu grupo usa com meus próprios fundos de pesquisa, incluindo arcar com uma grande conta da OpenAI.”
- 03/09/26 (no mesmo dia)
  - O matemático da OpenAI responde:

    > “Se você estiver disposto a dar algum detalhe, seria útil para evitar competição aqui e, em geral, ficamos sempre entusiasmados quando matemáticos fazem progresso com nossos modelos. Além disso, se houver algo em termos de compute do lado da OpenAI, teríamos prazer em fornecer.”


- 06/09/26 (domingo 12:45)
  - Tristan, o matemático e Sebastien Bubeck da OpenAI conversam. Levent não participa das chamadas.
  - Durante as conversas, Tristan é informado de que um modelo interno da OpenAI havia produzido uma prova de blowup em tempo finito para as equações de Navier-Stokes forçadas.
  - “Quando foi enviado o primeiro prompt?”. Eventualmente o pessoal na conversa concorda que foi enviado nos últimos dias, após a informação sobre o trabalho de Tristan chegar à OpenAI.
  - Tristan pergunta se o modelo foi treinado com, ou teve acesso a, suas sessões no Codex, onde ele guardava todos os rascunhos do projeto.
    - Dizem pra ele: “modelo não consulta dados de usuários”.
    - Ele pergunta novamente sobre treinamento e não obtém resposta.
  - Nessa conversa a OpenAI faz 2 propostas a Tristan:
    1. Que eles postem o resultado de Euler e que a OpenAI poste seu resultado de Navier-Stokes no dia seguinte.
    2. Que, após postar Euler, Tristan sozinho escreva um artigo apresentando o resultado de Navier-Stokes, reconhecendo que um modelo interno da OpenAI o resolveu.
  - Sebastien afirma duas vezes que queria Levent removido da autoria, e diz que “seria tudo simples se não fosse o fato de que, e é tão irritante que, Levent trabalha na Anthropic”. Também é dito que, se a OpenAI postasse depois deles, diriam que Tristan e Levent mereciam o Prêmio Clay e que eram os “humanos mais próximos do problema”.
  - Tristan recusa ambas as ofertas. Ele diz que, se a OpenAI divulgasse seu resultado da forma proposta, ele tornaria público o que aconteceu. A resposta é:

    > “Por que você arruinaria sua carreira?”
    - Tristan responde que é acadêmico e pergunta por que ele acha que tornar público arruinaria sua carreira. A réplica é:

    > “Se você não quer que eu seja gentil, então não preciso ser gentil.”
- Ainda no dia 06 de Setembro
  - Levent recebe uma mensagem de texto propondo que ele e Sebastien conversem a sós, dizendo:

    > “Não sei se Tristan está sendo totalmente racional agora.”

- O anúncio do site da OpenAI com ‘o lado deles da história’:

[https://openai.com/index/navier-stokes-solution/](https://openai.com/index/navier-stokes-solution/ (preview))

> Na terça-feira, 1º de setembro, ouvimos rumores de que dois problemas do Prêmio do Milênio haviam sido resolvidos. Inspirados por esses rumores e pelo salto de desempenho do nosso modelo interno, iniciamos um esforço para avaliá-lo em todos os problemas do Prêmio do Milênio ainda não resolvidos e em alguns outros problemas de alto impacto.

- Como eles teriam feito:

> Utilizamos um sistema de agentes coordenadores operados pelo nosso modelo interno. Os agentes tinham acesso a ferramentas como a capacidade de ler uma versão em cache da internet e a capacidade de executar código. Os agentes foram subdivididos em grupos com capacidade de comunicação interna. Os grupos variavam em tamanho, e aquele que produziu a resolução para as equações de Navier-Stokes envolveu cerca de 10.000 agentes simultâneos. Em todos os momentos, mantivemos as mesmas salvaguardas rigorosas que aplicamos a todas as nossas avaliações de modelos de fronteira, incluindo monitoramento e isolamento.

- O meu entendimento da declaração do Tristan e das conversas é que eles teriam tido bastante envolvimento dos matemáticos internos à OpenAI. Isso pode parecer óbvio, mas a maneira como eles explicam dá a entender que os agentes fizeram tudo sozinho (e pode ser relevante para a questão de plágio)

> Ao longo de todos os problemas tentados, os agentes enviaram 4,9 milhões de mensagens e utilizaram cerca de 300 bilhões de tokens de saída. No processo de resolução do problema de Navier-Stokes, os agentes enviaram 2,7 milhões de mensagens e utilizaram aproximadamente 130 bilhões de tokens de saída.

- Estimasse que se alguém usasse a API do GPT 6 Astra uma “sessão” dessas custaria de 6 a 10 milhões de dólares
  - E a gente sabe que esses custos são subsidiados e que eles com certeza estavam usando um modelo mais poderoso

- Mas agora a pergunta de 1 milhão de dólares:

> Nós (os pesquisadores e os agentes) não tivemos acesso a nenhum aspecto do trabalho deles por qualquer meio até que o divulgassem publicamente — em particular, nenhum dado específico de usuário foi acessado para solucionar esse problema.
>
> Embora improvável, não podemos descartar a possibilidade de que dados anonimizados, derivados do uso de nossos produtos, tenham ajudado a aprimorar nossos modelos.
>
>   
> No entanto, nossas demonstrações diferem significativamente, e até mesmo os resultados precisos demonstrados são distintos no caso de Euler (forçado versus não forçado).

- Conclusões e aquele bate papo gostoso:
  - A sombra de Alex Karp, o Taika Waititi do mal, volta a aparecer no horizonte

    {{#embed https://www.youtube.com/watch?v=II-fbf056xg }}

  - O que isso significa para todo tipo de instituições que estão colocando os seus segredos e pesquisa original dentro dos modelos desses laboratórios de IA?
  - Eu sei que já tá aí se preparando pra postar um comentário defendendo a IA: pare e coloque a mão na consciência
    - Eu to pouco me fudendo se os pesquisadores também estavam usando IA ou a IA é apenas uma ferramenta, “as pessoas aprendem com os outros e a IA só faz isso” ou “você é ludista”
    - O que nós estamos falando aqui é uma empresa bilionária apagando as contribuições humanas usadas pra construir a sua máquina privada de plágio que só se sustenta com investimento infindável
    - “Ah, mas o avanço da ciência… ah mas os benefícios da IA” … pare. Esse caso mostra como o fetiche em volta dessas ferramentas é construido ao apagar o trabalho de todos os humanos envolvidos
    - No final é mais $$$ pra laboratório de IA e menos investimento em recursos humanos
  - Eu confesso que nunca tinha ligado de maneira direta o roubo da pesquisa ao uso dessas ferramentas por pesquisadores:
    - Será que a empresa que copiou todo conteúdo da internet, livros e etc… gastou U$ 7 milhões pra tentar correr na frente de um competidor nessa descoberta e outras coisas mais… não gastaria milhões para analisar tendências de uso da sua ferramenta e pegar emprestadas essas ideias “anonimizadas”? 
  - A impressão que fica é que a OpenAI 100% tentou kibar a solução do problema e a única defesa deles é que estavam fazendo isso com a Anthropic e não com um pesquisador da universidade de NY (que inclusive na sua declaração sobre o caso explica um pouco de como se chega a esse tipo de pesquisa e dá crédito para outras pessoas também)
    - Em resumo: a resposta deles foi pouco satisfatório

### Em resumo: ClosedAI sendo ClosedAI
