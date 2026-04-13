# O ‘browsergate’ do Linkedin

O Linkedin está sendo alvo de uma ação coletiva na União Europeia com relação ao monitoramento de extensões nos navegadores de seus usuários. O grupo Fairlinked lançou a campanha ‘browsergate’

[https://browsergate.eu/](https://browsergate.eu/ (preview))

[https://www.tudocelular.com/seguranca/noticias/n251726/linkedin-processos-escaneamento-extensoes-chrome.html](https://www.tudocelular.com/seguranca/noticias/n251726/linkedin-processos-escaneamento-extensoes-chrome.html (preview))

- Primeiro queria dizer que o nome tinha que ter Linkedin no meio, quando eu li essa história eu demorei pra entender o que era, achei que tinha algo a ver com os navegadores terem feito alguma coisa

- Sergundo, queria falar pros cínicos de plantão que vão escrever:
  - “Mas todos os sites fazem isso!”
  - “Quando você entra na internet você aceita que todos seus dados vazaram”
  - “Isso não é notícia”

- Eu não gosto de fazer um vídeo se é só pra apontar pra um negócio e não fazer nada, então esse vídeo vai tentar ser:
  - informativo e didático sobre a situação
  - explicar a problemática do Linkedin (e sim, de todas as outras) empresas fazerem isso
  - indicar como navegadores e sistemas operacionais poderiam bloquear isso
  - Será que alguém da ANPD assite o canal? Presta atenção aqui ó

- Outro aspecto importantíssimo é como esses dados são agregados e pra quem eles são vendidos ou compartilhados:
  - Micro$oft e seus parceiros
  - Persona (já falamos sobre isso antes)
  - Uma empresa chamada Human, um grupo de cibersegurança israelense
- Recomendação de vídeo sobre como a agregação de dados funciona para fins comerciais e de vigilância

{{#embed https://www.youtube.com/watch?v=9ffIOt7dpZg}}

### Como funciona essa detecção?

> No momento em que este artigo foi escrito, esse código baixava uma lista de 6.222 produtos de software e forçava a detecção de cada um deles. A varredura cobre extensões com uma base de usuários combinada de aproximadamente 405 milhões de pessoas.

- Quando usuários estão num browser baseado em Chrome (a maioria deles) o Linkedin baixa um script que tenta descobrir as extensões instaladas no navegador ao:
  1. procurar por extensões que expõe canais de comunicação
  2. tentar o carregamento de arquivos usados por essas extensões
  3. verificar modificações comuns que estas extensões fazem no código

- Enquanto o método 1 é uma maneira explicita e esperada das extensões anunciarem sua existência, a 2 e a 3 já extrapolam um limite e talvez navegadores pudessem colocar medidas explícitas para bloquear esse tipo de descoberta.
- Lista de extensões aqui: https://browsergate.eu/extensions/

### Como funciona o ‘fingerprinting’

- Toda vez que entramos em um site nós inadvertidamente compartilhamos algumas informações únicas do nosso ambiente:
  - Tipo de dispositivo e sistema operacional
  - Navegador web e sua versão
  - Linguagem do navegador
  - Hardware (microfone, câmera, GPU)
  - Tamanho da tela
  - Opções do navegador (do not track, javascript desligado)
  - Cookies
  - Extensões

[https://amiunique.org/fingerprint](https://amiunique.org/fingerprint (preview))

- Cada um desses dados não é tão único, podendo milhões de pessoas terem, por exemplo a mesma versão do navegador que a sua, a mesma resolução de tela.
  - Mas juntando alguns deles a probabilidade de que o seu perfil seja único chega a basicamente 100%

#### Extensões de navegador 🤝 seus hábitos

- Agora a parte prática de como essas empresas podem usar isso. Assuma que elas tem:
  - Sua identidade e histórico de emprego (Linkedin)
  - O fingerprint do seu navegador e cookies
  - Partes do seu histórico de navegação, propagandas, informações de redes sociais
  - As suas extensões de navegador, que também revelam:

> - Opiniões políticas dos usuários, por meio de extensões como “Anti-woke”, “Anti-Zionist Tag” e “No more Musk”
> - Crenças religiosas, por meio de extensões como “PordaAI” (desfocar conteúdo haram) e “Deen Shield” (bloqueia sites haram)
> - Deficiência e neurodivergência, através de extensões como “simplify” (para usuários neurodivergentes)
> - Situação empregatícia, por meio de 509 extensões de busca de emprego que revelam quem está procurando trabalho na própria plataforma onde seu empregador atual pode ver seu perfil
> - Segredos comerciais de milhões de empresas, mapeando quais organizações usam quais produtos concorrentes, da Apollo ao ZoomInfo

- Como isso poderia ajudar na venda de produtos? Exposição a conteúdo nas redes sociais? Vigilância de regimes autoritários

### Alou ANPD!!!

- Se uma coisa é ilegal na Europa, não necessariamente é ilegal no Brasil, MAS eu tenho certeza que se olhar com carinho dá pra encontrar diversos problemas com essas práticas do Linkedin aqui
  - E de novo, não são só eles
- Os adevogados aí do xét poderiam olhar isso hein? De repente a gente faz um documentinho pra mandar pra ANPD ou outras agências reguladoras

- Enfim, espero que tenham entendido o problema e aprendido alguma coisa no caminho. Nos vemos na próxima.
