# Nightmare Eclipse é o pior pesadelo da Micro$oft

Uma pessoa misteriosa está se tornando o pesadelo da Microsoft nos últimos meses. Toda semana uma revelação de falha de segurança nova e a promessa de que 14 de Julho vai sair algo grande. Isso é o que sabemos até agora sobre ‘Nightmare Eclipse’.

- Eu vou contar pra vocês tipo uma fofoquinha por que eu não sou um pesquisador da área de segurança e não vou entrar nos detalhes mais técnicos, mas vou deixar uns links aqui no roteiro

[https://blog.barracuda.com/2026/05/19/nightmare-eclipse-zero-days-grudge](https://blog.barracuda.com/2026/05/19/nightmare-eclipse-zero-days-grudge (preview))

- Umas semanas atrás eu falei muito de falhas de segurança no Linux, mas é por que eu amo, eu uso, represento. As falhas do Windows não me interessam tanto… mas além de utilidade pública essa história aqui é quente

- Essa pessoa chamada ‘Nightmare Eclipse’, as vezes ‘Chaotic Eclipse’, está liberando várias falhas de segurança 0-day no Windows desde Abril/26 e prometeu uma ‘revelaçāo’ maior no dia 14 de Julho…
  - Documentos internos da Microsoft?
  - Um exploit com RCE?

- Algumas coisas que já foram liberadas:

> - BlueHammer — Blue is Microsoft's brand color, and a hammer is a blunt-force tool. This is about hammering Microsoft's own branded product.
> - RedSun — Red signals danger. This exploit sheds light on Microsoft Defender's flaws through a different code path than BlueHammer.
> - UnDefend —A portmanteau that mocks Windows Defender directly: un-Defend, as in making Defender unable to defend.
> - YellowKey — Yellow signals caution, and the key references unlocking BitLocker-protected drives.
> - GreenPlasma — Green signals go/execution. Plasma suggests energized power — gaining elevated privileges.
> - Mini Plasma

- O exploit YellowKey chamou muita atenção, uma maneira de quebrar a criptografia de disco da oficial da Microsoft, o BitLocker, apenas espetando um USB batizado
  - Na realidade parece uma função de debug que desbloqueia o disco sem precisar da chave… basicamente um bypass do bitlocker e que só funciona no Windows 11… Suspeito

> 99% leigos ficando sem acesso aos seus dados e 1% FBI acessando por um backdoor

- Por que essa pessoa faria isso? Segundo Nightmare Eclipse, existe um histórico da MSRC não ter pago as recompensas, terem exigido tempo de disclosure e não dado crédito, mudado os termos dos pagamentos e etc…

- De novo, eu não trabalho no campo, mas já ouvi diversos relatos que o trabalho de achar bug bounties como ‘pesquisador de segurança’ pode ser muito inglório e as vezes perigoso também. Essa história tende a confirmar isso, embora só tenhamos o lado da pessoa com avatar de anime.

- Mas em resumo, não tem incentivo financeiro, nem whitehat nem blackhat. Basicamente essa pessoa odeia muito a Microsoft… e não falta motivo

[https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure](https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure (preview))

- A conta de ‘Nightmare Eclipse’ foi banida do Github (controlado pela Microsoft) e do Gitlab e na postagem da Microsoft tratando da situação todo mundo entendeu que tem ameaças diretas à pesquisadora.

- E por fim o que muito gente tá especulando é que tem um historico aí, talvez alguém que já trabalhou ou foi terceirizada lá na MS. O que deixa o dia 14/07/26 mais interessante…

- Mas em resumo é essa fofoca. Curioso que começaram esses lançamentos de vulnerabilidades em Abril e no dia 1 de Abril temos o vídeo do TeClas “pq odiamos a Microsoft” não é mesmo?

{{#embed https://www.youtube.com/watch?v=RcMClWI_GnA }}

- Pergunta pro xét: qual nome errado da Microsoft vocês preferem?
  - O clássico “Micro$oft” ?
  - O moderno “microslop” ?
