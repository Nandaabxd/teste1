# 🚀 BUILD COMPLETO NFC WRITER PRO2 - GOOGLE COLAB
# ================================================
# Execute cada célula em ordem

# CÉLULA 1: Montar Google Drive
from google.colab import drive
drive.mount('/content/drive')

# CÉLULA 2: Instalar dependências do sistema
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

# CÉLULA 3: Configurar Java
import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-17-openjdk-amd64'
os.environ['PATH'] = f"{os.environ['JAVA_HOME']}/bin:{os.environ['PATH']}"
!java -version

# CÉLULA 4: Instalar buildozer
!pip install buildozer==1.4.0

# CÉLULA 5: Copiar arquivos do projeto
# ALTERE O CAMINHO CONFORME SUA ESTRUTURA NO GOOGLE DRIVE
!cp -r /content/drive/MyDrive/apps/nfc-writer-pro2/* /content/

# CÉLULA 6: Verificar arquivos copiados
!ls -la /content/
!echo "Arquivos Python encontrados:"
!ls -la *.py

# CÉLULA 7: Fazer build do APK
%cd /content
!yes | buildozer android debug --verbose

# CÉLULA 8: Verificar se APK foi gerado
!ls -la bin/
!echo "APKs encontrados:"
!find . -name "*.apk" -type f

# CÉLULA 9: Download do APK
from google.colab import files
import os
import glob

# Encontrar APKs
apk_files = glob.glob('bin/*.apk')
print(f"APKs encontrados: {apk_files}")

# Download do primeiro APK
if apk_files:
    apk_file = apk_files[0]
    print(f"📱 Fazendo download do APK: {apk_file}")
    files.download(apk_file)
    print("✅ Download concluído!")
    
    # Mostrar informações
    size = os.path.getsize(apk_file)
    print(f"📊 Tamanho do APK: {size / (1024*1024):.1f} MB")
else:
    print("❌ Nenhum APK encontrado!")
    print("📋 Verifique os logs de build acima")

print("🎉 Build concluído!")
