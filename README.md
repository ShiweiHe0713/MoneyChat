# MoneyChat 💵 🤖️

Table of Contents:
- [WireFrame](#WireFrame)

## WireFrame
### Background
This is a project I plan to finish during the [Out In Tech](https://outintech.com/) Mentorship program (4/11-6/13, 2024), under the guidance of Raika Dail (Huge thanks to Raika!! 🥰)

- **What is MoneyChat?**
MoneyChat is a chatbot that helps you manage your money. It is built using the GPT and the Banks API(BOA, Chase) <br><br>

- **What inspired MoneyChat?**
I am a broke college student and I found my bank's app to be very confusing and not very accessible. I wanted to create a chatbot that would help me manage my money in a more user-friendly way.

### Objectives
- **What can MoneyChat do?**
A ChatBot that's connected with customers' bank account and provide them with information and visualization about their transactions. It can also help customers refine their budget and provide them with financial advice.
<br><br>
- **Why is it helpful?**
Finance for outsiders can be confusing, and the traditional way of interacting with website or app charts is not the future. Chatting with an AI that knows everything about your finance, MoneyChat will be like a personal finance assistant/doctor, keep clients finance condition healthy.

#### Some use case scenarios
**"Hey, MoneyChat!"**

1. "What's my last month's overall expenses like? Rank each category by expenses, and draw me a pie chart."<br><br>

2. "According to my last 6 months' expense, make me an achievable yet economical budget plan for this month."<br><br>

3. "What is my fixed bills every month? And what is the total amount of my fixed expense?"<br><br>

4. "Based on my last 3 months' cash flow, give me some advice on improving my finance."<br><br>

5. "Have I defaulted on any my credit card dues? Give me my credit card activities for every month."<br><br>

### Scope 
#### Ene Goal of the Product
- A knowledgeable Finance Chatbot who knows a lot about personal finance and finance in general.
- Backend connect to Third-party banks like Bank of America and JPMorgan Chase.
- A neat, beautiful and interactive website to interact with using automatic front-end techniques like Streamlit.

#### Mimimum Viable Product
- A ChatBot that can chat based on our monthly bank's statements(Since Bank's API may not be accessible for me.)

#### Stretching Goals
1. Building the wesbite's UI using **React.js**
2. Adding **dashboards** to display clients' most common viewed graphs or data.(Sort of like Tableau baords)
3. Building an **IOS** App and release on App Store

### Timeframe
| ID | Task | Start Date | End Date |
| -- | ---- | -----------| ---------|
| 1 | Thorough Wireframe    | May 3  | May 10 |
| 2 | Train a Finance LLM   | May 10 | May 17 |
| 3 | Support Banks' API    | May 17 | May 24 |
| 4 | Building the frontend | May 24 | May 31 |
| 5 | New features adding   | May 31 | June 7 | 
| 6 | Test & Marketing      | June 7 | June 13|

### Monitoring and Evaluation
For every task above, the corresponding evaluation could be:
1. A **PDF file** that clearly demonstrated the development process of the whole app.
2. A local **LLM** that can chat about finance in general, and can analyze bank statement.
3. Can use function/prompt to retrieve my bank account data, do some simple analysis based on the data.
4. Depends on the progress, I will either deliver an UI using Streamlit or React.
5. If the product is done at this stage, I will share the product in OIT slack channel and my friends.

## AI model
- [AdaptLLM/finance-chat](https://huggingface.co/AdaptLLM/finance-chat)
- gpt-3.5-turbo-0125(At the moment, only fine-tuned versions of gpt-3.5-turbo-0125 are supported.)

## Data Collection
Right I'm using my own bank statements to feed the model, and use GPT-4-Turbo assistant as the model for th initial testing. 

## Data Storage
We can manually retrieve the bank statement and other data and store the previous one in the database for direct usage, and every month after the new bank statements gets issued, that's when the API needs to retrieve the new bank statement and append them to our database.
1. [OpenAI vector store](https://platform.openai.com/docs/assistants/tools/file-search/creating-vector-stores-and-adding-files)

## Working prompt
Search all files, and find me the most significant single transaction from "Withdrawals and other subtractions" 
        from 2024-02-1 to 2024-04-30,
        And tell me why is it the biggest expense, and report your timeframe for your search.

## Resources
1. [OpenAI-Python Streaming Helpers](https://github.com/openai/openai-python/blob/main/helpers.md)
2. [OpenAI Assistants API](https://platform.openai.com/docs/assistants/overview?lang=python)

# Second Phase
After the attempt to connect to Bank of America API fails, I try to shift my focus on make the user interact with the excel sheet of our transactions. The procedures are:
1. The users download the transaction history from their banks(We use BofA as demo here.)
2. The user upload their csv/xlsx files to our system through the UI.
3. We take the csv file and 
   - Convert the documents into a structured format (e.g., JSON).
   - Read the file content and format it as a string.
   - Send the string to the OpenAI API to generate insights or responses.

Some other attempts:
I firstly use GPT Assistant to do the AI interaction, but it's not very customizable, so I refactor the code into using raw OpenAI API.

The Assistant has attachign file feature, but we have to interact with the vector stores to play with the files.

- User upload their file through POST -> receive file on the server -> pass on file to GPT