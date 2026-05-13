# Vamos falar mal do Google

Hoje é dia de falar de algumas coisas que o Google tem preparado pra gente e vocês podem ter certeza que vamos falar mal do nosso chefinho. 4GB de IA local sem te perguntar, novo recaptcha que precisa do Google Services e a solução pro “sideload” no Android.

- Vamos começar falando sobre a maior canalhice de todas que é baixar um modelo de IA pra dentro do seu computador sem tem perguntar:

[https://diolinux.com.br/noticias/chrome-ia-de-4-gb-no-computador.html](https://diolinux.com.br/noticias/chrome-ia-de-4-gb-no-computador.html (preview))

- “Ué, mas achei que você gostava de modelos de IA locais”, “Você literalmente mostrou o modelo da Google num vídeo semana passada”, “Melhor do que mandar os dados pra nuvem”
- Eu adoro poder baixar os modelos abertos, EU MESMO, e rodar esses modelos nos meus próprios termos, não é difícil entender o porquê… mas eu sei que pode aparecer esses comentários
- Isso faz parte dessa iniciativa do Google de criar uma “Prompt API” que permitiria sites e aplicativos rodando num navegador terem acesso consistente a um modelo IA que roda prompts. Isso tem algumas vantagens realmente:
  - Usuários do seu serviço não precisam baixar um modelo localmente, o navegador já tem um padrão
  - Uma possível padronização das interfaces pra chamada desses modelos
  - Seus dados não seriam transferidos para um terceiro para fazer uso de um LLM
  - O CUSTO DE RODAR O MODELO PODE SER REPASSADO AO CLIENTE LOCAL
- E os desenvolvedores da Mozilla tiveram uma pequena rusga com o Google quando rolou essa proposta e eles tão certos

[https://github.com/mozilla/standards-positions/issues/1213](https://github.com/mozilla/standards-positions/issues/1213 (preview))

- Tem tanta coisa errada com essa história que eu vou só listar aqui:
  - Tem que perguntar pra instalar 4GB de bloat na minha máquina caralho (aparentemente se apagar ele baixa de volta, artigo do Diolinux mostra como desabilitar)
  - Existe muito pouca esperança dessa API ser realmente compatível com diferentes modelos
  - O custo de rodar inferência TOTALMENTE ÚTIL™ de IA de qualquer site aleatório agora vai ficar no seu processador e bateria 😃
  - Isso vai permitir sites arbitrários que você visita rodarem prompts perigosos sem nem pagarem pelos tokens, aumentando infinitamente a superfície de ataque dos navegadores
  - O Google acabou mesmo de fazer 60%-70% dos usuários desktop baixarem 4GB no  seu computador?
- Notem que nenhum desses motivos é “eu sou ludista e quero matar a IA”… eu vou deixar todos esses pra vocês nos comentários
- Nas minhas distros Linux eu tenho o Chromium e Chrome e não achei o modelo instalado ainda, mas vocês podem verificar On Device Model em chrome://components ou procurar o arquivos weights.bin

### A API de “Prevenção de Fraude” precisa do Google Play Services

- Agora vamos falar sobre as mais novas funcionalidades pra te deixar mais seguro que cada vez mais fecham o Android e os usuários dentro do seu ecossistema

[https://www.reddit.com/r/degoogle/comments/1t9vnwv/google_tied_the_new_generation_of_recaptcha_to/](https://www.reddit.com/r/degoogle/comments/1t9vnwv/google_tied_the_new_generation_of_recaptcha_to/ (preview))

[https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users](https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users (preview))

> O Google vinculou seu sistema reCAPTCHA de última geração aos Serviços do Google Play no Android, o que significa que qualquer pessoa que use um telefone sem os serviços do Google falhará automaticamente na verificação quando o sistema decidir desafiá-la.
>
> A exigência força os usuários do Android a executarem a versão 25.41.30 ou superior da estrutura de aplicativos proprietária do Google apenas para provar que são humanos.
>
> Quando o reCAPTCHA sinaliza o que considera atividade suspeita, ele abandona os antigos quebra-cabeças de imagens e exige que você escaneie um código QR. Essa leitura requer que os Serviços do Google Play estejam em execução em segundo plano, comunicando-se com os servidores do Google. Se você estiver usando o GrapheneOS ou qualquer outra ROM personalizada que remova o software do Google, a verificação falhará.

- Um ataque direto a Custom ROMs de Android e potencialmente outros competidores do Google que queiram construir algo fora do Google Play Services. Ainda mais que:

> A assimetria do iOS: Claramente, isso não tem a ver com segurança. No iOS 16.4 e versões mais recentes, essa mesma verificação funciona perfeitamente de forma nativa, sem exigir que o usuário instale nenhum software do Google. O Google está restringindo artificialmente os usuários do Android, enquanto permite que os usuários do iOS passem despercebidos.

- Isso quer dizer que sites usando o recaptcha para se proteger de ataques ou verificar a humanidade dos usuários não vão funcionar com sistemas ‘De-Googled’
- Aqui o Google mostra de maneira muito didática como ter o controle do sistema operacional E de outras infraestruturas importantes da web permite a eles acabarem com a concorrência e a possibilidade de fugir dos seus serviços

### O Google explicou o “fluxo avançado” para instalar apps de fora da loja

- E a gente pode aproveitar pra fazer uma atualização da situação do “sideload” de apps no Android. Lembrando que vai rolar em Setembro de 2026 para o Brasil.

{{#embed https://www.youtube.com/watch?v=F0LuS9ByHic}}

- O Google sentiu a pressão da comunidade e resolveu deixar claro pra comunidade que vai existir uma maneira de fazer o “sideload” dos aplicativos em Android sem necessariamente ser um desenvolvedor registrado e pagar as taxas. 
  - A linguagem de “sideload” já é complicada, a comunidade tem razão, o celular deveria ser seu então não é “side” porcaria nenhuma

[https://9to5google.com/2026/03/19/android-advanced-flow-sideloading/](https://9to5google.com/2026/03/19/android-advanced-flow-sideloading/ (preview))

- O pessoal do Keep Android Open continua na campanha e explicou bem:

[https://keepandroidopen.org/pt-BR/](https://keepandroidopen.org/pt-BR/ (preview))

- Parece uma boa hora pra fazermos um conteúdo sobre custom roms, GrapheneOS e investigar concorrentes como o HarmonyOS então eu peço que me apontem no caminho certo pra gente começar nos comentários. Vlw
