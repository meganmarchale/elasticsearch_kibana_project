# elasticsearch_kibana_project

## Structure of the repo





## Installation and set-up

The project is based on an [Apache sample](https://www.kaggle.com/datasets/vishnu0399/server-logs), downloaded from Kaggle. This is a synthetic server logs dataset based on Apache Server logs format.  
This dataset is stored in a 'data' folder.

ElasticSearch is greedy: you'll need to increase your Docker volume in order to be able to run the program. 

**Components in Log Entry :**  
- IP of client: This refers to the IP address of the client that sent the request to the server.
Remote Log Name: Remote name of the User performing the request. In the majority of the applications, this is confidential information and is hidden or not available.  
- User ID: The ID of the user performing the request. In the majority of the applications, this is a piece of confidential information and is hidden or not available.  
- Date and Time in UTC format: The date and time of the request are represented in UTC format as follows: Day/Month/Year:Hour:Minutes: Seconds +Time-Zone-Correction. 
- Request Type: The type of request (GET, POST, PUT, DELETE) that the server got. This depends on the operation that the request will do.  
- API: The API of the website to which the request is related. Example: When a user accesses a carton shopping website, the API comes as /usr/cart.  
- Protocol and Version: Protocol used for connecting with server and its version.  
- Status Code: Status code that the server returned for the request. Eg: 404 is sent when a requested resource is not found. 200 is sent when the request was successfully served.  
- Byte: The amount of data in bytes that was sent back to the client.  
- Referrer: The websites/source from where the user was directed to the current website. If none it is represented by “-“.  
- UA String: The user agent string contains details of the browser and the host device (like the name, version, device type etc.).  
- Response Time: The response time the server took to serve the request. This is the difference between the timestamps when the request was received and when the request was served.

View of the first entrey log:  
```/bash 
233.223.117.90 - - [27/Dec/2037:12:00:00 +0530] "DELETE /usr/admi5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likei/537.3.759.0" 45
/```


**Install requirements**



# Elasticsearch & Kibana Log Analysis Project

"Elasticsearch is an open source, distributed search and analytics engine built for speed, scale, and AI applications."
"Kibana is an open-source data visualization and exploration platform that provides a user-friendly interface to interact with data stored in Elasticsearch." - https://www.elastic.co/kibana 

## Overview

This project demonstrates a complete log ingestion, indexing, querying, and visualization pipeline using Python, Elasticsearch, and Kibana. It allows you to:  
- Parse and index web server logs.  
- Query logs for errors or specific URL patterns.  
- Perform aggregations (requests per status code, top IPs).  
- Visualize results using Kibana Lens (time series, pie charts, top IPs).  
- Test alerting logic by simulating error spikes.  

The project is organized in modular Python scripts for maintainability:  
- log.py → Handles parsing and bulk ingestion.  
- queries.py → Contains reusable Elasticsearch queries.  
- aggregations.py → Defines aggregation queries.  
- main.py → Orchestrates the workflow.

**Prerequisites**

- Docker  
- Python 3.12+ with virtual environment  
- Python packages: elasticsearch, python-dateutil  

**Setup**  

Start Elasticsearch:  

```/bash
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.13.4
docker run -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.13.4
/```


Start Kibana (link to Elasticsearch container):

docker run -d --link <elasticsearch_container_id>:elasticsearch -p 5601:5601 -e ELASTICSEARCH_HOSTS=http://host.docker.internal:9200 docker.elastic.co/kibana/kibana:8.13.4


Set up Python environment:

python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt


Run the main workflow:

python main.py


In Kibana:

Go to Stack Management → Data Views.

Create a Data View for logs and select timestamp as the time field.

Use Discover and Lens to explore and visualize data.

Project Methodology
Parsing & Ingestion

Logs are parsed using a regular expression and dateutil.parser.

Timestamps are converted to ISO 8601 for Elasticsearch compatibility.

Bulk ingestion uses the helpers.bulk method with proper error handling.

Querying & Aggregations

Queries are reusable and modular.

Examples: find errors (status_code >= 400), search by URL pattern.

Aggregations: requests per status code, top IPs.

Visualization

Kibana Lens visualizations:

Time series (requests over time).

Pie charts (status code distribution).

Bar charts (top IPs).

Advantages

Scalable: Works with large datasets via bulk indexing.

Flexible: Modular queries and aggregations allow easy customization.

Real-time insights: Kibana dashboards update dynamically.

Reusable: Scripts and functions can be adapted for different log sources.

Limitations & Precautions

Index mapping matters: Timestamps must match the format Elasticsearch expects (ISO 8601 recommended).

Existing indices: Re-running with old indices may fail due to mapping conflicts or _id duplicates. Always delete/recreate indices when changing mapping.

Time range in Kibana: If logs are outside the default time filter (e.g., future dates), Discover may appear empty. Always set the appropriate time range.

Data quality: Malformed logs may fail to parse — errors should be logged and handled.

Resource consumption: Large logs can consume significant memory during bulk ingestion. Consider batching or streaming.

Security & credentials: For production, secure Elasticsearch with proper authentication and TLS.

Future Enhancements

Alerting for error spikes or unusual patterns.

Advanced visualizations: heatmaps, geographic maps (IP locations).

Integration with log shippers like Filebeat or Logstash for real-time ingestion.

Automated tests for queries and aggregations.

Conclusion

This project demonstrates an end-to-end methodology for log analysis with Elasticsearch and Kibana, highlighting the benefits of structured log ingestion, flexible queries, and real-time visualization while cautioning about mapping, data quality, and index management.
