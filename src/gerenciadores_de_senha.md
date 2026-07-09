# Introdução a gerenciadores de senha e como usá-los

Hoje vamos apresentar o conceito de gerenciador de senhas, por que uma dessas ferramentas dessas pode ser útil pra você e introduzir as funcionalidades básicas da minha favorita que é o KeepassXC.

- Senhas e códigos secretos já são basicamente sinônimo com o nosso mundinho digital conectado e o bom gerenciamento delas é vital para que consigamos manter os nossos dados seguros.

- Uma boa gestão de suas senhas e alguns cuidados simples podem elevar o seu nível de segurança do 0 para um nível aceitável sem muito esforço.

- Piores práticas de segurança relacioandas a senhas:
  - Não usar senhas
  - Anotar as senhas
  - Reusar as senhas (ataques de ‘credential stuffing’ após vazamentos)
  - Senhas fracas e previsíveis

- Só que isso enseja aquele problema: “como é que eu vou lembrar de uma senha única para cada um dos serviços que eu uso?”

- Não precisa, apresentado: gerenciadores de senha!

- O que são gerenciadores de senha?
  - Um banco de dados criptografado das suas senhas
  - Com uma senha mestra (e as vezes um arquivo chave) para desbloquear as senhas
  - Gerador de senhas longas e complexas
  - Funcionalidade de detectar sites / auto digitar a senha
  - Por vezes tem integrado a função de autenticação de 2 fatores

- Hoje eu vou recomendar o KeepassXC, um projeto aberto e bastante completo. Ele não tem a sincronização automática do banco de senhas entre máquinas diferentes, mas quem procura uma solução desse tipo eu deixo o Bitwarden

[https://keepassxc.org/](https://keepassxc.org/ (preview))

- Funcionalidades simples:
  - Criar novo banco de senhas
  - Criar e gerar uma nova senha
  - Digitar a senha num serviço

- A maneira mais fácil de ir se familiarizando com um gerenciador de senhas é:
  - Use ele para todos novos serviços que se cadastrar e coloque usuário/senha
  - Não tente pensar numa senha para os serviços, use o gerador de senhas interno com uma complexidade alta. Ele vai digitar a senha para você
  - Toda nova senha que você precisar trocar ou renovar já entra também no gerenciador de senhas
  - Use ele todos os dias para se acostumar com o processo e ter sempre em mente a senha mestra
  - Use o campo de notas em cada serviço para deixar avisos para você mesmo

- Boas práticas de segurança:
  - Não compartilhe e nem esqueça a sua senha mestra!
  - Tenha sempre um backup do seu arquivos .kdbx (e da sua chave se estiver usando)
    - Eu uso o Nextcloud para sincronizar entre computadores e celular (pode usar Dropbox, Onedrive, Syncthing, etc…)
  - Use senhas únicas e complexas para todos os seus serviços (você não precisa mais lembrar delas)
  - Se familiarize com as opções de segurança oferecidas, por exemplo fechar o cofre de senhas a cada 10 min é uma boa prática.

- Sobre autenticação de 2 fatores e TOTP (Time based One Time Password):
  - O TOTP é uma maneira mais segura do que um SMS/email de fazer autenticação de 2 fatores
  - Um código que você guarda e que gera uma senha única a cada 30 segundos, e por isso é usado juntamente com um software ‘autenticador’ que gera essas senhas
  - O KeepassXC, o Bitwarden e outros podem adicionar o código diretamente no registro de cada serviço
  - É muito útil, porém eu prefiro ter o smartphone como o gerador dessas senhas pra realmente ter 2 fatores diferentes de autenticação

- Para reiterar novamente:
  - Se você não estava familiarizado com esse conceito, vá devagar e pense em migrar aos poucos
  - Se feito com responsabilidade e cuidado essa é uma prática que requere muito pouco esforço e aumenta demais a sua segurança
    - Não esqueça nem anote a senha mestra
    - Tenha um becape do banco de senhas

  

- Existem diversas práticas simples de segurança digital que se feitas em conjunto e com disciplina vão deixar você seguro contra a maioria dos ataques mais comuns:
  - Gerenciadores de senha
  - autenticação de dois fatores
  - usar softwares seguros e atualizados\*
  - compartimentalizar ambiente de trabalho e pessoal
  - evitar comportamentos de risco

- Gostaram? Perguntas? Deixem um comentário e considerem apoiar o nosso trabalho!
