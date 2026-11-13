# Tutorial de Jellyfin

Hoje vamos finalmente fazer aquele tutorial inicial de Jellyfin. Tenha seu próprio servidor de mídia para organizar suas músicas e filmes, rodando como um “Netflix” privado na sua rede local.

**Veja também no canal:**
{{#embed https://www.youtube.com/watch?v=vWUWZpDP63E}}

[https://jellyfin.org/](https://jellyfin.org/ (preview))

### O que é?

> O Jellyfin é um servidor de mídia e um conjunto de aplicativos multimídia, gratuitos e de código aberto, projetados para organizar, gerenciar e compartilhar arquivos de mídia digital com dispositivos conectados a uma rede. O Jellyfin consiste em um aplicativo servidor, instalado em uma máquina que utiliza Linux, Microsoft Windows ou macOS, e um aplicativo cliente, executado em dispositivos como smartphones, tablets, smart TVs, reprodutores de mídia para streaming, consoles de videogame ou por meio de um navegador da web. O Jellyfin também pode transmitir conteúdo para dispositivos compatíveis com DLNA e Chromecast.

### Por que Jellyfin e não Emby, Plex, Navidrome ou <X>

- No geral, porque **eu** gosto mais. O Emby e o Plex tem modelos de monetização baseado no uso do servidor e assinaturas por isso descartei eles.
  - Nada contra a necessidade de monetização, mas me parece que esse tipo de modelo pode comprometer a privacidade dos usuários
- O projeto tem uma comunidade ativa e vibrante focada em soluções abertas
- O resto eu não tenho experiência nenhuma, então façam sua própria pesquisa e usem o que acharem melhor. 

### Como eu uso?

- Para tocar, arquivar e atualizar metadados da minha coleção de música de 20+ anos
  - Acesso pelo navegador, programas ou apps de celular para tocar
- Para organizar a coleção de filmes e series em formato digital
  - Principalmente acesso pelo navegador ou apps de smart tv para tocar

### Como instalar? Quais são os requisitos?

- Geralmente os requisitos de hardware são modestos:
  - Uns 100gb de espaço em disco para cache, logs e arquivos de transcodificação
  - De preferência alguma placa gráfica (pode ser onboard) para transcodificação
  - Um HD ou volume na rede para os arquivos de mídia
  - “Um computador não muito antigo”

[https://jellyfin.org/docs/general/administration/hardware-selection/](https://jellyfin.org/docs/general/administration/hardware-selection/ (preview))

- No meu primeiro vídeo sobre homelabs eu recomendo o uso de um laptop pelo perfil menor de consumo e a praticidade. Mas se vocês quiserem podem usar um raspberry PI ou fazerem um setup num computador em nuvem:

{{#embed https://youtube.com/watch?v=wxl4K_L9qLQ}}

- Para instalar (pela primeira vez tem um tutorial “de Windows” aqui):

[https://jellyfin.org/docs/general/installation/](https://jellyfin.org/docs/general/installation/ (preview))

- Instalação para Linux com o script (eu no meu homelab agora estou movendo tudo pra docker compose, mas fica pro futuro mostrar isso):

> curl -s <https://repo.jellyfin.org/install-debuntu.sh> -O && \
> curl -s <https://repo.jellyfin.org/install-debuntu.sh.sha256sum> -O && sha256sum -c install-debuntu.sh.sha256sum
>
> sudo bash install-debuntu.sh

- Acesse `http://SEU_IP:8096` e finalize o processo

### Corrigir permissões no Linux:

> sudo usermod -a -G $USER jellyfin  
> sudo setfacl -m u:jellyfin:rx /pasta/pai  
> sudo setfacl -m g:jellyfin:rx /pasta/pai

### Usando o Jellyfin:

- Conta de admin
- Menu de administração
- Adicionando pastas com mídia
- Escaneando a biblioteca de mídia
- Gerenciando usuários
- Sistema de plugins

### Clientes de música

- Feishin: um clone da interface modernosa estilo Spotify + recomendações e letras integradas <https://github.com/jeffvli/feishin>

- Supersonic: um player honesto e levinho com tudo que é você precisa <https://github.com/dweymouth/supersonic/>

- Finamp: Um player pra Android/iOS e Desktop com uma interface bonita, recomendações, letras, filas e etc… <https://github.com/finamp-app/finamp>

### Aplicações Jellyfin para TVs e celular

- Para consumir mídia nas suas smart tvs é possível usar o navegador integrado e logar no seu servidor Jellyfin

- Muitas smart tvs também possuem aplicativos Jellyfin em suas respectivas lojas
  - TVs desbloqueadas também permitem a instalação de aplicativos Jellyfin com mais funcionalidades ainda (mas eu não vi necessidade)

- Para celular é possível também usar o navegador e apps nativos. O F-DROID tá lotado de aplicativos, mas o que me serviu foi o Findroid

### Outras dicas:

- Para acessar de fora da sua rede local eu recomendo muito um Netbird ou Tailscale. A mídia funciona sem precisar configurar nenhuma porta do roteador então pra mim é 10/10

{{#embed https://youtube.com/watch?v=ZapFOyutsis}}

- História: na casa de uns amigos eu até consegui usar `socat` pra direcionar a porta 8096 do meu servidor pra 8096 do meu laptop e acessar meu servidor na TV dos outros 👍 

- Quick Connect: para logar rapidamente em TVs e outros dispositivos sem digitar a senha. Clique na opção ‘Quick Connect’ no dispositivo e vá no seu dispositivo já logado

- É possível usar o menu de administração e alguns aplicativos pra controlar TV/Desktop remotamente e ou instalar aplicativos de controle remoto

- Organizar tags, fotos e letras de álbuns: no geral o Jellyfin é bem conservador em buscar e modificar dados das suas músicas, aqui vão algumas dicas:
  - Plugin do lyric db
  - Diretórios como `[Artista]/[Ano] - [Álbum]/[Faixa] - [Título]` ajuda
  - Imagens “logo”, “folder” e “backdrop” são usadas pra página do artista
  - Imagem “cover” no diretório do álbum é usada como capa
  - Use o <https://musicbrainz.org> para álbuns não identificados
    - Menu ‘…’ → Identify e coloque o id do álbum
    - As vezes você vai ter que editar as tags na mão e tatu do bem

- Plugins recomendados pelo Hiago (mais aqui <https://github.com/awesome-jellyfin/awesome-jellyfin#-plugins>)

> \* Intro Skipper: Detecta e coloca uma opção de pular abertura das séries que vc adiciona no seu catálogo <https://github.com/intro-skipper/intro-skipper>
>
> \* DLNA: Serve só pra adicionar o Jellyfin como uma opção de DLNA na sua rede, fazendo com que funcione com vários dispositivos que tem função de navegar por mídias na rede, como o PS4 que não tem app de Jellyfin, mas tem essa opção de DLNA pelo aplicativo oficial Media Player
>
> \* Open Subtitles: Esse é pra procurar automaticamente legendas dos filmes e séries que vc adicionou ao catálogo
>
> \* Projectionist/CinemaMode: Dá a opção de colocar prerolls/trailers pra tocar antes do conteúdo selecionado no catálogo (não consegui usar o CinemaMode, achei o projectonist mais fácil)
>
> \* InPlayer Episode Preview: Adiciona um botão no player que mostra todos os episódios da série que você tá assistindo.
>
> \* Jellyfin Enhanced: Adiciona algumas customizações no Jellyfin <https://github.com/n00bcodr/Jellyfin-Enhanced>
