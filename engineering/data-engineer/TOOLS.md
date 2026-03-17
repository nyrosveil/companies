# TOOLS.md -- Data Engineer

## Core Skills

- `para-memory-files` - Memory operations and knowledge management
- `apache-spark` - Large-scale data processing with PySpark/Spark SQL
- `dbt-transformation-patterns` - Data transformation and testing workflows
- `data-engineering-data-pipeline` - Pipeline orchestration and design
- `database-cloud-optimization` - Cloud data platform optimization

## Industry Tools

### Data Processing
- **Apache Spark** - Distributed data processing (batch & streaming)
- **Apache Flink** - Real-time stream processing
- **dbt** - Data transformation, testing, documentation
- **Apache Kafka** - Event streaming platform
- **Databricks** - Unified analytics platform

### Data Lakehouse
- **Delta Lake** - ACID transactions on data lakes
- **Apache Iceberg** - Open table format for big datasets
- **Apache Hudi** - Data lakes with upserts and incremental processing

### Cloud Platforms
- **Microsoft Fabric** - Unified data platform
- **Azure Synapse Analytics** - Enterprise data warehousing
- **AWS Glue** - Serverless data integration
- **Amazon Redshift** - Cloud data warehouse
- **Google BigQuery** - Serverless data warehouse
- **Snowflake** - Cloud data platform

### Data Quality
- **Great Expectations** - Data validation and testing
- **Soda** - Data quality monitoring
- **Deequ** - Data quality verification (AWS)

### Orchestration
- **Apache Airflow** - Workflow orchestration
- **Prefect** - Modern workflow orchestration
- **Dagster** - Data orchestration platform

## Integration Recommendations

- Use Great Expectations for comprehensive data quality validation
- Implement Delta Lake for time travel and ACID guarantees
- Use dbt for transformation logic and documentation
- Set up Airflow for complex pipeline dependencies
- Integrate with monitoring tools (Datadog, Grafana) for pipeline observability
