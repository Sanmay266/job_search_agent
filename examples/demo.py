"""
Demo script showing how to use the Job Search Agent system
"""
import sys
import os

# Add parent directory to path to import agents
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.job_search_agent import JobSearchAgent, JobOpportunity


def main():
    print("=" * 60)
    print("Job Search Agent Demo")
    print("=" * 60)
    
    # Sample user profile
    user_profile = {
        'name': 'Jane Developer',
        'email': 'jane.dev@example.com',
        'phone': '+1-555-0123',
        'location': 'San Francisco, CA',
        'linkedin': 'https://linkedin.com/in/janedev',
        'skills': [
            'Python', 'JavaScript', 'SQL', 'AWS', 'Docker',
            'React', 'FastAPI', 'PostgreSQL', 'Git', 'CI/CD'
        ],
        'resume': {
            'experience': [
                {
                    'company': 'Tech Innovations Inc',
                    'title': 'Senior Software Engineer',
                    'duration': '2020 - Present',
                    'achievements': [
                        'Built scalable microservices using Python and FastAPI serving 1M+ users',
                        'Reduced API response time by 40% through database optimization',
                        'Led team of 3 engineers on critical project delivery',
                        'Implemented CI/CD pipeline using GitHub Actions and Docker'
                    ]
                },
                {
                    'company': 'Startup Solutions',
                    'title': 'Full Stack Developer',
                    'duration': '2018 - 2020',
                    'achievements': [
                        'Developed responsive web applications using React and Node.js',
                        'Designed and implemented RESTful APIs with PostgreSQL backend',
                        'Reduced deployment time by 60% through automation'
                    ]
                }
            ],
            'education': [
                {
                    'degree': 'Bachelor of Science in Computer Science',
                    'institution': 'State University',
                    'year': '2018'
                }
            ],
            'certifications': [
                {
                    'name': 'AWS Certified Developer - Associate',
                    'issuer': 'Amazon Web Services',
                    'year': '2022'
                }
            ]
        }
    }
    
    # Initialize the agent
    print("\n1. Initializing Job Search Agent...")
    agent = JobSearchAgent(user_profile)
    print("✓ Agent initialized")
    
    # Sample job opportunity
    job = JobOpportunity(
        job_id='JOB-12345',
        title='Senior Python Developer',
        company='Amazing Tech Co',
        description="""
        We are looking for a Senior Python Developer with 3+ years of experience.
        
        Requirements:
        - Strong Python programming skills
        - Experience with FastAPI or Django
        - Knowledge of SQL databases (PostgreSQL preferred)
        - AWS cloud experience
        - Docker and containerization
        - CI/CD pipeline experience
        - Strong problem-solving and communication skills
        
        Nice to have:
        - React or frontend experience
        - Kubernetes knowledge
        - Machine learning background
        """,
        requirements=['Python', 'FastAPI', 'SQL', 'AWS', 'Docker', 'CI/CD'],
        salary_range='$120,000 - $160,000',
        location='San Francisco, CA (Hybrid)',
        url='https://example.com/jobs/12345'
    )
    
    print(f"\n2. Analyzing Job: {job.title} at {job.company}")
    print("-" * 60)
    
    # Evaluate job fit
    print("\n3. Evaluating job fit...")
    result = agent.evaluate_job_fit(job)
    
    print(f"\n✓ Match Score: {result.match_score:.0%}")
    print(f"✓ Recommendation: {result.recommendation}")
    
    print(f"\n✓ Matched Skills ({len(result.matched_skills)}):")
    for skill in result.matched_skills:
        print(f"  • {skill}")
    
    if result.missing_skills:
        print(f"\n⚠ Missing Skills ({len(result.missing_skills)}):")
        for skill in result.missing_skills[:3]:
            print(f"  • {skill}")
    
    # Prepare application materials
    print("\n4. Preparing application materials...")
    application = agent.prepare_application(job, result)
    
    print("\n✓ Tailored Resume Generated")
    print(f"  • Summary: {application['resume']['summary'][:100]}...")
    print(f"  • Top Skills: {', '.join(application['resume']['skills'][:5])}")
    
    print("\n✓ Cover Letter Generated")
    print("-" * 60)
    print(application['cover_letter'])
    print("-" * 60)
    
    # Show statistics
    print("\n5. Search Statistics")
    stats = agent.get_search_stats()
    print(f"  • Total Applications: {stats['total_applications']}")
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Copy config.example.json to config.json")
    print("2. Update config.json with your information")
    print("3. Integrate with job board APIs")
    print("4. Start applying to jobs!")


if __name__ == '__main__':
    main()
