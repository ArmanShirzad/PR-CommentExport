# PR-CommentExport

A Python tool to export pull request comments from Azure DevOps repositories. This tool helps developers and teams to easily extract and save PR comments for documentation, analysis, or archival purposes.

## Features

- Export pull request comments from Azure DevOps repositories
- Save comments to text files with proper formatting
- Configurable through environment variables
- Easy to set up and use

## Prerequisites

- Python 3.6 or higher
- Azure DevOps access token
- Azure DevOps organization and project details

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

Edit the `.env` file with your Azure DevOps details:

```env
AZURE_DEVOPS_PAT=your_personal_access_token
AZURE_DEVOPS_ORG=your_organization
AZURE_DEVOPS_PROJECT=your_project
```

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