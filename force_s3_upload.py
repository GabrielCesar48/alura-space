"""
    Script para forçar o upload de arquivos estáticos para o S3
"""
import os
import django
import boto3
import glob
from pathlib import Path

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.conf import settings

def upload_directory_to_s3(local_directory, s3_prefix='static'):
    """
        Faz upload de todos os arquivos em um diretório para o S3
    """
    # Inicializar cliente S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    
    # Raiz do projeto
    base_dir = settings.BASE_DIR
    
    # Diretório completo para upload
    full_dir = os.path.join(base_dir, local_directory)
    
    print(f"Fazendo upload de {full_dir} para s3://{settings.AWS_STORAGE_BUCKET_NAME}/{s3_prefix}/")
    
    # Encontrar todos os arquivos no diretório e subdiretórios
    for filepath in glob.glob(f"{full_dir}/**/*.*", recursive=True):
        # Caminho relativo para o S3
        relative_path = os.path.relpath(filepath, full_dir)
        s3_path = f"{s3_prefix}/{relative_path.replace(os.sep, '/')}"
        
        print(f"Enviando {filepath} para {s3_path}")
        
        # Fazer upload do arquivo
        try:
            s3.upload_file(filepath, settings.AWS_STORAGE_BUCKET_NAME, s3_path)
            print(f"Arquivo enviado com sucesso: {s3_path}")
        except Exception as e:
            print(f"Erro ao enviar {filepath}: {e}")

if __name__ == "__main__":
    if not settings.USE_S3:
        print("S3 não está configurado. Defina USE_S3=True em seu arquivo .env")
        exit(1)
        
    # Upload dos diretórios de arquivos estáticos
    upload_directory_to_s3('setup/static', 'static')
    upload_directory_to_s3('static', 'static')
    
    print("Upload concluído!")