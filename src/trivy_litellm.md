# O hack do Trivy e do LiteLLM

Um dos pacotes mais usados para rodar LLMs foi comprometido. Não dá gurizada, agora é um hack de grande repercussão a cada semana e dessa vez eu quase rodei.

- No dia 24/03/26 o projeto litellm, que é um adaptador para facilitar o uso de diferentes provedores de LLM a projetos python foi comprometida e lançou duas versões batizadas a **1\.82.7** (instala o malware quando a lib é importada) e a **1\.82.8** (instala o malware quando qualquer processo python roda!)

- Coincidentemente nesse mesmo dia eu estava lançando um vídeo em que eu falava do projeto por nome e por muita sorte essa linha de código aqui no `pyproject.toml` nos salvou

```
"litellm>=1.80.9",
```

{{#embed https://www.youtube.com/watch?v=pjy44tKtXPE }}

<https://github.com/lfzawacki/meridiano>

- E tá tudo bem depender de projetos externos, é uma boa prática e é como fazemos as coisas no desenvolvimento de software... só que não tá tudo bem não

### Linha do tempo dos eventos

- É útil pois tem muitos pequenos detalhes que aconteceram e que simplesmente não

<https://ramimac.me/teampcp/>

### Uma boa explicação

<https://futuresearch.ai/blog/no-prompt-injection-required/>

- O desenvolvedor que reportou o comportamento estranho originalmente estava rodando cursor num mac com 48GB de ram e notou a máquina ficar lenta e travar.
  - Isso era o malware rodando e foi um efeito não planejado de um bug no próprio malware
- Ele faz uma análise dos logs e reporta o bug para o projeto litellm que parece ser o culpado

- O projeto investiga, tira a versão afetada de circulação e abre uma issue para discussão.

- A issue original é marcada como 'não planejada' e bombardeada por contas do github fazendo comentários de spam tipo: "uau legal", "muito obrigado", "eu também". Além de várias reações inúteis

<https://github.com/BerriAI/litellm/issues/24512>

- Fica claro que a conta do mantenedor foi comprometida e que várias contas comprometidas estão tentando enterrar a discussão sobre o problema. Em algum momento é lançada a segunda e mais letal versão do malware.

- Depois a gente descobre que o litellm não fez nada errado e eles foram os alvos escolhidos após o serviço de segurança Trivy ter sido comprometido
- Da mesma forma o repositório do Trivy recebeu spam para tentar enterrar as discussões sobre o assunto

<https://github.com/aquasecurity/trivy/discussions/10420>

- É muito complicado explicar aqui, mas o trivy foi vítima de uma github action vulnerável (automação baseada em novas versões do código) e usando as credenciais do projeto lançou uma action vulnerável ele mesmo
- Essas actions são usadas por milhares de outros projetos que as rodam automaticamente para checar por... falhas de segurança

- Nessa aí o litellm rodou
- Importante entender que foi descoberto relativamente rápido pelo fato que a versão do malware no PC do relator original tinha o bug que fazia um 'forkbomb'
  - E se não tivesse?
  - Quantos outros estão rodando silenciosamente por aí?

### Medidas de prevenção

- Sempre pinnar pacotes
- Rotacionar chaves de tempos em tempos
- Diminuir o número de dependências
- Reduzir superfície de ataque

### Ferramenta para testar por pacote

`pip show litellm`

ou

`find . | grep "litellm-1.8"`

<https://futuresearch.ai/tools/litellm-checker/>

### Conclusões

- O nível dos ataques cresceu de uma maneira muito mais rápida do que os engenheiros de software conseguem acompanhar
- A automação, a cadeia de suprimentos e a geração de código indiscrminada criam vetores de ataque nunca antes imaginados (mentira a gente tá falando aqui no canal faz tempo)
- Como cada um vai lidar com isso?
  - Menos dependência em infraestrutura compartilhada? (por obscuridade)
  - Corrida armamentista com os criadores de malware?
  - Um esforço dedicado para ir mais devagar e criar mecanismos de segurança? ... 🤣🤣🤣🤣
