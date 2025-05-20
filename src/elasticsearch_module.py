from elasticsearch import Elasticsearch

from src.midi_melodies import build_melodies_from_midi_files

es = Elasticsearch(
    "http://localhost:9200", headers={"Content-Type": "application/json"}
)

INDEX_NAME = "melodies"


def clear_all_data():
    # Apenas remove o índice usado pela aplicação
    if es.indices.exists(index=INDEX_NAME):
        es.indices.delete(index=INDEX_NAME)


def create_index():
    if es.indices.exists(index=INDEX_NAME):
        es.indices.delete(index=INDEX_NAME)

    settings = {
        "settings": {
            "analysis": {
                "analyzer": {
                    "melody_analyzer": {
                        "type": "custom",
                        "tokenizer": "ngram_tokenizer",
                    }
                },
                "tokenizer": {
                    "ngram_tokenizer": {
                        "type": "ngram",
                        "min_gram": 2,
                        "max_gram": 3,
                        "token_chars": ["letter"],
                    }
                },
            }
        },
        "mappings": {
            "properties": {
                "melody_id": {"type": "keyword"},
                "melody_pattern": {"type": "text", "analyzer": "melody_analyzer"},
            }
        },
    }

    es.indices.create(index="melodies", body=settings)


def populate_data():
    melodies = build_melodies_from_midi_files()

    for doc in melodies:
        es.index(index=INDEX_NAME, document=doc)


def get_melodies(pattern: str):
    query = {
        "query": {
            "match": {"melody_pattern": {"query": pattern, "fuzziness": "0"}}
        }
    }
    response = es.search(index="melodies", body=query, size=5)
    return response


def setup_database():
    clear_all_data()
    create_index()
    populate_data()
    print("Elasticsearch initialized and populated.")
