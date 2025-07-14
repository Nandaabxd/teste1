# 🚀 NFC Writer PRO2 - Google Colab Build
# =========================================
# Cole este código no Google Colab para buildar seu APK

# 1. Montar Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. Instalar dependências do sistema
!sudo apt-get update -qq
!sudo apt-get install -y -qq \
    python3-pip \
    build-essential \
    git \
    python3-dev \
    openjdk-17-jdk \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    autoconf \
    libtool \
    pkg-config \
    cmake \
    libffi-dev \
    libssl-dev \
    ccache \
    unzip \
    zip

# 3. Configurar Java
import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-17-openjdk-amd64'
os.environ['PATH'] = f"{os.environ['JAVA_HOME']}/bin:{os.environ['PATH']}"

# 4. Instalar buildozer
!pip install buildozer==1.4.0

# 5. Copiar arquivos do projeto (ajuste o caminho conforme sua estrutura)
!cp -r /content/drive/MyDrive/apps/nfc-writer-pro2/* /content/
# OU se você colocou diretamente na pasta apps:
# !cp -r /content/drive/MyDrive/apps/* /content/

# 6. Navegar para o diretório
%cd /content

# 7. Verificar arquivos copiados
!ls -la

# 8. Fazer build do APK
!yes | buildozer android debug --verbose

# 9. Verificar se APK foi gerado
!ls -la bin/

# 10. Fazer download do APK
from google.colab import files
import os

# Listar APKs gerados
apk_files = [f for f in os.listdir('bin') if f.endswith('.apk')]
print(f"APKs encontrados: {apk_files}")

# Download do primeiro APK encontrado
if apk_files:
    apk_file = apk_files[0]
    print(f"📱 Fazendo download do APK: {apk_file}")
    files.download(f'bin/{apk_file}')
    print("✅ Download concluído!")
else:
    print("❌ Nenhum APK encontrado!")
    
# 11. Mostrar informações do build
!echo "🎉 Build Information:"
!echo "📱 App: NFC Writer PRO2"
!echo "📁 Diretório: $(pwd)"
!echo "📊 Arquivos bin/:"
!ls -lh bin/
!echo "✅ Build concluído!"
