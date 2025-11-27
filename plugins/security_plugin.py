"""
Security Plugin - Article 15 Cybersecurity

Provides security scanning tools using SonnyLabs.ai API.
"""

import os
from typing import Dict, Any
from .base import BasePlugin


class SecurityPlugin(BasePlugin):
    """
    Plugin for EU AI Act Article 15 cybersecurity compliance.
    
    Provides tools for:
    - scan_for_prompt_injection
    - check_sensitive_file_access
    
    Integrates with SonnyLabs.ai API for threat detection.
    """
    
    def get_name(self) -> str:
        return "SecurityPlugin"
    
    def get_description(self) -> str:
        return "Provides EU AI Act Article 15 cybersecurity tools with SonnyLabs.ai integration"
    
    def get_tools(self) -> Dict[str, Any]:
        return {
            "scan_for_prompt_injection": self.scan_for_prompt_injection,
            "check_sensitive_file_access": self.check_sensitive_file_access
        }
    
    def scan_for_prompt_injection(
        self,
        user_input: str,
        sonnylabs_api_token: str,
        sonnylabs_analysis_id: str,
        tag: str = "mcp_scan"
    ) -> Dict[str, Any]:
        """
        Scans user input for prompt injection attacks using SonnyLabs.ai API.
        
        Helps comply with EU AI Act Article 15 cybersecurity requirements.
        Detects attempts to manipulate AI behavior through prompt injection.
        
        Args:
            user_input: The user input text to scan for threats
            sonnylabs_api_token: Your SonnyLabs API token (Bearer token)
            sonnylabs_analysis_id: Your SonnyLabs analysis ID
            tag: Optional identifier for this scan (default: "mcp_scan")
        
        Returns:
            Dictionary with threat analysis and EU AI Act compliance info
        """
        import requests
        
        try:
            # Call SonnyLabs API
            url = f"https://sonnylabs-service.onrender.com/v1/analysis/{sonnylabs_analysis_id}"
            
            response = requests.post(
                url,
                params={
                    "tag": tag,
                    "scan_type": "input",
                    "detections": "prompt_injection,long_prompt_injection"
                },
                headers={
                    "Authorization": f"Bearer {sonnylabs_api_token}",
                    "Content-Type": "text/plain"
                },
                data=user_input.encode('utf-8'),
                timeout=10
            )
            
            response.raise_for_status()
            result = response.json()
            
            # Extract prompt injection scores
            prompt_injection_score = 0.0
            long_injection_score = 0.0
            attack_type = "none"
            
            for item in result.get("analysis", []):
                if item.get("name") == "prompt_injection" and item.get("type") == "score":
                    prompt_injection_score = item.get("result", 0.0)
                elif item.get("name") == "long_prompt_injection" and item.get("type") == "score":
                    long_injection_score = item.get("result", 0.0)
            
            # Determine attack severity
            max_score = max(prompt_injection_score, long_injection_score)
            is_attack = max_score > 0.7
            
            if max_score > 0.9:
                risk_level = "CRITICAL"
                recommendation = "BLOCK immediately - high confidence attack"
            elif max_score > 0.7:
                risk_level = "HIGH"
                recommendation = "BLOCK this input - likely attack"
            elif max_score > 0.5:
                risk_level = "MEDIUM"
                recommendation = "WARN user - suspicious input"
            else:
                risk_level = "LOW"
                recommendation = "ALLOW - input appears safe"
            
            if is_attack:
                attack_type = "instruction_override" if prompt_injection_score > long_injection_score else "long_form_injection"
            
            return {
                "is_prompt_injection": is_attack,
                "confidence": round(max_score, 3),
                "attack_type": attack_type,
                "risk_level": risk_level,
                "recommendation": recommendation,
                "scores": {
                    "basic_injection": round(prompt_injection_score, 3),
                    "long_form_injection": round(long_injection_score, 3)
                },
                "eu_ai_act_relevance": "Article 15 - Cybersecurity and robustness requirements",
                "article_15_compliance": "Detecting and preventing manipulation attempts meets Article 15(1) requirements",
                "sonnylabs_analysis": {
                    "detection_method": "Multi-model ensemble (pattern matching + LLM classifier)",
                    "api_endpoint": url,
                    "tag": tag
                },
                "next_steps": [
                    "Block input if risk level is HIGH or CRITICAL",
                    "Log incident for security audit",
                    "Consider implementing rate limiting",
                    "Review similar patterns in historical data"
                ] if is_attack else [
                    "Process input normally",
                    "Continue monitoring for anomalies"
                ]
            }
            
        except Exception as e:
            return {
                "error": "SonnyLabs API request failed",
                "details": str(e),
                "is_prompt_injection": None,
                "recommendation": "Unable to verify - proceed with caution or use fallback detection",
                "eu_ai_act_relevance": "Article 15 - Unable to verify cybersecurity compliance",
                "fallback_suggestion": "Implement basic keyword filtering as temporary measure"
            }
    
    def check_sensitive_file_access(
        self,
        file_path: str,
        agent_action: str,
        sonnylabs_api_token: str,
        sonnylabs_analysis_id: str,
        tag: str = "file_access_check"
    ) -> Dict[str, Any]:
        """
        Checks if AI agent is attempting to access sensitive files using SonnyLabs.ai API.
        
        Helps comply with EU AI Act Article 15 (Security) and Article 10 (Data governance).
        Prevents unauthorized access to confidential files and system resources.
        
        Args:
            file_path: The file path being accessed by the AI agent
            agent_action: The action being performed (e.g., "read", "write", "execute")
            sonnylabs_api_token: Your SonnyLabs API token (Bearer token)
            sonnylabs_analysis_id: Your SonnyLabs analysis ID
            tag: Optional identifier for this check (default: "file_access_check")
        
        Returns:
            Dictionary with file sensitivity analysis and access recommendations
        """
        import requests
        
        try:
            # Create analysis text
            analysis_text = f"Agent attempting to {agent_action} file: {file_path}"
            
            # Call SonnyLabs API
            url = f"https://sonnylabs-service.onrender.com/v1/analysis/{sonnylabs_analysis_id}"
            
            response = requests.post(
                url,
                params={
                    "tag": tag,
                    "scan_type": "input",
                    "detections": "sensitive_path_detection"
                },
                headers={
                    "Authorization": f"Bearer {sonnylabs_api_token}",
                    "Content-Type": "text/plain"
                },
                data=analysis_text.encode('utf-8'),
                timeout=10
            )
            
            response.raise_for_status()
            result = response.json()
            
            # Extract sensitive path detections
            sensitive_paths = []
            is_sensitive = False
            sensitivity_level = "LOW"
            detected_data_types = []
            
            for item in result.get("analysis", []):
                if item.get("type") == "sensitive_path_detection":
                    paths = item.get("result", [])
                    for path_info in paths:
                        sensitive_paths.append(path_info)
                        is_sensitive = True
                        
                        # Determine sensitivity level
                        confidence = path_info.get("confidence", 0)
                        category = path_info.get("category", "unknown")
                        
                        if confidence > 0.9 or category in ["system_file", "credential_file"]:
                            sensitivity_level = "HIGHLY_CONFIDENTIAL"
                        elif confidence > 0.7 or category in ["config_file", "database"]:
                            sensitivity_level = "CONFIDENTIAL"
                        elif sensitivity_level not in ["HIGHLY_CONFIDENTIAL", "CONFIDENTIAL"]:
                            sensitivity_level = "SENSITIVE"
                        
                        # Track data types
                        if category not in detected_data_types:
                            detected_data_types.append(category)
            
            # Determine recommendation
            if is_sensitive and sensitivity_level == "HIGHLY_CONFIDENTIAL":
                recommendation = "DENY access immediately - highly sensitive file"
                action = "BLOCK"
            elif is_sensitive:
                recommendation = "REQUIRE explicit authorization before allowing access"
                action = "REQUIRE_AUTH"
            else:
                recommendation = "ALLOW access - file does not appear sensitive"
                action = "ALLOW"
            
            return {
                "is_sensitive": is_sensitive,
                "sensitivity_level": sensitivity_level,
                "detected_paths": sensitive_paths,
                "detected_data_types": detected_data_types,
                "file_path": file_path,
                "agent_action": agent_action,
                "recommendation": recommendation,
                "action": action,
                "eu_ai_act_relevance": "Article 10 - Data governance requirements & Article 15 - Security measures",
                "article_10_compliance": "AI systems must only access data necessary for their intended purpose",
                "article_15_compliance": "AI systems must implement security measures to prevent unauthorized access",
                "access_control_recommendation": "Implement role-based access control (RBAC) with principle of least privilege",
                "sonnylabs_analysis": {
                    "detection_method": "Pattern matching + File path analysis",
                    "api_endpoint": url,
                    "tag": tag
                },
                "security_measures": [
                    "Implement file access logging",
                    "Require authentication for sensitive directories",
                    "Use allowlist for permitted file paths",
                    "Monitor and alert on suspicious access patterns",
                    "Regularly audit AI agent file access permissions"
                ],
                "compliance_actions": [
                    "Document access attempt in audit log",
                    "Verify AI agent has legitimate need for file access",
                    "Implement technical safeguards (encryption, access controls)",
                    "Conduct regular security reviews of AI agent permissions"
                ] if is_sensitive else [
                    "Log access for audit trail",
                    "Continue monitoring access patterns"
                ]
            }
            
        except Exception as e:
            return {
                "error": "SonnyLabs API request failed",
                "details": str(e),
                "is_sensitive": None,
                "recommendation": "Unable to verify - deny access by default for security",
                "action": "DENY_SAFE",
                "eu_ai_act_relevance": "Article 15 - Unable to verify security compliance"
            }
