import json
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# 1. Carregar e formatar os dados do JSON
def carregar_json_para_docs(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    documentos = []
    for item in dados:
        texto = f"""
Projeto: {item.get("Projeto")}
Sprint: {item.get("Sprint_ID")}
User Story: {item.get("Descritivo_da_US")}
Módulo: {item.get("Modulo")}
Operação: {item.get("Operacao")}
Tarefa: {item.get("Tarefa_mapeada") or item.get("Tarefa_original")}
Camada: {item.get("Camada")}
Linguagem: {item.get("Linguagem")}
Framework: {item.get("Framework")}
Requisito Não Funcional: {item.get("NFR_Tipo")} - {item.get("NFR_Atributo")}
Detalhes NFR: {item.get("NFR_Sentença")}
        """
        documentos.append(Document(page_content=texto.strip()))
    return documentos

# 2. Carregar documentos
docs = carregar_json_para_docs("dados.json")

# 3. Dividir documentos em pedaços menores
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 4. Criar embeddings com modelo leve do HuggingFace
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 5. Criar banco vetorial (em memória)
db = Chroma.from_documents(chunks, embeddings)

# 6. Carregar modelo local via Ollama
llm = Ollama(model="deepseek-r1:14b")

# 7. Criar pipeline RAG
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    chain_type="stuff",
    return_source_documents=True
)

# 8. Exemplo de consulta
consulta = "Liste os NFQ"
resposta = qa(consulta)

# 9. Exibir resposta
print("\n📌 Pergunta:", consulta)
print("\n🧠 Resposta:")
print(resposta["result"])

# 10. (Opcional) Exibir fontes dos documentos usados
print("\n📚 Fontes:")
for doc in resposta["source_documents"]:
    print("-", doc.page_content[:200], "...\n")