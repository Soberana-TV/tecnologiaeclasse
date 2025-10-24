# A queda global da AWS

Um aparente erro simples de resolução de DNS causou (novamente) uma indisponibilidade global dos serrviços da AWS e potencialmente bilhões de dólares em prejuízo.

<https://edition.cnn.com/business/live-news/amazon-tech-outage-10-20-25-intl>

> "O incidente destaca a complexidade e a fragilidade da internet, bem como o quanto cada aspecto do nosso trabalho depende dela para funcionar", disse Daoudi em um comunicado à CNN. "O impacto financeiro dessa interrupção chegará facilmente a centenas de bilhões de dólares, devido à perda de produtividade de milhões de trabalhadores que não conseguem realizar suas tarefas, além de operações comerciais interrompidas ou atrasadas — de companhias aéreas a fábricas."

<https://www.bbc.com/news/articles/cev1en9077ro>

> The places hit by the outage vary significantly. It took out major social media platforms like Snapchat and Reddit, banks like Lloyds and Halifax, and games like Roblox and Fortnite.

<https://www.cnnbrasil.com.br/tecnologia/apagao-global-entenda-a-falha-e-como-funciona-a-aws/>

> Entre os serviços afetados estavam [plataformas populares](https://www.cnnbrasil.com.br/tecnologia/quais-empresas-foram-afetadas-pelo-apagao-da-aws/) como Facebook, Prime Video e o jogo Fortnite. A falha [também atingiu](https://www.cnnbrasil.com.br/tecnologia/especialista-falha-em-servidor-na-america-do-norte-teve-efeito-domino/) dispositivos domésticos conectados, como sistemas de iluminação inteligente, demonstrando o alcance e a dependência atual de infraestruturas em nuvem.

- Aparentemente foi um problema de resolução do DNS (!!!!) que impediu que servidores da AWS acessacem bancos DynamoDB internamente

- ATUALIZAÇÃO: temos o post mortem <https://aws.amazon.com/message/101925/>

- Esse vídeo do LINUX TIPS tb foi bom:

{{#embed https://www.youtube.com/watch?v=ZS4WMx6D8QM}}

##### Por que a AWS tem tanta 'influência' na internet

### Internet das coisas (ruins)

<https://www.404media.co/the-aws-outage-bricked-peoples-2-700-smartbeds/>

- Experimento:
  - Você consegue fazer alguma coisa no seu celular ou computador quando a internet está desligada?
  - Quantos dos seus eletrodomésticos funcionam de maneira "parcial" sem acesso a internet?
  - O aplicativo que você desenvolve tem um modo offline? Como ele poderia ter? Por quê?
