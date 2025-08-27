"""
docker pull docker.elastic.co/kibana/kibana:8.13.4

docker run --link elasticsearch:elasticsearch -p 5601:5601 \
  -e ELASTICSEARCH_HOSTS=http://host.docker.internal:9200 \
  docker.elastic.co/kibana/kibana:8.13.4
"""

def error_spike_alert(client, threshold=10):
    errors = requests_per_status_code(client)
    for e in errors:
        if e["key"] >= 400 and e["doc_count"] > threshold:
            print(f"Alert: High number of errors ({e['doc_count']}) for status {e['key']}")
