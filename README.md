# PR-CommentExport

A Python tool to export pull request comments from github repositories. This tool helps developers and teams to easily extract and save PR comments for documentation, analysis, or archival purposes.

## Features

- Export pull request comments from github repositories
- Save comments to text files with proper formatting
- Configurable through environment variables
- Easy to set up and use

## Prerequisites

- Python 3.6 or higher
- GitHub access token with repo permissions
- GitHub repository details

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/PR-CommentExport.git
cd PR-CommentExport
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and configure your settings:
```bash
cp .env.example .env
```

## Configuration

Edit the `.env` file with your GitHub details:

```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_REPO_OWNER=owner_username
GITHUB_REPO_NAME=repository_name
GITHUB_PR_NUMBER=pull_request_number
```

These environment variables are required:
- `GITHUB_TOKEN`: Your GitHub Personal Access Token with repo access
- `GITHUB_REPO_OWNER`: The owner/organization of the repository
- `GITHUB_REPO_NAME`: The name of the repository
- `GITHUB_PR_NUMBER`: The number of the pull request to export comments from

## Usage

Run the main script:

```bash
python export.py
```

The script will export all PR comments to a text file in the current directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
