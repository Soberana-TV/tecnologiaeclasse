# O hack das carteiras BTC “Coldcard”

Semana passada nós vimos uma ‘invasão’ das carteiras bitcoin Coldcard e isso aconteceu de uma maneira extremamente ‘divertida’ … por que eu não perdi nenhum dinheiro. Vamos explicar

**Assista no canal:**
{{#embed https://www.youtube.com/watch?v=ODr94h4ihZg}}

- “Eu vou esperar o vídeo do Fireship”

{{#embed https://www.youtube.com/watch?v=2X2V3xv_jik }}

- O vídeo deles ficou legitimamente bom, mas considerem que eles lançam um excerto de 5 minutos a cada 2-3 dias e são uma empresa enorme com investimento de capital privado. Óbvio que vai ficar bom o vídeo

- Aqui uma matéria :

[https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/](https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/ (preview))

- Aqui o vendedor do hardware de carteira “fria”: 

  [https://coldcard.com/](https://coldcard.com/ (preview))

- Vamos explicar como funcionam alguns conceitos:
- Dinâmica entre carteira Hot (“conectada à internet”) e Cold (“guardada apenas num dispositivo offline”)
- Afinal o que são carteiras Bitcoin? Apenas uma chave privada que identifica você na rede:
  - Um número de 128 bits ← extremamente difícil de gerar 2 iguais e ‘adivinhar’
  - Gerado uma vez quando você cria a carteira a partir de uma semente aleatória
  - Qualquer um que possua o mesmo número pode autenticar transações em seu nome
  - Lembrando que o ‘saldo’ de uma carteira BTC é a soma de todas transações envolvendo ela
  - E que a blockchain de uma criptomoeda nada mais é do que uma lista de todas as transações já feitas na rede

- A segurança da sua carteira tem a ver com o fato que é infinitamente improvável a geração de 2 chaves de carteira iguais e também é computacionalmente impossível adivinhar uma chave apenas olhando para as transações na rede pública

- Mas e se a semente que gera a chave pública aleatória não for tão aleatória quanto imaginamos???

- Vocês já ouviram falar de RNG Manipulation?

[https://retailrng.com/emerald/beginner/introduction/](https://retailrng.com/emerald/beginner/introduction/ (preview))

{{#embed https://www.youtube.com/watch?v=v1fxop08yOs&list=PL4o9bTT3px_h08zUFb3oChEFku_jG6zyt&index=16 }}

- Agora que eu expliquei uma coisa nerd com uma outra coisa mais nerd e vocês entenderam… foi basicamente isso que fizeram para descobrir um número mais limitado de possibilidades das sementes das carteiras

- Exemplo:

[https://randomos.co.uk/tools/seeded-rng/](https://randomos.co.uk/tools/seeded-rng/ (preview))

- O hardware da carteira não tinha acesso a uma fonte confiável de números aleatórios e portanto eles escreveram o seu próprio firmware que gerava essa aleatoriedade para gerar a seed inicial… porém tinha um erro no código

```
#define MICROPY_HW_ENABLE_RNG (0)

// mais tarde no código de geração de chaves

#ifndef MICROPY_HW_ENABLE_RNG
    gerar_com_custom_rng();
#else
    gerar_com_hw_rng();
```

- Acontece que o código SEMPRE tomava o segundo caminho porque o ifndef testa a definição e não o valor verdade da constante.

- Isso gerou uma entropia extremamente limitada na hora de gerar as chaves e na prática reduziu aquele conjunto colossal de chaves em 128bits para um muito menor, que pode ser explorado com um simples ataque força bruta.

- A única maneira de salvar as suas bitcoins é com a transferência delas para uma nova carteira gerada com uma seed mais segura.
  - Como atacantes com chaves de carteiras válidas podem assinar transações por você, aparentemente está rolando um ataque onde eles monitoram transações e fazem elas antes dos donos (oferecendo uma taxa melhor)

- Em resumo… uma grande confusão

### Respostas da comunidade:

“Putz, perdi U$1.6 mi… comprem meu livro”

<https://xcancel.com/itscoachgoodman/status/2083527082223563157>

“Vocês perderam dinheiro porque são fracos! Descentralização é isso 🤪 ”

<https://xcancel.com/HalesFall/status/2085140029463257333>

“Por favor devolvam a grana. Teremos que envolver o governo!”

<https://xcancel.com/skysupersonic/status/2083912951027634204>

### Conclusão

- As soluções descentralizadas são maravilhas tecnológicas e legitimamente muito interessantes de um ponto de vista técnico

- Na prática do dia a dia diversos problemas assim aparecem e por diversas vezes nós somos obrigados a colocar regras, legislações, acordos e contratos que extrapolam o protocolo tecnológico e nos obrigam a… viver em sociedade.

- Hoje tivemos mais um lembrete do porque é impossível fugir da natureza social do ser humano… infelizmente vocês vão ter que tomar banho e conversar com outros humanos. 
