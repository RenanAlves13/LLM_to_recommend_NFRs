import openai

client = openai.OpenAI(api_key="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")

file = client.files.create(
    file=open("fine_tuning_data.jsonl", "rb"),
    purpose="fine-tune"
)

print("Arquivo enviado com sucesso:", file.id)

job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"
)

print("Fine-tuning iniciado com sucesso! ID do job:", job.id)

