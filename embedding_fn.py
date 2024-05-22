from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings


def embedding_fn():
    # pip3 install boto3
    # pydantic.v1.error_wrappers.ValidationError: 1 validation error for BedrockEmbeddings
    # Could not load credentials to authenticate with AWS client.
    # Please check that credentials in the specified profile name are valid.
    # Bedrock error: The config profile (default) could not be found (type=value_error)

    # embeddings = BedrockEmbeddings(
    #     credentials_profile_name="default", region_name="us-east-1"
    # )

    # ValueError: Error raised by inference API HTTP code: 404,
    # {"error":"model 'nomic-embed-text' not found, try pulling it first"}

    # run on terminal, ollama pull llama2 or ollama pull mistral - after success ask a query
    # then, ollama serve {to serve the model as REST API, runs ollama server on localhost:11434}
    #running serve again shows, Error: listen tcp 127.0.0.1:11434: bind: address already in use
    #use netstat cmd onterminal 

    #ValueError: Error raised by inference API HTTP code: 404, {"error":"model 'nomic-embed-text' not found, 
    # try pulling it first"}
    # ollama pull nomic-embed-text {its 274 MB}

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
