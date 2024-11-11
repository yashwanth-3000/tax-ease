from datetime import timedelta
from restack_ai.workflow import workflow, import_functions
#from restack_ai import log
from dataclasses import dataclass
from typing import List, Dict
import logging as log


# Import the necessary functions
with import_functions():
    from functions.function import llm_complete, FunctionInputParams
    from functions.query_guidelines import  query_guidelines

@dataclass
class WorkflowInputParams:
    query_text: str
    collection_name: str
    limit: int = 5

@workflow.defn(name="search_and_process_workflow")
class SearchAndProcessWorkflow:
    @workflow.run
    async def run(self, input: WorkflowInputParams):
        # Step 1: Query the collection using the user's input
        search_results = await workflow.step(
            query_guidelines,
            FunctionInputParams(
                query_text=input.query_text,
                collection_name=input.collection_name,
                limit=input.limit
            ),
            start_to_close_timeout=timedelta(seconds=120)
        )
        
        # Step 2: Format the search results for LLM processing
        formatted_context = "\n".join([
            f"Relevance: {result['relevance_score']}\nGuideline: {result['guideline']}"
            for result in search_results
        ])
        
        # Step 3: Create prompt for LLM with search results
        prompt = f"""
        Based on the following search results:

        {formatted_context}

        User Query: {input.query_text}

        Please analyze these guidelines and provide a comprehensive response addressing the query.
        """
        
        # Step 4: Process with LLM
        llm_result = await workflow.step(
            llm_complete,
            FunctionInputParams(prompt=prompt),
            start_to_close_timeout=timedelta(seconds=120)
        )
        
        # Log the final result
        log.info("Workflow completed", 
                search_results=search_results,
                llm_response=llm_result)
        
        # Return both search results and LLM response
        return {
            "search_results": search_results,
            "llm_response": llm_result
        }