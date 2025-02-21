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
