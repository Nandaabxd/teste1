"""
🛠️ Utilitários do NFC Reader App
=================================

Funções auxiliares e utilitários para o aplicativo NFC Reader.
"""

import json
import os
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional


class FileManager:
    """Gerenciador de arquivos para o app"""
    
    @staticmethod
    def ensure_app_directory():
        """Garante que o diretório do app existe"""
        app_dir = os.path.join(os.path.expanduser('~'), '.nfc_reader')
        if not os.path.exists(app_dir):
            os.makedirs(app_dir)
        return app_dir
    
    @staticmethod
    def save_json(data: Dict, filename: str) -> bool:
        """Salva dados em formato JSON"""
        try:
            app_dir = FileManager.ensure_app_directory()
            filepath = os.path.join(app_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            logging.error(f"Erro ao salvar {filename}: {e}")
            return False
    
    @staticmethod
    def load_json(filename: str) -> Optional[Dict]:
        """Carrega dados de arquivo JSON"""
        try:
            app_dir = FileManager.ensure_app_directory()
            filepath = os.path.join(app_dir, filename)
            
            if not os.path.exists(filepath):
                return None
            
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        except Exception as e:
            logging.error(f"Erro ao carregar {filename}: {e}")
            return None
    
    @staticmethod
    def export_history_csv(history: List[Dict], filename: str) -> bool:
        """Exporta histórico para CSV"""
        try:
            app_dir = FileManager.ensure_app_directory()
            filepath = os.path.join(app_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                # Cabeçalho
                f.write("Timestamp,Tipo,Conteudo,Dados_Brutos\n")
                
                # Dados
                for entry in history:
                    timestamp = entry.get('timestamp', '')
                    entry_type = entry.get('type', '')
                    content = entry.get('content', '').replace('"', '""')  # Escape aspas
                    raw_data = entry.get('raw_data', '')
                    
                    f.write(f'"{timestamp}","{entry_type}","{content}","{raw_data}"\n')
            
            return True
        except Exception as e:
            logging.error(f"Erro ao exportar CSV: {e}")
            return False


class DataValidator:
    """Validador de dados NFC"""
    
    @staticmethod
    def is_valid_text_encoding(payload: bytes) -> bool:
        """Verifica se o payload tem encoding válido"""
        try:
            if len(payload) < 2:
                return False
            
            # Primeiro byte contém informações de encoding
            encoding_byte = payload[0]
            lang_length = encoding_byte & 0x3F
            
            if lang_length >= len(payload):
                return False
            
            # Tenta decodificar
            encoding = 'utf-8' if (encoding_byte & 0x80) == 0 else 'utf-16'
            text_start = 1 + lang_length
            payload[text_start:].decode(encoding)
            
            return True
        except:
            return False
    
    @staticmethod
    def is_valid_uri(uri_string: str) -> bool:
        """Verifica se é uma URI válida"""
        try:
            valid_schemes = ['http', 'https', 'ftp', 'mailto', 'tel', 'sms']
            return any(uri_string.lower().startswith(scheme) for scheme in valid_schemes)
        except:
            return False
    
    @staticmethod
    def sanitize_content(content: str, max_length: int = 1000) -> str:
        """Sanitiza conteúdo para exibição segura"""
        if not isinstance(content, str):
            content = str(content)
        
        # Remove caracteres de controle
        sanitized = ''.join(char for char in content if ord(char) >= 32 or char in '\n\t')
        
        # Limita tamanho
        if len(sanitized) > max_length:
            sanitized = sanitized[:max_length] + '...'
        
        return sanitized


class HexFormatter:
    """Formatador de dados hexadecimais"""
    
    @staticmethod
    def format_hex(data: bytes, group_size: int = 2, groups_per_line: int = 8) -> str:
        """Formata bytes em hexadecimal legível"""
        if not data:
            return ""
        
        hex_string = data.hex().upper()
        
        # Agrupa em pares
        groups = [hex_string[i:i+group_size*2] for i in range(0, len(hex_string), group_size*2)]
        
        # Organiza em linhas
        lines = []
        for i in range(0, len(groups), groups_per_line):
            line_groups = groups[i:i+groups_per_line]
            lines.append(' '.join(line_groups))
        
        return '\n'.join(lines)
    
    @staticmethod
    def hex_to_ascii(data: bytes) -> str:
        """Converte hex para ASCII legível"""
        try:
            ascii_chars = []
            for byte in data:
                if 32 <= byte <= 126:  # Caracteres imprimíveis
                    ascii_chars.append(chr(byte))
                else:
                    ascii_chars.append('.')
            return ''.join(ascii_chars)
        except:
            return ""


class PerformanceMonitor:
    """Monitor de performance"""
    
    def __init__(self):
        self.start_times = {}
        self.metrics = {}
    
    def start_timer(self, operation: str):
        """Inicia timer para uma operação"""
        self.start_times[operation] = datetime.now()
    
    def end_timer(self, operation: str):
        """Finaliza timer e registra métrica"""
        if operation in self.start_times:
            duration = (datetime.now() - self.start_times[operation]).total_seconds()
            
            if operation not in self.metrics:
                self.metrics[operation] = []
            
            self.metrics[operation].append(duration)
            del self.start_times[operation]
            
            return duration
        return None
    
    def get_average_time(self, operation: str) -> Optional[float]:
        """Obtém tempo médio de uma operação"""
        if operation in self.metrics and self.metrics[operation]:
            return sum(self.metrics[operation]) / len(self.metrics[operation])
        return None
    
    def get_stats(self) -> Dict[str, Dict[str, float]]:
        """Obtém estatísticas completas"""
        stats = {}
        for operation, times in self.metrics.items():
            if times:
                stats[operation] = {
                    'count': len(times),
                    'average': sum(times) / len(times),
                    'min': min(times),
                    'max': max(times),
                    'total': sum(times)
                }
        return stats


class ByteAnalyzer:
    """Analisador de dados em bytes"""
    
    @staticmethod
    def analyze_payload(payload: bytes) -> Dict[str, Any]:
        """Analisa payload e retorna informações detalhadas"""
        analysis = {
            'size': len(payload),
            'is_text': False,
            'is_binary': False,
            'has_nulls': False,
            'printable_ratio': 0.0,
            'entropy': 0.0,
            'patterns': []
        }
        
        if not payload:
            return analysis
        
        # Análise de caracteres
        printable_count = 0
        null_count = 0
        
        for byte in payload:
            if 32 <= byte <= 126:  # ASCII imprimível
                printable_count += 1
            elif byte == 0:
                null_count += 1
        
        analysis['printable_ratio'] = printable_count / len(payload)
        analysis['has_nulls'] = null_count > 0
        analysis['is_text'] = analysis['printable_ratio'] > 0.7
        analysis['is_binary'] = analysis['printable_ratio'] < 0.3
        
        # Análise de entropia (simplicado)
        byte_counts = {}
        for byte in payload:
            byte_counts[byte] = byte_counts.get(byte, 0) + 1
        
        entropy = 0
        for count in byte_counts.values():
            probability = count / len(payload)
            if probability > 0:
                entropy -= probability * (probability.bit_length() - 1)
        
        analysis['entropy'] = entropy
        
        # Padrões comuns
        if payload.startswith(b'http'):
            analysis['patterns'].append('HTTP_URL')
        if payload.startswith(b'ftp'):
            analysis['patterns'].append('FTP_URL')
        if b'@' in payload and b'.' in payload:
            analysis['patterns'].append('POSSIBLE_EMAIL')
        if payload.startswith(b'{') and payload.endswith(b'}'):
            analysis['patterns'].append('POSSIBLE_JSON')
        if payload.startswith(b'<') and payload.endswith(b'>'):
            analysis['patterns'].append('POSSIBLE_XML')
        
        return analysis


class SecurityHelper:
    """Auxiliar de segurança"""
    
    @staticmethod
    def is_safe_url(url: str) -> bool:
        """Verifica se URL é segura"""
        try:
            dangerous_patterns = [
                'javascript:', 'data:', 'vbscript:', 'file:',
                '<script', '</script>', 'onload=', 'onerror='
            ]
            
            url_lower = url.lower()
            return not any(pattern in url_lower for pattern in dangerous_patterns)
        except:
            return False
    
    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """Sanitiza nome de arquivo"""
        # Remove caracteres perigosos
        dangerous_chars = '<>:"/\\|?*'
        for char in dangerous_chars:
            filename = filename.replace(char, '_')
        
        # Limita tamanho
        if len(filename) > 100:
            filename = filename[:100]
        
        return filename


# Instâncias globais para uso em toda a aplicação
file_manager = FileManager()
data_validator = DataValidator()
hex_formatter = HexFormatter()
performance_monitor = PerformanceMonitor()
byte_analyzer = ByteAnalyzer()
security_helper = SecurityHelper()
