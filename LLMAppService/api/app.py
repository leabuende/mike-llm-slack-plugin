import pathway as pw
import os
from common.embedder import embeddings, index_embeddings
from common.prompt import prompt


def run(host, port):
    query, response_writer = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=QueryInputSchema,
        autocommit_duration_ms=50,
    )
    board_data = pw.io.jsonlines.read(
        "./data",
        schema=DataInputSchema,
        mode="streaming"
    )
    embedded_data = embeddings(context=board_data, data_to_embed=board_data.card)
    index = index_embeddings(embedded_data)
    embedded_query = embeddings(context=query, data_to_embed=pw.this.query)
    responses = prompt(index, embedded_query, pw.this.query)
    response_writer(responses)
    pw.run()


class DataInputSchema(pw.Schema):
    card: str


class QueryInputSchema(pw.Schema):
    query: str