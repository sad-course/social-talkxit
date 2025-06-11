from datetime import datetime

def current_time():
    """Retorna o horário atual com fuso horário UTC."""
    return datetime.utcnow()