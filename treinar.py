from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key)

path_data = os.path.join("Data")

file = client.files.create(
    file=open(f"{path_data}\\fine_tuning_data.jsonl", "rb"),
    purpose="fine-tune"
)

print("Arquivo enviado com sucesso:", file.id)

job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"
)

print("Fine-tuning iniciado com sucesso! ID do job:", job.id)

