# 🚀 Guia Completo para Build do NFC Writer PRO2

## ⚠️ Importante: Buildozer funciona apenas em Linux/WSL

O buildozer não funciona nativamente no Windows. Use uma das opções abaixo:

## 🔧 Opção 1: Google Colab (Recomendado)

### 1. Preparar arquivos no Google Drive
```
MyDrive/
└── apps/
    └── nfc-writer-pro2/
        ├── main.py
        ├── nfc_automation.py
        ├── nfc_writer.py
        ├── utils.py
        ├── config.py
        ├── requirements.txt
        ├── buildozer.spec
        └── templates/
            └── AndroidManifest.tmpl.xml
```

### 2. Código para Google Colab
```python
# 1. Montar Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. Copiar projeto
!cp -r /content/drive/MyDrive/apps/nfc-writer-pro2/* /content/

# 3. Instalar dependências do sistema
!sudo apt-get update
!sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    openjdk-17-jdk \
    unzip \
    zip

# 4. Instalar buildozer
!pip install buildozer==1.4.0

# 5. Configurar Java
import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-17-openjdk-amd64'
os.environ['PATH'] = f"{os.environ['JAVA_HOME']}/bin:{os.environ['PATH']}"

# 6. Navegar para o projeto
%cd /content

# 7. Instalar Android SDK automaticamente e buildar
!yes | buildozer android debug

# 8. Verificar se APK foi gerado
!ls -la bin/
```

### 3. Download do APK
```python
# Fazer download do APK gerado
from google.colab import files
import os

apk_files = [f for f in os.listdir('bin') if f.endswith('.apk')]
if apk_files:
    files.download(f'bin/{apk_files[0]}')
    print(f"✅ APK {apk_files[0]} disponível para download!")
else:
    print("❌ Nenhum APK encontrado!")
```

## 🔧 Opção 2: WSL (Windows Subsystem for Linux)

### 1. Instalar WSL
```powershell
# No PowerShell como administrador
wsl --install -d Ubuntu
```

### 2. Configurar no WSL
```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    openjdk-17-jdk \
    unzip \
    zip

# Instalar buildozer
pip3 install buildozer==1.4.0

# Configurar Java
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

# Copiar projeto para WSL
cp -r /mnt/c/Users/maria/OneDrive/Desktop/teste1/* ~/nfc-project/
cd ~/nfc-project

# Buildar
buildozer android debug
```

## 🔧 Opção 3: Docker (Avançado)

### 1. Criar Dockerfile
```dockerfile
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    openjdk-17-jdk \
    unzip \
    zip

RUN pip3 install buildozer==1.4.0

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

WORKDIR /app
COPY . .

CMD ["buildozer", "android", "debug"]
```

### 2. Buildar com Docker
```bash
# Buildar imagem
docker build -t nfc-builder .

# Executar build
docker run -v $(pwd):/app nfc-builder
```

## 📱 Configurações do buildozer.spec

Seu arquivo já está configurado corretamente:

```plaintext
requirements = python3,kivy==master, https://github.com/kivymd/KivyMD/archive/master.zip,pyjnius==1.6.1,android
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools = 33.0.2
```

## 🎯 Resultado Esperado

Após o build bem-sucedido, você terá:
- ✅ APK gerado em `bin/`
- ✅ Arquivo: `nfcwriterpro2-2.0-armeabi-v7a-debug.apk`
- ✅ Pronto para instalar no Android

## 🔍 Troubleshooting

### Se der erro de licença Android SDK:
```bash
# Aceitar licenças
yes | sdkmanager --licenses
```

### Se der erro de memória:
```bash
# No Google Colab
!echo "export GRADLE_OPTS='-Xmx2g -Dorg.gradle.jvmargs=\"-Xmx2g\"'" >> ~/.bashrc
```

### Se der erro de NDK:
```bash
# Forçar download do NDK
buildozer android debug --verbose
```

## 📋 Checklist Final

- [ ] Todos os arquivos copiados para o ambiente Linux
- [ ] Dependências do sistema instaladas
- [ ] Java 17 configurado
- [ ] Buildozer instalado
- [ ] Comando `buildozer android debug` executado
- [ ] APK gerado na pasta `bin/`
- [ ] APK testado no dispositivo Android

## 🌟 Dica PRO

Para builds mais rápidos, use cache do buildozer:
```bash
# Manter cache entre builds
export BUILDOZER_CACHE_DIR=~/.buildozer-cache
buildozer android debug
```

---

**✨ Recomendação:** Use o Google Colab para facilidade, pois já tem tudo pré-configurado!
