# 📱 Guia de Compilação - NFC Reader & Writer PRO

## 🚀 Como Compilar o APK

### 📋 Pré-requisitos

1. **Python 3.9+** instalado e no PATH
2. **Git** instalado
3. **Pelo menos 8GB** de espaço livre em disco
4. **Conexão estável** com a internet

### 🔧 Preparação do Ambiente

#### No Windows:

```bash
# 1. Clone ou baixe o projeto
cd C:\Users\maria\OneDrive\Desktop\teste1

# 2. (Opcional) Crie um ambiente virtual
python -m venv buildozer_env
buildozer_env\Scripts\activate

# 3. Instale dependências básicas
pip install buildozer Cython==0.29.33

# 4. Verifique se todos os arquivos estão presentes
dir main.py buildozer.spec templates\AndroidManifest.tmpl.xml
```

### 🏗️ Processo de Build

#### Método 1: Script Automático (Recomendado)

```bash
# Execute o script de build
build_apk.bat
```

#### Método 2: Manual

```bash
# Limpe builds anteriores (se necessário)
buildozer android clean

# Compile o APK em modo debug
buildozer android debug

# Para versão release (após testes)
buildozer android release
```

#### Método 3: Com Monitoramento

```bash
# Terminal 1: Execute o build
build_apk.bat

# Terminal 2: Monitore o progresso
monitor_build.bat
```

### ⏱️ Tempo Estimado

- **Primeira compilação**: 20-40 minutos
  - Download Android SDK: ~10-15 min
  - Download Android NDK: ~5-10 min
  - Download dependências Python: ~5 min
  - Compilação: ~5-10 min

- **Compilações subsequentes**: 3-8 minutos

### 📁 Estrutura de Arquivos Após Build

```
teste1/
├── main.py                     # Código principal
├── buildozer.spec             # Configuração do build
├── templates/
│   └── AndroidManifest.tmpl.xml  # Manifest personalizado
├── .buildozer/                # Cache de build (criado automaticamente)
│   └── android/
│       ├── platform/          # Android SDK/NDK
│       └── app/               # Arquivos temporários
└── bin/                       # APKs gerados
    └── nfcwriterpro-2.0-debug.apk
```

### 🎯 Arquivos de Saída

- **Debug APK**: `bin/nfcwriterpro-2.0-debug.apk`
- **Release APK**: `bin/nfcwriterpro-2.0-release.apk` (se compilado)

### 📱 Instalação no Dispositivo

#### Via ADB (Recomendado):

```bash
# 1. Conecte o dispositivo via USB
# 2. Ative "Depuração USB" nas configurações do desenvolvedor
# 3. Execute:
adb install bin/nfcwriterpro-2.0-debug.apk
```

#### Via Transferência Manual:

1. Copie o APK para o dispositivo
2. Ative "Fontes desconhecidas" nas configurações
3. Toque no arquivo APK para instalar

### 🔧 Resolução de Problemas

#### Erro: "Python not found"
```bash
# Adicione Python ao PATH ou use caminho completo
C:\Python39\python.exe -m pip install buildozer
```

#### Erro: "SDK/NDK download failed"
```bash
# Limpe o cache e tente novamente
buildozer android clean
# Configure proxy se necessário
set HTTP_PROXY=http://proxy:port
set HTTPS_PROXY=http://proxy:port
```

#### Erro: "Out of space"
```bash
# Verifique espaço em disco
dir C:\ | findstr bytes
# Limpe arquivos temporários
buildozer android clean
```

#### Erro: "Build failed"
```bash
# Aumente o log level para debug
buildozer android debug -v
# Ou verifique o log detalhado
type .buildozer\android\platform\.buildozer.log
```

### 📊 Configurações Avançadas

#### Para modificar a versão:
```ini
# Em buildozer.spec
version = 2.1
android.numeric_version = 21
```

#### Para adicionar permissões:
```xml
<!-- Em templates/AndroidManifest.tmpl.xml -->
<uses-permission android:name="android.permission.CAMERA" />
```

#### Para otimizar tamanho do APK:
```ini
# Em buildozer.spec
android.archs = armeabi-v7a  # Apenas uma arquitetura
source.exclude_dirs = tests, docs, examples
```

### 🚀 Configurações de Release

Para gerar APK de produção:

```bash
# 1. Crie uma keystore (apenas uma vez)
keytool -genkey -v -keystore nfcpro.keystore -alias nfcpro -keyalg RSA -keysize 2048 -validity 10000

# 2. Configure no buildozer.spec
android.keystore = nfcpro.keystore
android.keyalias = nfcpro
android.keystore_passwd = SUA_SENHA
android.keyalias_passwd = SUA_SENHA

# 3. Compile release
buildozer android release
```

### 📈 Otimizações de Performance

1. **Use perfil de release** para distribuição
2. **Minimize dependências** desnecessárias
3. **Otimize recursos** (imagens, assets)
4. **Configure ProGuard** para ofuscação

### 🔍 Verificação do APK

```bash
# Verifique informações do APK
aapt dump badging bin/nfcwriterpro-2.0-debug.apk

# Verifique permissões
aapt dump permissions bin/nfcwriterpro-2.0-debug.apk

# Verifique tamanho dos componentes
unzip -l bin/nfcwriterpro-2.0-debug.apk
```

### 🎯 Checklist Final

- [ ] ✅ Python 3.9+ instalado
- [ ] ✅ Buildozer instalado
- [ ] ✅ Arquivos do projeto completos
- [ ] ✅ buildozer.spec configurado
- [ ] ✅ AndroidManifest.tmpl.xml presente
- [ ] ✅ Espaço em disco suficiente (8GB+)
- [ ] ✅ Conexão com internet estável
- [ ] ✅ APK gerado com sucesso
- [ ] ✅ APK testado em dispositivo real

---

**💡 Dica**: Mantenha o cache do buildozer (.buildozer/) entre builds para acelerar compilações futuras.

**🔒 Segurança**: Para builds de produção, sempre use keystores seguros e senhas fortes.

**🐛 Debug**: Use `buildozer android debug -v` para logs detalhados em caso de problemas.
