# 📁 Configuração do Google Drive para NFC Writer PRO2

## 🎯 Estrutura do Google Drive

Crie esta estrutura exata no seu Google Drive:

```
MyDrive/
└── apps/
    └── nfc-writer-pro2/
        ├── main.py
        ├── main_clean.py
        ├── nfc_automation.py
        ├── nfc_writer.py
        ├── utils.py
        ├── config.py
        ├── requirements.txt
        ├── buildozer.spec
        ├── README.md
        ├── README_PRO.md
        ├── Dockerfile
        ├── .github/
        │   └── workflows/
        │       └── build-apk.yml
        └── templates/
            └── AndroidManifest.tmpl.xml
```

## 📂 Passos para Upload

### 1. Criar as pastas no Google Drive:
1. Acesse [Google Drive](https://drive.google.com)
2. Crie a pasta `apps`
3. Dentro de `apps`, crie a pasta `nfc-writer-pro2`
4. Dentro de `nfc-writer-pro2`, crie as pastas:
   - `templates`
   - `.github` (depois crie `workflows` dentro dela)

### 2. Fazer upload dos arquivos principais:
Faça upload destes arquivos para `MyDrive/apps/nfc-writer-pro2/`:

**Arquivos Python:**
- `main.py`
- `main_clean.py`
- `nfc_automation.py`
- `nfc_writer.py`
- `utils.py`
- `config.py`

**Arquivos de configuração:**
- `requirements.txt`
- `buildozer.spec`
- `Dockerfile`

**Documentação:**
- `README.md`
- `README_PRO.md`

### 3. Upload dos arquivos especiais:

**Para `MyDrive/apps/nfc-writer-pro2/templates/`:**
- `AndroidManifest.tmpl.xml`

**Para `MyDrive/apps/nfc-writer-pro2/.github/workflows/`:**
- `build-apk.yml`

## 🚀 Comandos para Google Colab

Depois de fazer o upload, use estes comandos no Google Colab:

```python
# 1. Montar o Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. Copiar arquivos do projeto
!cp -r /content/drive/MyDrive/apps/nfc-writer-pro2/* /content/

# 3. Verificar se os arquivos foram copiados
!ls -la /content/

# 4. Verificar se os arquivos Python estão presentes
!ls -la /content/*.py

# 5. Verificar se buildozer.spec está presente
!ls -la /content/buildozer.spec

# 6. Verificar se a pasta templates está presente
!ls -la /content/templates/
```

## 🛠️ Comandos para configurar no Colab

```python
# Instalar dependências
!pip install -r /content/requirements.txt

# Configurar ambiente para Android
!apt update
!apt install -y openjdk-17-jdk

# Instalar buildozer
!pip install buildozer

# Navegar para o diretório do projeto
%cd /content

# Inicializar buildozer (se necessário)
!buildozer init

# Compilar APK
!buildozer android debug
```

## 📋 Lista de Verificação

- [ ] Pasta `MyDrive/apps/nfc-writer-pro2/` criada
- [ ] Todos os arquivos `.py` foram enviados
- [ ] `buildozer.spec` foi enviado
- [ ] `requirements.txt` foi enviado
- [ ] Pasta `templates/` criada com `AndroidManifest.tmpl.xml`
- [ ] Pasta `.github/workflows/` criada com `build-apk.yml`
- [ ] Arquivos README enviados
- [ ] Dockerfile enviado

## 🎯 Resultado Final

Após seguir estes passos, você terá:
- ✅ Projeto organizado no Google Drive
- ✅ Fácil acesso via Google Colab
- ✅ Estrutura compatível com buildozer
- ✅ Backup seguro na nuvem

## 💡 Dicas Importantes

1. **Nomes dos arquivos**: Mantenha os nomes exatos dos arquivos
2. **Estrutura de pastas**: Respeite a hierarquia das pastas
3. **Arquivos ocultos**: A pasta `.github` pode não aparecer em alguns visualizadores
4. **Backup**: Sempre mantenha um backup local dos arquivos

---

**✨ Pronto! Agora você pode usar o comando no Colab:**
```python
!cp -r /content/drive/MyDrive/apps/nfc-writer-pro2/* /content/
```
