# Dirty Frag é o Copyfail 2

Deja vu, eu já estive nesse lugar antes. Sejam bem vindos a segunda feira da escalação de privilégios. Sim, hoje vamos falar de novo sobre uma vulnerabilidade que permite um usuário comum adquirir permissões de administrador no Linux. Estou cansado chefe

- Pra quem não viu, nós fizemos um vídeo semana passada falando sobre o Copyfail. Esse exploit misturava a escrita do kernel em algumas páginas de memória e uma API de criptografia. Um erro de lógica permitia a corrupção de páginas de cache na memória e a criação de uma versão do su que elevava o usuário a administrador sem pedir a senha.

{{#embed https://www.youtube.com/watch?v=JHXWF-AoDRA }}

- “sir, a second exploit has hit the kernel”

[https://www.tomshardware.com/tech-industry/cyber-security/dirty-frag-exploit-gets-root-on-most-linux-machines-since-2017-no-patches-available-no-warning-given-copy-fail-like-vulnerability-had-its-embargo-broken](https://www.tomshardware.com/tech-industry/cyber-security/dirty-frag-exploit-gets-root-on-most-linux-machines-since-2017-no-patches-available-no-warning-given-copy-fail-like-vulnerability-had-its-embargo-broken (preview))

- O Dirty Frag na realidade é 2 outras vulnerabilidades que derivam do mesmo erro lógico só que em outros módulos do kernel. Um deles no esp4 e esp6 e outro no rxrpc 

- A existência desse exploit foi revelada 07/05/26. Com 0 patches prontos, foi lançado no seco… por quê? Nós já vamos falar, mas primeiro a explicação e mitigação.

- Discussão no reddit /r/sysadmin

[https://www.reddit.com/r/sysadmin/comments/1t6ocb8/dirty_frag_new_root_exploit_targeting_newest/](https://www.reddit.com/r/sysadmin/comments/1t6ocb8/dirty_frag_new_root_exploit_targeting_newest/ (preview))

- Repositório oficial do exploit:

[https://github.com/V4bel/dirtyfrag/](https://github.com/V4bel/dirtyfrag/ (preview))

> RedHat: https://access.redhat.com/security/vulnerabilities/RHSB-2026-003
>
> Amazon Linux: https://aws.amazon.com/pt/security/security-bulletins/rss/2026-027-aws/
>
> Ubuntu: https://ubuntu.com/blog/dirty-frag-linux-vulnerability-fixes-available
>
> Fedora: https://bodhi.fedoraproject.org/updates/FEDORA-2026-8cffa03dad
>
> Alma Linux: https://almalinux.org/blog/2026-05-07-dirty-frag/

### Explicação simples:

- É de novo um uso do método splice para juntar duas páginas na memória. O Copyfail usava isso para juntar uma página de criptografia que o módulo algif_aedusava com pagínas na memória que se queria corromper. Esse novo exploit vai na mesma linhas, mas usando os móduilos esp4, esp6 e rxrpc

### Como mitigar:

- Dependendo de quando você ver esse vídeo talvez já tenha uma versão atualizada do kernel Linux para a sua distribuição, mas para mitigar é possível desabilitar os módulos como da outra vez.

```
sh -c "printf 'install esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' > /etc/modprobe.d/dirtyfrag.conf; rmmod esp4 esp6 rxrpc 2>/dev/null; echo 3 > /proc/sys/vm/drop_caches; true"
```

Em mais linhas:

```

echo "install esp4 /bin/false" | sudo tee /etc/modprobe.d/dirty-frag.conf
echo "install esp6 /bin/false" | sudo tee -a /etc/modprobe.d/dirty-frag.conf
echo "install rxrpc /bin/false" | sudo tee -a /etc/modprobe.d/dirty-frag.conf

rmmod esp4 esp6 rxrpc 2>/dev/null;

echo 3 > /proc/sys/vm/drop_caches; true"
```

- Desabilitar isso aqui vai fazer algumas funcionalidades do kernel não funcionarem. Eu tentei procurar pra vocês o que seria. Da postagem do Ubuntu:

> ## Mitigation regression risk
>
> The mitigations disable the kernel modules that are used for IPsec  ESP and RxRPC, respectively. The mitigations will affect functionality  if these are in use by either:
>
> - IPsec deployments. These are common with VPN implementations such as StrongSwan.
> - AFS (Andrew File System) or another application of RxRPC.
>
> As the vulnerabilities are independent, disabling only the esp4/esp6 modules or only the rxrpc modules would leave the remaining ones exploitable.

### Por que foi revelado assim no susto?

> Timeline of disclosure:     
>
> - 2026-04-30: Submitted detailed information about the esp  vulnerability and a weaponized exploit that achieves root privileges on  several major distributions to security@kernel.org.     
> - 2026-04-30: Submitted the patch for the esp vulnerability to the  netdev mailing list. Information about this issue was published  publicly.     
> - 2026-04-30 (+9h): Kuan-Ting Chen submitted a vulnerability report for the esp vulnerability with a reproducer to security@kernel.org.     
> - 2026-05-04: Kuan-Ting Chen submitted the shared-frag approach patch to the netdev mailing list.
> - 2026-05-07: The patch was merged into the netdev tree.     
> - 2026-05-07: Submitted detailed information about the vulnerability  and the exploit to the linux-distros mailing list. The embargo was set  to 5 days, with an agreement that if a third party publishes the exploit  on the internet during the embargo period, the Dirty Frag exploit would  be published publicly.     
> - 2026-05-07: Detailed information and the exploit for this  vulnerability were published publicly by an unrelated third party,  breaking the embargo.     
> - 2026-05-07: After obtaining agreement from distribution  maintainers to fully disclose Dirty Frag, the entire Dirty Frag document  was published.     

[https://afflicted.sh/blog/posts/copy-fail-2.html](https://afflicted.sh/blog/posts/copy-fail-2.html (preview))

- Sim, isso mostra mais uma vez como a disponibilidade de LLMs bons o suficientes está criando situações perigosas.
  - Hoje dá pra ter tempo hábil de ficar monitorando todos commits no Linux e descobrir que uma dessas pequenas mudanças era uma correção de vulnerabilidade que está no período de embargo.
  - Nesse momento se esse texto tivesse sido escrito por um LLM eu ia dizer: “e isso muda o jogo” ou “e aqui está o pulo do gato”
  - O que eu vou dizer é que não é só as agências de inteligência que podem fazer isso agora e isso tem suas partes boas e ruins.

### Por que esse exploit é tão perigoso agora \[2\]

- Essa parte é reciclada do vídeo do copyfail, mas é importante lembrar

- A maneira que ele é explorado é rápida, portável e a junção dos 2 exploits consegue explorar basicamente todas as distros mais populares.

- Poderia estar sendo explorado por aí de uma maneira silenciosa.

- Não é um exploit com RCE (remote code execution), mas vai ser incluído nas ferramentas de invasão como um segundo passo após conseguir um shell numa máquina.
  - Fora isso, alguém com acesso local à sua máquina conseguiria root sem senha.

## 

- Hoje esse tipo de vulnerabilidade, junto com ferramentas de CI, VPS, malwares distribuídos pela cadeia de suprimentos se torna bem mais desastroso e é por isso que administradores de sistemas passaram mais um final de semana arrancando os cabelos 🙂 

  
<https://github.com/V4bel/dirtyfrag/issues/28/>

Boa semana para todos e que o Linus tenha piedade da nossa nação
