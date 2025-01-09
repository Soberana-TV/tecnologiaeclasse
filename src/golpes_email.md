# Investigando Golpes de e-mail

![meme.jpg](./golpes_email/meme.jpg)

- Fato divertido sobre mim:
  - Eu sou o suporte técnico da minha família e amigos
  - E agora eu sou o suporte técnico de vocês
- Então vamos fazer um aviso de utilidade pública.

### Golpe 1:

- Este é um golpe comun que tem circulado há bastante tempo

- Em resumo é um email onde o remetente:
  - Insinua que invadiu suas contas/dispositivos usando o malware Pegasus. O fato do email ser mandado do SEU PRÓPRIO endereço reforça a 'veracidade' ameaças
  - Alega ter fotos pessoais e/ou material comprometedor sobre você que será espalhado para família, amigos, internet...
  - Pede um depósito de algum valor exorbitante num endereço de bitcoin em um período de 48 horas
  - Diz que você não deve pedir ajuda e nem buscar as autoridades pois nesse caso irá espalhar o material de chantagem
- O e-mail geralmente vem com o SEU PRÓPRIO E-MAIL como remetente
- Texto completo

  > Hello pervert,  
  > I want to inform you about a very bad situation for you. However, you can benefit from it, if you will act wisely.  
  > Have  you heard of Pegasus? This is a spyware program that installs on  computers and smartphones and allows hackers to monitor the activity of  device owners. It provides access to your webcam, messengers, emails,  call records, etc. It works well on Android, iOS, and Windows. I guess,  you already figured out where I’m getting at.  
  > It’s been a few months  since I installed it on all your devices because you were not quite  choosy about what links to click on the internet. During this period,  I’ve learned about all aspects of your private life, but one is of  special significance to me.  
  > I’ve recorded many videos of you jerking  off to highly controversial porn videos. Given that the “questionable”  genre is almost always the same, I can conclude that you have sick  perversion.  
  > I doubt you’d want your friends, family and co-workers to know about it. However, I can do it in a few clicks.  
  > Every  number in your contact book will suddenly receive these videos – on  WhatsApp, on Telegram, on Skype, on email – everywhere. It is going to  be a tsunami that will sweep away everything in its path, and first of  all, your former life.  
  > Don’t think of yourself as an innocent victim.  No one knows where your perversion might lead in the future, so  consider this a kind of deserved punishment to stop you.  
  > Better late than never.  
  > I’m  some kind of God who sees everything. However, don’t panic. As we know,  God is merciful and forgiving, and so do I. But my mercy is not free.
  >
  > Transfer $1220 USD to my bitcoin wallet: [ENDEREÇO BTC]
  >
  > Once I receive confirmation of the transaction, I will permanently  delete all videos compromising you, uninstall Pegasus from all of your  devices, and disappear from your life. You can be sure – my benefit is  only money. Otherwise, I wouldn’t be writing to you, but destroy your  life without a word in a second.
  >
  > I’ll be notified when you open my email, and from that moment you  have exactly 48 hours to send the money. If cryptocurrencies are  unchartered waters for you, don’t worry, it’s very simple. Just google  “crypto exchange” and then it will be no harder than buying some useless  stuff on Amazon.
  >
  > I strongly warn you against the following:  
  > ) Do not reply to this email. I sent it from a temp email so I am untraceable.  
  > )  Do not contact the police. I have access to all your devices, and as  soon as I find out you ran to the cops, videos will be published.  
  > ) Don’t try to reset or destroy your devices.  
  > As I mentioned above: I’m monitoring all your activity, so you either agree to my terms or the videos are published.
  >
  > Also, don’t forget that cryptocurrencies are anonymous, so it’s impossible to identify me using the provided address.  
  > Good luck, my perverted friend. I hope this is the last time we hear from each other.
  >
  > And some friendly advice: from now on, don’t be so careless about your online security.”

- Do que se trata na realidade:
  - É um scam que copia/cola a mesma mensagem e se utiliza de medos comuns e da publicidade que o Pegasus recebeu (ele é real) para assustar você
  - É possível que os emails e/ou qualquer customização da mensagem com seus dados pessoais sejam vindos de vazamentos online
  - Porém essa pessoa não tem os seus dados pessoais e esse golpe é feito no atacado para tentar pescar desavisados que realmente depositem BTC nesse endereço
- Uma coisa sobre o protocolo de email: ele é facilmente fraudável ou como os nerds chamam 'é facil fazer o **spoofing**'
- Uma maneira de se previnir é procurar inconsistências no endereço ou remetente da mensagem
- Por exemplo o protocolo **spf**

```
...
Received: from cpusales.com (185.149.147.68) by
 BN2PEPF000055DE.mail.protection.outlook.com (10.167.245.8) with Microsoft
 SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id
 15.20.8207.0 via Frontend Transport; Mon, 24 Nov 2024 11:26:38 +0000
From: "meuemail@hotmail.com" <meuemail@hotmail.com>
To: "meuemail@hotmail.com" <meuemail@hotmail.com>
...
received-spf: Fail (protection.outlook.com: domain of hotmail.com does not
 designate 185.149.147.68 as permitted sender)
 receiver=protection.outlook.com; client-ip=185.149.147.68; helo=cpusales.com;
```

### Golpe 2:

- É um email com o seu nome/sobrenome no título e com o seu número de telefone
- A mensagem, ao invés de no corpo do email, veio dentro de um pdf
  - Tática comum para impedir a detecção por filtros de spam
  - Como regra geral nunca confie em imagens, documentos pdf, word, excel e outros anexos que vem de contatos desconhecidos
- O texto da mensagem é bastante similar ao primeiro. Em resumo, seus dispositivos foram comprometidos por um malware e agora essa pessoa tem acesso a todos seus dados
- No final a maneira de 'se salvar' é mandar bitcoin para um endereço, num período de 24 horas
- Da mesma maneira que o primeiro golpe, temos o apelo a um dado 'secreto' (tenho seu número e nome) em conjunto com um aspecto técnico 'arcano' (um malware em todos seus dispositivos) e a cereja no bolo é o ultimato para que o pagamento seja feito de forma urgente. Deixe que o medo desligue seu cérebro  
- Diversos desses golpes são variações do mesmo tipo de texto e usam as mesmas técnicas para tentar 'converter' pagamentos em criptomoedas
- E de onde vem os dados? Uma rápida pesquisa no Google acusa que houve um vazamento de nomes de pessoas + números de telefone incompletos (da plataforma Gemini). Exatamente o formato usado para esse golpe
- Por isso a importância de se manter atualizado por serviços como <https://haveibeenpwned.com/>

#### Dicas de segurança em geral

- Não confie em links estranhos que você recebe no email e SMS (e em nenhum lugar)
- Mantenha todas as suas contas com autenticação de 2 fatores
- Tente usar as versões mais atualizadas de todos softwares que você depende
- Use um antivirus / antimalware (Kaspersky, Malware Bytes, Norton, Windows Defender, ...)
- Cuidado ao explorar as partes mais **SUS** da internet
- Fique atento a comportamentos estranhos em suas contas e logins / requisições de senhas suspeitas
- Use senhas seguras e diferenciadas. Busque aprender a usar um gerenciador de senhas

#### Referências

<https://www.valimail.com/blog/what-is-spf/>

<https://malwaretips.com/blogs/have-you-heard-about-pegasus-blackmail-email-scam/>
