# MSG Gov não é um WhatsApp brasileiro

Recentemente foi lançado um aplicativo de mensagens estatal, em parceria com a ABIN e Universidade Federal do Ceará. Está sendo reportado como WhatsApp brasileiro, mas é diferente, vamos falar sobre. 

- E saiu extensivamente na mídia como o ‘WhatsApp do governo’:

[https://exame.com/tecnologia/abin-regulamenta-msg-gov-app-de-mensagens-para-funcionarios-publicos-deixarem-o-whatsapp/](https://exame.com/tecnologia/abin-regulamenta-msg-gov-app-de-mensagens-para-funcionarios-publicos-deixarem-o-whatsapp/ (preview))

> O MSG Gov não é liberado ao público: pode ser baixado normalmente nas lojas de aplicativos, mas o acesso depende de credenciais específicas.
>
> Por ora, atende ao Sisbin, mas a ambição declarada do governo é maior, a ideia, ainda sem prazo definido, é transformar o aplicativo na ferramenta oficial de comunicação de toda a administração pública federal, não apenas da comunidade de inteligência.
>
> …
>
> A ideia não é original: países como a França, com o Tchap, e a Alemanha, com o BundesMessenger, já adotam solução parecida havia anos.

- Termos de uso do MSG Gov 

https://web-dvcom.df-1.estaleiro.serpro.gov.br/termos-de-uso

> O msg gov é um conjunto de aplicações - operadas em caráter experimental  - oferecidas pelo governo federal do Brasil para uso em comunicações  seguras no interesse da Administração Pública brasileira. As aplicações  permitem troca de mensagens de texto, chamadas de voz e vídeo, envio de  documentos, organização de grupos, entre outras funcionalidades.
>
> O msg gov  utiliza criptografia ponto a ponto desenvolvida pelo Centro de Pesquisa  e Desenvolvimento para Segurança das Comunicações da Agência Brasileira  de Inteligência (CEPESC/ABIN), resultado de mais de quatro décadas de  pesquisa e desenvolvimento. A criptografia utilizada garante a segurança  das comunicações, principalmente em assuntos sensíveis que possam  envolver, por exemplo, segurança pública, defesa nacional, segurança do  Estado ou atividades de investigação e repressão de infrações penais.

- Tudo que se encontra na internet são cópias do anúncio oficial e vídeos de ancap maluco debochando e dando informação errada:

- O aplicativo está presente nas lojas de aplicativo, porém não funciona sem conta autorizada do gov.br
  - Fico me perguntando se não era melhor ser um app de escopo privado, porque a confusão persiste lá nos comentários

[https://play.google.com/store/apps/details?id=br.gov.comunicacaosegura&hl=pt](https://play.google.com/store/apps/details?id=br.gov.comunicacaosegura&hl=pt (preview))

- Então sobre o aplicativo em si o que é importante entender é que ele não é um aplicativo para uso geral a curto e nem médio prazo
  - Ele serve pra ministro do STF não conseguir mandar mensagem pro Vorcaro do telefone de trabalho

- Como a criptografia funciona? Não sabemos ao certo… aqui vai algumas ESPECULAÇÕES
  - Um nível “comercial” + um nível de “estado”
  - Isso parece indicar que será um esquema de criptografia com uma espécie de backdoor para auditoria estatal
  - Criptografia “normal” só que com um órgão ou algum nodo capaz de acessar os dados não é um esquema seguro e privado “de verdade”, mas conceitualmente a ideia é ser uma ferramenta do serviço público
  - Se estiverem se perguntando como isso vai funcionar, eu sempre lembro do suposto esquema do “grupo de três pessoas” que pode ser usado em apps E2EE

- Mas daí eu me perguntei se a gente tem como saber mais detalhes técnicos do app?
- E eu descobri algumas coisas:
  - Rodando provavelmente na “nuvem soberana” da SERPRO
  - Implementado sobre o protocolo aberto Matrix
  - Com o algoritmo de criptografia próprio e pós quântico implementado em Rust (tinha que incluir)

- Onde eu achei isso? Tem um site do Insight Lab da UF do Ceará com algumas informações e entrevistas:

[https://www.insightlab.ufc.br/coordenador-do-insight-lab-e-homenageado-pela-abin-durante-seminario-sobre-inteligencia-e-soberania-digital/](https://www.insightlab.ufc.br/coordenador-do-insight-lab-e-homenageado-pela-abin-durante-seminario-sobre-inteligencia-e-soberania-digital/ (preview))

[https://www.insightlab.ufc.br/professor-jose-macedo-fala-sobre-o-msg-gov-em-entrevista-ao-programa-questao-de-ordem-da-alece/](https://www.insightlab.ufc.br/professor-jose-macedo-fala-sobre-o-msg-gov-em-entrevista-ao-programa-questao-de-ordem-da-alece/ (preview))

- E também porque palestras sobre o projeto vão ser apresentadas na conferência do Matrix:

[https://cfp.2026.matrix.org/matrix-conference-2026/talk/LNVNTW/](https://cfp.2026.matrix.org/matrix-conference-2026/talk/LNVNTW/ (preview))

[https://cfp.2026.matrix.org/matrix-conference-2026/talk/TZ8ZYX/](https://cfp.2026.matrix.org/matrix-conference-2026/talk/TZ8ZYX/ (preview))

- Eu acho fascinante estudar a infra de sistemas assim e eu tenho certeza que rola um medo de revelar detalhes para o público geral, mas lembrem-se que o sistema mais seguro é aquele que permanece seguro mesmo que se saibam seus detalhes internos de implementação

- Talvez a gente pudesse tentar fazer uma investigação maior depois de rolar essas palestras
  - e quem sabe no futuro algo sobre o PIX??

- É isso pessoal, vlw
