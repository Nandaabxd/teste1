# 🐳 TUTORIAL COMPLETO: Compilar APK com Docker

## 🎯 **Por que usar Docker?**

✅ **Ambiente isolado** - Não afeta seu sistema  
✅ **Dependências garantidas** - Todas as ferramentas certas  
✅ **Reproduzível** - Funciona igual em qualquer máquina  
✅ **Mais rápido** - Sem conflitos de versão  
✅ **Limpo** - Não deixa resíduos no sistema  

---

## 📋 **PRÉ-REQUISITOS**

### **1. Instalar Docker Desktop**
1. **Baixe**: https://www.docker.com/products/docker-desktop/
2. **Instale** seguindo o assistente
3. **Reinicie** o computador se solicitado
4. **Abra Docker Desktop** e aguarde inicializar

### **2. Verificar Instalação**
```powershell
# Abra PowerShell e teste:
docker --version
docker-compose --version
```

**Saída esperada**:
```
Docker version 24.x.x
Docker Compose version v2.x.x
```

---

## 🚀 **MÉTODO 1: Script Automático (RECOMENDADO)**

### **Passo 1: Execute o Script**
```powershell
# No diretório do projeto (teste1):
.\build_docker.bat
```

### **O que o script faz**:
1. 🏗️ **Cria imagem Docker** com Android SDK/NDK
2. 📦 **Copia seu código** para o container
3. 🔧 **Configura ambiente** Python/Kivy
4. ⚙️ **Compila o APK** automaticamente
5. 📱 **Copia APK** de volta para Windows

### **Tempo estimado**: 15-25 minutos

---

## 🛠️ **MÉTODO 2: Passo a Passo Manual**

### **Passo 1: Criar Dockerfile**
```dockerfile
# Já criado em: Dockerfile
# Contém toda configuração necessária
```

### **Passo 2: Construir Imagem**
```powershell
# Construir imagem (demora ~10 minutos na primeira vez)
docker build -t nfc-app-builder .
```

### **Passo 3: Executar Compilação**
```powershell
# Executar container e compilar
docker run --rm -v ${PWD}:/workspace nfc-app-builder
```

### **Passo 4: Verificar APK**
```powershell
# Ver APK gerado
ls bin/
```

---

## 📁 **ESTRUTURA DO PROJETO**

```
teste1/
├── 📄 main.py                 # Seu app NFC
├── 📄 buildozer.spec         # Configuração Android
├── 🐳 Dockerfile            # Configuração Docker
├── 📄 build_docker.bat      # Script automático
├── 📄 requirements.txt      # Dependências Python
└── 📁 bin/                  # APK será gerado aqui
    └── nfcwriterpro-2.0-debug.apk
```

---

## 🔍 **MONITORAMENTO EM TEMPO REAL**

### **Ver Logs Durante Compilação**
```powershell
# Em outro PowerShell:
docker logs -f <container_id>
```

### **Encontrar Container ID**
```powershell
# Ver containers rodando:
docker ps
```

### **Entrar no Container (Debug)**
```powershell
# Se precisar investigar:
docker run -it --rm -v ${PWD}:/workspace nfc-app-builder bash
```

---

## 🎛️ **CONFIGURAÇÕES AVANÇADAS**

### **1. Acelerar Build (Cache)**
```powershell
# Usar cache da imagem base:
docker build --cache-from nfc-app-builder -t nfc-app-builder .
```

### **2. Build Multi-Stage (Menor)**
```dockerfile
# Dockerfile já otimizado com multi-stage
FROM ubuntu:22.04 as builder
# ... build steps ...

FROM ubuntu:22.04 as runtime
# ... copy only essentials ...
```

### **3. Personalizar Versões**
```bash
# Edite buildozer.spec para ajustar:
android.api = 33           # API Android
android.minapi = 21        # API mínima
android.ndk = 25b          # NDK version
```

---

## 🔧 **TROUBLESHOOTING**

### **❌ "Docker não reconhecido"**
**Solução**:
```powershell
# 1. Reinicie Docker Desktop
# 2. Adicione ao PATH: C:\Program Files\Docker\Docker\resources\bin
# 3. Reinicie PowerShell
```

### **❌ "Sem permissão no volume"**
**Solução**:
```powershell
# Habilite drive sharing no Docker Desktop:
# Settings > Resources > File Sharing > Add: C:\
```

### **❌ "Build falha por memória"**
**Solução**:
```powershell
# Aumentar memória Docker:
# Settings > Resources > Memory: 6GB+
```

### **❌ "Container não inicia"**
**Solução**:
```powershell
# Limpar containers antigos:
docker system prune -f

# Rebuild sem cache:
docker build --no-cache -t nfc-app-builder .
```

### **❌ "APK não gerado"**
**Solução**:
```powershell
# Ver logs detalhados:
docker run --rm -v ${PWD}:/workspace nfc-app-builder bash -c "cd /workspace && buildozer android debug -v"
```

---

## 📊 **ETAPAS DA COMPILAÇÃO**

| Etapa | Duração | Descrição |
|-------|---------|-----------|
| **1. Pull Base Image** | 2-3 min | Ubuntu 22.04 |
| **2. Install Dependencies** | 5-8 min | Java, Python, build tools |
| **3. Download Android SDK** | 3-5 min | SDK Tools, Platform Tools |
| **4. Download Android NDK** | 2-3 min | NDK r25b |
| **5. Setup Buildozer** | 1-2 min | Python dependencies |
| **6. Build APK** | 8-12 min | Compile & package |
| **📱 Total** | **20-30 min** | **APK Pronto!** |

---

## 🎉 **SUCESSO! APK GERADO**

### **Localizar APK**
```powershell
# APK estará em:
ls bin/nfcwriterpro-2.0-debug.apk
```

### **Testar APK**
1. **📲 Copie** para o celular Android
2. **⚙️ Habilite** "Fontes desconhecidas"
3. **📱 Instale** tocando no arquivo
4. **🔍 Teste** com tag NFC

### **Informações do APK**
- **Nome**: NFC Writer PRO
- **Versão**: 2.0
- **Tamanho**: ~15-25 MB
- **Min Android**: 5.0 (API 21)
- **Target**: Android 13 (API 33)

---

## 🔄 **BUILDS SUBSEQUENTES**

### **Build Rápido (2ª vez)**
```powershell
# Cache Docker torna builds muito mais rápidos:
.\build_docker.bat
# Tempo: ~5-8 minutos
```

### **Clean Build**
```powershell
# Se tiver problemas, build limpo:
docker rmi nfc-app-builder
.\build_docker.bat
```

### **Update do App**
```powershell
# Após modificar main.py:
.\build_docker.bat
# Automático: novo APK com mudanças
```

---

## 🚀 **PRÓXIMOS PASSOS**

### **1. Teste Completo**
- ✅ Instalar APK no celular
- ✅ Testar leitura NFC
- ✅ Verificar todas as funcionalidades

### **2. Deploy Produção**
```powershell
# Build release (assinado):
docker run --rm -v ${PWD}:/workspace nfc-app-builder buildozer android release
```

### **3. Upload Play Store**
- ✅ APK release gerado
- ✅ Criar conta Google Play Console
- ✅ Upload e publicação

---

## 💡 **DICAS PRO**

### **🎯 Otimização**
```bash
# buildozer.spec otimizado:
[app]
requirements = python3,kivy==2.1.0,pyjnius==1.6.1,android
android.arch = arm64-v8a,armeabi-v7a  # Multi-arch
android.release_artifact = aab         # Android App Bundle
```

### **🔧 Debug**
```bash
# Logs detalhados:
buildozer -v android debug
```

### **📱 Teste Automático**
```bash
# Instalar via ADB:
adb install bin/nfcwriterpro-2.0-debug.apk
```

---

**🎯 Está pronto para compilar seu APK com Docker!**

**Execute**: `.\build_docker.bat` e aguarde seu APK ficar pronto! 🚀
