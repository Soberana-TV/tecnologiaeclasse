# TVs espiãs (e todos dispositivos smart)

Infelizmente vivemos num presente futurista fubango onde nossas televisões nos espionagem e isso não é 1984 george orweeeel. É capitalismo na veia mesmo.

**Veja no nosso canal:**
{{#embed https://www.youtube.com/watch?v=WyidL9mCG5I }}

- Você tem uma SmartTV na sua casa? Você sabe que ela possui diversas funções que mostram propaganda, coletam dados e realizam telemetria de tudo que você faz na TV. Afinal, tudo hoje faz isso, não é mesmo? Você é o produto, etc…

- Porém uma série de vídeos do canal Gamer Nexus expôs o nível absurdo de invasão de privacidade que esses dispositivos fazem:

{{#embed https://www.youtube.com/watch?v=Q9uefFYe6bM }}

{{#embed https://www.youtube.com/watch?v=6IFVTcM28KA }}

- A única coisa que eu consigo dizer é: putaquepariucaralhoporravaitomanocu

- Este vídeo do canal RTINGS também faz alguns experimentos e mostra que é um “problema” comum de todas as marcas. Nos deixando chegar à conclusão que isso é o modelo de negócios

{{#embed https://www.youtube.com/watch?v=IvFu343KNek }}

- A única reclamação que eu tenho sobre o vídeo é fazer uma equivalência ao “acesso barato a dispositivos” com “comprar eles com nossos dados”. Eu quero saber onde estão esses dispositivos mais caros sem nenhuma funcionalidade “smart”? 

### O que as smart TVs sabem sobre você?

- Perfis de uso de aplicativos e apps
- Capturas de áudio e vídeo dos periféricos incluídos na TV
- Captura do estado da rede e todos os dispositivos conectados na rede (seus computadores, celulares, eletrodomesticos smart e etc…)
- ACR (“automated content recognition”): uma foto do que está passando na tela da TV que é analisada e tem os metadados extraidos

- Essas coisas todas estão escondidas atrás de termos de uso confusos e dark patterns e criam situações legais que são impossíveis, como por exemplo, a reponsabilidade transitiva de avisar às outras pessoas em volta da sua televisão que elas também aceitam os termos 

- O Steve no seu documentário sobre a LG focou nas TVs da marca, mas isso é uma prática comum em todas as smart tv atuais.

- Como eles demonstram isso inclusive é orgulhosamente anunciado pelos executivos da LG que repetem de boca cheia “somos donos da tela”, “somos donos da sala”, “temos X milhões de telas para nossos anunciantes”

- Como parte do vídeo ele enfatiza que estão fazendo contato com ativistas e políticos que irão focar na regulamentação e proibição dessas práticas.
  - Alguém que entende de LGPD pode assistir esse vídeo e pensar em fazer o mesmo aqui no Brasil? Eu posso tentar ajudar
  - Por exemplo como fica a coleta de dados de crianças? Existe mesmo anonimização de dados sensíveis com esse nível de coleta? Existe essa figura legal do “aceitar os termos” pelos outros? Muitas perguntas…

- Outro aspecto importante é que nem mesmo “desligadas” ou desconectados da rede as TVs da LG param a espionagem. Eles demonstraram coleta dos microfones com a tv em modo “standby” e também que a TV guarda dados para enviar quando conectada na rede ou que até mesmo poderia se conectar a redes abertas de maneira independente para enviar os dados.

### Então eu hackeei a TV…

- No vídeo o Gamer Nexus traz um cidadão que demonstra a facilidade de invadir essas TVs, que geralmente são um Linux/Android customizado chamado WebOS

- E isso é outro aspecto cabuloso. Mesmo que a LG, Samsung, Hisense e etc… não estejam abusando dessa coleta de dados… os dispositivos são FACILMENTE invadidos e podem ser usados para a espionagem “ilegal”

- Qual a dificuldade de invadir a sua TV?

[https://cani.rootmy.tv/](https://cani.rootmy.tv/ (preview))

- Que me levou a:

[https://github.com/throwaway96/slopbro](https://github.com/throwaway96/slopbro (preview))

- Para fazer o root da sua TV e configurar direitinho tem que seguir aqui:

<https://www.webosbrew.org/rooting/>

- Ao rodar o script eu só precisei confirmar a conexão na TV e eu estava com um shell com root dentro dela
  - Eu mudei a senha padrão do root e adicionei uma chave SSH
  - Ele instalou um “Homebrew Channel” para aplicativos instalados de fora das lojas
  - E fiz o tutorial do GN para remover o máximo de telemetria e consentimentos da TV

[https://forum.level1techs.com/t/lg-tv-block-mini-how-to/255178](https://forum.level1techs.com/t/lg-tv-block-mini-how-to/255178 (preview))

- Foi relativamente fácil, mas o tutorial poderia estar mais adaptado a tipos de tv diferentes e para iniciantes. No momento eu não recomendaria qualquer pessoas que não manja de Linux seguir ele.

- Agora eu supostamente estou com vários tipos de telemetria e consentimento da LG desabilitados, porém eu ainda vejo propagandas da LG e tenho acesso à loja de aplicativos … eu senti que podia fazer mais

- Solução é o Pihole que pode bloquear a resolução dos domínios de propaganda e da LG

https://pi-hole.net/

[https://github.com/pi-hole/pi-hole/#one-step-automated-install](https://github.com/pi-hole/pi-hole/#one-step-automated-install (preview))

- Agora os aplicativos da LG não funcioam e eu não vejo mais propaganda na tela da TV e o Jellyfin funciona 😉 😌 

- Claro que a melhor maneira de fazer isso seria desplugar a TV da internet e usar um dispositivo “burro” que só reproduz mídia, mas eu espero que essa descrição seja útil pra alguém

- Foda né pessoal… eu queria mesmo é uma guerra da LGPD com a LGTV. Será que a gente consegue isso?
