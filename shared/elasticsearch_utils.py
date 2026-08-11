from elasticsearch import Elasticsearch


def create_es_client(host='localhost', port=9200, scheme='http',
                     username='elastic', password=None):
    auth = (username, password) if password else None
    client = Elasticsearch(
        [{'host': host, 'port': port, 'scheme': scheme}],
        basic_auth=auth,
    )

    try:
        if client.ping():
            print("Connected to Elasticsearch!")
        else:
            print("Failed to connect to Elasticsearch.")
    except Exception as e:
        print(f"Error connecting to Elasticsearch: {e}")

    return client
