import requests
import json
import logging
import os

class HealthcareAIAnalyzer:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('GROQ_API_KEY', 'your-api-key-here')
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def analyze_with_groq(self, doctor_info):
        """Use Groq AI to analyze doctor profile"""
        try:
            prompt = f"""
Analyze this doctor profile and provide pros, cons, and recommendation:

Doctor: {doctor_info.get('Doctors name', 'N/A')}
Specialty: {doctor_info.get('Specialty', 'N/A')}
Experience: {doctor_info.get('Years of experience', 'N/A')} years
Rating: {doctor_info.get('Ratings', 'N/A')}
Clinic: {doctor_info.get('Clinic/Hospital', 'N/A')}

Provide response in this exact format:
PROS: [list 2-3 key strengths]
CONS: [list 1-2 concerns or limitations]
RECOMMENDATION: [brief recommendation with reasoning]
"""
            
            payload = {
                "model": "llama3-8b-8192",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 300,
                "temperature": 0.3
            }
            
            response = requests.post(self.base_url, headers=self.headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                return self.parse_groq_response(content)
            else:
                logging.warning(f"Groq API error: {response.status_code}")
                return self.fallback_analysis(doctor_info)
                
        except Exception as e:
            logging.error(f"Groq analysis failed: {e}")
            return self.fallback_analysis(doctor_info)
    
    def parse_groq_response(self, content):
        """Parse Groq response into structured format"""
        try:
            lines = content.strip().split('\n')
            pros = cons = recommendation = ""
            
            for line in lines:
                if line.startswith('PROS:'):
                    pros = line.replace('PROS:', '').strip()
                elif line.startswith('CONS:'):
                    cons = line.replace('CONS:', '').strip()
                elif line.startswith('RECOMMENDATION:'):
                    recommendation = line.replace('RECOMMENDATION:', '').strip()
            
            return {
                'pros': pros or "Qualified medical professional",
                'cons': cons or "No major concerns identified",
                'recommendation': recommendation or "Consult for your medical needs"
            }
        except:
            return self.fallback_analysis({})
    
    def fallback_analysis(self, doctor_info):
        """Fallback analysis when Groq fails"""
        rating = float(doctor_info.get('Ratings', 4.0))
        experience = int(doctor_info.get('Years of experience', 5))
        
        if rating >= 4.5 and experience >= 10:
            return {
                'pros': "Highly rated with good experience",
                'cons': "No significant concerns",
                'recommendation': "Highly recommended specialist"
            }
        elif rating >= 4.0:
            return {
                'pros': "Good patient satisfaction",
                'cons': "Standard consultation fees",
                'recommendation': "Recommended for consultation"
            }
        else:
            return {
                'pros': "Available for consultation",
                'cons': "Limited patient feedback",
                'recommendation': "Consider with other options"
            }

    def analyze_doctor_profile(self, doctor_info):
        """Analyze doctor using Groq AI"""
        analysis = self.analyze_with_groq(doctor_info)
        
        doctor_info['Summary of Pros and Cons (Summary of reviews), and recommendation'] = f"PROS: {analysis['pros']} | CONS: {analysis['cons']} | {analysis['recommendation']}"
        
        return doctor_info

    def batch_analyze_doctors(self, doctor_list):
        """Analyze all doctors with Groq AI"""
        results = []
        for i, doctor in enumerate(doctor_list):
            if i % 10 == 0:
                logging.info(f"Analyzing doctor {i+1}/{len(doctor_list)}")
            analyzed = self.analyze_doctor_profile(doctor.copy())
            results.append(analyzed)
        return results