---
name: social-media-trends-research
description: "Programmatic trend research using free/low-cost tools: pytrends (Google Trends), Reddit public JSON endpoints, Perplexity MCP (Twitter/TikTok/LinkedIn/Web), YouTube Data API v3 (free tier), arXiv API (academic research acceleration), Indeed RSS (job market signals), yfinance (sector/financial signals), and PatentsView API (patent R&D momentum). Use when finding trending topics, tracking keyword velocity, monitoring Reddit, discovering viral content, spotting academic research acceleration, measuring hiring demand, tracking VC funding, or analyzing patent filing trends. Mostly zero-cost with built-in rate limiting."
---

# Social Media Trends Research

## Overview

Programmatic trend research using three free tools:
- **pytrends**: Google Trends data (velocity, volume, related queries)
- **yars**: Reddit scraping without API keys
- **Perplexity MCP**: Twitter/TikTok/Web trends (via Claude's built-in MCP)

This skill provides executable code for trend research. Use alongside `content-marketing-social-listening` for strategy and `perplexity-search` for deep queries.

## Quick Setup

<!-- ```bash
# Core dependencies (free, no API keys required for most tools)
pip install pytrends requests yfinance --break-system-packages
``` -->

**Optional API keys (free tiers):**
- **YouTube Data API v3**: Free key from [Google Cloud Console](https://console.cloud.google.com) → APIs & Services → YouTube Data API v3. Quota: 10,000 units/day.

No API keys needed for: Google Trends (pytrends), Reddit, arXiv, Indeed RSS, PatentsView patents, yfinance sector ETFs.

---

## Tool 1: pytrends (Google Trends)

### What It Provides
- Real-time trending searches by country
- Interest over time for keywords
- Related queries (rising = velocity indicators)
- Interest by region
- Related topics

### Basic Usage

```python
from pytrends.request import TrendReq
import time

# Initialize (no API key needed)
pytrends = TrendReq(hl='en-US', tz=240)  # tz=240 for Calgary 

# Get real-time trending searches
trending = pytrends.trending_searches(pn='US')
print(trending.head(20))
```

### Research Your Niche Keywords

```python
from pytrends.request import TrendReq
import time

pytrends = TrendReq(hl='en-US', tz=330)

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
```

### Find Viral/Breakout Topics

```python
from pytrends.request import TrendReq
import time

pytrends = TrendReq(hl='en-US', tz=330)

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
breakouts = find_breakout_topics('heart health', geo='IN')
print(breakouts)
```

### Rate Limiting Rules for pytrends

```python
import time

# SAFE: 1 request per 3-5 seconds for casual use
time.sleep(5)

# BULK RESEARCH: 1 request per 60 seconds
time.sleep(60)

# If you get rate limited (429 error): Wait 60-120 seconds, then continue
# If persistent issues: Wait 4-6 hours before resuming
```

### Useful Timeframes

| Timeframe | Use Case |
|-----------|----------|
| `'now 1-H'` | Last hour (real-time spikes) |
| `'now 4-H'` | Last 4 hours |
| `'now 1-d'` | Last 24 hours |
| `'now 7-d'` | Last 7 days (best for trends) |
| `'today 1-m'` | Last 30 days |
| `'today 3-m'` | Last 90 days (velocity analysis) |
| `'today 12-m'` | Last year (seasonal patterns) |

---

## Tool 2: Reddit (No API Keys - Public JSON Endpoints)

### What It Provides
- Search Reddit for any keyword
- Get hot/top/rising posts from subreddits
- Post engagement data (upvotes, comments)
- No authentication required

### Basic Usage

```python
import requests
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Search Reddit for your niche
url = "https://www.reddit.com/search.json?q=heart+health&limit=10&sort=relevance&t=week"
response = requests.get(url, headers=headers, timeout=10)
data = response.json()

# Display results
for child in data.get('data', {}).get('children', []):
    post = child.get('data', {})
    print(f"Title: {post.get('title')}")
    print(f"Subreddit: r/{post.get('subreddit')}")
    print(f"Score: {post.get('score')}")
    print("---")
```

### Get Hot Posts from Specific Subreddits

```python
import requests
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Define subreddits relevant to your niche
subreddits = ['cardiology', 'health', 'medicine']

for sub in subreddits:
    print(f"\n=== Hot in r/{sub} ===")
    try:
        url = f"https://www.reddit.com/r/{sub}/hot.json?limit=10"
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        
        for child in data.get('data', {}).get('children', [])[:5]:
            post = child.get('data', {})
            print(f"- [{post.get('score')}] {post.get('title')[:60]}...")
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(3)  # Rate limiting between requests
```

### Using the Bundled Reddit Scraper

A helper class is included in `scripts/reddit_scraper.py`:

```python
from scripts.reddit_scraper import SimpleRedditScraper

scraper = SimpleRedditScraper()

# Search
results = scraper.search("heart health tips", limit=20)
for post in results['posts']:
    print(f"[{post['score']}] r/{post['subreddit']}: {post['title']}")

# Get subreddit hot posts
results = scraper.get_subreddit("health", sort="hot", limit=10)
for post in results['posts']:
    print(f"[{post['score']}] {post['title']}")
```

### Rate Limiting Rules for Reddit

```python
import time

# SAFE: 1 request per 2-3 seconds
time.sleep(3)

# If you get 429 errors: Wait 5-10 minutes
# Never do more than 60 requests per hour
```

---

## Tool 3: Perplexity MCP (Twitter/TikTok/Web)

Use Claude's built-in Perplexity MCP for platforms you can't scrape directly.

### Query Templates for Trend Research

**Twitter/X Trends:**
```
"What are the most discussed [YOUR NICHE] topics on Twitter/X this week? 
Include specific examples of viral tweets and their engagement."
```

**TikTok Trends (works from India):**
```
"What [YOUR NICHE] content is trending on TikTok right now? 
Include hashtags, view counts, and content formats that are working."
```

**YouTube Trends:**
```
"What [YOUR NICHE] videos are getting the most views on YouTube this week? 
Include channel names, view counts, and video topics."
```

**LinkedIn Professional:**
```
"What [YOUR NICHE] topics are professionals discussing on LinkedIn this week? 
Include examples of high-engagement posts."
```

**General Viral Content:**
```
"What [YOUR NICHE] content has gone viral across social media in the past 7 days? 
Include platform, format, and why it resonated."
```

### Using Perplexity with perplexity-search Skill

If you have the perplexity-search skill installed:

```bash
python scripts/perplexity_search.py \
  "What cardiology topics are trending on Twitter and TikTok this week? Include specific viral posts and hashtags." \
  --model sonar-pro
```

---

## Tool 4: YouTube Trends (YouTube Data API v3)

### What It Provides
- Platform-wide trending videos by category and region
- Search-ranked videos by topic (ordered by view count or recency)
- Channel and engagement signals (views, likes, comments)
- Leading indicator: what topics are generating outsized watch time

### Setup

```python
# Key lives in scripts/config.py — loaded from environment variable YOUTUBE_API_KEY
# Set it once:  $env:YOUTUBE_API_KEY = "your-key-here"  (PowerShell)
#               export YOUTUBE_API_KEY="your-key-here"   (bash)
from scripts.config import YOUTUBE_API_KEY
```

### Get Platform-Wide Trending Videos

```python
import requests
from scripts.config import YOUTUBE_API_KEY

# Common category IDs: 0=all, 22=people&blogs, 24=entertainment, 28=science&tech
def get_youtube_trending(region='US', category_id=0, max_results=20):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        'part': 'snippet,statistics',
        'chart': 'mostPopular',
        'regionCode': region,
        'maxResults': max_results,
        'videoCategoryId': category_id,
        'key': YOUTUBE_API_KEY,
    }
    data = requests.get(url, params=params).json()
    videos = []
    for item in data.get('items', []):
        videos.append({
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'views': int(item['statistics'].get('viewCount', 0)),
            'likes': int(item['statistics'].get('likeCount', 0)),
            'comments': int(item['statistics'].get('commentCount', 0)),
            'published': item['snippet']['publishedAt'][:10],
        })
    return sorted(videos, key=lambda x: x['views'], reverse=True)

# Usage
trending = get_youtube_trending(region='US', category_id=28)  # Science & Tech
for v in trending[:10]:
    print(f"[{v['views']:,} views] {v['title']} — {v['channel']}")
```

### Search by Topic (Velocity Signal)

```python
import requests
from datetime import datetime, timedelta
from scripts.config import YOUTUBE_API_KEY

def search_youtube_topic(query, days_back=30, max_results=25, order='viewCount'):
    """Search YouTube for a topic. order: viewCount, date, relevance, rating"""
    cutoff = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%dT00:00:00Z')
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'order': order,
        'maxResults': max_results,
        'publishedAfter': cutoff,
        'key': YOUTUBE_API_KEY,
    }
    data = requests.get(url, params=params).json()
    videos = []
    for item in data.get('items', []):
        videos.append({
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'published': item['snippet']['publishedAt'][:10],
            'video_id': item['id']['videoId'],
            'url': f"https://youtube.com/watch?v={item['id']['videoId']}",
        })
    return videos

# Usage: find what's getting traction on a topic in the last 30 days
results = search_youtube_topic('AI agents', days_back=30, order='viewCount')
for v in results[:10]:
    print(f"{v['published']} | {v['title']} — {v['channel']}")
    print(f"  {v['url']}")
```

### Rate Limiting for YouTube API

| Operation | Cost (units) | Daily quota (free) |
|-----------|-------------|-------------------|
| videos.list (trending) | 1 | ~10,000 calls |
| search.list | 100 | ~100 searches |
| channels.list | 1 | ~10,000 calls |

> Reserve search calls — they cost 100 units each. Trending video list costs 1 unit.

---

## Tool 5: Academic Research Trends (arXiv)

### What It Provides
- Recent paper submissions by topic (no API key required)
- Research velocity: are paper submissions accelerating?
- Leading indicator for emerging technologies 6–24 months before mainstream
- Author and institution signals (who's publishing = who's investing)

### Search Recent Papers

```python
import requests
import xml.etree.ElementTree as ET
import time
from datetime import datetime, timedelta

def search_arxiv(query, max_results=15, days_back=90):
    """Search arXiv for recent papers. No API key required. Rate limit: 1 req/3s."""
    url = "http://export.arxiv.org/api/query"
    params = {
        'search_query': f'all:{query}',
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
    }
    response = requests.get(url, params=params, timeout=30)
    time.sleep(3)  # Required: arXiv enforces 1 request per 3 seconds

    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    root = ET.fromstring(response.content)
    cutoff = datetime.now() - timedelta(days=days_back)

    papers = []
    for entry in root.findall('atom:entry', ns):
        published = entry.find('atom:published', ns).text
        pub_date = datetime.strptime(published[:10], '%Y-%m-%d')
        if pub_date < cutoff:
            continue
        papers.append({
            'title': entry.find('atom:title', ns).text.strip(),
            'summary': entry.find('atom:summary', ns).text.strip()[:300],
            'published': published[:10],
            'authors': [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)][:3],
            'url': entry.find('atom:id', ns).text,
        })
    return papers

# Usage
papers = search_arxiv('agentic AI', days_back=60)
print(f"Found {len(papers)} papers in last 60 days")
for p in papers[:5]:
    print(f"{p['published']} | {p['title']}")
    print(f"  Authors: {', '.join(p['authors'])}")
    print(f"  {p['url']}")
```

### Measure Research Velocity (Paper Count by Quarter)

```python
import requests
import xml.etree.ElementTree as ET
import time

def count_arxiv_papers_by_year(query, years=3):
    """Count paper submissions per year to detect R&D acceleration."""
    from datetime import datetime
    current_year = datetime.now().year
    counts = {}
    ns = {'opensearch': 'http://a9.com/-/spec/opensearch/1.1/'}

    for yr in range(current_year - years, current_year + 1):
        url = "http://export.arxiv.org/api/query"
        params = {
            'search_query': f'all:{query} AND submittedDate:[{yr}01010000 TO {yr}12312359]',
            'max_results': 0,
        }
        response = requests.get(url, params=params, timeout=30)
        time.sleep(3)
        root = ET.fromstring(response.content)
        total = root.find('opensearch:totalResults', ns)
        counts[yr] = int(total.text) if total is not None else 0

    return counts

# Usage
counts = count_arxiv_papers_by_year('large language model')
for yr, n in counts.items():
    print(f"{yr}: {n:,} papers")
```

---

## Tool 6: Job Market Signals (Indeed RSS)

### What It Provides
- Job posting volume by keyword = real hiring demand signal
- Skill-level demand via Google Trends on "[skill] jobs" queries
- Leading indicator: companies hire ahead of product launches
- Lagging indicator: when everyone's hiring, the market is crowded

### Search Indeed Job Postings (RSS, No Key)

```python
import requests
from xml.etree import ElementTree as ET
import time

def search_indeed_jobs(query, location='', limit=25):
    """
    Pull Indeed job listings via RSS (no API key).
    High posting volume = strong market demand signal.
    """
    url = f"https://www.indeed.com/rss?q={query.replace(' ', '+')}&l={location}&limit={limit}"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; trend-research-bot/1.0)'}
    response = requests.get(url, headers=headers, timeout=15)
    time.sleep(3)

    root = ET.fromstring(response.content)
    channel = root.find('channel')
    jobs = []
    for item in (channel.findall('item') if channel is not None else []):
        jobs.append({
            'title': item.findtext('title', ''),
            'company': item.findtext('{indeed.com}company', 'Unknown'),
            'location': item.findtext('{indeed.com}city', ''),
            'date': item.findtext('pubDate', ''),
            'url': item.findtext('link', ''),
        })
    return jobs

# Usage
jobs = search_indeed_jobs('AI product manager', location='United States')
print(f"Found {len(jobs)} recent job postings")
for j in jobs[:5]:
    print(f"{j['company']} | {j['title']} | {j['location']}")
```

### Compare Skill Demand via Google Trends

```python
from pytrends.request import TrendReq
import time

def compare_skill_demand(skills, period='today 12-m', geo='US'):
    """
    Compare hiring demand for competing skills/technologies.
    Uses search volume for '[skill] jobs' as a proxy for employer demand.
    """
    pytrends = TrendReq(hl='en-US', tz=0)
    job_queries = [f"{s} jobs" for s in skills[:5]]
    pytrends.build_payload(job_queries, timeframe=period, geo=geo)
    time.sleep(5)
    interest = pytrends.interest_over_time()
    if 'isPartial' in interest.columns:
        interest = interest.drop(columns=['isPartial'])
    return interest

# Usage: which ML framework has more hiring momentum?
df = compare_skill_demand(['PyTorch', 'TensorFlow', 'JAX'])
print(df.tail(12))  # Last 12 data points
```

---

## Tool 7: Financial & Funding Signals (yfinance)

### What It Provides
- Sector ETF performance = capital flowing into/out of markets
- Individual stock momentum for public companies in a space
- Volume trends = institutional attention signal
- Funding news via Perplexity MCP (VC rounds, valuations)

### Track Sector ETF Performance

```python
import yfinance as yf
import time

# Common sector ETFs:
# XLK=Tech, XLV=Health, XLF=Finance, XLE=Energy
# ARKK=Innovation, ARKG=Genomics, ARKF=Fintech
# IBB=Biotech, ROBO=Robotics, BOTZ=AI/Automation

def track_sector_momentum(tickers, period='6mo'):
    """
    Compare ETF performance over a period.
    Rising sector ETF = capital inflow = growing market interest.
    """
    results = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=period)
            if hist.empty:
                continue
            start_price = hist['Close'].iloc[0]
            end_price = hist['Close'].iloc[-1]
            avg_volume = hist['Volume'].mean()
            recent_volume = hist['Volume'].iloc[-10:].mean()
            results[ticker] = {
                'return_pct': round(((end_price / start_price) - 1) * 100, 1),
                'current_price': round(end_price, 2),
                'volume_trend': 'rising' if recent_volume > avg_volume * 1.1 else 'flat',
            }
        except Exception as e:
            results[ticker] = {'error': str(e)}
        time.sleep(1)
    return results

# Usage
sectors = track_sector_momentum(['XLK', 'ARKK', 'BOTZ', 'ARKG'], period='6mo')
for ticker, data in sectors.items():
    if 'error' not in data:
        trend = data['volume_trend']
        print(f"{ticker}: {data['return_pct']:+.1f}% | Volume: {trend}")
```

### Get Funding News via Perplexity MCP

Use these prompt templates with Claude's Perplexity MCP for VC/funding intelligence:

**Recent Funding Rounds:**
```
"List recent venture capital funding rounds in [MARKET/SECTOR] from the last 90 days.
For each deal include: company name, amount raised, round type (Seed/A/B/C), lead investor.
Sort by round size descending."
```

**Funding Velocity:**
```
"Compare VC investment activity in [SECTOR] between [YEAR-1] and [YEAR].
Has deal count increased or decreased? Are round sizes growing? What stage is most active?"
```

**Notable Investors:**
```
"Which venture capital firms have made the most investments in [SECTOR] in the past 12 months?
Include deal count and notable portfolio companies."
```

---

## Tool 8: Patent Trend Tracking (PatentsView API)

### What It Provides
- Patent filing counts by topic — R&D investment signal
- Assignee analysis: which companies are investing in R&D
- Filing velocity by year: is innovation accelerating or plateauing?
- No API key required (PatentsView is a USPTO initiative)

### Search Recent Patents

```python
import requests
import time

def search_patents(query, date_from='2022-01-01', max_results=10):
    """
    Search US patents via PatentsView API (no API key required).
    Docs: https://patentsview.org/apis/api-endpoints/patents
    """
    url = "https://api.patentsview.org/patents/query"
    payload = {
        "q": {"_and": [
            {"_text_any": {"patent_title": query}},
            {"_gte": {"patent_date": date_from}},
        ]},
        "f": ["patent_title", "patent_date", "patent_abstract", "assignee_organization"],
        "o": {"sort": [{"patent_date": "desc"}], "per_page": max_results},
    }
    response = requests.post(url, json=payload, timeout=20)
    time.sleep(2)
    data = response.json()
    patents = []
    for patent in data.get('patents') or []:
        assignees = patent.get('assignees') or [{}]
        patents.append({
            'title': patent.get('patent_title', ''),
            'date': patent.get('patent_date', ''),
            'assignee': assignees[0].get('assignee_organization', 'Individual'),
            'abstract': (patent.get('patent_abstract') or '')[:300],
        })
    return patents

# Usage
patents = search_patents('large language model', date_from='2023-01-01')
for p in patents[:5]:
    print(f"{p['date']} | {p['assignee']}")
    print(f"  {p['title']}")
```

### Measure Patent Filing Velocity by Year

```python
import requests
import time

def patent_velocity(query, years_back=4):
    """Count patent filings per year to detect R&D momentum shifts."""
    from datetime import datetime
    current_year = datetime.now().year
    counts = {}

    for yr in range(current_year - years_back, current_year + 1):
        payload = {
            "q": {"_and": [
                {"_text_any": {"patent_title": query}},
                {"_gte": {"patent_date": f"{yr}-01-01"}},
                {"_lte": {"patent_date": f"{yr}-12-31"}},
            ]},
            "f": ["patent_id"],
            "o": {"per_page": 1},
        }
        try:
            r = requests.post("https://api.patentsview.org/patents/query", json=payload, timeout=20)
            data = r.json()
            counts[yr] = data.get('total_patent_count', 0)
        except Exception as e:
            counts[yr] = f"error: {e}"
        time.sleep(2)

    return counts

# Usage: is AI chip patent activity accelerating?
counts = patent_velocity('neural processing unit')
for yr, n in counts.items():
    bar = '█' * min(int(n / 10), 50) if isinstance(n, int) else ''
    print(f"{yr}: {n:>5}  {bar}")
```

### Top Assignees (Who's Investing in R&D)

```python
import requests
import time

def top_patent_assignees(query, date_from='2022-01-01', top_n=10):
    """Find which companies are filing the most patents on a topic."""
    url = "https://api.patentsview.org/assignees/query"
    payload = {
        "q": {"_and": [
            {"_text_any": {"patent_title": query}},
            {"_gte": {"patent_date": date_from}},
        ]},
        "f": ["assignee_organization", "assignee_total_num_patents"],
        "o": {"sort": [{"assignee_total_num_patents": "desc"}], "per_page": top_n},
    }
    response = requests.post(url, json=payload, timeout=20)
    time.sleep(2)
    data = response.json()
    return [
        {'company': a.get('assignee_organization', 'Unknown'),
         'patent_count': a.get('assignee_total_num_patents', 0)}
        for a in (data.get('assignees') or [])
    ]

# Usage
leaders = top_patent_assignees('generative AI', date_from='2023-01-01')
for r in leaders:
    print(f"{r['patent_count']:>5} patents | {r['company']}")
```

---

## Combined Research Workflow

### Complete Trend Research Function

```python
from pytrends.request import TrendReq
import requests
import time
import json
from datetime import datetime

class TrendResearcher:
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=330)
        self.reddit_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def _reddit_request(self, url):
        """Make a Reddit API request."""
        try:
            response = requests.get(url, headers=self.reddit_headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {'error': str(e)}
    
    def research_niche(self, keywords, subreddits=None, geo='IN'):
        """
        Complete trend research for a niche.
        
        Args:
            keywords: List of keywords (max 5)
            subreddits: List of subreddit names to monitor
            geo: Geographic region code
        
        Returns:
            Dictionary with all research data
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'keywords': keywords,
            'google_trends': {},
            'reddit': {},
            'recommendations': []
        }
        
        # 1. Google Trends - Interest Over Time
        print("📊 Fetching Google Trends data...")
        try:
            self.pytrends.build_payload(keywords[:5], timeframe='now 7-d', geo=geo)
            results['google_trends']['interest'] = self.pytrends.interest_over_time().to_dict()
            time.sleep(5)
            
            # Related queries (rising topics)
            related = self.pytrends.related_queries()
            results['google_trends']['rising_queries'] = {}
            for kw in keywords[:5]:
                rising = related[kw]['rising']
                if rising is not None:
                    results['google_trends']['rising_queries'][kw] = rising.head(10).to_dict()
            time.sleep(5)
        except Exception as e:
            results['google_trends']['error'] = str(e)
        
        # 2. Reddit Research
        print("👽 Fetching Reddit discussions...")
        if subreddits:
            for sub in subreddits[:5]:
                try:
                    url = f"https://www.reddit.com/r/{sub}/hot.json?limit=10"
                    data = self._reddit_request(url)
                    posts = []
                    for child in data.get('data', {}).get('children', [])[:5]:
                        post = child.get('data', {})
                        posts.append({
                            'title': post.get('title', ''),
                            'score': post.get('score', 0),
                            'comments': post.get('num_comments', 0)
                        })
                    results['reddit'][sub] = posts
                    time.sleep(3)
                except Exception as e:
                    results['reddit'][sub] = {'error': str(e)}
        
        # 3. Keyword search on Reddit
        print("🔍 Searching Reddit for keywords...")
        for kw in keywords[:3]:
            try:
                url = f"https://www.reddit.com/search.json?q={kw}&limit=10&sort=relevance&t=week"
                data = self._reddit_request(url)
                posts = []
                for child in data.get('data', {}).get('children', [])[:5]:
                    post = child.get('data', {})
                    posts.append({
                        'title': post.get('title', ''),
                        'subreddit': post.get('subreddit', ''),
                        'score': post.get('score', 0),
                        'comments': post.get('num_comments', 0)
                    })
                results['reddit'][f'search_{kw}'] = posts
                time.sleep(3)
            except Exception as e:
                results['reddit'][f'search_{kw}'] = {'error': str(e)}
        
        # 4. Generate recommendations
        results['recommendations'] = self._generate_recommendations(results)
        
        return results
    
    def _generate_recommendations(self, data):
        """Generate content recommendations from research data"""
        recommendations = []
        
        # From rising queries
        rising = data.get('google_trends', {}).get('rising_queries', {})
        for kw, queries in rising.items():
            if isinstance(queries, dict) and 'query' in queries:
                for query in list(queries['query'].values())[:3]:
                    recommendations.append({
                        'source': 'Google Trends',
                        'topic': query,
                        'reason': f"Rising search term related to '{kw}'"
                    })
        
        # From Reddit hot posts
        for sub, posts in data.get('reddit', {}).items():
            if isinstance(posts, list):
                for post in posts[:2]:
                    if post.get('score', 0) > 50:
                        recommendations.append({
                            'source': f'Reddit r/{sub}',
                            'topic': post.get('title', ''),
                            'reason': f"High engagement ({post.get('score')} upvotes)"
                        })
        
        return recommendations

# Usage Example
if __name__ == "__main__":
    researcher = TrendResearcher()
    
    results = researcher.research_niche(
        keywords=['heart health', 'cardiology', 'cholesterol'],
        subreddits=['cardiology', 'health', 'medicine'],
        geo='IN'
    )
    
    # Save results
    with open('trend_research.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    # Print recommendations
    print("\n🎯 CONTENT RECOMMENDATIONS:")
    for rec in results['recommendations']:
        print(f"- [{rec['source']}] {rec['topic']}")
        print(f"  Why: {rec['reason']}")
```

---

## Quick Reference Commands

### Daily Trend Check (5 minutes)

```python
from pytrends.request import TrendReq
import requests
import time

# Quick Google Trends check
pytrends = TrendReq(hl='en-US', tz=330)
pytrends.build_payload(['your keyword'], timeframe='now 1-d')
print(pytrends.related_queries()['your keyword']['rising'])

time.sleep(5)

# Quick Reddit check  
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
url = "https://www.reddit.com/search.json?q=your+keyword&limit=10&t=day"
response = requests.get(url, headers=headers, timeout=10)
data = response.json()
for child in data.get('data', {}).get('children', [])[:5]:
    post = child.get('data', {})
    print(f"[{post.get('score')}] {post.get('title')}")
```

### Weekly Deep Dive

```python
# Use the TrendResearcher class above with:
# - 5 core keywords
# - 5 relevant subreddits
# - 90-day timeframe for velocity analysis

# Then use Perplexity MCP for:
# - Twitter trends in your niche
# - TikTok viral content
# - YouTube trending videos
# - LinkedIn discussions
```

---

## Integration with Writing Skills

After research, pass findings to your writing skills:

```
1. Run trend research (this skill)
2. Identify top 3-5 opportunities
3. Use content-marketing-social-listening for strategy
4. Use cardiology-content-repurposer or similar for content creation
5. Use authentic-voice for final polish
```

---

## Troubleshooting

### pytrends Issues

| Error | Solution |
|-------|----------|
| 429 Too Many Requests | Wait 60 seconds, then increase sleep time |
| Empty results | Check if keyword has search volume |
| Connection error | Check internet, retry in 5 minutes |

### Reddit Issues

| Error | Solution |
|-------|----------|
| 429 Rate Limited | Wait 10 minutes |
| Subreddit not found | Check subreddit name spelling |
| Empty results | Subreddit may be private or quarantined |
| Connection timeout | Increase timeout, check internet |

---

## Best Practices

1. **Always use rate limiting**: Sleep between requests
2. **Research in batches**: Do weekly deep dives, not constant polling
3. **Save results**: Cache research data locally
4. **Cross-reference**: Validate trends across multiple platforms
5. **Act fast**: Viral windows are short (24-72 hours)

---

## Platform Coverage Summary

| Platform | Tool | Cost | API Key? |
|----------|------|------|----------|
| Google Trends | pytrends | Free | No |
| Reddit | requests (public JSON) | Free | No |
| Twitter/X | Perplexity MCP | Free† | No |
| TikTok | Perplexity MCP | Free† | No |
| YouTube (trending) | Perplexity MCP | Free† | No |
| YouTube (programmatic) | YouTube Data API v3 | Free (10k units/day) | Yes — Google Cloud |
| LinkedIn | Perplexity MCP | Free† | No |
| Academic research | arXiv API | Free | No |
| Job market | Indeed RSS + pytrends | Free | No |
| Sector/stock signals | yfinance | Free | No |
| VC/funding news | Perplexity MCP | Free† | No |
| Patents | PatentsView API | Free | No |

†Uses Claude's built-in Perplexity MCP or OpenRouter credits if using perplexity-search skill

---

## Bundled Resources

- `scripts/trend_research.py`: Main CLI tool for complete trend research
- `scripts/reddit_scraper.py`: Simple Reddit scraper class (no API keys)
