"""
Resume Agent - Tailors resumes for specific job opportunities
"""
from typing import List, Dict, Optional
from datetime import datetime


class ResumeAgent:
    """Manages resume tailoring and optimization for job applications"""
    
    def __init__(self, user_profile: Dict):
        """
        Initialize resume agent
        
        Args:
            user_profile: User's profile containing resume data
        """
        self.user_profile = user_profile
        self.base_resume = user_profile.get('resume', {})
    
    def tailor_resume(self, job, matched_skills: List[str]) -> Dict:
        """
        Tailor resume for a specific job
        
        Args:
            job: JobOpportunity object
            matched_skills: Skills that match the job
            
        Returns:
            Tailored resume dictionary
        """
        tailored = {
            'header': self._create_header(),
            'summary': self._create_summary(job, matched_skills),
            'skills': self._prioritize_skills(matched_skills),
            'experience': self._tailor_experience(job, matched_skills),
            'education': self.base_resume.get('education', []),
            'certifications': self._relevant_certifications(matched_skills),
        }
        
        return tailored
    
    def _create_header(self) -> Dict:
        """Create resume header with contact info"""
        return {
            'name': self.user_profile.get('name', 'Your Name'),
            'email': self.user_profile.get('email', '[email]'),
            'phone': self.user_profile.get('phone', '[phone]'),
            'location': self.user_profile.get('location', ''),
            'linkedin': self.user_profile.get('linkedin', ''),
            'portfolio': self.user_profile.get('portfolio', ''),
        }
    
    def _create_summary(self, job, matched_skills: List[str]) -> str:
        """
        Create a tailored professional summary
        
        Args:
            job: Target job
            matched_skills: Matched skills
            
        Returns:
            Professional summary text
        """
        skills_str = ', '.join(matched_skills[:3])
        
        summary = (
            f"Results-driven professional with expertise in {skills_str}. "
            f"Seeking {job.title} position to leverage technical skills and "
            f"contribute to {job.company}'s success."
        )
        
        return summary
    
    def _prioritize_skills(self, matched_skills: List[str]) -> List[str]:
        """
        Prioritize skills based on job match
        
        Args:
            matched_skills: Skills that matched the job
            
        Returns:
            Prioritized skill list
        """
        # Put matched skills first, then other skills
        all_skills = self.base_resume.get('skills', [])
        
        # Sort: matched skills first, then others
        prioritized = []
        for skill in matched_skills:
            if skill in all_skills:
                prioritized.append(skill)
        
        # Add remaining skills
        for skill in all_skills:
            if skill not in prioritized:
                prioritized.append(skill)
        
        return prioritized[:10]  # Top 10 skills
    
    def _tailor_experience(self, job, matched_skills: List[str]) -> List[Dict]:
        """
        Tailor experience section to highlight relevant achievements
        
        Args:
            job: Target job
            matched_skills: Matched skills
            
        Returns:
            List of tailored experience entries
        """
        experiences = self.base_resume.get('experience', [])
        tailored_exp = []
        
        for exp in experiences:
            tailored_entry = {
                'company': exp.get('company'),
                'title': exp.get('title'),
                'duration': exp.get('duration'),
                'achievements': self._filter_achievements(
                    exp.get('achievements', []),
                    matched_skills
                )
            }
            tailored_exp.append(tailored_entry)
        
        return tailored_exp
    
    def _filter_achievements(self, achievements: List[str], matched_skills: List[str]) -> List[str]:
        """
        Filter achievements to highlight those relevant to matched skills
        
        Args:
            achievements: List of achievements
            matched_skills: Skills to highlight
            
        Returns:
            Filtered and prioritized achievements
        """
        scored_achievements = []
        
        for achievement in achievements:
            score = 0
            achievement_lower = achievement.lower()
            
            # Score based on skill mentions
            for skill in matched_skills:
                if skill.lower() in achievement_lower:
                    score += 1
            
            scored_achievements.append((achievement, score))
        
        # Sort by score (descending) and return top achievements
        scored_achievements.sort(key=lambda x: x[1], reverse=True)
        return [ach for ach, _ in scored_achievements[:5]]
    
    def _relevant_certifications(self, matched_skills: List[str]) -> List[Dict]:
        """
        Filter certifications relevant to matched skills
        
        Args:
            matched_skills: Skills to match against
            
        Returns:
            List of relevant certifications
        """
        all_certs = self.base_resume.get('certifications', [])
        relevant = []
        
        for cert in all_certs:
            cert_name = cert.get('name', '').lower()
            for skill in matched_skills:
                if skill.lower() in cert_name:
                    relevant.append(cert)
                    break
        
        return relevant
    
    def optimize_for_ats(self, resume: Dict) -> Dict:
        """
        Optimize resume for Applicant Tracking Systems (ATS)
        
        Args:
            resume: Resume dictionary
            
        Returns:
            ATS-optimized resume
        """
        optimized = resume.copy()
        
        # Flatten structure for ATS compatibility
        optimized['ats_text'] = self._generate_ats_text(resume)
        
        # Add keywords for ATS scanning
        optimized['keywords'] = self._extract_keywords(resume)
        
        return optimized
    
    def _generate_ats_text(self, resume: Dict) -> str:
        """Generate plain text version for ATS"""
        text_parts = []
        
        # Header
        header = resume.get('header', {})
        text_parts.append(f"{header.get('name', '')}")
        text_parts.append(f"{header.get('email', '')} | {header.get('phone', '')}")
        
        # Summary
        if resume.get('summary'):
            text_parts.append(f"\nPROFESSIONAL SUMMARY\n{resume['summary']}")
        
        # Skills
        if resume.get('skills'):
            text_parts.append(f"\nSKILLS\n{', '.join(resume['skills'])}")
        
        # Experience
        if resume.get('experience'):
            text_parts.append("\nEXPERIENCE")
            for exp in resume['experience']:
                text_parts.append(f"{exp.get('title')} at {exp.get('company')}")
                for achievement in exp.get('achievements', []):
                    text_parts.append(f"- {achievement}")
        
        return '\n'.join(text_parts)
    
    def _extract_keywords(self, resume: Dict) -> List[str]:
        """Extract keywords from resume for ATS"""
        keywords = set()
        
        # Add skills
        keywords.update(resume.get('skills', []))
        
        # Add certifications
        for cert in resume.get('certifications', []):
            keywords.add(cert.get('name', ''))
        
        return list(keywords)
