# tecnologiaeclasse
Roteiros para as lives do canal Tecnologia e Classe.

## Links

- [Tecnologia e Classe](https://teclas.soberana.tv/)
- [Soberana](https://soberana.tv/)

## Notificacoes

Os avisos do topo ficam em `src/notifications.json`:

- `enabled`: liga/desliga a area de avisos.
- `mode`: `"random"` (um aviso aleatorio a cada carregamento de pagina) ou
  `"cycle"` (um aviso apos o outro, em ordem, a cada carregamento).
- `dismissible`: se `true`, o visitante pode fechar o aviso (ele nao volta).
- `notifications`: lista de avisos com `id` (unico), `label`, `message` e
  `link` (`text` e `url`, opcional).

Observacao: o JSON e carregado via `fetch`, entao e preciso abrir o site por
um servidor (`mdbook serve`), nao direto por `file://`.
