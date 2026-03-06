# Vamos falar de HomeLab/Self hosting

Em algum momento do ano passado eu comecei a levar mais a sério a jornada de hospedar "um monte de bagulho" aqui na minha casa. Esse vídeo é pra dividir essa experiência com vocês e mandar algumas ideias.

- Primeiro eu já queria deixar bem claro que esse vídeo é um tutorial mais motivacional, não exaustivo de como fazer "o homelab perfeito"
  - Eu vou jogar um monte de papo fora, se isso te irrita, por favor saia do vídeo
- Seria muito bom entender um pouco (um monte na realidade) de GNU/Linux, protocolos de rede, hardware, segurança e yadda yadda

- O que eu vou mostrar pra vocês hoje:
  - Motivacional uhuuuul
  - O que eu estou rodando no momento no 'homelab'?
  - Algumas ideias de como vocês poderiam fazer algo parecido
  - Algumas estratégias para gerenciar a rede e os becapes
  - Algo muito básico de Linux
  - Como acessar seu home lab 'fora de casa'

- Tem vários motivos por que vocês podem querer um home lab:
  - Aprender a usar Linux/Unix e hospedar alguns serviços num ambiente muito mais seguro e controlado
  - Substituir serviços de big techs aos quais vocês estão dependentes
  - Colocar pra funcionar aquele hardware que está parado na sua casa

- O mais importante é você fazer um plano para começar pequeno:
  - ter estratégia de becape
  - um espaço seguro para deixar os computadores
  - organizar acesso e gerencia da sua rede
  - entender os custos, por exemplo com energia, e escolher o hardware

- Você pode fazer um homelab em qualquer sistema e hardware que você tiver acesso, mas eu comecei com um laptop velho e agora estou com dois
  - Pode usar Raspberry PI
  - Celulares antigos (com termux)
  - Desktops
  - E é claro hardware específico comprado para isso

- Eu gerencio tudo com Linux e tirando o que eu vou mostrar logo em seguida, pela linha de comando. Porém eu recomendo começarem com um sistema que tem interface gráfica, ele ainda serve pra ser um servidor e facilita a vida de vocês!

- Essa é uma boa oportunidade para aprender um pouco de Linux num ambiente 'controlado'. Estudem sobre:
  - **ssh** para acesso remoto, autenticação com senha e chaves
  - gerencia da rede, hostnames, portas o firewall padrão que vem no seu sistema (**/etc/hosts**, **ufw**...)
  - comandos básicos de criação e gerencia de arquivos (**ls**, **cp**, **mv**, ...)
  - instalação de pacotes (**apt-get**, **snap**, **flatpak**, **docker**, ...)
  - softwares de monitoramento (desde o ps, top, systemctl passando por monit e pm2 até apps mais completos como dashboards do sistema)

- Agora eu vou mostrar o meu 'homelab' pra vocês:

<http://192.168.15.57:8080>

- A primeira dica que eu vou dar pra vocês: tudo que vocês foram fazendo, escrevam num pequeno diário / tutorial para vocês mesmos
  - Isso vai servir para o seu eu futuro 'eu' lembrar como vocês fizeram as coisas
  - Mas também como uma maneira de fixar o que vocês estão aprendendo e pensar em como vocês poderiam melhorar

- O meu maior objetivo tem sido organizar arquivos importantes e pessoais apenas em dispositivos que eu tenho controle:
  - Nextcloud para fotos e vídeos da família
    - becape num HD externo
    - uso de sincronização de arquivos para armazenar arquivos importantes em múltiplos computadores
    - Também guardo a coleção de livros de Kindle e ebooks usando um servidor 'calibre'
  - Jellyfin para ouvir música / assistir filmes
    - Usando os players **Supersonic** no desktop e **Finamp** no celular
    - Posso ver mídia na televisão da sala pois ela tem acesso ao homelab
  - O laptop com Linux na sala me permite usar o steamplay do PC de streaming que fica no escritório
  - Sistema improvisado de webcam usada como ipcam apenas dentro de casa
  - Teste para o deploy de aplicativos, tanto dentro de casa quanto externo, vamos falar como fazer isso mais tarde.

- Eu decidi fazer essa interface porque no processo de documentar todos os serviços que eu tava instalando eu percebi que tinha 'um diretório' de serviços. Aí eu pensei:

```
<li>
  <a href="http://192.168.15.6:8080">NextCloud</a>
  <a href="192.168.15.57:8096">Jellyfin</a>
  ...
</li>
```

- Evoluiu pra algo um pouco mais complexo por que agora tem os ícones, status do serviço, links externos e é editável por yml. Foi um projeto bem simples que eu fiz com vibe coding e aproveitei pra aprender um pouco de React Server Components

- Essa maneira de enxergar me permitiu ver o homelab / selfhosted como uma maneira de fazer uma 'biblioteca de serviços' que eu preciso e é um hobby legal tentar pensar quantos outros serviços eu posso substituir e como deixar mais eficiente minha organização interna.

- A próxima dica é começar a estudar como funcionam endereços IP, hostnames e portas, rede local VS interna e todas essas coisas *maravilhosas*

- O meu sistema de becapes não é perfeito, mas ele funciona mais ou menos assim:
  - Um HD externo e um comando **rsync**
  - 2 cópias de cada arquivo
  - Arquivos importantes estão em múltiplos computadores e/ou na nuvem

- Para fazer acesso remoto do seu homelab geralmente a ideia mais comum é uma VPN (virtual private network). Você pode construir ela 'na mão' com openvpn ou usar projetos como o Wireguard, Tailscale e Netbird

{{#embed https://www.youtube.com/watch?v=62Tmt1THacs }}

{{#embed https://www.youtube.com/watch?v=jnGsStleHd0 }}

- No momento eu estou usando o Netbird por causa da facilidade de expor os serviços externamente e a possibilidade de autohospedar o meu próprio servidor

- Outra ideia para expor serviços à rede externa seria o túnel de algumas portas para um servidor externo e o uso de um domínio e um proxy http para garantir um pouco de segurança:


```
# exemplo com nginx

server {
  server_name meuservidor.com.br;

  location / {
    proxy_pass http://localhost:8080/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
  }

}
```

- As portas podem ser expostas com um túnel SSH ou com algum dos milhares de projetos abertos como o [rathole](https://github.com/rathole-org/rathole)

- Uma ideia diabólica é o uso de chatbots de Telegram, Discord ou qualquer outro serviço que você controle que se conectam à internet e esperam comandos:

```
-> Você: Olá meu casa, poderia colocar essa festa às 18h de amanhã na agenda?
-> HomeBot: Claro queridão, tá aqui.
-> Você: E quais eventos eu tenho na agenda hoje?
-> HomeBot: Tá lotado hein.
```

- Mas é isso pessoal, agora que eu mostrei o meu homelab a gente deixa aberto pra dúvidas aqui nos comentários e eu peço pra vocês me dizerem como estão construindo os seus. tmj

### Referências

Comandos Linux: <https://aurelio.net/shell/>

Chaves SSH: <https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>

Guias de Homelab:

<https://www.technodabbler.com/the-ultimate-homelab-guide/>

<https://labstackguide.com/homelab-for-beginners/>

<https://diolinux.com.br/tecnologia/do-zero-ao-homelab.html>
