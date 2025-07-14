FROM ubuntu:20.04

# Evitar interações durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    git \
    openjdk-8-jdk \
    unzip \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Configurar Java
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# Instalar Buildozer
RUN pip3 install buildozer

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto
COPY . .

# Comando para compilar o APK
CMD ["buildozer", "android", "debug"]
