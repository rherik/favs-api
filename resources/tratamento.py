import os
import boto3
import uuid
from dotenv import load_dotenv

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'heic']
# Variáveis boto3
load_dotenv()
s3 = boto3.client("s3", 
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                aws_secret_access_key=os.getenv('AWS_ACCESS_KEY_SECRET'))
bucket_name = os.getenv('BUCKET_NAME')
regiao = "sa-east-1"

def allowed_files(filename):
    extensao_arq = filename.rsplit('.')[-1].lower()
    if extensao_arq in ALLOWED_EXTENSIONS:
        return True
    else:
        return False
    
def retorna_arquivo(arq):
    if allowed_files(arq):
        # Definição do arquivo
        new_filename = uuid.uuid4().hex + '.' + arq.rsplit('.', 1)[1].lower()
        # Armazena a imagem no bucket aws
        # Implementar read object antes do upload
        with open('rb', arq):
            s3.upload_fileobj(arq, bucket_name, new_filename)
        # Fim do tratamento da imagem
        url_img = f"https://{bucket_name}.s3.{regiao}.amazonaws.com/{arq}"
        print(f'Seu arquivo {url_img} passou pela função retorna_arquivo do backend.')
        return url_img
    else:
        return {'message': 'File extention not permited.'}