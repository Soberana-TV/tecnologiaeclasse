# Valve e a sua aposta na interoperabilidade

Faz mais ou menos um mês que ficou claro que a Valve vem financiando o projeto Fex e fez um fork do projeto Waydroid. Isso mostra uma aposta pesada na compatibilidade de software e vamos falar hoje sobre isso.

- Recentemente a Valve anunciou o seu novo "PC/videogame" chamado de "Steam Machine" e um óculos de realidade virtual chamado "Steam Frame"
  - Steam Machine tem o hardware baseado em x86 e provavelmente custará em torno de **U$ 1000**
  - Steam Frame poderá custar de **U$ 500** a **U$ 1000**

{{#embed https://youtube.com/watch?v=M9KhMLia8OI }}

- Uma das partes mais legais (pelo menos para mim) é o foco em rodar seus jogos localmente e usar a Steam Machine e os Steam Frames para o streaming
  - Uma espécie de ecossistema de media centers que você controla
  - Porém o Steam Frame também é um computador independente, que usa ARM

- E no finalzinho de 2025, tudo ficou mais interessante com uma postagem inocente:

<https://fex-emu.com/FEXiversary/>

> Quero agradecer ao pessoal da Valve por estar aqui desde o início e me permitir dar o pontapé inicial neste projeto. Eles confiaram em mim a responsabilidade de conceber e estruturar o projeto de forma que ele possa funcionar a longo prazo; não apenas para seus casos de uso, mas também para mantê-lo como um projeto aberto que qualquer pessoa pode adaptar para seus próprios casos de uso.

- Isso quer dizer que a Valve está investindo nisso "secretamente" desde 2018 e isso era um 'segredo aberto'!

- O Fex é uma camada de compatibilidade da arquitetura x86 rodando em arm.
  - Jogos (e software em geral) que rodam no seu desktop, por exemplo Portal, poderiam rodar num processador de celular
- Além disso, vazamentos do steamdb mostram que a Valve também fez um fork do Waydroid chamado Lepton:
  - Jogos (e software em geral) que roda no Android poderia ser rodado num ambiente Linux
  - Aparentemente o código ainda não está disponível e eles não contataram os desenvolvedores diretamente
  - Isso provavelmente vai permitir que o Frame rode software dos outros óculos VR como o Meta Quest
- Precisamos lembrar do precedente da Valve financiando o Proton (e o Wine) e o DXVK. Esses projetos causaram um impacto imenso na adoção de Linux como uma plataforma de jogos

  <https://diolinux.com.br/noticias/steam-chega-ao-arm64.html>


### Conclusões

- A Valve está apostando na interoperabilidade entre diferentes hardwares como estratégia
- A Valve está investindo pesado nos projetos open source que usa.
  - Não só como doação, mas contratando desenvolvedores
  - Os projetos continuam sendo open source e disponíveis para a comunidade
- As diferentes camadas de compatibilidade permitem a Valve superar esse período de transição estranho do seu hardware (x86 é muito caro e gasta muita energia) dando uma saída para desenvolvedores reaproveitarem seus jogos em diferentes arquiteturas
- Os projetos serem abertos deixa a porta aberta para a competição de outros fabricantes de hardware reutilizarem eles para criação de diferentes produtos
  - China, eu estou olhando para você

- Falando em China, esses projetos podem ajudar com a transição que o governo Chinês anunciou para Linux e RISC-V

> “if you program and want any longevity to your work, make a game. all else recycles, but people rewrite architectures to keep games alive.”   
> ― Why The Lucky Stiff

### Referências

{{#embed https://youtube.com/watch?v=zkDjLWsMg1A }}

{{#embed https://youtube.com/watch?v=3yDXyW1WERg }}
