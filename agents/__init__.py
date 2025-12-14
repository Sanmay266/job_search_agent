"""
Job Search Agent - Intelligent job search automation system
"""

__version__ = '0.1.0'

from agents.job_search_agent import JobSearchAgent, JobOpportunity, SearchResult
from agents.jd_agent import JDAnalyzer
from agents.resume_agent import ResumeAgent
from agents.message_agent import MessageAgent

__all__ = [
    'JobSearchAgent',
    'JobOpportunity',
    'SearchResult',
    'JDAnalyzer',
    'ResumeAgent',
    'MessageAgent',
]
