"""
Role Determination Plugin - Article 3

Provides role determination for EU AI Act compliance.
"""

from typing import Dict, Any
from .base import BasePlugin


class RoleDeterminationPlugin(BasePlugin):
    """
    Plugin for EU AI Act role determination.
    
    Provides tools for:
    - determine_eu_ai_act_role
    """
    
    def get_name(self) -> str:
        return "RoleDeterminationPlugin"
    
    def get_description(self) -> str:
        return "Provides EU AI Act role determination (Provider, Deployer, etc.)"
    
    def get_tools(self) -> Dict[str, Any]:
        return {
            "determine_eu_ai_act_role": self.determine_eu_ai_act_role
        }
    
    def determine_eu_ai_act_role(
        self,
        company_description: str,
        company_location: str,
        develops_ai_system: bool = False,
        uses_ai_system: bool = False,
        sells_ai_system: bool = False,
        imports_to_eu: bool = False,
        distributes_in_eu: bool = False,
        integrates_ai_into_product: bool = False,
        represents_non_eu_provider: bool = False,
        under_own_name_or_trademark: bool = False,
        substantial_modification: bool = False,
        change_intended_purpose: bool = False
    ) -> Dict[str, Any]:
        """
        Determine which EU AI Act role(s) apply to your organization.
        
        Different roles have different obligations under the EU AI Act.
        Understanding your role is CRITICAL to knowing which requirements apply.
        
        Args:
            company_description: Brief description of your company/organization
            company_location: Country/region where company is based
            develops_ai_system: You develop AI systems or commission their development
            uses_ai_system: You use AI systems in your operations
            sells_ai_system: You sell or offer AI systems
            imports_to_eu: You bring AI systems from outside EU into EU market
            distributes_in_eu: You distribute/resell AI systems in EU
            integrates_ai_into_product: You integrate AI into physical products
            represents_non_eu_provider: You represent a non-EU AI provider in the EU
            under_own_name_or_trademark: AI system bears your name/trademark
            substantial_modification: You substantially modify existing AI systems
            change_intended_purpose: You change the intended purpose of AI systems
        
        Returns:
            Role determination with definitions and applicable obligations
        """
        
        roles_identified = []
        role_details = {}
        is_in_eu = company_location.lower() in ["eu", "european union"] or any(
            country in company_location.lower() 
            for country in ["germany", "france", "spain", "italy", "netherlands", 
                           "belgium", "austria", "ireland", "portugal", "greece"]
        )
        
        # Step 1: Check if PROVIDER
        is_provider = (
            develops_ai_system or
            (sells_ai_system and under_own_name_or_trademark) or
            substantial_modification or
            change_intended_purpose
        )
        
        if is_provider:
            reason_parts = []
            if develops_ai_system:
                reason_parts.append("develops AI systems")
            if sells_ai_system and under_own_name_or_trademark:
                reason_parts.append("places AI on market under own name/trademark")
            if substantial_modification:
                reason_parts.append("substantially modifies AI systems")
            if change_intended_purpose:
                reason_parts.append("changes intended purpose of AI systems")
            
            roles_identified.append("PROVIDER")
            role_details["provider"] = {
                "article": "Article 3(3)",
                "definition": "Develops the AI system or has it developed, and places it on the market or puts it into service under own name or trademark",
                "applies_to_you": True,
                "reason": f"You {' and '.join(reason_parts)}",
                "key_obligations": [
                    "Establish risk management system (Article 9)",
                    "Data governance and quality (Article 10)",
                    "Technical documentation (Article 11)",
                    "Automatic logging (Article 12)",
                    "Design for human oversight (Article 14)",
                    "Accuracy and robustness (Article 15)",
                    "Cybersecurity measures (Article 15)",
                    "Quality management system (Article 17)",
                    "Conformity assessment (Article 43)",
                    "CE marking (Article 48)",
                    "EU database registration (Article 49)"
                ],
                "deadline": "2027-08-02 (for high-risk systems)",
                "penalties": "Up to €15M or 3% of global turnover for non-compliance"
            }
        
        # Step 2: Check if DEPLOYER
        is_deployer = uses_ai_system
        
        if is_deployer:
            roles_identified.append("DEPLOYER")
            role_details["deployer"] = {
                "article": "Article 3(4)",
                "definition": "Uses an AI system under their authority, except for personal non-professional activity",
                "applies_to_you": True,
                "reason": "You use AI systems in your operations",
                "key_obligations": [
                    "Use AI according to instructions (Article 26(1))",
                    "Ensure human oversight (Article 26(2))",
                    "Monitor AI system operation (Article 26(3))",
                    "Report serious incidents (Article 26(4))",
                    "Keep logs generated by AI system (Article 26(5))",
                    "Conduct fundamental rights impact assessment (Article 27)",
                    "Inform workers about AI monitoring systems (Article 26(7))",
                    "Ensure input data quality (Article 26(6))"
                ],
                "deadline": "2027-08-02 (for high-risk systems)",
                "penalties": "Up to €15M or 3% of global turnover for non-compliance"
            }
        
        # Step 3: Check if IMPORTER
        is_importer = (
            not is_in_eu and
            imports_to_eu and
            (sells_ai_system or distributes_in_eu) and
            under_own_name_or_trademark
        )
        
        if is_importer:
            roles_identified.append("IMPORTER")
            role_details["importer"] = {
                "article": "Article 3(5)",
                "definition": "Places on the market an AI system that bears the name or trademark of a person established outside the EU",
                "applies_to_you": True,
                "reason": f"You are based in {company_location} and import AI systems to EU market",
                "key_obligations": [
                    "Verify provider's conformity assessment (Article 23(1))",
                    "Verify CE marking and documentation (Article 23(2))",
                    "Ensure registration in EU database (Article 23(3))",
                    "Keep copy of technical documentation (Article 23(4))",
                    "Provide authorities with documentation (Article 23(5))",
                    "Ensure storage/transport doesn't affect compliance (Article 23(6))",
                    "Appoint authorized representative in EU (Article 22)"
                ],
                "deadline": "2027-08-02",
                "penalties": "Up to €15M or 3% of global turnover for non-compliance"
            }
        
        # Step 4: Check if DISTRIBUTOR
        is_distributor = (
            distributes_in_eu and
            not is_provider and
            not is_importer and
            sells_ai_system
        )
        
        if is_distributor:
            roles_identified.append("DISTRIBUTOR")
            role_details["distributor"] = {
                "article": "Article 3(6)",
                "definition": "Makes an AI system available on the market without being the provider or importer",
                "applies_to_you": True,
                "reason": "You distribute AI systems in the EU market",
                "key_obligations": [
                    "Verify CE marking present (Article 24(1))",
                    "Verify required documentation provided (Article 24(2))",
                    "Verify provider/importer obligations met (Article 24(3))",
                    "Inform provider/importer of non-compliance (Article 24(4))",
                    "Cooperate with authorities (Article 24(5))"
                ],
                "deadline": "2027-08-02",
                "penalties": "Up to €15M or 3% of global turnover for non-compliance"
            }
        
        # Step 5: Check if AUTHORIZED REPRESENTATIVE
        is_authorized_rep = (
            is_in_eu and
            represents_non_eu_provider
        )
        
        if is_authorized_rep:
            roles_identified.append("AUTHORIZED REPRESENTATIVE")
            role_details["authorized_representative"] = {
                "article": "Article 3(7)",
                "definition": "Natural or legal person located in the EU who has received a written mandate from a provider outside the EU",
                "applies_to_you": True,
                "reason": f"You are based in {company_location} (EU) and represent a non-EU AI provider",
                "key_obligations": [
                    "Perform tasks specified in mandate (Article 22(1))",
                    "Provide copy of technical documentation to authorities (Article 22(2))",
                    "Cooperate with authorities (Article 22(3))",
                    "Terminate mandate if provider non-compliant (Article 22(4))"
                ],
                "deadline": "2027-08-02",
                "penalties": "Provider's penalties may apply"
            }
        
        # Step 6: Check if PRODUCT MANUFACTURER
        is_product_manufacturer = (
            integrates_ai_into_product and
            under_own_name_or_trademark
        )
        
        if is_product_manufacturer:
            roles_identified.append("PRODUCT MANUFACTURER")
            role_details["product_manufacturer"] = {
                "article": "Article 3(8) + Article 25",
                "definition": "Manufactures a product and integrates an AI system into it, where the AI is a safety component or the product itself",
                "applies_to_you": True,
                "reason": "You integrate AI systems into physical products under your name/trademark",
                "key_obligations": [
                    "Assume provider obligations for AI component (Article 25(1))",
                    "Ensure AI system complies with requirements (Article 25(2))",
                    "Affix own name/trademark to product (Article 25(3))",
                    "Follow relevant product safety legislation",
                    "Conduct conformity assessment for AI component"
                ],
                "deadline": "2027-08-02",
                "penalties": "Provider penalties apply (up to €15M or 3% of turnover)"
            }
        
        # Determine primary role
        if not roles_identified:
            return {
                "primary_role": "NO DIRECT ROLE",
                "additional_roles": [],
                "role_details": {},
                "company_description": company_description,
                "company_location": company_location,
                "assessment": "Based on provided information, you may not have direct EU AI Act obligations",
                "recommendation": "If you interact with AI systems in any way, review the questions again. You may be a deployer if you use AI systems.",
                "next_steps": [
                    "Verify you are not using AI systems in your operations",
                    "If you are using AI, you are likely a DEPLOYER",
                    "Monitor for regulatory changes that may affect your activities"
                ]
            }
        
        primary_role = roles_identified[0]
        additional_roles = roles_identified[1:] if len(roles_identified) > 1 else []
        
        return {
            "primary_role": primary_role,
            "additional_roles": additional_roles,
            "all_roles": roles_identified,
            "role_details": role_details,
            "company_description": company_description,
            "company_location": company_location,
            "is_eu_based": is_in_eu,
            "total_roles": len(roles_identified),
            "critical_note": "If you have multiple roles, you must comply with ALL obligations for each role",
            "most_common_combination": "Many companies are both PROVIDER (they develop) and DEPLOYER (they use their own AI)",
            "recommendation": f"Focus first on {primary_role} obligations, then address {', '.join(additional_roles) if additional_roles else 'other compliance areas'}",
            "next_steps": [
                f"Review all {primary_role} obligations in detail",
                "Determine which AI systems are high-risk vs limited-risk",
                "Create compliance timeline based on deadlines",
                "Assign responsibility for each obligation",
                "Consider consulting legal counsel for complex cases"
            ]
        }
