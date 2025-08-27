from elasticsearch import Elasticsearch

class LogAggregations:
    """Reusable Elasticsearch aggregations for log analysis."""

    def __init__(self, client, index_name="logs"):
        self.client = client
        self.index_name = index_name

    def requests_per_status_code(self):
        """Return counts of requests per status code."""
        body = {
            "size": 0,
            "aggs": {"status_counts": {"terms": {"field": "status_code"}}}
        }
        return self.client.search(index=self.index_name, body=body)["aggregations"]["status_counts"]["buckets"]

    def top_ips(self, top_n=10):
        """Return top N IP addresses by number of requests."""
        body = {
            "size": 0,
            "aggs": {"top_ips": {"terms": {"field": "ip", "size": top_n}}}
        }
        return self.client.search(index=self.index_name, body=body)["aggregations"]["top_ips"]["buckets"]

# ---------- Wrap execution in a main() function ----------
def main():
    """Run sample aggregations on the Elasticsearch logs index."""
    client = Elasticsearch("http://localhost:9200")
    agg = LogAggregations(client)

    print("=== Requests per Status Code ===")
    for bucket in agg.requests_per_status_code():
        print(f"Status {bucket['key']}: {bucket['doc_count']} requests")

    print("\n=== Top IPs ===")
    for bucket in agg.top_ips():
        print(f"IP {bucket['key']}: {bucket['doc_count']} requests")

# Allow running this script directly
if __name__ == "__main__":
    main()
