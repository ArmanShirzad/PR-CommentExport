import os
from datetime import datetime
import requests
from load_config import *  # This will load our configuration

# GitHub API details
token = os.environ.get('GITHUB_TOKEN')
repo_owner = os.environ.get('GITHUB_REPO_OWNER')
repo_name = os.environ.get('GITHUB_REPO_NAME')
pr_number = os.environ.get('GITHUB_PR_NUMBER')

if not all([token, repo_owner, repo_name, pr_number]):
    raise ValueError("Missing required environment variables. Please check your configuration.")

base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github-commitcomment.full+json"  # Get full comment details
}

def fetch_all_pages(url, params=None):
    """Fetch all pages of results using GitHub's pagination"""
    if params is None:
        params = {}
    
    all_results = []
    page = 1
    
    while True:
        params['page'] = page
        params['per_page'] = 100  # Maximum items per page
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            print(response.json())
            break
            
        results = response.json()
        if not results:  # No more results
            break
            
        all_results.extend(results)
        page += 1
    
    return all_results

# Fetch all types of comments with sorting and direction
params = {
    'sort': 'created',
    'direction': 'asc',
    # 'since': '2024-01-01T00:00:00Z'  # Uncomment and modify to filter by date
}

# Fetch all types of comments
review_comments = fetch_all_pages(f"{base_url}/pulls/{pr_number}/comments", params)  # Review comments
issue_comments = fetch_all_pages(f"{base_url}/issues/{pr_number}/comments", params)  # General PR comments
reviews = fetch_all_pages(f"{base_url}/pulls/{pr_number}/reviews", params)  # Review threads

# Combine and format all comments
all_comments = []

# Process review comments (comments on specific lines)
for comment in review_comments:
    all_comments.append({
        'type': 'Review Comment',
        'body': comment['body'],
        'body_html': comment.get('body_html', 'N/A'),
        'path': comment.get('path', 'N/A'),
        'line': comment.get('line', 'N/A'),
        'created_at': datetime.strptime(comment['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
        'user': comment['user']['login']
    })

# Process general PR comments
for comment in issue_comments:
    all_comments.append({
        'type': 'PR Comment',
        'body': comment['body'],
        'body_html': comment.get('body_html', 'N/A'),
        'path': 'N/A',
        'line': 'N/A',
        'created_at': datetime.strptime(comment['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
        'user': comment['user']['login']
    })

# Process review threads
for review in reviews:
    if review.get('body'):  # Only include if there's a comment body
        all_comments.append({
            'type': 'Review',
            'body': review['body'],
            'body_html': review.get('body_html', 'N/A'),
            'path': 'N/A',
            'line': 'N/A',
            'created_at': datetime.strptime(review['submitted_at'], '%Y-%m-%dT%H:%M:%SZ'),
            'user': review['user']['login']
        })

# Sort all comments by creation time
all_comments.sort(key=lambda x: x['created_at'])

# Export to plain text
with open("all_pr_comments.txt", "w", encoding="utf-8") as file:
    for index, comment in enumerate(all_comments, 1):
        file.write(f"{index}. ")
        if comment['path'] != 'N/A':
            file.write(f"File: {comment['path']} (Line: {comment['line']})\n")
        else:
            file.write("File: General PR Comment\n")
        file.write(f"   Time: {comment['created_at'].strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"   Comment: {comment['body']}\n")
        file.write("---\n")

print("All comments exported to all_pr_comments.txt")