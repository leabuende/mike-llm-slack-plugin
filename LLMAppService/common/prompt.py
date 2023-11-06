import pathway as pw
from datetime import datetime
from common.model_helper import openai_chat_completion


def prompt(index, embedded_query, user_query):

    @pw.udf
    def build_prompt(local_indexed_data, query):
        docs_str = "\n".join(local_indexed_data)
        prompt = f"Given the following data: \n {docs_str} \nanswer this query: {query}, Assume that current date is: {datetime.now()}. Be friendly in your answer and respond like a colleague would. Don't offer further assistance."
        return prompt

    query_context = embedded_query + index.get_nearest_items(
        embedded_query.vector, k=3, collapse_rows=True
    ).select(local_indexed_data_cards=pw.this.card).promise_universe_is_equal_to(embedded_query)
    
    prompt = query_context.select(
        prompt=build_prompt(pw.this.local_indexed_data_cards, user_query)
    )

    return prompt.select(
        query_id=pw.this.id,
        result=openai_chat_completion(pw.this.prompt),
    )