"""
Main Job Search Agent - Orchestrates the job search process
"""
from typing import Optional, Dict, List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class JobOpportunity:
    """Represents a job opportunity"""
    job_id: str
    title: str
    company: str
    description: str
    requirements: List[str]
    salary_range: Optional[str] = None
    location: Optional[str] = None
    posted_date: Optional[str] = None
    url: Optional[str] = None


@dataclass
class SearchResult:
    """Result of a job search operation"""
    job: JobOpportunity
    match_score: float
    matched_skills: List[str]
    missing_skills: List[str]
    recommendation: str


class JobSearchAgent:
    """Main agent for orchestrating job search operations"""
    
    def __init__(self, user_profile: Dict):
        """
        Initialize the job search agent
        
        Args:
            user_profile: Dictionary containing user's skills, experience, preferences
        """
        self.user_profile = user_profile
        self.search_history = []
        self.applications = []
        
    def search_jobs(self, query: str, filters: Optional[Dict] = None) -> List[JobOpportunity]:
        """
        Search for jobs based on query and filters
        
        Args:
            query: Search query (e.g., "Python Developer")
            filters: Optional filters (location, salary range, experience level)
            
        Returns:
            List of job opportunities
        """
        # This would integrate with job APIs (LinkedIn, Indeed, etc.)
        jobs = self._fetch_jobs(query, filters)
        self.search_history.append({
            'query': query,
            'filters': filters,
            'timestamp': datetime.now(),
            'results_count': len(jobs)
        })
        return jobs
    
    def evaluate_job_fit(self, job: JobOpportunity) -> SearchResult:
        """
        Evaluate how well a job matches the user's profile
        
        Args:
            job: Job opportunity to evaluate
            
        Returns:
            SearchResult with match score and recommendations
        """
        from agents.jd_agent import JDAnalyzer
        
        analyzer = JDAnalyzer()
        match_score, matched_skills, missing_skills = analyzer.analyze(
            job.description,
            self.user_profile.get('skills', [])
        )
        
        recommendation = self._generate_recommendation(
            match_score, missing_skills
        )
        
        return SearchResult(
            job=job,
            match_score=match_score,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            recommendation=recommendation
        )
    
    def prepare_application(self, job: JobOpportunity, result: SearchResult) -> Dict:
        """
        Prepare application materials for a job
        
        Args:
            job: Target job
            result: Evaluation result
            
        Returns:
            Dictionary with resume and cover letter
        """
        from agents.resume_agent import ResumeAgent
        from agents.message_agent import MessageAgent
        
        resume_agent = ResumeAgent(self.user_profile)
        message_agent = MessageAgent()
        
        tailored_resume = resume_agent.tailor_resume(job, result.matched_skills)
        cover_letter = message_agent.generate_cover_letter(job, result)
        
        application = {
            'job': job,
            'resume': tailored_resume,
            'cover_letter': cover_letter,
            'prepared_at': datetime.now()
        }
        
        self.applications.append(application)
        return application
    
    def _fetch_jobs(self, query: str, filters: Optional[Dict] = None) -> List[JobOpportunity]:
        """Fetch jobs from external APIs"""
        # Placeholder for API integration
        return []
    
    def _generate_recommendation(self, match_score: float, missing_skills: List[str]) -> str:
        """Generate recommendation based on match score"""
        if match_score >= 0.8:
            return "Excellent fit - Apply immediately"
        elif match_score >= 0.6:
            return "Good fit - Consider applying"
        elif missing_skills:
            return f"Moderate fit - Consider learning: {', '.join(missing_skills[:2])}"
        else:
            return "Not a strong match at this time"
    
    def get_search_stats(self) -> Dict:
        """Get statistics about search activity"""
        return {
            'total_searches': len(self.search_history),
            'total_applications': len(self.applications),
            'search_history': self.search_history
        }
