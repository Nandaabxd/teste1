"""
🔧 Configurações do NFC Reader App
==================================

Arquivo de configuração para personalizar o comportamento do aplicativo.
"""

# Configurações da interface
UI_CONFIG = {
    'primary_color': (0.2, 0.6, 1, 1),      # Azul principal
    'success_color': (0.2, 0.8, 0.2, 1),    # Verde sucesso
    'warning_color': (0.9, 0.7, 0.2, 1),    # Amarelo aviso
    'error_color': (0.9, 0.3, 0.3, 1),      # Vermelho erro
    'info_color': (0.5, 0.5, 0.9, 1),       # Azul info
    'background_color': (0.95, 0.95, 0.97, 1),  # Fundo claro
    'font_size_title': '24sp',
    'font_size_normal': '16sp',
    'font_size_small': '14sp',
    'animation_duration': 0.3,
}

# Configurações do histórico
HISTORY_CONFIG = {
    'max_entries': 50,                        # Máximo de entradas no histórico
    'auto_save': True,                        # Salvar automaticamente
    'save_file': 'nfc_history.json',          # Arquivo de histórico
    'show_raw_data': False,                   # Mostrar dados brutos por padrão
}

# Configurações de logging
LOGGING_CONFIG = {
    'level': 'INFO',                          # DEBUG, INFO, WARNING, ERROR
    'log_to_file': True,                      # Salvar logs em arquivo
    'log_file': 'nfc_reader.log',             # Nome do arquivo de log
    'max_log_size': 1024 * 1024,             # 1MB máximo
    'backup_count': 3,                        # Manter 3 backups
}

# Configurações NFC
NFC_CONFIG = {
    'timeout_seconds': 5,                     # Timeout para leitura
    'retry_attempts': 3,                      # Tentativas de releitura
    'auto_decode': True,                      # Decodificar automaticamente
    'supported_types': [                      # Tipos NDEF suportados
        'RTD_TEXT',
        'RTD_URI', 
        'RTD_SMART_POSTER',
        'MIME_MEDIA',
        'EXTERNAL_TYPE'
    ],
}

# Configurações de debug/desenvolvimento
DEBUG_CONFIG = {
    'enable_test_mode': True,                 # Habilitar modo de teste
    'simulate_nfc': False,                    # Simular NFC no desktop
    'verbose_logging': False,                 # Logs verbosos
    'show_raw_bytes': True,                   # Mostrar bytes brutos
    'performance_monitoring': False,          # Monitorar performance
}

# Configurações de notificações
NOTIFICATION_CONFIG = {
    'enable_sounds': True,                    # Sons de notificação
    'enable_vibration': True,                 # Vibração no Android
    'success_sound': 'success.wav',           # Som de sucesso
    'error_sound': 'error.wav',               # Som de erro
    'vibration_duration': 200,                # Duração da vibração (ms)
}

# Configurações de exportação
EXPORT_CONFIG = {
    'formats': ['JSON', 'CSV', 'TXT'],        # Formatos de exportação
    'include_timestamp': True,                # Incluir timestamp
    'include_raw_data': False,                # Incluir dados brutos
    'date_format': '%d/%m/%Y %H:%M:%S',       # Formato de data
}

# Textos da interface (internacionalização básica)
UI_TEXTS = {
    'pt_br': {
        'app_title': '🔍 NFC Reader',
        'waiting_tag': '👋 Aproxime uma tag NFC para começar...',
        'nfc_not_available': '❌ NFC não disponível',
        'reading_tag': '🔍 Lendo tag NFC...',
        'read_success': '✅ Tag lida com sucesso!',
        'read_error': '❌ Erro ao ler tag',
        'history_empty': '📋 Histórico vazio',
        'history_cleared': '🗑️ Histórico limpo',
        'test_mode': '🧪 Modo de teste ativo',
    },
    'en': {
        'app_title': '🔍 NFC Reader', 
        'waiting_tag': '👋 Bring an NFC tag closer to start...',
        'nfc_not_available': '❌ NFC not available',
        'reading_tag': '🔍 Reading NFC tag...',
        'read_success': '✅ Tag read successfully!',
        'read_error': '❌ Error reading tag',
        'history_empty': '📋 Empty history',
        'history_cleared': '🗑️ History cleared',
        'test_mode': '🧪 Test mode active',
    }
}

# Configuração ativa (pode ser alterada em runtime)
ACTIVE_LANGUAGE = 'pt_br'

def get_text(key):
    """Obtém texto localizado"""
    return UI_TEXTS.get(ACTIVE_LANGUAGE, {}).get(key, key)

def get_config(section):
    """Obtém configuração de uma seção específica"""
    configs = {
        'ui': UI_CONFIG,
        'history': HISTORY_CONFIG,
        'logging': LOGGING_CONFIG,
        'nfc': NFC_CONFIG,
        'debug': DEBUG_CONFIG,
        'notification': NOTIFICATION_CONFIG,
        'export': EXPORT_CONFIG,
    }
    return configs.get(section, {})
