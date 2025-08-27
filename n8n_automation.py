#!/usr/bin/env python3
# Weekly automation script for doctor data scraping
# This gets called by n8n to update our doctor database

import sys
import os
import json
from datetime import datetime
from robust_pune_scraper import RobustPuneScraper
import logging

def setup_logging():
    # Create log file for this automation run
    log_file = f"doctor_scraping_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return log_file

def run_automation():
    # Main function that does all the work
    log_file = setup_logging()
    
    try:
        logging.info("Starting robust doctor data scraping")
        
        # Start the robust scraper
        scraper = RobustPuneScraper()
        
        # Run comprehensive scraping
        doctor_list = scraper.scrape_comprehensive()
        
        # Always save to the same file so frontend can find it
        output_file = 'healthcare_doctors.xlsx'
        scraper.save_results(doctor_list, output_file)
        scraper.close()
        
        # Send results back to n8n
        run_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        success_result = {
            'status': 'success',
            'total_doctors': len(doctor_list),
            'filename': output_file,
            'log_file': log_file,
            'timestamp': run_time,
            'areas_covered': ['Aundh', 'Baner', 'Wakad', 'Kothrud', 'Viman Nagar', 'Hadapsar', 'Pune City', 'Camp', 'Koregaon Park', 'Deccan'],
            'specialties_done': ['Cardiology', 'Dermatology', 'Neurology', 'Orthopedic', 'Pediatric', 'Gynecology', 'General Medicine', 'Oncology', 'Psychiatry', 'ENT', 'Ophthalmology', 'Urology'],
            'data_sources': ['Practo', 'JustDial', '1mg', 'Lybrate', 'Apollo'],
            'doctor_info_fields': [
                'Complete address', 'Doctors name', 'Specialty', 'Clinic/Hospital',
                'Years of experience', 'Contact number', 'Ratings', 'Contact email',
                'Reviews', 'Summary of Pros and Cons (Summary of reviews), and recommendation', 'Source'
            ]
        }
        
        logging.info(f"Robust scraping completed successfully: {success_result}")
        print(json.dumps(success_result))  # n8n reads this output
        
        return success_result
        
    except Exception as error:
        # Something went wrong, let n8n know
        error_info = {
            'status': 'failed',
            'error_message': str(error),
            'log_file': log_file,
            'timestamp': datetime.now().isoformat()
        }
        
        logging.error(f"Scraping failed: {error_info}")
        print(json.dumps(error_info))
        
        return error_info

if __name__ == "__main__":
    run_automation()