from elasticsearch import Elasticsearch

class LogQueries:
    """Reusable Elasticsearch queries for log analysis."""

    def __init__(self, client, index_name="logs"):
        self.client = client
        self.index_name = index_name

    def find_errors(self, min_status=400):
        """Return all logs with status code >= min_status."""
        query = {"query": {"range": {"status_code": {"gte": min_status}}}}
        return self.client.search(index=self.index_name, body=query)["hits"]["hits"]

    def search_by_url(self, url_pattern):
        """Search logs by URL pattern (wildcard)."""
        query = {"query": {"wildcard": {"url": f"*{url_pattern}*"}}}
        return self.client.search(index=self.index_name, body=query)["hits"]["hits"]

# ---------- Wrap execution in a main() function ----------
def main():
    """Run sample queries on the Elasticsearch logs index."""
    # Connect to Elasticsearch
    client = Elasticsearch("http://localhost:9200")
    queries = LogQueries(client)

    print("=== Sample: Find errors (status >= 400) ===")
    errors = queries.find_errors()
    for hit in errors[:5]:  # show first 5 for brevity
        print(hit["_source"])

    print("\n=== Sample: Search logs by URL pattern '/api' ===")
    results = queries.search_by_url("/api")
    for hit in results[:5]:
        print(hit["_source"])

# Allow running this script directly
if __name__ == "__main__":
    main()
