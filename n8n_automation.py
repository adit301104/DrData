#!/usr/bin/env python3
# Weekly automation script for doctor data scraping
# This gets called by n8n to update our doctor database

import sys
import os
import json
from datetime import datetime
from multi_healthcare_scraper import MultiHealthcareScraper
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
        logging.info("Starting doctor data scraping")
        
        # Areas and specialties we want to scrape
        pune_areas = ['Aundh', 'Baner', 'Wakad']
        medical_specialties = [
            'Cardiology', 'Dermatology', 'Neurology', 'Oncology', 
            'General Surgery', 'Orthopaedics', 'Neurosurgery', 
            'Paediatrics', 'Obstetrics/Gynecology', 'Psychiatry'
        ]
        
        # Start the scraper
        scraper = MultiHealthcareScraper()
        doctor_list = []
        
        # Go through each specialty and collect doctors
        for specialty in medical_specialties:
            logging.info(f"Working on {specialty}")
            found_doctors = scraper.scrape_all_sources(specialty)
            doctor_list.extend(found_doctors)
            logging.info(f"Found {len(found_doctors)} doctors for {specialty}")
        
        # Remove duplicates and clean up the data
        final_data = scraper.remove_duplicates(doctor_list)
        
        # Always save to the same file so frontend can find it
        output_file = 'healthcare_doctors.xlsx'
        
        scraper.save_to_excel(final_data, output_file)
        scraper.close_driver()
        
        # Send results back to n8n
        run_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        success_result = {
            'status': 'success',
            'total_doctors': len(final_data),
            'filename': output_file,
            'log_file': log_file,
            'timestamp': run_time,
            'areas_covered': ['Pune', 'Aundh', 'Baner', 'Wakad'],
            'specialties_done': medical_specialties,
            'data_sources': ['JustDial'],
            'doctor_info_fields': [
                'Name', 'Specialty', 'Clinic/Hospital', 'Address',
                'Years of Experience', 'Contact Number', 'Email',
                'Rating', 'Reviews Count', 'Pros', 'Cons', 'Recommendation'
            ]
        }
        
        logging.info(f"Scraping completed successfully: {success_result}")
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