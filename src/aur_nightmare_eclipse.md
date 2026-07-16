# Ataque ao AUR, o retorno de Nightmare Eclipse e mais

Hoje vamos trazer aquela mescla gostosa de notícias sobre segurança da informação. Um pouco GNU/Linux, um pouco Windows. E principalmente a continuação da saga de Nightmare Eclipse, será que rolaram as revelações???

**Veja também no canal**:

{{#embed https://www.youtube.com/watch?v=OdWvZhXzkLU}}

### Invasão dos pacotes do AUR

[https://cybersecuritynews.com/arch-linux-aur-packages-compromised/](https://cybersecuritynews.com/arch-linux-aur-packages-compromised/ (preview))

- AUR (Arch User Repository) é um repositório mantido pela comunidade do Arch Linux. Não é o repositório oficial do Arch e não tem o mesmo tipo de escrutíneo de segurança

- Os atacantes tomaram controle de projetos abandonados, muitas vezes usando os próprios processos de ‘adoção’ de projetos que não tem mais mantenedores. 

> Once in control, attackers modified the packages’ PKGBUILD scripts, which are the build instruction files that AUR helpers like yay and paru execute during installation.
>
> The malicious PKGBUILDs were altered to silently fetch and install two rogue npm packages: atomic-lockfile and js-digest.  These packages acted as the primary malware delivery mechanism,  executing during the standard package build process without triggering  obvious warnings to end users.

- Os pacotes comprometidos adicionaram a instalação de INFOSTEALERS no passo de build dos pacotes, roubando:
  - Senhas e cookies nos navegadores
  - Chaves de API, chaves ssh, tokens de segurança
  - Carteiras de criptomoeda

[https://gist.github.com/Kidev/85756c3dcad3623ca5604a8135bafd14](https://gist.github.com/Kidev/85756c3dcad3623ca5604a8135bafd14 (preview))

- O malware também mantinha uma persistência nas máquinas se passando por processos válidos do sistema

- Nós já falamos repetidas vezes sobre esse tipo de ataque da cadeia de suprimentos, mas é sempre bom lembrar que atacar usuários de Linux, e portanto desenvolvedores, é um ótimo negócio.
  - Chaves de API e tokens de segurança que permitem rodar mais exploits
  - O encadeamento de exploits do ambiente Python, JS, Ruby, Linux, Java e etc… cria uma hidra de worms 

- Exemplo de apenas 2 outros malwares com o mesmo objetivo:

- Começando na lib ensmallen

[https://www.stepsecurity.io/blog/the-hades-campaign-pypi-packages](https://www.stepsecurity.io/blog/the-hades-campaign-pypi-packages (preview))

- Começando no pacote pyrogram

[https://checkmarx.com/zero-post/operation-navy-ghost-pyrogram-telegram-supplychain-attack/](https://checkmarx.com/zero-post/operation-navy-ghost-pyrogram-telegram-supplychain-attack/ (preview))

### Exploitarium

- No início do mês um outro pesquisador de segurança largou um calhamaço de vulnerabilidades num repositório do github

[https://fieldeffect.com/blog/exploitarium-repository-publishes-poc-exploits](https://fieldeffect.com/blog/exploitarium-repository-publishes-poc-exploits (preview))

- Segundo ele o processo é um fuzzing + o GPT 5.3, mas que você não precisa de modelos “estado da arte” pra conseguir o mesmo resultado

- Vulnerabilidades no ffmpeg, curl, firefox, libssh2, discord, anydesk, …

- O repositório dele continua lá no github, não foi banido. Por que seria não é mesmo?

### Quando o segundo exploit chegar…

- Lembram de Nightmare Eclipse, a atacante misteriosa que é o terror da Micro$oft? Da última vez que trouxemos aqui no canal a promessa era que 14/07/26 ia rolar algo foda… e aí?

[https://www.theregister.com/security/2026/07/15/microsofts-serial-tormentor-drops-legacyhive-0-day/5271723](https://www.theregister.com/security/2026/07/15/microsofts-serial-tormentor-drops-legacyhive-0-day/5271723 (preview))

- Foi lançado mais um exploit, mas não era o que a gente imaginava…
- Na real se eu seguisse o blog dela eu saberia que já foi cancelado

[https://deadeclipse666.blogspot.com/2026/06/regarding-july-14th.html?m=1](https://deadeclipse666.blogspot.com/2026/06/regarding-july-14th.html?m=1 (preview))

- E no meio tempo já foi lançado mais uma vulnerabilidade chamada Rogue Planet:

[https://www.picussecurity.com/resource/blog/rogueplanet-anatomy-of-the-nightmare-eclipse-microsoft-defender-zero-day](https://www.picussecurity.com/resource/blog/rogueplanet-anatomy-of-the-nightmare-eclipse-microsoft-defender-zero-day (preview))

- Nightmare Eclipse é debochada e gosta de lançar os exploits logo após a ‘patch tuesday’ da Micro$oft.

- Mas no post de blog fala que os últimos exploits tem exigido muito dela e precisa descansar além de não ter sido sua intenção espalhas ‘pânico’ com aquela postagem

- Temos a primeira influenciadora de 0-days antes do GTA6

Pesquisador de segurança anônimo divulga zero-day em 15 softwares de código aberto, sem notificar previamente os mantenedores: as vulnerabilidades foram publicadas no repositório “exploitarium” (já removido pelo GitHub), envolvendo projetos como libssh2, Splunk, RustDesk, 7-Zip, VLC, AnyDesk, OpenVPN, c-ares, Gitea e Floci. Entre elas estão a CVE-2026-55200 no libssh2, que permite execução remota de código sem autenticação, ainda sem correção; e a CVE-2026-20896 no Gitea self-hosted em Docker, que possibilita a invasores remotos assumirem o controle do servidor Git, corrigida na versão 1.26.3. As informações são do site The Register.

[https://www.stepsecurity.io/blog/the-hades-campaign-pypi-packages](https://www.stepsecurity.io/blog/the-hades-campaign-pypi-packages (preview))
