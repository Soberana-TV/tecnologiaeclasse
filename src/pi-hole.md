# Pi Hole: um tutorial

Todo mundo odeia propagandas. No vídeo de hoje vamos aprender como funciona, como instalar e configurar o projeto Pi Hole que nos ajuda a bloquear essas pestes a nível de DNS.

**Veja também no canal:**
{{#embed https://www.youtube.com/watch?v=67D5DyGF0yQ}}

- Todo mundo odeia propagandas na internet, mas além de chatas elas podem ajudar empresas a coletar seus dados e as vezes até entregar malware diretamente no seu computador.

- Uma solução mais popular é usar extensões de bloqueio de propagandas no seu navegador, mas nisso nem sempre é o ideal:
  - As próprias extensões podem não ser confiáveis
  - Como usar fora do navegador? Como usar em smartphones?

- Uma outra solução mais avançada é configurar algo como o Ad Guard DNS, que bloqueia as propagandas a um nível de rede antes de chegarem ao seu dispositivo:

  [https://adguard-dns.io](https://adguard-dns.io (preview))

- No tutorial de hoje nós vamos aprender a fazer exatamente isso só que hospedado por nós mesmos e com muito mais controle e possibilidades, usando o Pi Hole. 

[https://pi-hole.net/](https://pi-hole.net/ (preview))

- O que é o [Pi hole](https://pi-hole.net/)?

> O Pi Hole é um projeto de software livre que implementa um *DNS Sinkhole* (cratera ou buraco negro) e impede que seus dispositivos carreguem propagandas, trackers e sites indesejados.

- E primeiro temos que entender para que serve o DNS: Domain Name Resolution

- Quando um dispositivo precisa abrir uma conexão o endereço que ele usa é o IP (exemplo *192.168.0.135*). Só que a gente usa endereços como *meuservidor.com.br* por conveniência. Quem faz esse mapeamento é o protocolo DNS

[](https://dnsimple.com/comics/how-dns-works/pt-br/ep1/ (preview))

- E esse processo funciona em etapas, sempre delegando para outro servidor DNS se a informação não pode ser encontrada localmente:

> Quem é tecnologiaeclasse.com.br?
>
> Consulta tabela do dispositivo **\[NÃO SEI\]**
>
> Consulta o roteador **\[NÃO SEI\]**
>
> Consulta um servidor DNS externo **\[EU SEI\]**
>
> Resposta: **3.231.35.217**

- Comandos úteis para fazer esses testes: *dig*, *nslookup*, e *resolvectl*

- Mas então como o Pi Hole pode nos ajudar contra as propagandas?
  - Propagandas carregam de domínios externos
  - Se nós colocarmos um passo intermediário que é o Pi Hole ele pode ‘sugar’ as conexões e impedir nossos dispositivos de acessarem esses domínios

> Quem é doubleclick.net?
>
> Consulta tabela do dispositivo **\[NÃO SEI\]**
>
> Consulta o roteador **\[NÃO SEI\]**
>
> Consulta DNS interno (Pi Hole) **\[EU SEI\]**
>
> Resposta: **0.0.0.0**

- O mais interessante disso é que com uma configuração adequada do Pi Hole nós podemos bloquear propagandas (e muito mais) de todos nossos dispositivos de uma maneira bem elegante. 

- Agora nós vamos pra instalação, que é bem fácil, então na realidade a parte mais difícil é encontrar o lugar pra instalar, configurar do jeitinho certo, configurar o roteador, servidor, cabo de rede….

- Exemplo de instalação:

> curl -sSL <https://install.pi-hole.net> | bash

- Aqui tem outros métodos de instalação, principalmente usando docker <https://github.com/pi-hole/pi-hole/#one-step-automated-install>

- A interface de configuração estará em `http://IPPIHOLE/admin`

- E daí nós podemos colocar o IP do pi hole na nossa rede como o servidor DNS de cada dispositivo:

> dig doubleclick.net  
> doubleclick.net.	2	IN	A	0.0.0.0
>
> (ou com o servidor DNS explícito)
>
> dig doubleclick.net @192.168.0.130  
> doubleclick.net.	2	IN	A	0.0.0.0
>
> dig doubleclick.net @1.1.1.1  
> → doubleclick.net.	254	IN	A	142.251.129.174

- No Linux vocês podem usar o comando `resolvectl` para ver qual servidor DNS estão usando:

> Link 3 (wlp5s0)
> Current Scopes: DNS
> Protocols: +DefaultRoute +LLMNR -mDNS -DNSOverTLS DNSSEC=no/unsupported
> Current DNS Server: 192.168.0.130
> DNS Servers: 192.168.0.130

- Vamos dar uma olhada nas opções do pihole:
  - query log
  - listas de bloqueio
  - bloqueio/desbloqueio de domínios específicos
  - tabela de DNS próprio
  - ligar / desligar a filtragem

- A maneira mais esperta de configurar é fazendo com que seu próprio servidor DHCP (quem decide o endereço IP dos dispoitivos na rede) mande o servidor DNS do pi hole junto.
  - Em termos humanos: configurar seu roteador para usar o pi hole como DNS.
  - Aquele negócio de ir em `192.168.0.1` e mexer nas configurações do seu roteador. Eu não posso te ajudar especificamente aqui, mas você vai encontrar, eu tenho fé
  - O meu estava em *Configurações Avançadas → Menu → Rede → DNSv4*

- Uma maneira um pouco mais avançada de fazer a coisa é desativando o DHCP no roteador e deixando pro pi hole fazer o próprio DHCP
  - O pi hole decide o IP de cada dispositivo na sua rede
  - O pi hole já manda o seu DNS junto para cada dispositivo conectado
  - Eu não consegui achar a opção no meu roteador

- Onde instalar o pi hole? Vantagens e desvantagens.
  - No seu computador local? Provavelmente não.
  - Num servidor na sua rede? Sim
  - Num servidor na nuvem? Sim

- Pontos bônus: bloqueando domínios de dispositivos smart

{{#embed https://youtube.com/watch?v=WyidL9mCG5I}}

1. Ligue seu dispositivo e navegue pelas funcionalidades que mostram propaganda ou serviços invasivos.
2. Vá até o `query log` e comece a bloquear a resolução dos domínios
3. Reinicie o dispositivo
4. Verifique se as propagandas ou “serviços” online pararam de se comunicar 

- Esse método não é uma solução pra todos problemas, mas ele pode sim retirar as propagandas dos seus dispositivos e impedir que eles vazem seus dados.
  - O roteiro do vídeo original e o material suplementar tem mais sobre isso 

- Pontos bônus: juntar o servidor DHCP, DNS e os IPs do tutorial de Netbird para fazer uma intranet que funciona dentro e fora da sua rede

{{#embed https://youtube.com/watch?v=ZapFOyutsis}}

- Espero que vocês tenham gostado, vlw
