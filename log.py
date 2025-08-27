from elasticsearch import Elasticsearch, helpers
import re
from datetime import datetime
from elasticsearch.helpers import bulk, BulkIndexError

class LogIndexer:
    """Class to handle parsing, indexing, and querying log files in Elasticsearch."""

    def __init__(self, es_host="http://localhost:9200", index_name="logs", log_file="data/logfiles.log"):
        self.client = Elasticsearch(es_host)
        self.index_name = index_name
        self.log_file = log_file

        self.mapping = {
            "properties": {
                "timestamp": {"type": "date"},  # remove the 'format'
                "status_code": {"type": "integer"},
                "ip": {"type": "ip"},
                "url": {"type": "keyword"}
            }
        }

        self.log_pattern = re.compile(
            r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] '
            r'"(?P<request_type>\S+) (?P<url>\S+) [^"]+" (?P<status_code>\d+)'
        )

    def setup_index(self):
        """Delete and create the Elasticsearch index."""
        if self.client.indices.exists(index=self.index_name):
            self.client.indices.delete(index=self.index_name)
        self.client.indices.create(index=self.index_name, mappings=self.mapping)

    def parse_log_line(self, line):
        match = self.log_pattern.match(line.strip())
        if match:
            raw_ts = match.group("timestamp")  # e.g. "27/Dec/2037:12:00:00 +0530"
            try:
                parsed_ts = datetime.strptime(raw_ts, "%d/%b/%Y:%H:%M:%S %z")
                iso_ts = parsed_ts.isoformat()
            except Exception as e:
                print(f"❌ Failed to parse timestamp: {raw_ts} | Error: {e}")
                return None  # skip this line

            return {
                "timestamp": iso_ts,  # ISO 8601 string
                "status_code": int(match.group("status_code")),
                "ip": match.group("ip"),
                "url": match.group("url")
            }
        return None


    def generate_bulk_data(self):
        """Yield documents for bulk ingestion."""
        with open(self.log_file, "r", encoding="utf-8") as f:
            for line in f:
                doc = self.parse_log_line(line)
                if doc:
                    yield {"_index": self.index_name, "_source": doc}  # <- remove _id


    def index_logs(self):
        """Index all logs into Elasticsearch with per-document error debug."""
        start = datetime.now()
        actions = list(self.generate_bulk_data())  # convert generator to list for inspection

        print(f"Total documents prepared: {len(actions)}")

        try:
            success, errors = bulk(self.client, actions, raise_on_error=False, stats_only=False)
            print(f"✅ Successfully indexed: {success}")
            if errors:
                print(f"❌ Errors indexing documents: {len(errors)}")
                for e in errors[:5]:  # print first 5 errors
                    print(e)
        except BulkIndexError as e:
            print(f"Bulk indexing failed: {e}")

        print(f"Finished in {datetime.now() - start}")

# ---------- Wrap execution in a main() function ----------
def main():
    """Run the full log ingestion pipeline."""
    indexer = LogIndexer()
    indexer.setup_index()
    indexer.index_logs()
    print("First log entry:")
    # Optionally print the first document
    first_doc = next(indexer.generate_bulk_data(), None)
    if first_doc:
        print(first_doc["_source"])

# Allow running this script directly
if __name__ == "__main__":
    main()
