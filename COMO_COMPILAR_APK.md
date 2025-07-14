# Como Compilar APK no Windows

## IMPORTANTE: Limitações do Windows

O Buildozer não funciona nativamente no Windows para compilar APKs Android. 
Você tem algumas opções:

### Opção 1: Usar WSL (Windows Subsystem for Linux) - RECOMENDADO

1. **Instale o WSL2:**
   ```powershell
   wsl --install
   ```

2. **Abra o Ubuntu no WSL e execute:**
   ```bash
   # Atualize o sistema
   sudo apt update && sudo apt upgrade -y
   
   # Instale dependências
   sudo apt install -y python3-pip python3-venv git openjdk-8-jdk unzip
   
   # Instale o Buildozer
   pip3 install buildozer
   
   # Copie os arquivos do projeto para o WSL
   cp -r /mnt/c/Users/maria/OneDrive/Desktop/teste1 ~/nfc-app
   cd ~/nfc-app
   
   # Compile o APK
   buildozer android debug
   ```

### Opção 2: Usar uma VM Linux

1. Instale VirtualBox ou VMware
2. Crie uma VM Ubuntu
3. Siga os mesmos passos da Opção 1

### Opção 3: Usar Docker (Avançado)

```dockerfile
# Dockerfile para compilar APK
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \\
    python3-pip python3-venv git openjdk-8-jdk unzip \\
    build-essential libssl-dev libffi-dev python3-dev

RUN pip3 install buildozer

WORKDIR /app
COPY . .

CMD ["buildozer", "android", "debug"]
```

### Opção 4: Usar GitHub Actions (Online)

Crie um arquivo `.github/workflows/build-apk.yml`:

```yaml
name: Build APK

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    
    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y openjdk-8-jdk unzip
        pip install buildozer
    
    - name: Build APK
      run: buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v2
      with:
        name: apk
        path: bin/*.apk
```

## Requisitos para Qualquer Método

Independente do método escolhido, você precisará:

1. **Java Development Kit (JDK) 8**
2. **Android SDK** (será baixado automaticamente pelo Buildozer)
3. **Android NDK** (será baixado automaticamente pelo Buildozer)
4. **Python 3.7+**
5. **Git**

## Primeira Compilação

A primeira compilação pode demorar **30-60 minutos** pois o Buildozer precisa:
- Baixar o Android SDK (~1GB)
- Baixar o Android NDK (~1GB)
- Compilar as dependências Python
- Configurar o ambiente

## Resolução de Problemas Comuns

### Erro: "Command failed: ./gradlew assembleDebug"
- Certifique-se de que o Java 8 está instalado
- Verifique se as variáveis de ambiente estão configuradas

### Erro: "SDK not found"
- O Buildozer baixa automaticamente o SDK
- Aguarde a primeira compilação terminar

### Erro: "Permission denied"
- No Linux/WSL, use `chmod +x` nos scripts
- Certifique-se de ter permissões de escrita

## Resultado Final

Após a compilação bem-sucedida, você encontrará:
- `bin/nfcreader-0.1-debug.apk` - APK para instalação
- `.buildozer/` - Pasta com SDK e dependências (pode ser deletada para liberar espaço)

## Instalação no Dispositivo

```bash
# Via ADB (Android Debug Bridge)
adb install bin/nfcreader-0.1-debug.apk

# Ou transfira o APK para o dispositivo e instale manualmente
```

## Para Produção

Para gerar um APK assinado para publicação:

```bash
# Gere uma chave de assinatura
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000

# Configure no buildozer.spec:
# android.release_artifact = apk
# android.debug_artifact = apk

# Compile em modo release
buildozer android release
```
