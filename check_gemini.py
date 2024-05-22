# """
# At the command line, only need to run once to install the package via pip:
# 
# $ pip install google-generativeai
# """

import google.generativeai as genai

genai.configure(api_key="AIzaSyCzI0zngcLOjAI6c1rM6waH4V5IhSdvmlI")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Which Indian banking stock has the hightest market capitalization?"]
  },
  {
    "role": "model",
    "parts": ["## Largest Indian Banking Stock by Market Cap (as of November 2023)\n\nDetermining the exact top banking stock by market capitalization requires real-time data as it fluctuates frequently. However, I can provide you with information to help you find the current leader:\n\n**Top contenders typically include:**\n\n* **HDFC Bank:** Often recognized as the largest private sector bank in India, HDFC Bank has historically held a leading position in market capitalization.\n* **ICICI Bank:** Another major private sector bank with a substantial market presence, ICICI Bank often competes closely with HDFC Bank for the top spot.\n* **State Bank of India (SBI):** As the largest public sector bank in India, SBI also commands a significant market capitalization and could be among the leaders.\n\n**To determine the current leader:**\n\n1. **Financial News Websites:** Check reliable financial news websites or aggregators like Moneycontrol, Economic Times, or Bloomberg Quint. They often have dedicated sections for market capitalization rankings.\n2. **Stock Exchange Websites:** Visit the websites of major Indian stock exchanges like the National Stock Exchange (NSE) or Bombay Stock Exchange (BSE). They provide real-time market data, including market capitalization.\n3. **Online Brokerage Platforms:** If you have an account with an online brokerage, they usually offer market data tools and screeners where you can filter stocks by market capitalization.\n\n**Additional Factors:**\n\n* **Market conditions:** Market capitalization can change rapidly due to stock price fluctuations. \n* **Mergers and acquisitions:** Banking mergers can significantly impact market capitalization rankings. \n\nRemember, I can only provide information up to November 2023.  It's crucial to access up-to-date data to ascertain the current leader in market capitalization among Indian banking stocks."]
  },
])

convo.send_message("Please provide SWOT Analysis of HDFC Bank.")
print(convo.last.text)

# (venv) (base) dechamma@192 langchain_category % python3 check_gemini.py            
# Thank you for providing your input. I'll analyze it carefully and use it to improve my responses and overall performance. 

# Is there anything specific you'd like me to do with this input, or any particular way you'd like me to respond? 

# For example, I can:

# * **Answer questions:** If your input is a question, I can try my best to answer it comprehensively and informatively.
# * **Generate text:**  I can create different creative text formats,  like poems, code, scripts, musical pieces, email, letters, etc. I will try my best to fulfill all your requirements.
# * **Translate languages:**  I can translate between many languages. Just let me know the source and target languages.
# * **Summarize information:**  If you provide me with a large amount of text, I can summarize the key points for you. 
# * **Offer different perspectives:**  I can analyze your input and provide various viewpoints or interpretations. 

# Please let me know how I can assist you further. 

# (venv) (base) dechamma@192 langchain_category % python3 check_gemini.py
# ## SWOT Analysis of HDFC Bank (as of November 2023)

# HDFC Bank, a leading private sector bank in India, exhibits several strengths, weaknesses, opportunities, and threats that influence its market position and future growth.

# **Strengths:**

# * **Strong Brand Reputation:** HDFC Bank boasts a well-established and trusted brand image, known for its reliability, customer service, and financial stability.
# * **Extensive Distribution Network:** With a vast network of branches and ATMs across the country, HDFC Bank enjoys wide accessibility and reach, catering to diverse customer segments.
# * **Robust Financial Performance:** The bank consistently demonstrates strong financial performance with healthy profitability, asset quality, and capital adequacy.
# * **Digital Innovation:** HDFC Bank actively embraces technology and digital solutions, offering user-friendly online banking, mobile apps, and innovative financial products.
# * **Diversified Product Portfolio:** Catering to various financial needs, the bank offers a wide range of products and services, including retail banking, corporate banking, investment banking, and insurance.

# **Weaknesses:**

# * **Premium Pricing:**  HDFC Bank often charges premium pricing for its products and services compared to some competitors, potentially limiting its customer base to specific income groups. 
# * **Dependence on Wholesale Funding:** The bank relies significantly on wholesale funding sources, which can be susceptible to market fluctuations and interest rate risks.
# * **Limited Rural Penetration:** Despite its extensive network, HDFC Bank's presence in rural areas remains comparatively lower than some public sector banks, potentially hindering its overall market share.

# **Opportunities:**

# * **Growing Indian Economy:**  India's expanding economy presents significant opportunities for HDFC Bank to increase its customer base and credit growth.
# * **Rising Digital Adoption:** The increasing adoption of digital banking and fintech solutions offers avenues for further innovation and market expansion.
# * **Untapped Rural Markets:**  Expanding its reach in rural areas could unlock a vast customer base and contribute to financial inclusion initiatives.
# * **Strategic Partnerships and Acquisitions:** Collaborations with fintech companies or acquisitions of smaller banks can enhance its technological capabilities and market share.

# **Threats:**

# * **Intense Competition:** The Indian banking sector is highly competitive, with both public and private sector banks vying for market share, putting pressure on margins and growth.
# * **Economic Slowdown:**  Economic downturns or fluctuations can impact loan demand, asset quality, and overall profitability.
# * **Regulatory Changes:**  Evolving regulations in the financial sector can pose challenges and require adaptations in operations and compliance.
# * **Cybersecurity Risks:**  As the bank increases its digital footprint, it becomes more susceptible to cybersecurity threats and data breaches. 

# **Overall:**

# HDFC Bank enjoys a strong position in the Indian banking industry, leveraging its brand, financial stability, and digital innovation. However, navigating challenges like competition, economic conditions, and regulatory changes while capitalizing on growth opportunities will be crucial for maintaining its leadership in the market. 
