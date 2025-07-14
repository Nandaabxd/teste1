# 🚀 NFC Writer PRO2 - Build no Linux

## 📱 Sobre o App
**NFC Writer PRO2** é um aplicativo avançado para leitura e escrita de tags NFC com funcionalidades PRO:
- ✅ Leitura avançada de tags NFC
- ✅ Escrita personalizada de dados
- ✅ Sistema de perfis e automação
- ✅ Interface moderna com abas
- ✅ Comandos do sistema Android
- ✅ Integração completa com NFC

## 🛠️ Opções de Build

### 🔥 Opção 1: Google Colab (Recomendado)

1. **Organize seus arquivos no Google Drive:**
   ```
   MyDrive/apps/nfc-writer-pro2/
   ├── main.py
   ├── nfc_automation.py
   ├── nfc_writer.py
   ├── utils.py
   ├── config.py
   ├── requirements.txt
   ├── buildozer.spec
   └── templates/AndroidManifest.tmpl.xml
   ```

2. **Abra o Google Colab**
3. **Cole o código do arquivo `colab_build.py`**
4. **Execute célula por célula**
5. **Faça download do APK gerado**

### 🐧 Opção 2: Ubuntu/Linux

1. **Execute o script de instalação:**
   ```bash
   chmod +x install_linux.sh
   ./install_linux.sh
   ```

2. **Copie seus arquivos Python para o diretório criado**

3. **Execute o build:**
   ```bash
   ./build.sh
   ```

### 🔧 Opção 3: Manual

1. **Instalar dependências:**
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3-pip build-essential git python3-dev openjdk-17-jdk
   sudo apt-get install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
   sudo apt-get install -y libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
   ```

2. **Instalar buildozer:**
   ```bash
   pip3 install buildozer==1.4.0
   ```

3. **Configurar Java:**
   ```bash
   export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
   ```

4. **Buildar:**
   ```bash
   buildozer android debug
   ```

## 📁 Estrutura do Projeto

```
nfc-writer-pro2/
├── main.py                 # Aplicativo principal
├── nfc_automation.py       # Sistema de automação
├── nfc_writer.py          # Módulo de escrita NFC
├── utils.py               # Utilitários
├── config.py              # Configurações
├── requirements.txt       # Dependências Python
├── buildozer.spec         # Configuração do build
├── templates/
│   └── AndroidManifest.tmpl.xml
├── bin/                   # APKs gerados
├── .buildozer/           # Cache do buildozer
└── build.sh              # Script de build
```

## 🎯 Configurações do Build

### buildozer.spec
```ini
[app]
title = NFC Reader & Writer PRO2
package.name = nfcwriterpro2
package.domain = org.nfctools
version = 2.0
requirements = python3,kivy==master, https://github.com/kivymd/KivyMD/archive/master.zip,pyjnius==1.6.1,android

[buildozer]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools = 33.0.2
```

### Permissões Android
- `android.permission.NFC` - Acesso ao NFC
- `android.permission.INTERNET` - Conexão à internet
- `android.permission.BLUETOOTH` - Controle Bluetooth
- `android.permission.ACCESS_WIFI_STATE` - Controle Wi-Fi
- `android.permission.MODIFY_AUDIO_SETTINGS` - Controle de volume
- `android.permission.CAMERA` - Acesso à câmera
- `android.permission.FLASHLIGHT` - Controle da lanterna

## 🚀 Processo de Build

1. **Preparação do ambiente**
   - Instalar dependências do sistema
   - Configurar Java JDK 17
   - Instalar buildozer

2. **Download automático**
   - Android SDK
   - Android NDK
   - Build tools

3. **Compilação**
   - Compilar código Python
   - Gerar classes Java
   - Buildar APK

4. **Resultado**
   - APK gerado em `bin/`
   - Pronto para instalação

## 📱 Resultado Final

Você terá um APK com:
- **Nome:** `nfcwriterpro2-2.0-armeabi-v7a-debug.apk`
- **Tamanho:** ~30-50 MB
- **Compatibilidade:** Android 5.0+ (API 21+)
- **Arquitetura:** ARM 32-bit (armeabi-v7a)

## 🔧 Troubleshooting

### Erro de licença Android
```bash
yes | sdkmanager --licenses
```

### Erro de memória
```bash
export GRADLE_OPTS='-Xmx2g'
```

### Erro de NDK
```bash
rm -rf ~/.buildozer/android/platform/android-ndk-*
buildozer android debug
```

### Erro de SDK
```bash
rm -rf ~/.buildozer/android/platform/android-sdk-*
buildozer android debug
```

## 📋 Checklist de Build

- [ ] Ambiente Linux configurado
- [ ] Java JDK 17 instalado
- [ ] Dependências SDL2 instaladas
- [ ] Buildozer instalado
- [ ] Arquivos Python copiados
- [ ] buildozer.spec configurado
- [ ] AndroidManifest.tmpl.xml criado
- [ ] Build executado com sucesso
- [ ] APK gerado em bin/
- [ ] APK testado no dispositivo

## 🌟 Dicas PRO

1. **Use Google Colab** para builds rápidos
2. **Mantenha cache** do buildozer entre builds
3. **Teste sempre** no dispositivo real
4. **Monitore logs** para debugar problemas
5. **Use build release** para produção

## 📞 Suporte

Se houver problemas:
1. Verifique os logs do buildozer
2. Confirme que todas as dependências estão instaladas
3. Teste em ambiente limpo (Google Colab)
4. Verifique se os arquivos Python estão no local correto

---

**✨ Seu app NFC Writer PRO2 está pronto para ser buildado!**
