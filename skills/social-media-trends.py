from pytrends.request import TrendReq
import time
import pandas as pd

# Initialize (no API key needed)
pytrends = TrendReq(hl='en-US', tz=240)  # tz=240 for Calgary 

# Get real-time trending searches
trending = pytrends.trending_searches(pn='US')
print(trending.head(20))

# Define your niche keywords (max 5 per request)
keywords = ['heart health', 'cardiology', 'cholesterol']

# Build payload
pytrends.build_payload(keywords, timeframe='now 7-d', geo='IN')

# Get interest over time
interest = pytrends.interest_over_time()
print(interest)

# CRITICAL: Wait between requests to avoid rate limiting
time.sleep(3)

# Get related queries (THIS IS GOLD - shows rising topics)
related = pytrends.related_queries()
for kw in keywords:
    print(f"\n=== Rising queries for '{kw}' ===")
    rising = related[kw]['rising']
    if rising is not None:
        print(rising.head(10))

# Find breakout topics (potential viral content)
def find_breakout_topics(keyword, geo=''):
    """Find topics with explosive growth (potential viral content)"""
    pytrends.build_payload([keyword], timeframe='today 3-m', geo=geo)
    time.sleep(3)  # Rate limiting
    
    related = pytrends.related_queries()
    rising = related[keyword]['rising']
    
    if rising is not None:
        # Filter for breakout topics (marked as "Breakout" or very high %)
        breakouts = rising[rising['value'] >= 1000]  # 1000%+ growth
        return breakouts
    return None

# Example usage
# breakouts = find_breakout_topics('heart health', geo='IN')
# print(breakouts)