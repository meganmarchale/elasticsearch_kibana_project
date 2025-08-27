from log import main as ingest_logs
from query import main as run_queries
from agg import main as run_aggregations

def main():
    print("========== Step 1: Ingest Logs ==========")
    ingest_logs()

    print("\n========== Step 2: Run Queries ==========")
    run_queries()

    print("\n========== Step 3: Run Aggregations ==========")
    run_aggregations()

    print("\n========== All steps completed ==========")

# Entry point
if __name__ == "__main__":
    main()


"""
Once this has run: On to the Kibana part: 

# Pull the correct Kibana version
    docker pull docker.elastic.co/kibana/kibana:8.13.4

# Run Kibana
    docker run -d -p 5601:5601 -e ELASTICSEARCH_HOSTS=http://host.docker.internal:9200 --name kibana docker.elastic.co/kibana/kibana:8.13.4 cd48f5049a7288a64ee9df6ca6519748fbd6a7247d5f87795bdb6c97cc151260

"""