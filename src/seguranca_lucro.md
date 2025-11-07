#### Segurança, o incentivo ao lucro e afins

A segurança de um produto e o modelo de negócios das empresas nem sempre estão alinhados e essa relação é sempre muito difícil de aparecer na planilha semestral de lucros e investimentos. Hoje quero trazer um apanhado de notícias onde a segurança falhou, como por exemplo no museu do Louvre, e conectar com o mercado de trabalho e capitalismo em geral.

**Projeto  F-Droid, que distribui software open-source para Android, ameaça  encerramento caso Google implemente registro obrigatório de  desenvolvedores para instalação de aplicativos:** segundo Marc  Prud’hommeaux, membro do conselho do F-Droid, a mudança violaria a  política de não exigir cadastro dos usuários da plataforma e reforçaria o  controle sobre o ecossistema de software livre. Além disso, ele defende  que a plataforma é mais segura que a Play Store, visto que os  aplicativos são de código aberto e podem ser auditados publicamente. O  F-Droid busca apoio de reguladores e incentiva pressão política contra a  medida do Google, que entrará em vigor em setembro de 2026. As  informações são do site The Register.

<https://f-droid.org/2025/09/29/google-developer-registration-decree.html>

**Jogo verificado na Steam continha malware e rouba doações em cripto destinadas a tratamento de câncer de livestreamer:**  a situação aconteceu ao vivo, enquanto o streamer Raivo Plavnieks  realizava uma transmissão para arrecadar fundos para seu tratamento. O  jogo BlockBlasters já foi removido da plataforma, mas as perdas são  estimadas em 150 mil dólares, com centenas de usuários afetados. As  informações são do site BleepingComputer.       

<https://www.404media.co/steam-hosted-malware-game-that-stole-32-000-from-a-cancer-patient-live-on-stream/>

**Campanha de malvertising iniciada em redes sociais da Meta atinge Google Ads e YouTube:**  o esquema utiliza anúncios falsos de uma versão premium gratuita do  aplicativo TradingView para Android, o qual instala o malware Brokewell,  que rouba credenciais, intercepta cookies, registra interações como  toques, deslizes e textos digitados, além de atuar como trojan de acesso  remoto. No YouTube, os golpistas criaram um canal que se passa pela  legítima TradingView, com vídeos não listados que chegaram a ultrapassar  180 mil visualizações em poucos dias, distribuindo o Trojan Agent GOSL.  Ainda não há estimativa sobre o número de usuários afetados. As  informações são do site TechRadar.

<https://www.techradar.com/pro/security/this-devious-malware-has-jumped-from-meta-over-to-google-ads-and-youtube-to-spread-heres-how-to-stay-safe>

**Brasil e Itália são alvos de trojan para Android que simula digitação humana:**  o Herodotus é capaz de assumir controle total do dispositivo, alterar  permissões do sistema, instalar aplicativos e roubar senhas bancárias e  códigos de autenticação. No Brasil, ele é distribuído via campanhas de  phishing e disfarçado como o app “Módulo Segurança Stone”, apresentado  como um pacote do Chrome. Para burlar sistemas de segurança que detectam  comportamentos suspeitos, o malware simula digitação humana com  intervalos entre 0,3 e 3 segundos. As informações são do site Tecnoblog.

<https://tecnoblog.net/noticias/malware-que-finge-digitar-como-humano-e-usado-em-ataques-no-brasil/>

#### A senha do Louvre

<https://www.tomshardware.com/tech-industry/cyber-security/louvre-heist-reveals-glaring-security-weaknesses-previous-reports-say-museum-used-louvre-as-password-for-its-video-surveillance-still-has-workstations-with-windows-2000>

**Microsoft Azure sofreu pane global nesta quarta-feira:**  a interrupção durou mais de 8 horas e provocou instabilidade em  plataformas como GitHub, Microsoft 365, Minecraft e Xbox, além de  serviços essenciais de companhias aéreas. Segundo a empresa, o incidente  foi causado por uma alteração inadvertida que afetou o funcionamento do  Azure Front Door, impactando componentes de rede como DNS e CDN,  resultando em latência elevada, time-outs e falhas de acesso. As  informações são dos sites Reuters e The Verge.

<https://www.wired.com/story/the-microsoft-azure-outage-shows-the-harsh-reality-of-cloud-failures/>

**Cloudflare mitiga ataque DDoS recorde de 22,2 Tbps:**  o maior incidente anterior foi na faixa de 11,5 Tbps, registrado há  apenas três semanas atrás. A investida durou 40 segundos, com  intensidade equivalente à transmissão simultânea de um milhão de vídeos  em 4K. A Cloudflare não revelou detalhes sobre a origem do ataque. As  informações são do site BleepingComputer.

<https://www.bleepingcomputer.com/news/security/cloudflare-mitigates-new-record-breaking-222-tbps-ddos-attack/>

**Cloudflare derruba seus próprios serviços devido a bug em código React:**  o incidente, ocorrido no último dia 12, durou mais de uma hora e foi  causado por chamadas repetidas à Tenant Service API. O problema decorreu  de um hook useEffect com um objeto no array de dependências que se  recriava a cada alteração, executando a função várias vezes em uma única  renderização e sobrecarregando a API. Como medida preventiva, a  capacidade da Tenant Service foi reforçada e as chamadas de API  ajustadas para diferenciar tentativas repetidas de novas requisições. As  informações são do site The Register.       

<https://blog.cloudflare.com/deep-dive-into-cloudflares-sept-12-dashboard-and-api-outage/>

**Ataque à cadeia de suprimentos atinge mais de 180 pacotes do NPM:**  a campanha, denominada Shai-Hulud, contém um código malicioso capaz de  se autorreplicar para outras bibliotecas de um mesmo mantenedor. O  script injetado faz uso da ferramenta legítima TruffleHog para localizar  dados sensíveis expostos por engano, como chaves de API, senhas e  tokens em repositórios de código. Entre os módulos afetados estão  ctrl/tinycolor (nas versões 4.1.1 e 4.1.2, e corrigido na 4.2.0), com  mais de 2 milhões de downloads semanais, e outros publicados pela  CrowdStrike, que afirma já ter removido as dependências comprometidas.  Mais informações estão disponíveis no TabNews.       

<https://krebsonsecurity.com/2025/09/self-replicating-worm-hits-180-software-packages/>

**GitHub vai reforçar segurança do NPM para prevenir ataques à cadeia de suprimentos:**  as mudanças incluem autenticação em dois fatores obrigatória para  publicações locais, uso de tokens granulares com validade de sete dias, e  expansão do modelo de publicação confiável, que elimina a necessidade  de gerenciar tokens de API em sistemas de build. A implementação das  novas regras será gradual. Na semana passada, noticiamos um ataque à  cadeia de suprimentos denominado Shai-Hulud, que afetou mais de 180  pacotes da plataforma. As informações são do site BleepingComputer.

<https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/>

#### E como a gente amarra tudo isso?

<https://economictimes.indiatimes.com/tech/technology/meta-is-earning-a-fortune-on-a-deluge-of-fraudulent-ads-internal-documents-show/articleshow/125136744.cms>

- A Meta tem um sistema de avaliação de risco das propagandas que mostra para seus usuários
- Acima de um limiar de risco elas são canceladas
- Com um potencial grande de risco, mas abaixo do limiar, o preço dessas publicidades sobre para tentar 'desincentivar' os golpistas
