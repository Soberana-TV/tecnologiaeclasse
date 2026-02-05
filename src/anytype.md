# O Tutorial do TeClas sobre Anytype

Hoje eu quero fazer uma introdução a um dos meus softwares favoritos que se chama Anytype. Ele é um app de notas que engloba características de organização, descentralização, com low code e privacidade.

### O que é o Anytype

> Anytype is an **encrypted, local-first alternative** to the cloud-based Internet.

- O Anytype é um aplicativo de notas com Markdown e edição em blocos. Mas seguindo o modelo 'Notion' nós podemos criar relacionamentos e propriedades para essas páginas permitindo com muito pouco esforço criar aplicações inteiras para organizar dados complexos
- Os dados são guardados de maneira local primeiro e são trocados por um protocolo criptografado que permite um total controle do usuário sobre quem tem acesso além de permitir o uso self hosted ou totalmente offline
- O cliente é aberto e o protocolo, chamado Anysync, também é aberto.

### Por que eu acho esse projeto interessante?

{{#embed https://www.youtube.com/watch?v=KXiQlLHuK7g }}

- Lá pelo final de 2024 eu devo ter visto esse vídeo e eu andava pensando muito na depêndencia que as pessoas tem do Notion como uma plataforma de organização, com muitas empresas chegando a ter o seu backend inteiro organizado por ele
- Hoje apps como Notion, mas também Slack, Discord e etc... são usados como ferramentas de construção da web e de fato são muito úteis. Porém isso cria uma 'dark web', não indexada publicamente, e geralmente proprietária.
- O Notion hoje com texto, hiperlinks, propriedades e os seus 'bancos de dados' (que são tabelas glorificadas) inaugurou uma nova maneira de montar sites na web e é extremamente importante que exista uma versão aberta (e portante superior) dele.

- Eu estou colocando isso logo no início do tutorial porque eu acho mais importante começar a aprender uma ferramenta pensando nas vantagens e nos objetivos que temos ao invés de meramente nas capacidades técnicas

### Como eu tenho usado?

- Como um aplicativo de notas pessoais
- Como um banco de dados para ideias e para gerenciar projetos, sugestões, contatos e requisições do canal

- Como um organizador de livros, referências e coisas que quero estudar

### A documentação do Anytype

<https://doc.anytype.io/anytype-docs/>

### Como o protocolo funciona?

- Para usar você cria uma 'conta' que nada mais é do que uma chave privada que encripta os seus dados
  - Essa 'frase chave' é sua senha ao mesmo tempo que é a sua conta e deve ser guardada com cuidado.
  - Essa chave vai encriptar/desencriptar os seus dados na rede do Anytype
- Todas as suas edições de blocos são encriptadas e guardadas localmente. Em seguida elas são sincronizadas para um nodo da rede
  - Permite acesso remoto aos seus dados e colaboração
  - Apenas você e pessoas autorizadas pode desencriptar esses dados
  - Nodos de sincronização não tem acesso aos dados
- Por padrão você está conectado com a rede do Anytype que oferece 1GB de espaço e limites de colaboradores por espaço gratuitamente
  - Você pode mudar para o modo 'somento local' que sincroniza apenas com o seu computador e rede local
  - Ou pode autohospedar um nodo de sincronização e gerenciar o espaço você mesmo

**Mais em:** <https://doc.anytype.io/anytype-docs/advanced/data-and-security/how-we-keep-your-data-safe>

### Tutorial prático

- Criando páginas e escrevendo markdown
- Criando links e listas
- Propriedades dos objetos
- Diferentes visualizações para objetos
  - Kanban
  - Calendário
  - Grafo

- Queries e coleções

### Por que se chama Anytype?

- A parte mais interessante e que geralmente vocês não vão ouvir muito nos tutoriais (é difícil de explicar) é a possibilidade de criar tipos, templates e visualizações para os dados
- Com isso é possível construir pequenas aplicações e MVPs para o seu caso de uso de uma maneira 'low code'

### Usar um template pronto

- O Anytype oferece uma 'biblioteca de templates' de espaços do Anytype já prontos e customizados para aplicações específicas.
- Eu falei isso aqui mais pro fim do tutorial porque depois de entender um pouco melhor o que o Anytype faz fica mais claro como são úteis os templates.

### Colaboração com outros usuários

- Você pode chamar mais pessoas para colaborarem num espaço anytype.
- Cada nova pessoa aparece como um perfil dentro do espaço e pode ser adicionada como propriedade em campos como 'autor' / 'responsável' e etc...
- Recentemente o Anytype incorporou um chat a cada espaço, permitindo que toda colaboração seja feita lá por dentro
- Eu não tenho usado isso, mas agora a gente tem o potencial de substituir um Slack + Notion ao mesmo tempo e parece muito legal
- Você também pode compartilhar páginas do seu espaço como sites html usando o botão de 'Publish'

### Segurança

- Como eu disse no início os seus dados ficam encriptados na sua máquina e nos nodos de sincronização
- Porém o acesso a sua máquina ainda pode dar acesso aos seus dados, principalmente se a conta estiver desbloqueada.
- Então eu recomendo muito que quem se preocupa com segurança ative um PIN para a conta local e coloque um limite de tempo para que o Anytype se feche

### Como autohospedar

- Como citado anteriormente, é possível autohospedar o seu servidor para sincronizar entre diferentes clientes e não depender da rede padrão do Anytype. Além de poder gerenciar o espaço disponível pra sincronização.
- Para se juntar a uma rede autohospedada você precisa fazer o logout da rede padrão e criar uma nova chave nessa rede (isso é chato, eu sei)
- Todos os espaços e dados podem ser facilmente exportas/importados entre redes, só é chato

- O processo de autohospedagem em sim está fora do escopo desse tutorial, mas é relativamente fácil pra quem manja da parte mais técnica de servidor e GNU/Linux.

**Mais info aqui:** <https://doc.anytype.io/anytype-docs/advanced/data-and-security/self-hosting/self-hosted>

**Projeto útil pra quem quer testar:** <https://github.com/grishy/any-sync-bundle>
