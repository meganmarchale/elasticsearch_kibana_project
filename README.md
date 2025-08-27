# elasticsearch_kibana_project


## Project description:

### 📊 Log Analysis Dashboard (Mini-ELK)
**Dataset**: Sample [Apache](https://www.kaggle.com/datasets/vishnu0399/server-logs) or [Web Server](https://www.kaggle.com/datasets/eliasdabbas/web-server-access-logs) log files  

**Must-have**  
- Index logs with fields: timestamp, status code, IP, URL  
- Find all errors (`status >= 400`)  
- Search logs by URL pattern  

**Nice-to-have**  
- Aggregations: requests per status code, per hour, top IPs  
- Visualization in [Kibana](https://www.tutorialspoint.com/kibana/index.htm) (time series or pie charts)  
- Alerting (simulated) for error spikes  


1 repository and your code and queries should follow **clean coding practices**:  
- Use meaningful variable names  
- Add docstrings to functions  
- Organize queries in reusable functions  
- Avoid hardcoding values unnecessarily  

### 🌟 Nice-to-Have
If you finish early or want to explore advanced features:  
- Implement **autocomplete** for search input  
- Use the **“did you mean”** feature for misspelled queries  
- Add **advanced aggregations** (e.g., histograms, percentiles)  
- Visualize results in [Kibana](https://www.tutorialspoint.com/kibana/index.htm) or a custom web UI  
- Try **vector search** if your dataset supports embeddings for similarity queries  



👉 Choose **one project idea** that excites you. Keep it simple but complete!  



## Structure of the repo





## Installation and set-up

The project is based on an [Apache sample](https://www.kaggle.com/datasets/vishnu0399/server-logs), downloaded from Kaggle. This is a synthetic server logs dataset based on Apache Server logs format.  
This dataset is stored in a 'data' folder.

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
233.223.117.90 - - [27/Dec/2037:12:00:00 +0530] "DELETE /usr/admi5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likei/537.3.759.0" 45```


**Install requirements**

