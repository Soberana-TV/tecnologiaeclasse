### O que é preciso para ter um smart phone “abertolivre” de verdade?

Desde o vídeo de ontém, onde falamos sobre o MSG Gov, eu fiquei me perguntando tudo que falta para um aplicativo “soberano” num telefone Android. Esse vídeo é uma discussão inicial sobre.

- Além disso o Google está no processo de implementar a sua nova política de cadastro de desenvolvedores e mais restrições na distribuição de apps:

[https://keepandroidopen.org/](https://keepandroidopen.org/ (preview))

- Então quem sabe EU poderia fazer uma pesquisa e achar uma maneira de usar o meu telefone sem Android / sem Google?

- Com certeza o “Android” (na realidade AOSP) aberto que a gente mais ouve falar é o GrapheneOS

[https://grapheneos.org/](https://grapheneos.org/ (preview))

- Mas na realidade existem dezenas de distribuições alternativas além do GrapheneOS. Por exemplo: OpenHarmony, Murena, SailOS, LineageOS e muito outros (nem tudo é o mesmo tipo de coisa)

- Porém migrar para usar um sistema desses não é nada trivial (é bem nostálgico porque me lembra de migrar pra usar um Linux a uns \~15 anos atrás)

### Dificuldades que temos pelos caminho:

- Partes do sistema operacional que não funcionam sem o Google ou um terceiro entranhado no sistema:
  - Aplicativos “padrão” como mapas, emails, tradução e etc… dependem do Google, fabricante ou serviços externos
  - Distribuição, autenticação e validação de APKs
  - Notificações push
  - Drivers, firmwares, qualquer tipo de interação proprietária com hardware

- A maior parte das soluções que existem vão falhar em algum ponto específico ou só conseguem fazer todo o necessário em algum hardware muito específico…

- Além disso, temos uma resistência institucional, por motivo de “segurança”, em homologar aplicativos como por exemplo de bancos, para funcionarem com root / sem os GMS ou GApps

- E a legislação contra celulares / dispositivos sem medidas de “segurança”

https://cybernews.com/privacy/atlanta-man-border-search-prosecuted-grapheneos/

### Mas isso sou eu como indivíduo…

- E se a gente tivesse o apoio institucional em conjunto?
  - Se te pedissem para organizar um projeto de “smart phone seguro” da tua empresa
  - Se o estado brasileiro quisesse fazer um “Android 2” 

- Aí a coisa muda um pouco de figura porque não precisamos trabalhar com qualquer hardware, poderíamos fazer uma compra de um específico ou encomendar de algum fabricante

- Não precisamos trabalhar com o conceito de app store global, mas sim com a necessidade de distribuição interna para uma base de usuários menor

- Não precisamos de suporte global a aplicativos e serviços, mas apenas aos que são necessários para a tarefa específica.

- Esse é um escopo que, por exemplo, uma agência do governo poderia trabalhar para uma migração onde realmente usamos apenas o AOSP

- O foco no trabalho é interessante pra mim. Por mais que odiemos isso, as ferramentas do dia a dia de trabalho modal as nossas preferências fora do trabalho.
  - A adoção voraz da IA em todo o mercado de trabalho é, na minha opinião, o que tem normalizado a aceitação dessas ferramentas no nosso dia a dia

- Então em conclusão, eu acho que existe uma área enorme a se explorar aqui:
  - Temos dezenas de projetos de OS aberto para celular que podem ser a base para algo assim
  - Temos uma “checklist” de coisas que precisamos implementar ou exigir das big techs
  - Isso pode ser a base para uma legislação para o “desbloqueio” dos aparelhos.
    - “é preciso integrar servidores externos de push, é preciso autenticar aplicativos de lojas externas, é preciso integrar serviços de mapas abertos, etc…”

- É uma ideia bem inicial, mas acho que se desenvolvermos dá pra imaginar o nosso Brasdroid. O que acham?
