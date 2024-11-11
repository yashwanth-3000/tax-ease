import asyncio
import logging
import sys
from typing import List
from client import restack_client

# Import custom modules
from client import client
from functions.function import llm_complete
from functions.query_guidelines import query_guidelines
from workflows.workflow import search_and_process_workflow


async def main():
    await restack_client.start_service(
        workflows= [search_and_process_workflow],
        functions= [llm_complete]
    )

def run_services():
    asyncio.run(main())

if __name__ == "__main__":
    run_services()