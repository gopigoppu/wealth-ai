# WealthGPT: README

## Overview

**WealthGPT** is a digital private banker app orchestrating expert agents to deliver highly actionable, data-driven insights, recommendations, and visualizations for client portfolios. The solution routes queries to specialized agents backed by both internal data (BigQuery) and external intelligence to maximize value, clarity, and trust for users.

## Project Structure

```
.
├── main.py                  # entry point for WealthGPT (FastAPI/backend/app)
├── Dockerfile               # containerization setup
├── requirements.txt         # root dependencies for main service
├── .env                     # environment variables (API keys, DB settings)
└── thought_leadership/      # main package for agent orchestration
    ├── agent.py                      # agent manager and router logic
    ├── requirements.txt              # extra dependencies for sub-module
    ├── tools/                        # all plugins/utilities
    │   ├── bigquery_tool.py              # queries client/portfolio/account/asset data
    │   ├── rag_tools.py                  # retrieval-augmented generation, connects internal content
    │   └── visualization_tools.py        # chart/table/graph builder (matplotlib, plotly, etc.)
    └── sub_agents/
        ├── client_portfolio.py           # portfolio analysis, holding breakdowns, risk, exposures
        ├── market_intel.py               # live financial data, news, real-time events
        ├── content_intel.py              # internal research, strategist insights, macro themes
        ├── recommendations.py            # actionable advice, next steps, call-to-action logic
        └── visualization.py              # visual output rendering
```

## Agent Capabilities

- **client_portfolio_agent:**  
  Handles all client/account/portfolio queries: provides detailed asset breakdowns, risk exposures, and concentration tables using BigQuery data. Automatically routes results to visualization when needed.

- **recommendation_agent:**  
  Synthesizes insights and delivers explicit, highly actionable next steps or strategies. Always invoked for recommendations or if the user wants to know "what should I do?"

- **content_intelligence_agent:**  
  Summarizes strategist/internal research for macro themes and thought leadership. All summaries are well-cited for transparency.

- **market_intelligence_agent:**  
  Fetches real-time financial data, news, and market context from external sources to supplement internal data or cover gaps. Used for events, quotes, and breaking trends.

- **build_visualization:**  
  Builds charts, graphs, and tables to visually clarify results whenever numbers, rankings, or comparisons are involved.

## System Workflow

1. **True Intent Identification:**  
   The LLM always confirms and clarifies user queries before routing to agents.

2. **Smart Routing and Orchestration:**  
   Queries are directed to the most relevant agent/tool. If multi-perspective is needed, outputs are merged and presented in a unified answer.

3. **Graceful Fallback:**  
   For unknown or missing data, fallback agents use public content, explaining gaps and presenting alternate answers (transparently flagged in the response).

4. **Error Handling:**  
   If a tool or agent fails, the system informs the user and offers alternate suggestions.

5. **Actionable Endings:**  
   Every answer ends with a clear summary, next steps, or call-to-action.

## Setup & Deployment

1. **Prerequisites:**  
   - Python 3.9+  
   - Docker (optional, for containerized deployment)
   - Service credentials for BigQuery and any external APIs (set these in `.env`)

2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   cd thought_leadership
   pip install -r requirements.txt
   ```

3. **Set environment variables:**  
   - Fill out `.env` with API keys and DB credentials as needed.

4. **Run the app:**  
   ```bash
   python main.py
   ```

   Or build and run via Docker:
   ```bash
   docker build -t wealthgpt .
   docker run --env-file .env -p 8080:8080 wealthgpt
   ```

## Usage

- Start WealthGPT service.
- Query via API (see `main.py`), or connect with conversational UI.
- The LLM-powered orchestrator parses your query, routes tasks to appropriate agent(s), and delivers the most comprehensive, actionable, and client-appropriate answer—always ending with next steps.

## Example Query

_"What is the risk exposure in my client’s tech sector holdings and how should we rebalance for Q4?"_

- Workflow:
    - `client_portfolio_agent`: Lists tech holdings, exposures, concentrations (from BigQuery).
    - `content_intelligence_agent`: Summarizes strategist macro themes on tech sector.
    - `market_intelligence_agent`: Checks current tech sector trends, news, and real-time context.
    - `recommendation_agent`: Synthesizes all inputs, delivers a rebalancing recommendation with explicit action items.
    - `build_visualization`: Returns asset breakdown charts and recommended allocation tables.

## Principles

- Every answer is **well-cited**, clear, and tailored for private banking/high-net-worth clients.
- User always receives **next steps**—never a dead-end.
- Transparent fallback for data issues.

***

# WealthGPT Agent-Based System ArchitectureBased on the provided architectural overview and data analysis, I've created a comprehensive, well-defined architecture for the WealthGPT system that incorporates Google Cloud products, specialized agents, and tools. Here's the detailed architecture:## Architecture OverviewThe WealthGPT system is designed as a **cloud-native, multi-agent wealth management platform** built on Google Cloud Platform. The architecture follows a layered approach with seven distinct tiers, each optimized for specific functionality while maintaining enterprise-grade security and scalability.

## Core Architecture Components### 1. Client Interface Layer
- **Web Applications**: React/Angular-based interfaces
- **Mobile Applications**: React Native/Flutter apps  
- **API Clients**: Third-party system integrations
- **Authentication**: OAuth 2.0 and Google Cloud Identity integration

### 2. API Gateway Layer (`main.py`)
**Google Cloud Services Used:**
- **Cloud Endpoints**: API management and monitoring
- **Cloud Armor**: DDoS protection and WAF
- **Cloud Load Balancing**: Global traffic distribution
- **Cloud Identity**: Centralized authentication

**Features:**
- FastAPI-based request routing
- Rate limiting and throttling
- Request validation and documentation

### 3. Agent Orchestration Layer (`agent.py`)
**Google Cloud Services Used:**
- **Vertex AI**: Natural language understanding and intent detection
- **Cloud Functions**: Serverless orchestration logic
- **Pub/Sub**: Event-driven agent communication

**Capabilities:**
- Intelligent agent selection and routing
- Multi-agent coordination
- Context management across conversations
- Response aggregation and formatting

### 4. Specialized Subagents#### Portfolio Agent (`client_portfolio.py`)
- Asset allocation analysis and risk assessment
- Portfolio performance tracking
- Compliance verification
- Investment optimization recommendations

#### Market Intelligence Agent (`market_intel.py`) 
- Real-time market data processing via LSEG/Refinitiv
- Economic indicator analysis
- News sentiment analysis and trend detection

#### Content Intelligence Agent (`content_intel.py`)
- Research document retrieval and synthesis
- Thought leadership content analysis
- Regulatory update processing

#### Recommendations Agent (`recommendations.py`)
- Personalized investment suggestions
- Next best action identification
- Goal-based financial planning
- Risk-adjusted portfolio recommendations

#### Visualization Agent (`visualization.py`)
- Interactive chart generation
- Dashboard creation and custom reporting
- Mobile-responsive visualizations

### 5. Tools Layer#### BigQuery Tool (`bigquery_tool.py`)
**Purpose**: Secure data warehouse access
**Google Cloud Service**: **BigQuery**
- Customer profile queries (50+ customers with 34+ data points)
- Transaction analysis (15+ categories, real-time processing)
- Portfolio data retrieval
- Regulatory reporting and compliance

#### RAG Tools (`rag_tools.py`)
**Google Cloud Services**: **Vertex AI + Cloud Storage**
- Document embedding and semantic search
- Knowledge synthesis from research documents
- Multi-modal content processing

#### Visualization Tools (`visualization_tools.py`)
**Integration**: **Looker + Custom Charts**
- Interactive plotting with Plotly/D3.js
- Export capabilities (PDF, PNG, SVG)
- Real-time data visualization updates

### 6. Google Cloud Services Layer#### Data & Analytics
- **BigQuery**: Enterprise data warehouse (customer profiles, transactions, market data)
- **Cloud Storage**: Unstructured data storage (research docs, reports, images)  
- **Looker**: Business intelligence and embedded analytics

#### AI & ML Services
- **Vertex AI**: Unified ML platform for model hosting and training
- **Agentspace**: Enterprise AI agent management and orchestration

#### Infrastructure
- **Pub/Sub**: Real-time messaging for market feeds and notifications
- **Cloud Run**: Serverless container platform for agent services
- **Memorystore**: Redis caching layer for performance optimization

### 7. Data Sources Layer#### Internal Data
- Customer profiles (demographics, preferences, risk tolerance)
- Account balances and investment holdings
- Transaction history and spending patterns

#### External Data  
- **LSEG/Refinitiv**: Market data via BigQuery integration
- Economic indicators and news feeds
- Research reports and regulatory filings

#### Compliance Data
- KYC documents and AML records
- Audit trails and risk assessments

## Security Architecture**Authentication**: Google Cloud IAM with RBAC
**Data Protection**: AES-256 encryption at rest, TLS 1.3 in transit  
**Network Security**: VPC, Cloud Armor, Private Google Access
**Compliance**: SOC 2, PCI DSS, GDPR compliance

## Scalability Features- **Auto-scaling**: Cloud Run (0 to 1000+ instances)
- **Load Balancing**: Global traffic distribution
- **Caching**: Cloud CDN and Memorystore optimization
- **Monitoring**: Cloud Operations Suite for observability

## Data Flow Example1. User query → FastAPI (`main.py`)
2. Authentication → Google Cloud Identity  
3. Agent routing → Orchestrator (`agent.py`)
4. Specialized processing → Subagents (portfolio, market, etc.)
5. Data access → Tools (BigQuery, RAG, visualization)
6. Cloud services → GCP infrastructure
7. Response synthesis → Aggregated user response


**Contact:**  
For issues, suggestions, or agent customization: Open a Github issue or email the project owner.

**License:**  
MIT (or as specified in project LICENSE file).


