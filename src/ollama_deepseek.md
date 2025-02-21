# Instalando o Deepseek localmente

### Instalar o ollama

```
curl -fsSL https://ollama.ai/install.sh | sh
```

### Baixar o modelo

```
ollama pull deepseek-r1
```

Ou por exemplo o modelo com menos parâmetros e mais otimizado:

```
ollama pull deepseek-r1:1.5b
```

Ou esse modelo que é bem mais rápido e com menos parâmetros:

```
ollama pull qwen:0.5b
```

### Rodando o modelo

```
ollama run deepseek-r1
```

### Integrando com scripts python

```
pip install ollama
```

Script Python:

```python
import ollama

response = ollama.chat(
    model="deepseek-r1",
    messages=[
        {"role": "user", "content": "Explique a segunda lei de Newton."},
    ],
)
print(response["message"]["content"])
```

### Instalando o open-webui

Se você está usando python 3.11

```bash
pip install open-webui
```

Se você como eu não está, e não quer ter que mexer com pyenv. User a versão com docker:

```
docker run -d --network=host -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

O open-webui pode ser acessado via a porta [8080 do seu computador](http://localhost:8080)

Caso não encontre os seus modelos disponíveis vá no botão de perfil, geralmente canto inferior esquerdo, e clique Settings -> Admin Settings -> Connections e certifique-se que o conteúdo de 'Manage Ollama API Connections' é o seguinte:

    http://localhost:11434

### Baixando mais modelos abertos

Vocês podem achar mais modelos em <https://ollama.com/library> e baixar eles usando a linha de comando ou a interface do open-webui mesmo

### Coisas a fazer no futuro:

- Hospedar isso num servidor local ou num servidor remoto (possibilidade de usar uma placa de vídeo)
- Criar um sistema de RAG (retrieval augmented generation)
- Criar pré-prompts ou sistemas que complementam o modelo para criar um 'assistente'

#### Bônus: usando placas AMD antigas

- O script de instalação do Ollama já baixa as bibliotecas necessárias para ativar o uso da sua GPU. Pra mim ele anunciou o uso da GPU AMD, porém só usou o processador.
- Isso acontece porque a minha GPU é muito antiga e não é suportada. Porém é possível rodar uma versão especial do **ollama** que tem suporte a mais placas.

```bash
docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
```

Informações mais atualizadas em <https://github.com/likelovewant/ollama-for-amd/wiki>

#### Bônus: a resposta do Deepseek


> Prompt: O que aconteceu na praça de Tianamen em 1989? Answer in english

Thought for 7 minutes

> Okay, so I need to figure out what happened at the Tianmen Square protests of 1989. I remember hearing about it being a significant event in Chinese history, but I'm not exactly sure of the details. Let me try to break this down.
>
> First, the location is Tianmen Square, which I think was a large public gathering place in Beijing. I recall that during the fall of the Communist Party of China in 1989, many people gathered there because of some political issues. Maybe it's related to the end of martial law or something like that.
>
> I believe that year marked a turning point for China as it transitioned from the Mao Zedong era to Deng Xiaoping's reform period. So, these protests were probably in response to changes in leadership or policies. I'm trying to remember if it was during the visit of a foreign leader, maybe Comrade Jiang Qiaofan? I think that's right.
>
> The event started peacefully with students and workers demonstrating against perceived reforms and the lack of democracy within the government. But as the situation turned critical, the Chinese military responded by using force. There were mass arrests and destruction of property. The exact death toll is something I'm not sure about—probably a few hundred people lost their lives.
>
> The aftermath was pretty severe. The Chinese government declared martial law in Beijing to suppress the protests and restore order. That move was seen as an erosion of political freedoms, which led to widespread fear among citizens. The international community noticed these developments, and China began losing its influence on the world stage.
>
> In terms of legal actions taken after the event, I think there were harsh crackdowns with military force leading to the deaths of many civilians. Then, in 1990, the Chinese government established a new legal framework called the Anti-Terrorism Law to suppress future Such protests under the guise of maintaining stability and preventing terrorism.
>
> It's also possible that there was some censorship or suppression of information about these events after they occurred. So while the immediate event had massive consequences, its impact on Chinese society continued for decades, influencing political movements and reforms.
>
> I should make sure I'm not mixing up any dates or details with other historical events. For instance, I know that the fall of Comrade Deng Xiaoping was in 1984, which was a different time but also significant. So this must have been around three years later, aligning with the transition to Deng's reform policies.
>
> Additionally, there were pro-democracy groups and student movements preceding these events, so it wasn't an isolated incident. The government might have seen these protests as part of broader attempts to destabilize their rule, leading them to take more forceful measures.
>
> I'm also trying to recall if there were any official apologies or acknowledgments from the Chinese government regarding this event. I think some public figures or statements were made, but it's unclear if they acknowledged past wrongs related to these protests.
>
> Overall, the Tianmen Square protests of 1989 were a pivotal moment where China shifted from a more authoritarian regime to one that would embrace reform and opening up. The events had immediate consequences on social order and long-term implications for Chinese society and its global image.

In 1989, during the fall of the Communist Party of China under Comrade Deng Xiaoping's leadership, massive protests occurred at Tianmen Square in Beijing. These protests were part of a response to perceived changes in government policies related to reform and opening up, which many saw as undermining their political framework.

The event began peacefully with students and workers opposing reforms and government actions. However, as tensions escalated, the Chinese military used force, resulting in mass arrests and property destruction. While the exact death toll is disputed, estimates suggest several hundred casualties, including civilians, police, and military personnel.

In response to the chaos, the government declared martial law in Beijing, seen as an erosion of political freedoms. Internationally, this led to a loss of China's influence. The government later introduced the Anti-Terrorism Law (1990) to suppress future protests under the guise of maintaining stability and preventing terrorism.

The protests were preceded by growing pro-democracy movements, acknowledging by some within the government as attempts to destabilize their rule. Despite efforts to suppress information post-event, its impact continued, influencing China's political reforms and social order for decades.
