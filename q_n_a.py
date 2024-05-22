import argparse
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from embedding_fn import embedding_fn

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Given the following context:

{context}

---

Answer the question based on only the above context: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    # sample query = What are the names of the Lenders in the WILD OATS MARKETS credit agreement? Give the names only.
    # Mistral Response:  The text does not provide the names of the specific Lenders in the WILD OATS MARKETS credit agreement. 
    #  It only mentions that the Administrative Agent acts on behalf of the Lenders and that Participants, who are different from the Lenders, 
    #  have certain rights related to payments and setoffs.
    # Llama2 Response: Based on the context provided, the names of the Lenders in the WILD OATS MARKETS credit agreement are:
    #  1. Wells Fargo Bank, National Association
    #  2. U.S. Bank National Association
    # Expected Answer: Wells Fargo Bank, National Association AND U.S. Bank National Association AND Vectra Bank Colorado N.A. from SCHEDULE I

    # sample query = What are the names of the borrowers in the WILD OATS MARKETS credit agreement? Give the names only.
    # Mistral Response:  The name of the borrower in the WILD OATS MARKETS credit agreement is Wild Oats Markets, Inc.
    # Llama2 Response: * Wild Oats Markets, Inc.
    # Expected Answer: Wild Oats Markets, Inc.

    # sample query = From 'SCHEDULE I', List the names of the Lenders in the WILD OATS MARKETS credit agreement? Give the names only.
    # Mistral Response: The context provided does not directly contain a list of the Lenders' names from 'SCHEDULE I'. 
    #  However, it mentions that each Lender has an office designated as their Eurodollar Lending Office in Schedule I. 
    #  Therefore, you would need to refer to Schedule I itself to find the specific names of the Lenders.
    # Llama2 Response: Based on the context provided, the names of the Lenders in the WILD OATS MARKETS credit agreement are:
    #  1. Wells Fargo Bank, National Association
    #  2. U.S. Bank National Association
    # Expected Answer: Wells Fargo Bank, National Association AND U.S. Bank National Association AND Vectra Bank Colorado N.A. from SCHEDULE I

    # sample query = What is the arbitration amount beyond which 3 arbitrators are required? Give the amount only.
    # Mistral Response: The arbitration proceeding requires three arbitrators when the amount in controversy exceeds $5,000,000.00.
    # Llama2 Response: Based on the provided context, the answer to the question is: $10,000,000. --- but unit test RUN gave correct answer
    # Expected Answer: $5,000,000.00

    # sample query = Who is the Chief Executive Officer of Wild Oats? Give the name only.
    # Mistral Response: The text does not provide information about the Chief Executive Officer of Wild Oats. 
    #  It only mentions the contact information for the Chief Financial Officer and the General Counsel of Wild Oats Markets, Inc., 
    #  as well as some details regarding loan agreements and repurchase rights.
    # Llama2 Response: Perry D. Odak
    # Sources: ['data/Second Amended Credit Agreement WildOats Wells.pdf:86:1', 'data/Second Amended Credit Agreement WildOats Wells.pdf:18:1', 
    #  'data/Second Amended Credit Agreement WildOats Wells.pdf:70:3', 'data/Second Amended Credit Agreement WildOats Wells.pdf:64:4', 
    #  'data/Second Amended Credit Agreement WildOats Wells.pdf:52:0'] --- correct answer in page 64 4th chunk
    # Expected Answer: Perry Odak


    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = embedding_fn()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5) # k nearest neighbours

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(f" **Prompt is:  {prompt}")

    #model = Ollama(model="mistral")
    model = Ollama(model="llama2") # select the model

    response_text = model.invoke(prompt) # run the model with prompt

    sources = [doc.metadata.get("id", None) for doc, _score in results] # k nearest neighbours source chunks

    formatted_response = f"** Response: {response_text}\n\n** Sources: {sources}"
    print(formatted_response)
    print(" ")
    print("***********************************************************************************************")

    return response_text


if __name__ == "__main__":
    main()
