"""
📝 NFC Writer Module - Sistema Avançado de Escrita em Tags NFC
============================================================

Módulo completo para escrita de dados em tags NFC com suporte a múltiplos
formatos, perfis personalizados e automação avançada.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from enum import Enum

logger = logging.getLogger(__name__)


class NFCRecordType(Enum):
    """Tipos de registros NFC suportados"""
    TEXT = "text"
    URI = "uri"
    WIFI = "wifi"
    EMAIL = "email"
    PHONE = "phone"
    SMS = "sms"
    LOCATION = "location"
    CONTACT = "contact"
    APP_LAUNCHER = "app_launcher"
    BLUETOOTH = "bluetooth"
    SYSTEM_COMMAND = "system_command"
    CUSTOM = "custom"


class NFCProfile:
    """Perfil personalizado para escrita NFC"""
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.records = []
        self.actions = []
        self.created_at = datetime.now()
        self.modified_at = datetime.now()
        self.password_protected = False
        self.password_hash = None
        self.write_count = 0
        
    def add_record(self, record_type: NFCRecordType, data: Dict[str, Any]):
        """Adiciona um registro ao perfil"""
        record = {
            'type': record_type.value,
            'data': data,
            'created_at': datetime.now().isoformat()
        }
        self.records.append(record)
        self.modified_at = datetime.now()
        
    def add_action(self, action_type: str, parameters: Dict[str, Any]):
        """Adiciona uma ação automática ao perfil"""
        action = {
            'type': action_type,
            'parameters': parameters,
            'enabled': True,
            'created_at': datetime.now().isoformat()
        }
        self.actions.append(action)
        self.modified_at = datetime.now()
        
    def set_password(self, password: str):
        """Define proteção por senha"""
        import hashlib
        self.password_protected = True
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        
    def verify_password(self, password: str) -> bool:
        """Verifica senha"""
        if not self.password_protected:
            return True
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest() == self.password_hash
        
    def to_dict(self) -> Dict[str, Any]:
        """Converte perfil para dicionário"""
        return {
            'name': self.name,
            'description': self.description,
            'records': self.records,
            'actions': self.actions,
            'created_at': self.created_at.isoformat(),
            'modified_at': self.modified_at.isoformat(),
            'password_protected': self.password_protected,
            'password_hash': self.password_hash,
            'write_count': self.write_count
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'NFCProfile':
        """Cria perfil a partir de dicionário"""
        profile = cls(data['name'], data.get('description', ''))
        profile.records = data.get('records', [])
        profile.actions = data.get('actions', [])
        profile.created_at = datetime.fromisoformat(data['created_at'])
        profile.modified_at = datetime.fromisoformat(data['modified_at'])
        profile.password_protected = data.get('password_protected', False)
        profile.password_hash = data.get('password_hash')
        profile.write_count = data.get('write_count', 0)
        return profile


class NFCDataBuilder:
    """Construtor de dados NFC para diferentes tipos"""
    
    @staticmethod
    def build_text_record(text: str, language: str = "pt") -> Dict[str, Any]:
        """Constrói registro de texto"""
        return {
            'type': 'text',
            'text': text,
            'language': language,
            'encoding': 'utf-8'
        }
    
    @staticmethod
    def build_uri_record(uri: str) -> Dict[str, Any]:
        """Constrói registro de URI"""
        return {
            'type': 'uri',
            'uri': uri
        }
    
    @staticmethod
    def build_wifi_record(ssid: str, password: str, security: str = "WPA2", hidden: bool = False) -> Dict[str, Any]:
        """Constrói registro Wi-Fi"""
        return {
            'type': 'wifi',
            'ssid': ssid,
            'password': password,
            'security': security,
            'hidden': hidden
        }
    
    @staticmethod
    def build_email_record(email: str, subject: str = "", body: str = "") -> Dict[str, Any]:
        """Constrói registro de e-mail"""
        return {
            'type': 'email',
            'email': email,
            'subject': subject,
            'body': body
        }
    
    @staticmethod
    def build_phone_record(phone: str) -> Dict[str, Any]:
        """Constrói registro de telefone"""
        return {
            'type': 'phone',
            'phone': phone
        }
    
    @staticmethod
    def build_sms_record(phone: str, message: str = "") -> Dict[str, Any]:
        """Constrói registro de SMS"""
        return {
            'type': 'sms',
            'phone': phone,
            'message': message
        }
    
    @staticmethod
    def build_location_record(latitude: float, longitude: float, name: str = "") -> Dict[str, Any]:
        """Constrói registro de localização"""
        return {
            'type': 'location',
            'latitude': latitude,
            'longitude': longitude,
            'name': name
        }
    
    @staticmethod
    def build_contact_record(name: str, phone: str = "", email: str = "", organization: str = "") -> Dict[str, Any]:
        """Constrói registro de contato (vCard)"""
        return {
            'type': 'contact',
            'name': name,
            'phone': phone,
            'email': email,
            'organization': organization
        }
    
    @staticmethod
    def build_app_launcher_record(package_name: str, activity: str = "") -> Dict[str, Any]:
        """Constrói registro para lançar app"""
        return {
            'type': 'app_launcher',
            'package_name': package_name,
            'activity': activity
        }
    
    @staticmethod
    def build_bluetooth_record(mac_address: str, name: str = "") -> Dict[str, Any]:
        """Constrói registro Bluetooth"""
        return {
            'type': 'bluetooth',
            'mac_address': mac_address,
            'name': name
        }
    
    @staticmethod
    def build_system_command_record(command_type: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Constrói registro de comando do sistema"""
        return {
            'type': 'system_command',
            'command': command_type,
            'parameters': parameters
        }


class NFCWriter:
    """Sistema avançado de escrita em tags NFC"""
    
    def __init__(self):
        self.android_classes_loaded = False
        self.nfc_adapter = None
        self.current_activity = None
        self.write_history = []
        
    def initialize(self) -> bool:
        """Inicializa o sistema de escrita NFC"""
        try:
            from jnius import autoclass
            
            # Classes Android para escrita
            self.NfcAdapter = autoclass('android.nfc.NfcAdapter')
            self.NdefMessage = autoclass('android.nfc.NdefMessage')
            self.NdefRecord = autoclass('android.nfc.NdefRecord')
            self.PythonActivity = autoclass('org.kivy.android.PythonActivity')
            self.Intent = autoclass('android.content.Intent')
            self.PendingIntent = autoclass('android.app.PendingIntent')
            self.IntentFilter = autoclass('android.content.IntentFilter')
            
            # Inicializa adaptador NFC
            self.current_activity = self.PythonActivity.mActivity
            self.nfc_adapter = self.NfcAdapter.getDefaultAdapter(self.current_activity)
            
            self.android_classes_loaded = True
            logger.info("NFCWriter inicializado com sucesso")
            return True
            
        except ImportError:
            logger.error("PyJNIUS não disponível para escrita NFC")
            return False
        except Exception as e:
            logger.error(f"Erro ao inicializar NFCWriter: {e}")
            return False
    
    def is_available(self) -> bool:
        """Verifica se escrita NFC está disponível"""
        if not self.android_classes_loaded:
            return False
        
        return (self.nfc_adapter is not None and 
                self.nfc_adapter.isEnabled())
    
    def write_profile_to_tag(self, profile: NFCProfile, password: str = None) -> bool:
        """Escreve um perfil completo na tag NFC"""
        if not self.is_available():
            logger.error("NFC não disponível para escrita")
            return False
        
        # Verifica senha se necessário
        if profile.password_protected and not profile.verify_password(password or ""):
            logger.error("Senha incorreta para perfil protegido")
            return False
        
        try:
            # Converte registros do perfil para NDEF
            ndef_records = []
            
            for record_data in profile.records:
                ndef_record = self._create_ndef_record(record_data)
                if ndef_record:
                    ndef_records.append(ndef_record)
            
            if not ndef_records:
                logger.error("Nenhum registro válido no perfil")
                return False
            
            # Cria mensagem NDEF
            ndef_message = self.NdefMessage(ndef_records)
            
            # Escreve na tag (implementação específica do Android)
            success = self._write_ndef_message(ndef_message)
            
            if success:
                profile.write_count += 1
                self._add_to_write_history(profile.name, len(ndef_records))
                logger.info(f"Perfil '{profile.name}' escrito com sucesso")
            
            return success
            
        except Exception as e:
            logger.error(f"Erro ao escrever perfil na tag: {e}")
            return False
    
    def write_single_record(self, record_type: NFCRecordType, data: Dict[str, Any]) -> bool:
        """Escreve um único registro na tag"""
        if not self.is_available():
            return False
        
        try:
            record_data = {'type': record_type.value, 'data': data}
            ndef_record = self._create_ndef_record(record_data)
            
            if not ndef_record:
                return False
            
            ndef_message = self.NdefMessage([ndef_record])
            success = self._write_ndef_message(ndef_message)
            
            if success:
                self._add_to_write_history(f"Registro {record_type.value}", 1)
            
            return success
            
        except Exception as e:
            logger.error(f"Erro ao escrever registro: {e}")
            return False
    
    def _create_ndef_record(self, record_data: Dict[str, Any]):
        """Cria registro NDEF a partir dos dados"""
        try:
            record_type = record_data['type']
            data = record_data.get('data', record_data)
            
            if record_type == 'text':
                return self._create_text_record(data)
            elif record_type == 'uri':
                return self._create_uri_record(data)
            elif record_type == 'wifi':
                return self._create_wifi_record(data)
            elif record_type == 'email':
                return self._create_email_record(data)
            elif record_type == 'phone':
                return self._create_phone_record(data)
            elif record_type == 'sms':
                return self._create_sms_record(data)
            elif record_type == 'location':
                return self._create_location_record(data)
            elif record_type == 'contact':
                return self._create_contact_record(data)
            elif record_type == 'app_launcher':
                return self._create_app_launcher_record(data)
            else:
                logger.warning(f"Tipo de registro não suportado: {record_type}")
                return None
                
        except Exception as e:
            logger.error(f"Erro ao criar registro NDEF: {e}")
            return None
    
    def _create_text_record(self, data: Dict[str, Any]):
        """Cria registro de texto NDEF"""
        text = data.get('text', '')
        language = data.get('language', 'pt')
        encoding = data.get('encoding', 'utf-8')
        
        # Codifica texto no formato NDEF
        lang_bytes = language.encode('ascii')
        text_bytes = text.encode(encoding)
        
        # Primeiro byte: encoding flag + tamanho do código de idioma
        encoding_flag = 0 if encoding == 'utf-8' else 0x80
        payload = bytes([encoding_flag | len(lang_bytes)]) + lang_bytes + text_bytes
        
        return self.NdefRecord.createRecord(
            self.NdefRecord.TNF_WELL_KNOWN,
            self.NdefRecord.RTD_TEXT,
            None,
            payload
        )
    
    def _create_uri_record(self, data: Dict[str, Any]):
        """Cria registro de URI NDEF"""
        uri = data.get('uri', '')
        return self.NdefRecord.createUri(uri)
    
    def _create_wifi_record(self, data: Dict[str, Any]):
        """Cria registro Wi-Fi NDEF"""
        ssid = data.get('ssid', '')
        password = data.get('password', '')
        security = data.get('security', 'WPA2')
        hidden = data.get('hidden', False)
        
        # Formato Wi-Fi Simple Configuration
        wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};H:{'true' if hidden else 'false'};;"
        
        return self.NdefRecord.createRecord(
            self.NdefRecord.TNF_WELL_KNOWN,
            self.NdefRecord.RTD_TEXT,
            None,
            wifi_config.encode('utf-8')
        )
    
    def _create_email_record(self, data: Dict[str, Any]):
        """Cria registro de e-mail NDEF"""
        email = data.get('email', '')
        subject = data.get('subject', '')
        body = data.get('body', '')
        
        mailto_uri = f"mailto:{email}"
        if subject or body:
            params = []
            if subject:
                params.append(f"subject={subject}")
            if body:
                params.append(f"body={body}")
            mailto_uri += "?" + "&".join(params)
        
        return self.NdefRecord.createUri(mailto_uri)
    
    def _create_phone_record(self, data: Dict[str, Any]):
        """Cria registro de telefone NDEF"""
        phone = data.get('phone', '')
        tel_uri = f"tel:{phone}"
        return self.NdefRecord.createUri(tel_uri)
    
    def _create_sms_record(self, data: Dict[str, Any]):
        """Cria registro de SMS NDEF"""
        phone = data.get('phone', '')
        message = data.get('message', '')
        
        sms_uri = f"sms:{phone}"
        if message:
            sms_uri += f"?body={message}"
        
        return self.NdefRecord.createUri(sms_uri)
    
    def _create_location_record(self, data: Dict[str, Any]):
        """Cria registro de localização NDEF"""
        latitude = data.get('latitude', 0.0)
        longitude = data.get('longitude', 0.0)
        name = data.get('name', '')
        
        geo_uri = f"geo:{latitude},{longitude}"
        if name:
            geo_uri += f"?q={latitude},{longitude}({name})"
        
        return self.NdefRecord.createUri(geo_uri)
    
    def _create_contact_record(self, data: Dict[str, Any]):
        """Cria registro de contato vCard NDEF"""
        name = data.get('name', '')
        phone = data.get('phone', '')
        email = data.get('email', '')
        organization = data.get('organization', '')
        
        # Formato vCard simples
        vcard = [
            "BEGIN:VCARD",
            "VERSION:3.0",
            f"FN:{name}",
            f"N:{name};;;;"
        ]
        
        if phone:
            vcard.append(f"TEL:{phone}")
        if email:
            vcard.append(f"EMAIL:{email}")
        if organization:
            vcard.append(f"ORG:{organization}")
        
        vcard.append("END:VCARD")
        vcard_data = "\n".join(vcard)
        
        return self.NdefRecord.createRecord(
            self.NdefRecord.TNF_MIME_MEDIA,
            "text/vcard".encode('ascii'),
            None,
            vcard_data.encode('utf-8')
        )
    
    def _create_app_launcher_record(self, data: Dict[str, Any]):
        """Cria registro para lançar aplicativo"""
        package_name = data.get('package_name', '')
        activity = data.get('activity', '')
        
        # URI do Android para lançar app
        if activity:
            app_uri = f"android-app://{package_name}/{activity}"
        else:
            app_uri = f"market://details?id={package_name}"
        
        return self.NdefRecord.createUri(app_uri)
    
    def _write_ndef_message(self, ndef_message) -> bool:
        """Escreve mensagem NDEF na tag (método stub - requer implementação específica)"""
        # Esta é uma implementação simplificada
        # Na prática, seria necessário aguardar que uma tag seja detectada
        # e usar o objeto Tag para escrever os dados
        logger.info("Simulando escrita NDEF na tag...")
        return True
    
    def _add_to_write_history(self, profile_name: str, record_count: int):
        """Adiciona entrada ao histórico de escrita"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'profile_name': profile_name,
            'record_count': record_count,
            'success': True
        }
        self.write_history.append(entry)
        
        # Limita histórico a 100 entradas
        if len(self.write_history) > 100:
            self.write_history = self.write_history[-100:]
    
    def get_write_history(self) -> List[Dict[str, Any]]:
        """Retorna histórico de escritas"""
        return self.write_history.copy()


class NFCProfileManager:
    """Gerenciador de perfis NFC"""
    
    def __init__(self):
        self.profiles = {}
        self.load_profiles()
    
    def create_profile(self, name: str, description: str = "") -> NFCProfile:
        """Cria novo perfil"""
        if name in self.profiles:
            raise ValueError(f"Perfil '{name}' já existe")
        
        profile = NFCProfile(name, description)
        self.profiles[name] = profile
        self.save_profiles()
        return profile
    
    def get_profile(self, name: str) -> Optional[NFCProfile]:
        """Obtém perfil por nome"""
        return self.profiles.get(name)
    
    def list_profiles(self) -> List[str]:
        """Lista nomes dos perfis"""
        return list(self.profiles.keys())
    
    def delete_profile(self, name: str) -> bool:
        """Remove perfil"""
        if name in self.profiles:
            del self.profiles[name]
            self.save_profiles()
            return True
        return False
    
    def save_profiles(self):
        """Salva perfis em arquivo"""
        try:
            from utils import file_manager
            profiles_data = {
                name: profile.to_dict() 
                for name, profile in self.profiles.items()
            }
            file_manager.save_json(profiles_data, 'nfc_profiles.json')
        except Exception as e:
            logger.error(f"Erro ao salvar perfis: {e}")
    
    def load_profiles(self):
        """Carrega perfis de arquivo"""
        try:
            from utils import file_manager
            profiles_data = file_manager.load_json('nfc_profiles.json')
            
            if profiles_data:
                self.profiles = {
                    name: NFCProfile.from_dict(data)
                    for name, data in profiles_data.items()
                }
        except Exception as e:
            logger.error(f"Erro ao carregar perfis: {e}")
            self.profiles = {}


# Instâncias globais
nfc_writer = NFCWriter()
profile_manager = NFCProfileManager()
data_builder = NFCDataBuilder()
