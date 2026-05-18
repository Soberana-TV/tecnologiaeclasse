# LInux é bom nos jogos agora?

É 2026 e parece que o Linux como uma plataforma de jogos já está completamente estabelecido, eu queria tirar esse vídeo pra tentar conversar um pouco sobre como isso acontece e ensinar pra vocês sobre as diferenças dos sistemas operacionais

- Isso aqui me quebrou um pouco hehehe:

{{#embed https://www.youtube.com/watch?v=etBhMqt4Y1g }}

### Por que Linux tem dificuldade rodando jogos de Windows?

- Existem alguns problemas de compatibilidade entre softwares em diferentes máquinas:
  - Arquitetura da máquina que estamos rodando (x86 vs ARM por ex.)
  - Acesso a hardware (por ex. a placa de vídeo faz operações rápidas com 3D vs uma placa que só faz 2D)
  - O sistema operacional existe para ajudar a abstrair diferenças entre ambientes, mas daí sistemas operacionais diferentes tem ‘interfaces de programação’ diferentes 

#### Diferenças entre arquiteturas

```
# x86 ou processadores "intel"

section .data
a dd 10
b dd 20
resultado dd 0

section .text
global _start

_start:
    mov eax, [a]
    add eax, [b]
    mov [resultado], eax
```

```
# arquitetura arm

.data
a: .word 10
b: .word 20
resultado: .word 0

.text
.global _start

_start:
    ldr r0, =a
    ldr r1, [r0]

    ldr r0, =b
    ldr r2, [r0]

    add r3, r1, r2

    ldr r0, =resultado
    str r3, [r0]
```

#### Diferenças entre sistemas operacionais

```c
// Criando uma janela com a API win32
// x86_64-w64-mingw32-gcc main.c -o app.exe
#include <windows.h>

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    switch (msg) {
        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;
    }

    return DefWindowProc(hwnd, msg, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
                   LPSTR lpCmdLine, int nCmdShow) {

    const char CLASS_NAME[] = "MinhaJanela";

    WNDCLASS wc = {0};
    wc.lpfnWndProc = WndProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(
        0,
        CLASS_NAME,
        "Janela Windows",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT,
        800, 600,
        NULL, NULL,
        hInstance,
        NULL
    );

    ShowWindow(hwnd, nCmdShow);

    MSG msg = {0};

    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}
```

```c
// Criando uma janela com a libgtk4
// gcc gnome.c -o app `pkg-config --cflags --libs gtk4`
#include <gtk/gtk.h>

static void activate(GtkApplication *app, gpointer user_data) {
    GtkWidget *window;

    window = gtk_application_window_new(app);

    gtk_window_set_title(GTK_WINDOW(window), "Janela GNOME");
    gtk_window_set_default_size(GTK_WINDOW(window), 800, 600);

    gtk_widget_show(window);
}

int main(int argc, char **argv) {
    GtkApplication *app;
    int status;

    app = gtk_application_new(
        "com.exemplo.janela",
        G_APPLICATION_DEFAULT_FLAGS
    );

    g_signal_connect(app, "activate", G_CALLBACK(activate), NULL);

    status = g_application_run(G_APPLICATION(app), argc, argv);

    g_object_unref(app);

    return status;
}
```

- Incompatibilidades de hardware, API, versões de sistemas operacionais também acontecem no próprio Windows e o canal do Nathan Baggs é um ótimo recurso pra quem quiser ver como isso funciona prática

{{#embed https://www.youtube.com/watch?v=FUJY1jcWmJU}}

- As incompatibilidades entre o Windows e o Linux são imensas, tanto no nível de kernel quanto nas APIs necessárias (gráficos, áudio, inputs/outputs, escrita no sistema de arquivos)
- E esse é o trabalho que o projeto Wine faz. O Wine não é um emulador (WINE Is Not an Emulator). Ele reescreve as partes que são diferentes para que o processador possa rodar as partes que são compatíveis

- Vocês sabiam que isso existe?

[https://appdb.winehq.org/](https://appdb.winehq.org/ (preview))

### Aí que entra a Valve, o Proton, o Fex e etc…

[https://github.com/ValveSoftware/Proton/](https://github.com/ValveSoftware/Proton/ (preview))

[https://www.protondb.com](https://www.protondb.com (preview))

{{#embed https://www.youtube.com/watch?v=TRn8rE6SGUo }}


### E tem muito mais…

- Quando o assunto é compatibilidade, distribuição, emulação e etc… a comunidade do software livre dá um banho de bola

- Lutris (antigo Play on Linux), Batocera, Retroarch / Retropi, emuladores com suporte a online (faz um tempinho eu usava o truque do Steam Remote Play), todos aqueles consoles chineses rodando Linux

- Então na real eu sempre soube que dava pra se divertir com Linux. Eu tenho feito isso faz muito tempo. Mas eu realmente estou chocado com isso virando uma mais mainstream kkkkk

# Vencemo!

# Zawacki 🤝 Kowalski
