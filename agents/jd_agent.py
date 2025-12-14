"""
Job Description Analyzer - Analyzes job descriptions and matches skills
"""
from typing import List, Tuple
import re
from collections import Counter


class JDAnalyzer:
    """Analyzes job descriptions to extract requirements and match skills"""
    
    # Common skill keywords by category
    SKILL_KEYWORDS = {
        'python': ['python', 'py', 'django', 'flask', 'fastapi', 'pandas', 'numpy'],
        'javascript': ['javascript', 'js', 'typescript', 'react', 'vue', 'angular', 'node'],
        'java': ['java', 'spring', 'maven', 'gradle'],
        'csharp': ['c#', 'csharp', '.net', 'asp.net'],
        'sql': ['sql', 'mysql', 'postgresql', 'oracle', 'database'],
        'cloud': ['aws', 'azure', 'gcp', 'cloud', 'docker', 'kubernetes', 'k8s'],
        'devops': ['devops', 'ci/cd', 'jenkins', 'gitlab', 'github actions', 'terraform'],
        'data': ['data science', 'machine learning', 'ml', 'ai', 'analytics', 'tableau', 'power bi'],
        'frontend': ['html', 'css', 'ui', 'ux', 'responsive', 'accessibility'],
        'backend': ['backend', 'api', 'rest', 'microservices', 'scalability'],
    }
    
    # Soft skills
    SOFT_SKILLS = [
        'communication', 'teamwork', 'leadership', 'problem solving',
        'project management', 'agile', 'scrum', 'collaboration'
    ]
    
    def analyze(self, job_description: str, user_skills: List[str]) -> Tuple[float, List[str], List[str]]:
        """
        Analyze job description and match against user skills
        
        Args:
            job_description: Full job description text
            user_skills: List of user's skills
            
        Returns:
            Tuple of (match_score, matched_skills, missing_skills)
        """
        # Extract requirements from job description
        required_skills = self._extract_skills(job_description)
        
        # Normalize user skills for comparison
        user_skills_lower = [skill.lower() for skill in user_skills]
        
        # Find matches and misses
        matched = []
        missing = []
        
        for skill in required_skills:
            if self._skill_matches(skill, user_skills_lower):
                matched.append(skill)
            else:
                missing.append(skill)
        
        # Calculate match score
        match_score = self._calculate_match_score(matched, required_skills)
        
        return match_score, matched, missing
    
    def _extract_skills(self, text: str) -> List[str]:
        """Extract skills from job description"""
        text_lower = text.lower()
        found_skills = set()
        
        # Check against known skill keywords
        for skill_category, keywords in self.SKILL_KEYWORDS.items():
            for keyword in keywords:
                if keyword in text_lower:
                    found_skills.add(skill_category)
        
        # Check for soft skills
        for skill in self.SOFT_SKILLS:
            if skill in text_lower:
                found_skills.add(skill)
        
        # Extract years of experience mentions
        experience_pattern = r'(\d+)\+?\s*years?\s+(?:of\s+)?(?:experience|exp)'
        matches = re.findall(experience_pattern, text_lower)
        if matches:
            found_skills.add(f"{matches[0]}+ years experience")
        
        return list(found_skills)
    
    def _skill_matches(self, required_skill: str, user_skills: List[str]) -> bool:
        """Check if user has the required skill"""
        required_lower = required_skill.lower()
        
        for user_skill in user_skills:
            user_skill_lower = user_skill.lower()
            
            # Exact match
            if required_lower == user_skill_lower:
                return True
            
            # Partial match for categories
            if required_lower in user_skill_lower or user_skill_lower in required_lower:
                return True
        
        return False
    
    def _calculate_match_score(self, matched: List[str], required: List[str]) -> float:
        """Calculate overall match score (0-1)"""
        if not required:
            return 1.0
        
        return len(matched) / len(required)
    
    def extract_requirements(self, job_description: str) -> dict:
        """
        Extract structured requirements from job description
        
        Returns:
            Dictionary with required_skills, nice_to_have, experience_level, etc.
        """
        text_lower = job_description.lower()
        
        # Extract experience level
        experience_level = "mid-level"
        if "senior" in text_lower or "lead" in text_lower:
            experience_level = "senior"
        elif "junior" in text_lower or "entry" in text_lower:
            experience_level = "junior"
        
        # Extract years of experience
        exp_pattern = r'(\d+)\+?\s*years?\s+(?:of\s+)?(?:experience|exp)'
        exp_matches = re.findall(exp_pattern, text_lower)
        years_required = int(exp_matches[0]) if exp_matches else 0
        
        return {
            'required_skills': self._extract_skills(job_description),
            'experience_level': experience_level,
            'years_required': years_required,
            'job_type': self._extract_job_type(text_lower),
        }
    
    def _extract_job_type(self, text: str) -> str:
        """Extract job type (full-time, part-time, contract, etc.)"""
        if "full-time" in text or "full time" in text:
            return "full-time"
        elif "part-time" in text or "part time" in text:
            return "part-time"
        elif "contract" in text:
            return "contract"
        elif "freelance" in text:
            return "freelance"
        return "unknown"
