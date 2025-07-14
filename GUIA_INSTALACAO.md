# 🚀 GUIA COMPLETO - INSTALAÇÃO NFC WRITER PRO2

## 📱 **Opção 1: Google Colab (Mais Fácil)**

### 1. **Organize seus arquivos no Google Drive:**
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

### 2. **Acesse Google Colab:**
- Vá para: https://colab.research.google.com/
- Crie um novo notebook

### 3. **Cole e execute cada célula:**

**CÉLULA 1: Montar Google Drive**
```python
from google.colab import drive
drive.mount('/content/drive')
```

**CÉLULA 2: Instalar dependências**
```bash
!sudo apt-get update -qq
!sudo apt-get install -y -qq \
    python3-pip build-essential git python3-dev openjdk-17-jdk \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
    zlib1g-dev autoconf libtool pkg-config cmake libffi-dev \
    libssl-dev ccache unzip zip
```

**CÉLULA 3: Configurar Java**
```python
import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-17-openjdk-amd64'
os.environ['PATH'] = f"{os.environ['JAVA_HOME']}/bin:{os.environ['PATH']}"
!java -version
```

**CÉLULA 4: Instalar buildozer**
```bash
!pip install buildozer==1.4.0
```

**CÉLULA 5: Copiar arquivos**
```bash
!cp -r /content/drive/MyDrive/apps/nfc-writer-pro2/* /content/
!ls -la *.py
```

**CÉLULA 6: Fazer build**
```bash
%cd /content
!yes | buildozer android debug --verbose
```

**CÉLULA 7: Download do APK**
```python
from google.colab import files
import glob

apk_files = glob.glob('bin/*.apk')
if apk_files:
    files.download(apk_files[0])
    print("✅ Download concluído!")
```

---

## 🐧 **Opção 2: Ubuntu/Linux (WSL)**

### 1. **Abrir WSL Ubuntu:**
- Pressione `Windows + R`
- Digite `wsl` e Enter
- Ou procure "Ubuntu" no menu Iniciar

### 2. **Atualizar sistema:**
```bash
sudo apt update && sudo apt upgrade -y
```

### 3. **Instalar dependências:**
```bash
sudo apt install -y \
    python3 python3-pip python3-dev build-essential git \
    openjdk-17-jdk libsdl2-dev libsdl2-image-dev \
    libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev \
    libswscale-dev libavformat-dev libavcodec-dev \
    zlib1g-dev autoconf libtool pkg-config cmake \
    libffi-dev libssl-dev ccache unzip zip
```

### 4. **Configurar Java:**
```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
echo "export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64" >> ~/.bashrc
echo "export PATH=\$JAVA_HOME/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc
```

### 5. **Instalar buildozer:**
```bash
pip3 install --user buildozer==1.4.0
echo "export PATH=\$HOME/.local/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc
```

### 6. **Criar projeto:**
```bash
mkdir ~/nfc-writer-pro2
cd ~/nfc-writer-pro2
```

### 7. **Copiar arquivos Python:**
```bash
# Copiar do Windows para WSL
cp /mnt/c/Users/maria/OneDrive/Desktop/teste1/*.py ./
cp /mnt/c/Users/maria/OneDrive/Desktop/teste1/buildozer.spec ./
cp /mnt/c/Users/maria/OneDrive/Desktop/teste1/requirements.txt ./
cp -r /mnt/c/Users/maria/OneDrive/Desktop/teste1/templates ./
```

### 8. **Fazer build:**
```bash
buildozer android debug
```

---

## 🔧 **Opção 3: Script Automático (Ubuntu)**

### **Use o script que criamos:**

```bash
# Dar permissão
chmod +x install_linux.sh

# Executar
./install_linux.sh

# Copiar arquivos Python
cp *.py ~/nfc-writer-pro2/

# Fazer build
cd ~/nfc-writer-pro2
./build.sh
```

---

## 🎯 **Qual opção escolher?**

| Opção | Facilidade | Velocidade | Recomendação |
|-------|------------|------------|--------------|
| **Google Colab** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ **Melhor** |
| **WSL** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ **Boa** |
| **Script** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ **Boa** |

---

## 📱 **Resultado Final:**

Você terá um APK:
- **Nome:** `nfcwriterpro2-2.0-armeabi-v7a-debug.apk`
- **Tamanho:** ~30-50 MB
- **Compatibilidade:** Android 5.0+
- **Funcionalidades:** NFC completas

---

## 🆘 **Precisa de ajuda?**

1. **Google Colab não funciona?**
   - Verifique se os arquivos estão no Google Drive
   - Confirme o caminho dos arquivos

2. **WSL não abre?**
   - Execute como administrador: `wsl --install -d Ubuntu`
   - Reinicie o Windows

3. **Build falha?**
   - Verifique se todos os arquivos Python estão presentes
   - Confirme se o Java está configurado

**Qual opção você quer tentar primeiro?**
