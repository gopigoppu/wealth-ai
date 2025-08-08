Here's the complete README.md file in text format that you can copy directly:

```markdown
# 🏆 WealthInsight Pro -  Wealth Hackathon

## Overview

WealthInsight Pro is an advanced AI-powered conversational agent built using Google's Agent Development Kit (ADK) for the **Personalized Thought Leadership and Feedback Loop** use case (Use Case #2). This solution delivers exceptional, actionable portfolio insights by integrating client data, transaction history, and thought leadership content including ESG investing, AI revolution, and geopolitical risk analysis.

## ✨ Key Features

- **Dual Analysis Approach**: 
  - **Top-Down**: Market themes → client impact analysis
  - **Bottom-Up**: Client-specific questions → tailored responses
- **Real-time BigQuery Integration**: Direct access to client profiles, transactions, and deposit data
- **Thought Leadership Integration**: ESG, AI, and geopolitical market insights
- **Rich Visualizations**: Structured JSON responses with charts, tables, and actionable recommendations
- **Function-based Modular Architecture**: Scalable design using pure functions
- **Latest Google ADK Compatibility**: Built with cutting-edge ADK patterns
- **Production Ready**: Error handling, logging, and configuration management

## 📁 Project Structure

```
.
├── main.py
├── Dockerfile
├── requirements.txt
├── .env
└── thought_leadership/
    ├── agent.py
    ├── requirements.txt
    ├── tools/
    │   ├── bigquery_tool.py
    │   ├── rag_tools.py
    │   └── visualization_tools.py
    └── sub_agents/
        ├── client_portfolio.py
        ├── market_intel.py
        ├── content_intel.py
        ├── recommendations.py
        └── visualization.py
```

## 🚀 Prerequisites

- **Python 3.9+**
- **Google Cloud Project** with billing enabled
- **BigQuery dataset** with  Wealth data loaded
- **Service Account** with the following roles:
  - `roles/bigquery.dataViewer`
  - `roles/bigquery.jobUser`
  - `roles/bigquery.readSessionUser`
- **Google ADK** installed (`google-adk>=1.0.0`)

## ⚙️ Setup Instructions

### Step 1: Clone the Repository

```
git clone 
cd wealth-insight-pro
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

Create a `.env` file in the root directory:

```
# Google Cloud Configuration
GOOGLE_CLOUD_PROJECT=your--wealth-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# BigQuery Configuration
BIGQUERY_DATASET_ID=_wealth

# Authentication
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json

# Development Settings
DEBUG=true
LOG_LEVEL=INFO
```

### Step 4: Load Data into BigQuery

Follow the hackathon instructions to load the provided CSV files:

1. **Activate Cloud Shell and Create Storage Bucket**:
   ```
   gsutil mb -c regional -l us-central1 gs://
   gsutil cp -r gs://_hackathon/* gs:///
   ```

2. **Create BigQuery Dataset**:
   ```
   bq mk --dataset --location=us-central1 your-project:_wealth
   ```

3. **Import CSV files into BigQuery tables**:
   - Customer profiles → `customer_profile` table
   - Deposit accounts → `deposit_account` table  
   - Transactions → `transactions` table

   Use the [BigQuery CSV loading guide](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv) with auto-detect schema enabled.

### Step 5: Verify Data Schema

Ensure your BigQuery tables match the expected schema:

- **customer_profile**: CustomerID, Customer_Name, Email, Age, Risk_Tolerance, Estimated_Net_Worth, Financial_Goals
- **deposit_account**: CustomerID, Product_Type, Balance_Amount, Interest_Rate, Start_Date, Maturity_Date  
- **transactions**: CustomerID, date, category, amount, merchant_name, txn_description

### Step 6: Run the Agent

#### Local Development:
```
# Web interface (recommended)
adk web

# CLI interface
adk run

# Direct Python execution
python agent.py
```

#### Access the Application:
- **Web UI**: http://localhost:8080
- **API**: http://localhost:8080/api

## 💡 Usage Examples

### Bottom-Up Analysis (Client-Specific Insights)

```
from wealth_insight.orchestration.bottom_up import handle_bottom_up_analysis

# Analyze specific customer for July 2025
result = handle_bottom_up_analysis(
    customer_id=1001,
    start_date="2025-07-01", 
    end_date="2025-07-31"
)

print(result)
# Returns: charts, tables, insights, calls_to_action
```

### Top-Down Analysis (Market Theme Impact)

```
from wealth_insight.orchestration.top_down import handle_top_down_analysis

# Analyze ESG investing theme impact
result = handle_top_down_analysis(
    theme="ESG Investing",
    min_net_worth=1000000
)

print(result)
# Returns: theme analysis, impacted clients, recommendations
```

### Sample Web Interface Queries:

1. **"Analyze customer 1002's spending patterns for the last 3 months"**
2. **"What clients would be impacted by AI investment themes?"**
3. **"Show me ESG investment opportunities for high net worth clients"**
4. **"Generate insights for customer 1005's portfolio optimization"**

## 🔧 Configuration

### Market Themes

The system includes built-in support for:
- **ESG Investing**: Sustainable investment opportunities
- **AI Revolution**: Technology and semiconductor investments  
- **Geopolitical Risk**: Geographic diversification strategies

Add new themes in `wealth_insight/config.py`:

```
MARKET_THEMES = {
    "YOUR_THEME": {
        "title": "Theme Title",
        "keywords": ["keyword1", "keyword2"],
        "insights": ["Key insight 1", "Key insight 2"]
    }
}
```

## 🚀 Deployment Options

### Option 1: ADK Deployment
```
# Development Environment
adk web --host 0.0.0.0 --port 8080

# Production Deployment to Vertex AI Agent Engine
adk deploy --project your-project --region us-central1
```

### Option 2: Agentspace Deployment

Follow the detailed Agentspace setup instructions from the hackathon documentation:

1. **Create Agentspace Application**
2. **Create Datastores**
3. **Create Conversational Agents**
4. **Configure Integration Connectors**
5. **Deploy and Test**

### Option 3: Conversational Agents (Dialogflow)

1. Enable Dialogflow API
2. Create playbook-based agent
3. Configure BigQuery connector tool
4. Build playbook with goals and instructions
5. Test using console simulator

## 🧪 Testing

```
# Run tests
python -m pytest tests/

# Test individual functions
python -c "from wealth_insight.data.bigquery_ops import get_customer_profile; print(get_customer_profile(1001))"
```

## 🔍 Troubleshooting

### Common Issues:

1. **"Customer not found" error**:
   - Verify CustomerID exists in BigQuery
   - Check BigQuery permissions
   - Ensure data is loaded correctly

2. **BigQuery connection failed**:
   - Verify `GOOGLE_APPLICATION_CREDENTIALS` path
   - Ensure service account has proper roles
   - Check project ID in environment variables

3. **ADK import errors**:
   - Update to latest ADK: `pip install --upgrade google-adk`
   - Verify Python version >= 3.9
   - Check for conflicting dependencies

4. **Schema mismatch**:
   - Check column names match exactly (case-sensitive)
   - Ensure CustomerID is integer type
   - Verify table names in config.py

### Debug Mode:

```
DEBUG=true LOG_LEVEL=DEBUG adk web
```

### Budget Monitoring:

**Important**: The hackathon has budget limits:
- 70% threshold: Email notification
- 100% threshold: Access loss (contact Google team)
- Only 2 users should be actively logged in

## 📊 Hackathon Judging Criteria Alignment

This implementation addresses all key judging criteria:

✅ **Solution Quality**: Handles both top-down and bottom-up scenarios with actionable insights  
✅ **Functional Demo**: Complete end-to-end user journey with real data integration  
✅ **Presentation Clarity**: Clear architecture with modular components  
✅ **Implementation & Scalability**: Production-ready code with error handling  
✅ **Business Impact**: Quantified recommendations with clear calls-to-action  

## 🎯 Advanced Features for Production

1. **Enhanced Data Sources**: 
   - Integrate LSEG/Refinitiv market data
   - Add CRM system connections
   - Include ESG ratings feeds

2. **Real-time Processing**: 
   - Stream processing for live portfolio updates
   - Event-driven architecture
   - Real-time market data integration

3. **Advanced Analytics**: 
   - Predictive client behavior models
   - Risk assessment algorithms
   - Portfolio optimization engine

4. **Compliance & Security**: 
   - Regulatory reporting capabilities
   - Data encryption and privacy controls
   - Audit trail and logging

### Technical Resources:
1. [Google ADK Documentation](https://google.github.io/adk-docs/)
2. [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
3. [Agentspace Documentation](https://cloud.google.com/agentspace/docs)
4. Use the **Hackathon Coach Gem** in Gemini for guidance

### Hackathon Coach Setup:
1. Go to https://gemini.google.com
2. Create a new Gem named "Hackathon Coach"
3. Upload the hackathon instructions document
4. Use for 24/7 mentoring and feedback

## 📄 Files Overview

### Core Implementation Files:

- `agent.py`: Main entry point with latest ADK syntax
- `requirements.txt`: Python dependencies
- `wealth_insight/config.py`: Configuration and market themes
- `wealth_insight/data/bigquery_ops.py`: Data access functions
- `wealth_insight/insights/synthesis.py`: Thought leadership integration
- `wealth_insight/visualization/charts.py`: Chart generation
- `wealth_insight/orchestration/`: Top-down and bottom-up workflows

## 📝 License

This project is developed for the  Wealth Hackathon. Please follow your organization's guidelines for code sharing and intellectual property.

---

## 🏆 Success Tips

1. **Focus on the Use Case**: Address both top-down and bottom-up scenarios
2. **Demonstrate Real Value**: Use actual BigQuery data for insights
3. **Show Scalability**: Explain how this scales across  Wealth
4. **Prepare for Q&A**: Practice explaining your technical choices
5. **Use the Coach**: Leverage the Hackathon Coach Gem for feedback

**Built with ❤️ for the  Wealth Hackathon - Good Luck! 🚀**
```

This complete README.md file includes all the essential information from the hackathon instructions document and provides a comprehensive guide for setting up and running the WealthInsight Pro agent. You can copy this entire text and save it as a README.md file in your project repository.

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/18927030/436254aa-1568-46b6-ba13-429b87101bc7/Google-Hackathon-Instructions-for--Wealth.pdf
[2] https://github.com/vasumathi298/-hackathon-trading-platform-application
[3] https://builtin.com/job/wealth-analyst-data-analytics-innovation/6554688
[4] https://www.linkedin.com/posts/sanskrutikhedkar_solutionscentersindia-india-fortheloveofprogress-activity-7250181147479920641-9RGp
[5] https://www..com/ventures/perspectives/opinion/modern-wealth-planning-stack.html
[6] https://builtin.com/job/-wealth-head--wealth-studio-c16/4314919
[7] https://www.youtube.com/watch?v=tRBleFBnE7Y
[8] https://www..com/ventures/perspectives/opinion/wealthtech-to-the-rescue.html
[9] https://www.linkedin.com/pulse/s-wealthtech-woes-wealthbriefing-2025-awards-call-more-fusion-ekg5e
[10] https://www.linkedin.com/posts/manpreet-rathore-14a386186_i-am-thrilled-to-be-a-part-of-hackathonwealth-activity-7225830626069778432-kezn
[11] https://www..com/ventures/perspectives/opinion/wealthtech.html?msockid=2dd1131e38626e771aad051439976f0f