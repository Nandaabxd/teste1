# � NFC Writer PRO v2.0

Um aplicativo profissional completo para **leitura e escrita** de tags NFC com interface moderna e funcionalidades avançadas.

## 🔍 **Funcionalidades Principais**

### **✅ Leitura de Tags NFC**
- 📖 Decodificação automática de múltiplos tipos NDEF
- 🔍 Suporte a texto, URLs, Wi-Fi, e-mail, telefone, vCard
- 📊 Histórico completo de leituras com timestamp
- 🎯 Interface intuitiva e moderna

### **✅ Escrita de Tags NFC** 
- ✍️ **10 tipos de formulários dinâmicos**:
  - 📝 Texto Simples
  - 🌐 URL/Link  
  - 📶 Rede Wi-Fi (configuração automática)
  - 📧 E-mail (pré-preenchido)
  - 📞 Telefone (discagem direta)
  - 💬 SMS (mensagem pré-escrita)
  - 👤 Contato vCard (cartão de visita)
  - 📍 Localização GPS (Google Maps)
  - 📅 Evento Calendário (iCal)
  - 📱 Aplicativo (abertura automática)

### **✅ Interface Profissional**
- 🎨 Design moderno com ícones intuitivos
- ✅ Validação automática de dados em tempo real
- 👁️ Preview completo antes de escrever
- 📚 Sistema de perfis personalizados
- 🔧 Automação avançada com histórico

### 🔧 **Configurabilidade**
- Cores e temas customizáveis
- Configurações de histórico
- Opções de debug e export
- Textos localizáveis (PT/EN)

## 📋 Arquivos do Projeto

### 🔧 **Código Principal**
- `main.py` - App principal com interface moderna
- `config.py` - Configurações centralizadas
- `utils.py` - Utilitários e helpers
- `buildozer.spec` - Configuração de build Android

### 📚 **Documentação**
- `README.md` - Este arquivo
- `MELHORIAS_V2.md` - Detalhes das melhorias
- `GUIA_RAPIDO.md` - Guia de compilação rápida
- `COMO_COMPILAR_APK.md` - Tutorial detalhado

### 🚀 **Scripts de Build**
- `build_docker.bat` - Build com Docker (Windows)
- `setup_wsl.ps1` - Configuração WSL (Windows)
- `Dockerfile` - Container para compilação

## 🛠️ Requisitos para Build

### **Ambiente Recomendado:**
1. **Python 3.9+** (compatibilidade otimizada)
2. **Java Development Kit (JDK) 17+**
3. **Android SDK 30** e **Android NDK 25b**
4. **Buildozer 1.5.0+**
5. **4GB+ RAM** e **10GB+ espaço livre**

### **Dependências Python:**
```txt
kivy==2.1.0
pyjnius==1.4.2
buildozer>=1.5.0
cython>=0.29.0
```

## Como Compilar

### Windows:
```bash
# Execute o script de build
./build_apk.bat
```

### Linux/Mac:
```bash
# Torne o script executável
chmod +x build_apk.sh

# Execute o script
./build_apk.sh
```

### Manualmente:
```bash
# Instale as dependências
pip install -r requirements.txt

# Inicialize o buildozer
buildozer init

# Compile o APK
buildozer android debug
```

## Estrutura do Projeto

```
teste1/
├── main.py                    # Código principal do aplicativo
├── buildozer.spec            # Configuração do Buildozer
├── requirements.txt          # Dependências Python
├── build_apk.bat            # Script de build para Windows
├── build_apk.sh             # Script de build para Linux/Mac
├── templates/
│   └── AndroidManifest.tmpl.xml  # Template do manifesto Android
└── README.md                # Este arquivo
```

## Permissões Android

O aplicativo solicita as seguintes permissões:
- `android.permission.NFC` - Para acessar o hardware NFC
- `android.permission.INTERNET` - Para processamento de URIs
- `android.permission.WAKE_LOCK` - Para manter o dispositivo ativo durante a leitura

## Uso

1. Instale o APK no seu dispositivo Android
2. Abra o aplicativo
3. Aproxime uma tag NFC do dispositivo
4. O conteúdo será exibido na tela

## Observações

- O dispositivo deve ter suporte a NFC
- O NFC deve estar habilitado nas configurações do dispositivo
- Este é um exemplo conceitual que demonstra a integração Python-Android
- Para produção, considere adicionar tratamento de erros mais robusto

## Troubleshooting

### Erro: "NFC not available"
- Verifique se o dispositivo tem hardware NFC
- Certifique-se de que o NFC está habilitado

### Erro durante o build
- Verifique se o Java SDK está instalado
- Certifique-se de que as variáveis de ambiente estão configuradas
- Consulte a documentação do Buildozer para requisitos específicos

## Licença

Este projeto é apenas para fins educacionais e demonstrativos.
