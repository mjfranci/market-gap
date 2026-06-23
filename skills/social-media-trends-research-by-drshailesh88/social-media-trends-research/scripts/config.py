import os

# YouTube Data API v3
# Get a free key at: https://console.cloud.google.com → APIs & Services → YouTube Data API v3
# Set it once in your shell:
#   Mac/Linux: export YOUTUBE_API_KEY="your-key-here"
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")
