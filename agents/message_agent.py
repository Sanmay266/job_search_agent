"""
Message Agent - Generates cover letters and application communications
"""
from typing import Dict, Optional
from datetime import datetime


class MessageAgent:
    """Generates personalized cover letters and application messages"""
    
    def generate_cover_letter(self, job, evaluation_result) -> str:
        """
        Generate a tailored cover letter
        
        Args:
            job: JobOpportunity object
            evaluation_result: SearchResult from job evaluation
            
        Returns:
            Cover letter text
        """
        cover_letter = f"""Dear Hiring Manager,

I am writing to express my strong interest in the {job.title} position at {job.company}. 
With my background in {', '.join(evaluation_result.matched_skills[:2])}, I am confident 
in my ability to contribute meaningfully to your team.

RELEVANT EXPERIENCE & SKILLS
{self._format_matched_skills(evaluation_result.matched_skills)}

WHY I'M A GREAT FIT
{self._generate_fit_statement(job, evaluation_result)}

GROWTH OPPORTUNITIES
{self._generate_growth_statement(evaluation_result.missing_skills)}

I am excited about the opportunity to bring my expertise to {job.company} and would welcome 
the chance to discuss how I can contribute to your team's success. Thank you for considering 
my application.

Best regards,
[Your Name]
"""
        return cover_letter
    
    def _format_matched_skills(self, matched_skills) -> str:
        """Format matched skills for cover letter"""
        if not matched_skills:
            return "• Strong technical foundation across multiple domains"
        
        formatted = []
        for skill in matched_skills[:5]:
            formatted.append(f"• {skill.title()}")
        
        return '\n'.join(formatted)
    
    def _generate_fit_statement(self, job, result) -> str:
        """Generate statement about why candidate is a good fit"""
        match_percentage = int(result.match_score * 100)
        
        if result.match_score >= 0.8:
            return (
                f"My skills align closely ({match_percentage}% match) with your requirements. "
                f"I have demonstrated expertise in the key technologies and methodologies "
                f"your team uses, and I'm ready to make an immediate impact."
            )
        elif result.match_score >= 0.6:
            return (
                f"While I have {match_percentage}% of the required skills, I'm a quick learner "
                f"with a proven track record of rapidly acquiring new technologies. "
                f"My foundational knowledge will allow me to contribute effectively from day one."
            )
        else:
            return (
                f"I bring {match_percentage}% of the required skills and am genuinely interested "
                f"in developing the additional expertise needed for this role. "
                f"I'm committed to continuous learning and growth."
            )
    
    def _generate_growth_statement(self, missing_skills) -> str:
        """Generate statement about willingness to learn missing skills"""
        if not missing_skills:
            return "I'm eager to deepen my expertise and take on new challenges in this role."
        
        skills_to_learn = ', '.join(missing_skills[:2])
        return (
            f"I'm particularly interested in expanding my knowledge of {skills_to_learn}. "
            f"I'm committed to continuous professional development and am confident in my "
            f"ability to quickly master these areas."
        )
    
    def generate_follow_up_message(self, job, days_since_application: int = 7) -> str:
        """
        Generate a follow-up message after application
        
        Args:
            job: JobOpportunity object
            days_since_application: Days since initial application
            
        Returns:
            Follow-up message text
        """
        message = f"""Hi there,

I wanted to follow up on my application for the {job.title} position at {job.company}, 
which I submitted {days_since_application} days ago.

I remain very interested in this opportunity and would love to discuss how my skills 
and experience align with your team's needs. I'm happy to provide any additional 
information or clarification you might need.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
        return message
    
    def generate_rejection_response(self, job, reason: Optional[str] = None) -> str:
        """
        Generate a professional response to rejection
        
        Args:
            job: JobOpportunity object
            reason: Optional reason for rejection
            
        Returns:
            Response message
        """
        message = f"""Thank you for considering my application for the {job.title} position 
at {job.company}. While I'm disappointed not to move forward at this time, I appreciate 
the opportunity to learn more about your organization.

I remain interested in {job.company} and would welcome the opportunity to stay connected 
for future positions that align with my skills and experience.

Best regards,
[Your Name]
"""
        return message
    
    def generate_acceptance_response(self, job, offer_details: Optional[Dict] = None) -> str:
        """
        Generate acceptance message for job offer
        
        Args:
            job: JobOpportunity object
            offer_details: Optional details about the offer
            
        Returns:
            Acceptance message
        """
        message = f"""Thank you for the wonderful opportunity to join {job.company} as a 
{job.title}. I'm thrilled to accept this position and am excited to contribute to your team.

I look forward to starting on [start date] and to making a positive impact from day one. 
Please let me know if you need any additional information from me before my start date.

Best regards,
[Your Name]
"""
        return message
    
    def generate_email_subject_lines(self, job) -> list:
        """
        Generate multiple subject line options for application email
        
        Args:
            job: JobOpportunity object
            
        Returns:
            List of subject line options
        """
        return [
            f"Application for {job.title} Position",
            f"Experienced Professional Interested in {job.title} Role at {job.company}",
            f"{job.title} Application - [Your Name]",
            f"Interested in {job.title} Opportunity at {job.company}",
        ]
    
    def generate_linkedin_message(self, job, recruiter_name: str) -> str:
        """
        Generate a LinkedIn message to recruiter
        
        Args:
            job: JobOpportunity object
            recruiter_name: Name of recruiter
            
        Returns:
            LinkedIn message
        """
        message = f"""Hi {recruiter_name},

I came across the {job.title} position at {job.company} and was impressed by the role 
and your company's mission. I believe my background aligns well with what you're looking for.

I'd love to learn more about this opportunity and discuss how I can contribute to your team. 
Feel free to reach out if you'd like to connect.

Looking forward to hearing from you!
"""
        return message
