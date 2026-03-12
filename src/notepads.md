# Vulnerabilidades no Notepad.exe e Notepad++

Este vídeo é pra o deleite dos usuários de Linux ou Mac que não entendem como os programadores de Windows sobrevivem com os seus 'primitivos' notepads. Os últimos meses foram brabos

{{#embed https://www.youtube.com/watch?v=OgfdyH4iaps }}

- O que eu vou começar dizendo é que geralmente a dica que sempre damos é 'atualizem seus softwares', mas essa primeira história é foda...
- Em janeiro a Microsoft lançou uma atualização do Windows que ficou famosa por introduzir uma série de bugs. E um deles bastante curioso foi esse:

<https://superuser.com/questions/1933981/notepad-currently-not-available-in-my-account>

- Sim eles fizeram uma atualização do Notepad e essa versão nova vem da loja da Microsoft, sendo daí que veio o erro de permissão para rodar.
  - "Ainda existe a versão legada"
  - Eles "corrigiram" isso depois, maaas...
- Mas quais features teriam eles colocado no Notepad velho de guerra:
  - Suporte a renderizar Markdown
  - Integração com IA
- Os links de markdown tem um problema comum que é o seu texto ser diferente do que o link \[<https://microslop.com](https://sitecomvirus.com)>
- Porém foi um pouco pior que isso porque os links eram abertos com o `iexplore open LINK` e isso permitia a injeção de comandos dependendo do que se colocasse ali
- Por sorte não é mais possivel instalar arquivos `.msi` usando esse tipo de comando, porém um exploit em que você baixa um `.exe` malicioso e clica num link dentro do notepad poderia causar problemas
  - O problema está presente das versões **11\.0.0** até **11\.2510**

### Já o notepad++

- Por incrível que pareça eu tinha ouvido falar sobre o problema de segurança no notepad.exe, o clássico, e tinha achado que era esse aqui, não era.

**Patches de atualização do Notepad++ ficaram comprometidos por seis meses:**  hackers invadiram o servidor de hospedagem e passaram a redirecionar o  download do update para um instalador malicioso, que era executado como  se fosse uma nova release normal. A campanha teria afetado um número  limitado de vítimas entre junho e dezembro de 2025. O problema já foi  mitigado e recomenda-se atualizar manualmente o editor para a versão  mais recente. As informações são do site The Register.

<https://arstechnica.com/security/2026/02/notepad-updater-was-compromised-for-6-months-in-supply-chain-attack/>

{{#embed https://www.youtube.com/watch?v=C8wKomo4Wds }}

- Basicamente a maneira como o updater buscava um nova versão não usava criptografia e nem verificava a assinatura do arquivos `.exe` ao executar
- Permitia que um atacante interceptando o trágefo de um computador atualizando o notepad++ substituísse o executável
- Na realidade um pesquisador começou a suspeitar do problema em dezembro de 2025, mas não sabia exatamente qual era o vetor de ataque. Apenas que o atualizador do notepad++ parecia estar dando origem a processos de `curl`, `whoami` e todo tipo de comando suspeito.

  <https://doublepulsar.com/small-numbers-of-notepad-users-reporting-security-woes-371d7a3fd2d9>
- O que chamou atenção nessa história é que não foi explorado em quantidade, foi um negócio metódico atrás de um pequeno número de usuários que tiveram suas máquinas comprometidas por atacantes 'hands on'
- Está rolando por aí a teoria de que seriam 'hackers chineses', eu não sei exatamente qual a evidência. Se imagina que foi um 'estado nação' que fez pela complexidade do ataque, alvos reduzidos e pelo notepad++ ter apoiado a independência de Taiwan e se posicionar contra a Rússia na invasão da Ucrânia.
  - Não encontrei quem teriam sido os potenciais alvos e talvez isso deixe mais claro.
- A primeira versão segura é **8\.8.8**, mas os devs mandaram instalar pelo menos a **8\.9.1** diretamente do site.

> O Notepad++ há muito tempo atrai uma base de usuários grande e fiel por oferecer funções não disponíveis no editor de texto oficial do Windows, o Bloco de Notas. As recentes iniciativas da Microsoft para integrar a inteligência artificial Copilot ao Bloco de Notas impulsionaram ainda mais o interesse pelo editor alternativo. Infelizmente, como acontece com muitos outros projetos de código aberto, o financiamento do Notepad++ é insignificante em comparação com a dependência que a internet deposita nele. As deficiências que possibilitaram o compromisso de seis meses poderiam ter sido facilmente identificadas e corrigidas se houvesse mais recursos disponíveis.

- É mole?
