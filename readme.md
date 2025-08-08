<div align="center">
  <h1>Amazon Semantic Search</h1>
</div>

<p align="center">
  <img src="assets/Amazon-Search.png" alt="architecture_1" width="600">
</p>

## 🏗️ Project Structure

```text
.
├── data/                                          # Directory where dataset files and processed data will be downloaded.
├── superlinked_app/                               # Main application source code
├── tools/                                         # Utility scripts and helper tools
├── .env                                           # Environment variables for local development
├── .env.example                                   # Template for environment variables
├── Makefile                                       # Running commands shortcuts(linux only)
├── environment.yml                                # Conda environment dependencies and metadata
└── requirements.txt                               # dependencies using pip
```

## 💾 Dataset

We will use the [ESCI-S: extended metadata for Amazon ESCI dataset](https://github.com/shuttie/esci-s?tab=readme-ov-file) dataset released under the Apache-2.0 license.

It is an e-commerce dataset on Amazon products. 

The full dataset references ~1.8M unique products. We will work with a sample of 4400 products to make everything lighter, but the code is compatible with the whole dataset.


# 🚀 Setup Guide
You'll need access to:

| Service | Purpose | Cost | Required Environment Variables | Setup Guide |
|---------|---------|------|---------------------|-------------|
| [OpenAI API](https://openai.com/index/openai-api/) | LLM API | Pay-per-use | `OPENAI_API_KEY`<br>`OPENAI_MODEL_ID` | [Quick Start Guide](https://platform.openai.com/docs/quickstart) |
| [MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-database) | Vector DB | Free tier | `USE_MONGO_VECTOR_DB`<br>`MONGO_CLUSTER_URL`<br>`MONGO_DATABASE_NAME`<br>`MONGO_CLUSTER_NAME`<br>`MONGO_PROJECT_ID`<br>`MONGO_API_PUBLIC_KEY`<br>`MONGO_API_PRIVATE_KEY` | 1. [Create a free MongoDB Atlas account](https://www.mongodb.com/cloud/atlas/register/?utm_campaign=paul_iusztin&utm_medium=referral) <br> 2. [Create a Cluster](https://www.mongodb.com/docs/guides/atlas/cluster/?utm_campaign=paul_iusztin&utm_medium=referral) </br> 3. [Add a Database User](https://www.mongodb.com/docs/guides/atlas/db-user/?utm_campaign=paul_iusztin&utm_medium=referral) </br> 4. [Configure a Network Connection](https://www.mongodb.com/docs/guides/atlas/network-connections/?utm_campaign=paul_iusztin&utm_medium=referral) </br> 5. [Create an API Key](https://docs.superlinked.com/run-in-production/index-1/mongodb#creating-the-api-key) </br> 6. [Create an empty database](https://docs.superlinked.com/run-in-production/index-1/mongodb#creating-the-database) |

# 💻 Setup in 4 Steps

## 1. Install Dependencies(Using Conda)
Set up the project environment by running the following:
```bash
conda env create -f environment.yml
```
Activate conda env:
```bash
conda activate amazon-search
```

## 2. Configure Environment

Before running any components:
1. Create your environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and configure the required credentials following the inline comments (see [superlinked_app/config.py](superlinked_app/config.py) for all options).

3. Your final `.env` file should have these MongoDB-related variables:
   
```bash
OPENAI_API_KEY = 
USE_MONGO_VECTOR_DB=True
MONGO_CLUSTER_URL=username:password@free-cluster.xxxxx.mongodb.net
MONGO_DATABASE_NAME=your_database_name
MONGO_CLUSTER_NAME=free-cluster
MONGO_PROJECT_ID=your_project_id
MONGO_API_PUBLIC_KEY=your_public_key
MONGO_API_PRIVATE_KEY=your_private_key
```

## 3. Process data

1. Create Database:
  ```bash
  make create-mongodb-database
  ```
2. Download and process the dataset sample:
```bash
make download-and-process-sample-dataset
```
Full dataset is too big, a powerful cpu and gpu is required for full dataset, to try it:
```bash
make download-and-process-full-dataset
```

3. You should see this structure in your `data` folder:
```text
data/
├── processed_100_sample.jsonl
├── processed_300_sample.jsonl
├── processed_850_sample.jsonl
├── sample.json
└── sample.json.gz
```

4. Load data:
```bash
make load-data
```

## 4. Launch the Setup:
1. Start it up:
```bash
make start-superlinked-server
```

2. From a different terminal,Try some queries:
```bash
make post-filter-query     
make post-semantic-query   
make similar-item-query
```

3. Start the Streamlit UI:
```bash
make start-ui
```
Accessible at `http://localhost:8501/`