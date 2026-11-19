# Optimizely, nginx2root, java4shell e mais

Ficou fácil demais invadir sistemas. Sim é por causa das ferramentas de IA, mas é extremamente entediante e mundano. Temos muitas vulnerabilidades, muito rápido e ainda trabalhamos 90% do tempo fazendo novas features e 10% do tempo correndo para patchear as coisas.

**Veja também no canal:**

{{#embed https://youtube.com/watch?v=6vO-DrXvaPY}}

### Avisos de segurança

- nginx2root: <https://nginx2root.com/>
  - atualizar ou mitigação: desabilitar http2
- java4shell: <https://calif.io/java4shell>
  - atualizar ou mitigar (tem umas features do base64 que podem ser desabilitadas)
- \*sshole: <https://sshhole.com/>
  - presente em ssh rodando em ambientes com a musl ao invés de libc (geralmente containers alpine)
  - atualizar ou mitigar
- GTA6: Aproveitando pra falar para vocês, não existe AINDA versão pra PC do GTA 6. Por favor não baixem e instalem um .EXE do MediaFire de 72MB. É mentira.

### Mais um ataque na cadeia de suprimentos:

- Quero começar MESMO falando sobre mais um ataque da cadeira de suprimentos, dessa vez tendo como alvo a plataforma Optimizely usada para testes A/B

[https://arstechnica.com/security/2026/11/malicious-code-delivered-through-optimizely-hits-visitors-to-hundreds-of-sites/](https://arstechnica.com/security/2026/11/malicious-code-delivered-through-optimizely-hits-visitors-to-hundreds-of-sites/ (preview))

- 188 sites de 178 organizações foram afetados. Incluindo **Zoom, BBC, CNN, Salesforce, GitLab, IKEA, HSBC, Equifax, Air France-KLM, Ledger e Peacock**

> A Optimizely disponibiliza “trechos” (snippets) de código JavaScript que contêm tanto o código da própria empresa quanto o código fornecido por cada cliente. Esse JavaScript — que pode ser disponibilizado diretamente pela Optimizely ou a partir de um endpoint do cliente — é executado em todas as páginas que o cliente disponibiliza. De alguma forma, os invasores inseriram seu próprio código em uma parte do JavaScript de cada cliente afetado e, em seguida, fizeram com que ele fosse entregue a partir de cdn.optimizely.com. O JavaScript estava assinado com um certificado válido para esse domínio.

- O mais irônico é que, como um bom script malicioso, o código era servido em várias etapas especificas para cada tipo de dispositivo: 

> 1\. Crypto wallet address swapping
>
> 2\. Card skimming
>
> 3\. Cookie and screenshot theft
>
> 4\. The DarkSword and Coruna exploit kits for iOS

- O sistema da Optimizely teria sido comprometido por causa de uma falha no processo de registro de novas contas deles. Foi essa CVE aqui:

[https://nvd.nist.gov/vuln/detail/cve-2026-132224](https://nvd.nist.gov/vuln/detail/cve-2026-132224 (preview))

- Lista completa dos projetos: <https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/>

- Teve um exemplo bem mais próximo de casa de um ataque assim esses dias, passou batido porque não sou canal de infosec, 

- A loja virtual Convertr estava servindo um malware em um de seus scripts de carrinho de compras: <https://x.com/namcios/status/2115056992792252484>

[https://canaltech.com.br/seguranca/hackers-escondem-codigo-que-rouba-cartao-e-cpf-de-quem-compra-em-lojas-de-moda-no-brasil/](https://canaltech.com.br/seguranca/hackers-escondem-codigo-que-rouba-cartao-e-cpf-de-quem-compra-em-lojas-de-moda-no-brasil/ (preview))

- O ataque teria ficado ativo pelo menos de 24/10/26 até 27/10/26 e era, como no caso acima, um card skimmer

- Esse último trimestre de 2026 talvez seja lembrado como o momento que a balança de segurança finalmente quebrou. Eu basicamente não tenho mais banda aqui no canal pra fazer vídeo falando sobre 10% das coisas:
  - Fica a recomendação do Mano Deyvin que tá de parabéns porque está fazendo um trabalho melhor que eu aqui

{{#embed https://youtube.com/watch?v=1hCS9oOcy54}}

- Dava pra gente parar de adicionar novas features agora e ficar corrigindo só as falhas de segurança + endurecer as medidas de segurança e mesmo assim a gente ia estar fodido
  - Eu sei que parece pros desenvolvedores que estamos vivendo o caos no último ano, mas ainda não me parece que afetou DE VERDADE o resto da sociedade
  - Eu não tiro de questão que possamos viver uma nova “pandemia global” por causa de um conjunto de falhas tão grande a gente seja OBRIGADO a parar

- Eu fico pensando no que precisaria acontecer pra todas as empresas terem que parar e inverter a lógica de adicionar mais código e features e corrigir o que já existe:
  - Mesmo isso ia ser muito complicado porque mexer no que já tá funcionando sempre vai ser tênue. Quando faz uma obra sempre vai sair os ratos e baratas.
  - Pensem nos EUA que resolveu atualizar o sistema de controle de vôos
