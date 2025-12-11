"""
Risk Classification Plugin - Articles 5, 6, and Annex III

Provides risk classification and prohibited practices checking.
"""

import os
import json
from typing import Dict, Any
from .base import BasePlugin


class RiskClassificationPlugin(BasePlugin):
    """
    Plugin for EU AI Act risk classification and prohibited practices.
    
    Provides tools for:
    - classify_ai_system_risk
    - check_prohibited_practices
    """
    
    def get_name(self) -> str:
        return "RiskClassificationPlugin"
    
    def get_description(self) -> str:
        return "Provides EU AI Act risk classification and prohibited practices checking"
    
    def get_tools(self) -> Dict[str, Any]:
        return {
            "classify_ai_system_risk": self.classify_ai_system_risk,
            "check_prohibited_practices": self.check_prohibited_practices
        }
    
    def get_resources(self) -> Dict[str, Any]:
        return {
            "article50-rules://official-text": self.get_article50_rules_resource
        }
    
    def get_article50_rules_resource(self) -> str:
        """Resource: Article 50 rules"""
        rules_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "resources", 
            "article50_rules.json"
        )
        with open(rules_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def classify_ai_system_risk(
        self,
        system_description: str,
        use_case: str,
        biometric_data: bool = False,
        critical_infrastructure: bool = False,
        education: bool = False,
        law_enforcement: bool = False,
        predicts_criminal_behavior: bool = False,
        social_scoring: bool = False,
        emotion_detection_workplace: bool = False,
        generates_content: bool = False,
        interacts_with_users: bool = False
    ) -> Dict[str, Any]:
        """
        Determine AI system risk level per EU AI Act classification framework.
        
        Classifies system as: PROHIBITED, HIGH-RISK, LIMITED-RISK, or MINIMAL-RISK
        based on Articles 5, 6, and 50.
        
        Args:
            system_description: Description of the AI system
            use_case: Primary use case (e.g., "employment", "healthcare", "chatbot")
            biometric_data: Uses biometric identification/categorization
            critical_infrastructure: Used in critical infrastructure
            education: Used in education/vocational training
            law_enforcement: Used for law enforcement
            predicts_criminal_behavior: Predicts criminal behavior from profiling
            social_scoring: Performs social scoring
            emotion_detection_workplace: Detects emotions in workplace/education
            generates_content: Generates synthetic content
            interacts_with_users: Interacts with natural persons
        
        Returns:
            Risk classification with applicable obligations and deadlines
        """
        
        # Step 1: Check Article 5 - PROHIBITED practices
        if social_scoring:
            return {
                "risk_level": "PROHIBITED",
                "article": "Article 5(1)(c)",
                "reason": "Social scoring by public authorities or on their behalf",
                "system_description": system_description,
                "compliance_action": "MUST NOT deploy - System is prohibited",
                "penalties": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "deadline": "Immediate - Already in effect",
                "recommendation": "Discontinue development or deployment immediately"
            }
        
        if emotion_detection_workplace:
            return {
                "risk_level": "PROHIBITED",
                "article": "Article 5(1)(f)",
                "reason": "Emotion recognition in workplace or education (except medical/safety)",
                "system_description": system_description,
                "compliance_action": "MUST NOT deploy - System is prohibited",
                "exception": "Allowed only for medical or safety reasons",
                "penalties": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "deadline": "Immediate - Already in effect",
                "recommendation": "Remove emotion detection or limit to medical/safety contexts"
            }
        
        if predicts_criminal_behavior:
            return {
                "risk_level": "PROHIBITED",
                "article": "Article 5(1)(d)",
                "reason": "Risk assessment predicting criminal offenses based on profiling",
                "system_description": system_description,
                "compliance_action": "MUST NOT deploy - System is prohibited",
                "penalties": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "deadline": "Immediate - Already in effect",
                "recommendation": "Discontinue predictive profiling features"
            }
        
        # Step 2: Check Article 6 + Annex III - HIGH-RISK systems
        high_risk_checks = []
        
        if biometric_data:
            high_risk_checks.append({
                "reason": "Biometric identification or categorization",
                "annex_point": "Annex III point 1",
                "article_ref": "Article 6(2)"
            })
        
        if use_case.lower() in ["employment", "hiring", "hr", "recruitment"]:
            high_risk_checks.append({
                "reason": "AI system for employment, recruitment, or HR decisions",
                "annex_point": "Annex III point 4(a)",
                "article_ref": "Article 6(2)"
            })
        
        if education:
            high_risk_checks.append({
                "reason": "AI system for education or vocational training",
                "annex_point": "Annex III point 3",
                "article_ref": "Article 6(2)"
            })
        
        if law_enforcement:
            high_risk_checks.append({
                "reason": "AI system for law enforcement",
                "annex_point": "Annex III point 6",
                "article_ref": "Article 6(2)"
            })
        
        if critical_infrastructure:
            high_risk_checks.append({
                "reason": "AI system for critical infrastructure",
                "annex_point": "Annex III point 2",
                "article_ref": "Article 6(2)"
            })
        
        if high_risk_checks:
            return {
                "risk_level": "HIGH-RISK",
                "article": high_risk_checks[0]["article_ref"],
                "annex_reference": high_risk_checks[0]["annex_point"],
                "reason": high_risk_checks[0]["reason"],
                "system_description": system_description,
                "all_high_risk_factors": [check["reason"] for check in high_risk_checks],
                "applicable_obligations": [
                    "Risk management system (Article 9)",
                    "Data governance and management (Article 10)",
                    "Technical documentation (Article 11)",
                    "Record-keeping/logging (Article 12)",
                    "Transparency and information to users (Article 13)",
                    "Human oversight (Article 14)",
                    "Accuracy, robustness, cybersecurity (Article 15)",
                    "Quality management system (Article 17)",
                    "Conformity assessment (Article 43)",
                    "Registration in EU database (Article 49)",
                    "Post-market monitoring (Article 72)"
                ],
                "compliance_deadline": "2027-08-02",
                "penalties_if_non_compliant": "Up to €15 million or 3% of global annual turnover",
                "next_steps": [
                    "Conduct conformity assessment",
                    "Implement risk management system",
                    "Create technical documentation",
                    "Establish human oversight mechanisms",
                    "Register in EU database before deployment"
                ]
            }
        
        # Step 3: Check Article 50 - LIMITED-RISK systems
        limited_risk_checks = []
        
        if interacts_with_users:
            limited_risk_checks.append({
                "reason": "AI system interacts with natural persons",
                "article": "Article 50(1)",
                "obligation": "Must disclose AI interaction to users"
            })
        
        if generates_content:
            limited_risk_checks.append({
                "reason": "Generates synthetic audio, image, video, or text content",
                "article": "Article 50(2)",
                "obligation": "Must watermark AI-generated content"
            })
        
        if limited_risk_checks:
            return {
                "risk_level": "LIMITED-RISK",
                "article": "Article 50",
                "reason": "; ".join([check["reason"] for check in limited_risk_checks]),
                "system_description": system_description,
                "applicable_obligations": [check["obligation"] for check in limited_risk_checks],
                "compliance_deadline": "2026-08-02",
                "penalties_if_non_compliant": "Up to €15 million or 3% of global annual turnover",
                "next_steps": [
                    "Implement transparency disclosures (Article 50)",
                    "Add watermarks if generating content (Article 50(2))",
                    "Ensure users know they're interacting with AI (Article 50(1))"
                ]
            }
        
        # Step 4: Default - MINIMAL-RISK
        return {
            "risk_level": "MINIMAL-RISK",
            "article": "No specific article applies",
            "reason": "System does not fall under prohibited, high-risk, or limited-risk categories",
            "system_description": system_description,
            "applicable_obligations": [
                "Voluntary codes of conduct (Article 95)",
                "General transparency best practices"
            ],
            "compliance_deadline": "No mandatory deadline",
            "penalties_if_non_compliant": "None (voluntary compliance)",
            "next_steps": [
                "Consider voluntary transparency measures",
                "Follow industry best practices",
                "Monitor for regulatory updates"
            ]
        }
    
    def check_prohibited_practices(
        self,
        uses_subliminal_techniques: bool = False,
        exploits_vulnerabilities: bool = False,
        social_scoring: bool = False,
        predicts_crime_from_profiling: bool = False,
        scrapes_facial_images: bool = False,
        detects_emotions_in_workplace: bool = False,
        biometric_categorization_sensitive_attributes: bool = False,
        real_time_biometric_identification_public: bool = False
    ) -> Dict[str, Any]:
        """
        Check if AI system violates prohibited practices under Article 5.
        
        These practices carry the HIGHEST penalties: €35M or 7% of global revenue.
        
        Args:
            uses_subliminal_techniques: Manipulates behavior via subliminal techniques
            exploits_vulnerabilities: Exploits vulnerabilities of specific groups
            social_scoring: Social scoring by/for public authorities
            predicts_crime_from_profiling: Predicts criminal behavior from profiling
            scrapes_facial_images: Scrapes facial images from internet/CCTV
            detects_emotions_in_workplace: Emotion recognition in workplace/education
            biometric_categorization_sensitive_attributes: Infers race, politics, etc. from biometrics
            real_time_biometric_identification_public: Real-time biometric ID in public spaces
        
        Returns:
            Violations found with penalties and recommendations
        """
        
        violations = []
        
        if uses_subliminal_techniques:
            violations.append({
                "article": "Article 5(1)(a)",
                "violation": "Subliminal techniques to manipulate behavior",
                "description": "AI systems that deploy subliminal techniques beyond a person's consciousness to materially distort behavior",
                "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "exception": "None"
            })
        
        if exploits_vulnerabilities:
            violations.append({
                "article": "Article 5(1)(b)",
                "violation": "Exploitation of vulnerabilities",
                "description": "AI systems that exploit vulnerabilities of specific groups (age, disability, social/economic situation)",
                "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "exception": "None"
            })
        
        if social_scoring:
            violations.append({
                "article": "Article 5(1)(c)",
                "violation": "Social scoring",
                "description": "AI systems for social scoring by public authorities or on their behalf",
                "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "exception": "None"
            })
        
        if predicts_crime_from_profiling:
            violations.append({
                "article": "Article 5(1)(d)",
                "violation": "Predictive policing based on profiling",
                "description": "AI systems that make risk assessments of natural persons to predict criminal offenses based solely on profiling",
                "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "exception": "None"
            })
        
        if scrapes_facial_images:
            violations.append({
                "article": "Article 5(1)(e)",
                "violation": "Untargeted scraping of facial images",
                "description": "Creating or expanding facial recognition databases through untargeted scraping from internet or CCTV",
                "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "exception": "None"
            })
        
        if detects_emotions_in_workplace:
            violations.append({
                "article": "Article 5(1)(f)",
                "violation": "Emotion recognition in workplace or education",
                "description": "AI systems that infer emotions in workplace or educational institutions",
                "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "exception": "Medical or safety reasons only"
            })
        
        if biometric_categorization_sensitive_attributes:
            violations.append({
                "article": "Article 5(1)(g)",
                "violation": "Biometric categorization of sensitive attributes",
                "description": "Biometric categorization systems that infer race, political opinions, trade union membership, religious/philosophical beliefs, sex life, or sexual orientation",
                "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "exception": "Limited exceptions for law enforcement with safeguards"
            })
        
        if real_time_biometric_identification_public:
            violations.append({
                "article": "Article 5(1)(h)",
                "violation": "Real-time remote biometric identification in public",
                "description": "Real-time remote biometric identification systems in publicly accessible spaces for law enforcement",
                "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
                "exception": "Very limited exceptions for serious crimes with judicial authorization"
            })
        
        if violations:
            return {
                "is_prohibited": True,
                "severity": "CRITICAL - Highest penalty tier",
                "violations": violations,
                "violation_count": len(violations),
                "total_penalty_exposure": "Up to €35 million or 7% of global annual turnover PER violation",
                "recommendation": "STOP IMMEDIATELY - These AI practices are PROHIBITED under EU AI Act",
                "required_actions": [
                    "Cease development and deployment immediately",
                    "Notify relevant supervisory authorities",
                    "Assess alternatives that comply with EU AI Act",
                    "Consult legal counsel for remediation strategy"
                ],
                "compliance_status": "NON-COMPLIANT - Critical violation"
            }
        
        return {
            "is_prohibited": False,
            "severity": "None",
            "violations": [],
            "violation_count": 0,
            "recommendation": "No prohibited practices detected",
            "compliance_status": "COMPLIANT with Article 5 prohibitions",
            "next_steps": [
                "Continue to check high-risk and limited-risk classifications",
                "Monitor for regulatory updates",
                "Maintain compliance documentation"
            ]
        }
