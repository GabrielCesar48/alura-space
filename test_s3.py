import os
import boto3
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

print(f"USE_S3: {getattr(settings, 'USE_S3', False)}")

if hasattr(settings, 'AWS_ACCESS_KEY_ID'):
    try:
        session = boto3.Session(
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        s3 = session.resource('s3')
        bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
        
        print(f"Conectado ao bucket: {settings.AWS_STORAGE_BUCKET_NAME}")
        
        # Tenta fazer upload de um arquivo de teste
        with open('test_file.txt', 'w') as f:
            f.write('Teste de upload para S3')
        
        bucket.upload_file('test_file.txt', 'test_file.txt')
        print("Arquivo de teste enviado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao conectar ao S3: {e}")
else:
    print("Configurações AWS não encontradas!")