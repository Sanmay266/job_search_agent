# Job Search Agent

An intelligent job search automation system that helps you find, analyze, and apply to job opportunities with AI-powered matching and personalized application materials.

## Features

- **Smart Job Matching**: Analyzes job descriptions and matches them against your skills
- **Resume Tailoring**: Automatically customizes your resume for each job application
- **Cover Letter Generation**: Creates personalized cover letters highlighting relevant experience
- **ATS Optimization**: Ensures your application materials pass Applicant Tracking Systems
- **Application Tracking**: Keeps track of your job search history and applications

## Project Structure

```
job-search-agent/
├── agents/
│   ├── job_search_agent.py    # Main orchestrator
│   ├── jd_agent.py             # Job description analyzer
│   ├── resume_agent.py         # Resume tailoring
│   └── message_agent.py        # Cover letter & communications
├── examples/
│   └── demo.py                 # Usage examples
├── config.example.json         # Configuration template
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/job-search-agent.git
cd job-search-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your configuration:
```bash
cp config.example.json config.json
# Edit config.json with your information
```

## Quick Start

```python
from agents.job_search_agent import JobSearchAgent, JobOpportunity

# Set up your profile
user_profile = {
    'name': 'Your Name',
    'email': 'your.email@example.com',
    'skills': ['Python', 'JavaScript', 'SQL', 'AWS'],
    'experience': [
        {
            'company': 'Tech Corp',
            'title': 'Software Engineer',
            'duration': '2020-2023',
            'achievements': [
                'Built scalable APIs using Python and FastAPI',
                'Reduced database query time by 40%'
            ]
        }
    ]
}

# Initialize the agent
agent = JobSearchAgent(user_profile)

# Create a job opportunity
job = JobOpportunity(
    job_id='123',
    title='Senior Python Developer',
    company='Amazing Tech Co',
    description='Looking for a Python developer with 3+ years experience...',
    requirements=['Python', 'AWS', 'SQL']
)

# Evaluate the job fit
result = agent.evaluate_job_fit(job)
print(f"Match Score: {result.match_score:.0%}")
print(f"Matched Skills: {result.matched_skills}")

# Prepare application materials
application = agent.prepare_application(job, result)
print(application['cover_letter'])
```

## Usage Examples

See `examples/demo.py` for complete usage examples including:
- Job search and filtering
- Skill matching and gap analysis
- Resume tailoring
- Cover letter generation
- Follow-up messages

## Configuration

Create a `config.json` file based on `config.example.json`:

```json
{
  "user_profile": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "skills": ["Python", "JavaScript", "SQL"],
    "resume": { ... }
  }
}
```

## Roadmap

- [ ] Integration with job board APIs (LinkedIn, Indeed, Glassdoor)
- [ ] Web interface for easier interaction
- [ ] Database persistence for application tracking
- [ ] Email automation for sending applications
- [ ] Interview preparation assistance
- [ ] Salary negotiation guidance

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Disclaimer

This tool is designed to assist with job searching and application preparation. Always review and customize generated materials before submitting applications.
