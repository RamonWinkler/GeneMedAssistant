# GeneMedAssistant

## Objective
•	Lookup gene-related information (via API)

•	Recommend personalized treatments based on genetic profiles

•	Annotate and interpret genetic variants (via a robust pipeline)

•	Provide insights into gene-disease-drug interactions

##Data
▶ Download the following file from NCBI:
https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_info.gz

## PostgreSQL Container Startup
- When the docker-compose.yml file is executed with docker-compose up -d , Docker will pull the PostgreSQL image
(if not already pulled) and start a container from it.
- The PostgreSQL container will automatically create the database (as specified in the environment section) 
