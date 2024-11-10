from restack_ai.function import function, log, FunctionFailure
from openai import OpenAI
from pymilvus import MilvusClient
from dataclasses import dataclass
from typing import List, Dict
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class FunctionInputParams:
    query_text: str
    collection_name: str
    limit: int = 5

@function.defn(name="query_guidelines")
async def query_guidelines(input: FunctionInputParams) -> List[Dict]:
    """
    Search tax guidelines database with a query and return results as a list.
    
    Args:
        input (FunctionInputParams): Contains query_text, collection_name, and limit
        
    Returns:
        List[Dict]: List of search results, each containing relevance score and guideline text
    """
    try:
        # Initialize OpenAI client
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            log.error("OPENAI_API_KEY environment variable is not set.")
            raise ValueError("OPENAI_API_KEY environment variable is required.")

        # Initialize clients
        openai_client = OpenAI(api_key=api_key)
        milvus_client = MilvusClient("tax_guidelines.db")
        
        # Get embedding for query
        response = openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=[input.query_text]
        )
        query_embedding = response.data[0].embedding
        
        # Search in Milvus
        results = milvus_client.search(
            collection_name=input.collection_name,
            data=[query_embedding],
            limit=input.limit,
            output_fields=["text"]
        )
        
        # Store results in a list
        search_results = []
        if results and len(results) > 0:
            for hit in results[0]:
                search_results.append({
                    'relevance_score': 1 - hit['distance'],
                    'guideline': hit['entity']['text']
                })
                
        return search_results
        
    except Exception as e:
        log.error(f"Error querying guidelines: {e}")
        raise FunctionFailure(f"Error querying guidelines: {e}", non_retryable=True)