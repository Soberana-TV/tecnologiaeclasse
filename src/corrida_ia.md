# A guerra frIA entre EUA e China

Está começando mais um episódio da guerra frIA entre China e EUA pelo controle dos modelos de IA. E parece que a China está encostando e deixando os CEOs e dos laboratórios americanos cada vez mais nervosos e ressabiados com os modelos abertos.

*Veja no canal:*

{{#embed https://youtube.com/watch?v=AlKJ9bdwcMA }}

- Quem andava acompanhando as notícias, ou é dev, com certeza está familiarizado com o Fable 5 e com a sua suspensão. Ele recentemente voltou e o Mythos continua só para os parceiros.

[https://www.anthropic.com/news/redeploying-fable-5](https://www.anthropic.com/news/redeploying-fable-5 (preview))

- Tem algumas pegadinhas:
  - Chamadas podem ser roteadas para o Opus 4.8 se consideradas perigosas
  - Os planos de assinatura tem um limite de uso do Fable
  - A partir do dia 13/07 ele vai começar a ser acessível apenas por chamadas de API (pagando por token)
  - Pessoas reclamando que ele não está tão bom quanto da primeira vez e a gente não sabe se é gaslight da Anthropic ou psicose de IA

[https://olhardigital.com.br/2026/07/09/inteligencia-artificial/anthropic-vai-cobrar-a-mais-pelo-claude-fable-5/](https://olhardigital.com.br/2026/07/09/inteligencia-artificial/anthropic-vai-cobrar-a-mais-pelo-claude-fable-5/ (preview))

- Só que, como a gente já havia reportado, os benchmarks do Fable/Mythos não estavam tão distantes de outros modelos disponíveis por aí… inclusive de modelos abertos. O que nos leva a: 

  
Startups asiáticas lançam modelos de IA rivais do Claude Mythos em meio ao bloqueio de exportação da Anthropic imposto pelos EUA: entre eles estão Tulongfeng, da chinesa 360, e Fugu, da japonesa Sakana AI, cujo fundador, David Ha, afirma que depender de um único fornecedor de infraestrutura de IA para um país tornou-se um risco, já que o acesso a modelos avançados pode desaparecer de um dia para o outro. As informações são do site TechCrunch.

[https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/ (preview))

- E também ao modelo aberto da z.ai que está dando o que falar: o GLM 5.2. E inclusive olhem só o tipo de manchete totalmente não enviesada que sai na Forbes.

[https://www.forbes.com/sites/craigsmith/2026/06/28/buckle-up-the-bad-guys-now-have-a-model-as-powerful-as-mythos/](https://www.forbes.com/sites/craigsmith/2026/06/28/buckle-up-the-bad-guys-now-have-a-model-as-powerful-as-mythos/ (preview))

> A lição para conselhos de administração e CISOs não é que um lançamento chinês tenha revolucionado o cenário da noite para o dia. A conclusão é que a premissa de que a IA cibernética mais capaz permaneceria restrita a APIs fechadas e contratos governamentais já não se sustenta. O caso Mythos demonstrou que governos retiram de circulação modelos que consideram desestabilizadores. O GPT-5.6 mostrou laboratórios dos EUA aceitando essa restrição. Já o GLM-5.2 revelou o surgimento de uma tecnologia com o mesmo nível de capacidade na forma de infraestrutura aberta, sem que houvesse qualquer entidade em posição de retirá-la de circulação.

- Porém a China poderia estar pensando em restringir os modelos abertos?

https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/

- Isso me soou bastante estranho, principalmente considerando o dano que modelos de peso aberto tem feito aos laboratórios de IA estadunidenses e a trajetória de pesquisa dos maiores laboratórios chineses até o momento

- Uma pesquisa sobre o assunto me levou ao reddit, que as vezes acerta:

https://www.reddit.com/r/LocalLLaMA/comments/1upvw37/beijing_is_not_looking_at_curbing_overseas_access/

- Uma interpretação mais honesta das minutas obtidas pela Reuters seria algo como: “China está tentando balancear o modelo de usar pesos livres sem ter suas startups e laboratórios capturados por investimento estrangeiro”
  - Lembrem do caso da Manus AI que mudou suas operações pra Hong Kong e tentou vender pra Meta, mas o governo chinês impediu a venda (talvez tarde demais)

- Quer dizer que o governo chinês nunca irá restringir modelos ou regulamentar o acesso? Não, isso pode acontecer. Porém não parece ser uma análise correta do que estão  fazendo agora.

- O que nos leva a outra grande acusação: startups de IA chinesas estão destilando os modelos americanos:
  - O que é destilação?
  - “Ai nossa, que peninha da empresa de IA americana”

[https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks/ (preview))

> Identificamos campanhas em escala industrial conduzidas por três laboratórios de IA — DeepSeek, Moonshot e MiniMax — para extrair ilicitamente as capacidades do Claude a fim de aprimorar seus próprios modelos. Esses laboratórios geraram mais de 16 milhões de interações com o Claude por meio de aproximadamente 24.000 contas fraudulentas, violando nossos termos de serviço e as restrições regionais de acesso.

- O que mais me chama atenção aqui é como a Anthropic é de longe o laboratório de IA mais hostil aos modelos abertos, além de envelopar isso numa retórica nacionalista e “EUA polícia do mundo”

> Modelos obtidos por meio de destilação ilícita carecem das salvaguardas necessárias, gerando riscos significativos à segurança nacional. A Anthropic e outras empresas dos EUA desenvolvem sistemas que impedem atores estatais e não estatais de utilizar a IA para, por exemplo, desenvolver armas biológicas ou realizar atividades cibernéticas maliciosas. É pouco provável que modelos criados via destilação ilícita preservem tais salvaguardas, o que significa que capacidades perigosas podem se disseminar sem muitas das proteções originais.

- E claro, a gente não pode deixar de rir da ironia disso aqui:

> No entanto, a destilação também pode ser utilizada para fins ilícitos: concorrentes podem empregá-la para obter capacidades poderosas de outros laboratórios em uma fração do tempo — e a uma fração do custo — que seria necessária para desenvolvê-las de forma independente.

- Só que tem um “porém” nessa história. O uso de modelos da Anthropic é altamente restrito na China, pela Anthropic e pelos bloqueios de internet por lá?

- Esse tipo de acesso acontece usando as “transfer stations” e muitas vezes o acesso a modelos como o Claude fica até 90% mais barato! Como? Num esquema que eles chamam de “1 peixe, 3 refeições” (一鱼三吃)

https://news.ycombinator.com/item?id=48664814

[https://www.chinatalk.media/p/how-to-buy-cheap-claude-tokens-in](https://www.chinatalk.media/p/how-to-buy-cheap-claude-tokens-in (preview))

- Esses proxies permitem a contratação de chamadas de API por um “mercado paralelo” com o preço dos tokens extremamente baixo. É “esse um truque que a Anthropic odeia” e governo Chinês faz vista grossa:
  - Esses serviços criam milhares de contas gratuitas e pagas nos serviços como o Claude e se aproveitam dos tokens subsidiados nos planos de inscrição
  - É possível que haja a venda de uma chamada para o Opus 4.8 e resposta venha de um modelo chinês aberto como o GLM 5.2
  - Os logs das conversas podem ser vendidos para o uso em fraudes, golpes e para laboratórios de IA que desejam treinar como os prompts, respostas e racicínio dos modelos.

- E de novo, o discurso da Anthropic é muito bonito no papel e eles até negaram o contrato com o exército dos EUA… MAS semana que vem o Fable 5 entra pra jogo com chamadas custando U$10/U$50 por milhão de tokens entrada/saída e logo mais tem IPO
  - Essa é uma estratégia de marketing da Anthropic e inclusive os responsáveis por ela já estiveram dentro da OpenAI fazendo o mesmo

- O que nos leva a OpenAI, tadinha, anda meio apagada. Nós já falamos que o ChatGPT 5.6 também foi considerado perigoso e liberado apenas para parceiros e da aproximação dela com o governo dos EUA

> OpenAI estaria em negociações iniciais para dar 5% de participação ao governo dos EUA: a ideia é vista como uma forma de compartilhar os benefícios econômicos da tecnologia com a sociedade. É esperado que outras empresas do setor façam algo semelhante, mas ainda não há confirmação de que Google, Meta e Anthropic aceitariam a proposta. As informações são do site The Guardian.

[https://www.msn.com/en-us/money/companies/openai-proposes-5-stake-to-trump-administration-to-ease-washington-pressure-report/ar-AA2721GE](https://www.infomoney.com.br/business/a-openai-propoe-dar-ao-governo-dos-eua-uma-participacao-de-5-diz-ft/ (preview))

- Agora que tá perdendo ele diz: “realmente, esse negócio de IA é meio perigoso e pode fazer altos males pra sociedade… quem sabe o governo não garante a minha empresa e inclusive já regulamenta ela e todas outras concorrentes?”

- E esse é um movimento natural de se proteger do estouro da bolha, tanto pras startups e big techs quanto para a própria economia dos EUA que está impossivelmente agarrada no crescimento dessa indústria.

- A única coisa que eu consigo prever agora é uma aproximação cada vez maior dos governos com essas tecnologias e uma tentativa de banimento ou limitação dos modelos abertos nos EUA
