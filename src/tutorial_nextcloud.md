# Tenha seu próprio Nextcloud (estilo homelab ;)

No vídeo de hoje vamos fazer uma apresentação e tutorial do Nextcloud e eu vou demonstrar como eu estou rodando um dentro do meu homelab para gerenciar os meus dados pessoais.

### O que é o Nextcloud?

[https://nextcloud.com/](https://nextcloud.com/ (preview))

- Nextcloud é uma plataforma de software aberto concorrente ao Microsoft 365 ou o Google Drive
  - Arquivos (com sincronização automática)
  - Calendário e contatos
  - Vídeo Conferência
  - Integração com Collabora, OnlyOffice e outros projetos populares
  - E um sistema de plugins…

- O projeto surgiu de um fork do Owncloud em 2018 e começou a se desenvolver bem a tempo do do COVID-19 e o trabalho remoto

- É um projeto relativamente novo, surgido na Alemanha, e o Trump 1 e agora o Trump 2 tem feito a adoção dele pela União Europeia acelerar muito (e obviamente eu sei que muita gente tá usando no Brasil)

- É muito interessante como ele realmente agrega muito dos melhores projetos e iniciativas de software livre e é bastante customizável
  - Eu tenho usado ele nos vídeos do canal nos últimos 2 anos e vocês devem ter notado as mudanças durante o tempo

- Sim isso aqui que eu estou usando é um Nextcloud e ele está rodando detro de um mini computador que está na minha sala

- Eu estou usando ele para as notas, compartilhamento de documentos importantes, os meus ebooks e etc… vou fazer um demo de como o canal TeClas é feito mais tarde

### Como instalar:

[https://nextcloud.com/install](https://nextcloud.com/install (preview))

- Temos vários métodos de instalação e é um projeto relativamente complexo. 
  - Neste vídeo eu vou mostrar como fazer a instalação como um Ubuntu Snap
  - O método com docker-compose que é o “aio-docker” é a maneira mais fácil de fazer o setup num servidor com um endereço e certificado

- O objetivo hoje é instalar ele num computador local seu, customizar o seu espaço e etc…

- Não vamos ter o caso de uso mais avançado de servidor, segurança e etc…
  - Convença seus amigos da TI a fazerem um servidor pra vocês 🙂 

### Customizando a sua instalação

- Aparência
- Usuários
- Extensões

### Sincronização de arquivos automática

- Usando o Webdav (exemplo do ZorinOS)
- Usando o cliente Nextcloud Sync

### Coisas avançadas que eu queria ter descoberto logo no início

- Os arquivos da versão snap ficam em:
  - /var/snap/nextcloud/common/nextcloud/  
- O arquivo de configuração fica em:
  - /var/snap/nextcloud/current/nextcloud/config/config.php  
- Comando nextcloud.occ permite fazer várias coisas pela linha de comando (ou automatizar)
- Leia a documentação do snap e todos os seus comandos aqui https://github.com/nextcloud-snap/nextcloud-snap
- Otimizar as configurações do php vai fazer o seu Nextcloud rodar muito melhor:
  - Por exemplo o memory-limit, max-execution-time , post-max-size e o upload-max-filesize me ajudaram a acelerar (ou destravar o webdav)

### Segredos do Nextcloud do Canal TeClas

- Como eu uso o app de notas
- O aplicativo de fotos que eu testei (e desisti)
- As customizações de fontes e de cores
- A minha biblioteca de ebooks sincronizada com o Calibre

### Melhorias para o futuro

- Realmente usar o calendário e agregar meus compromissos

- Sistema de backups realmente funcional

- Melhor integração com outras partes do homelab?

- Segurança, setup em servidor, yadda yadda

### Conclusão

- Espero que esse vídeo seja um pontapé inicial para quem quer testar o Nextcloud e outros softwares livres para fugir da experiência padrão dentro das bigtechs

- Comentem se estão usando o Nextcloud ou algum outro software parecido e como estão fazendo isso.

- Ideias, críticas e sugestões? Valeu!

### Referências

- Para quem quer um tutorial de instalação num servidor ‘do 0’ e realmente aprender o que cada componente faz. Experimentem esse vídeo 

{{#embed https://www.youtube.com/watch?v=TGsGalCOl2k }}

