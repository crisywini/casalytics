## Objectives

- Get all the jsons by doing a requests
- Choose database after analyzing the data
- Extract information from database
- Use Visualization tool to create reports

  
### Steps
1. Get the curl command to extract all the information ✅
2. Research which type of database is better to store the json info [In Progress]
3. Decide if we are working with streaming or batch [Not Started]
4. if batch processing then create the database to extract all knowledge [Nor Started]


### Thoughts

The source of data came from FincaRaiz which is a web that has an API which I can query and extract the data that I need. The thing is that the data came as json response, which is great to analyze and also for web development, we might need to store that info (which is paginated) in batch, but we can also do streaming. 

Options to store the json info: 

1. Save chunks of json files
2. Convert the json files in a CSV file and treated it as the database
3. Store it in a relational Database 
4. Store it in a No-Relational Database

Things to consider: 
- The json has info such as links
- The json has images (urls) 
- The data that I will analyze would only consider prices, location and info from the home, such as number of rooms, and etcetera.

take into account to have enough data
