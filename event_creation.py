import re
import asyncio
from playwright.async_api import expect, async_playwright
import pandas as pd

excel_file_path = '/Users/varunm/Downloads/events_data.xlsx'
df = pd.read_excel(excel_file_path, dtype=str)

data_dict = {}
for column_name in df.columns:
    data_dict[column_name] = df[column_name].tolist()


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://authtest.gridlex.com/login/')
        await page.fill('#email_id', 'harish.b@gridlex.com')
        await page.fill('#password', 'Harish@123')
        await page.click('#login')
        await page.wait_for_load_state('networkidle')

        # data_dict = {'event_template':['SGD Event 2 with all required fields','SGD Event 2 with all required fields','SGD Event 2 with all required fields','SGD Event 2 with all required fields'],
        #     'event_title': ['From script 11', 'From script 12','From script 13','From script 14',],
        #     'event_description': ['Created using playwright script 1', 'Created using playwright script 2', 'Created using playwright script 3','Created using playwright script 4'],
        #     'event_format': ['1', '2', '1', '2'],
        #     'event_type': ['Zoom','Zoom','Zoom','Zoom'],
        #     'event_category': ['Django','Django','Django','Django'],
        #     'event_sub_category': ['Django Rest Framework','Django Rest Framework','Django Rest Framework','Django Rest Framework'],
        #     'event_timezone':['(GMT+05:30) Asia/Kolkata','(GMT+05:30) Asia/Kolkata','(GMT+05:30) Asia/Kolkata','(GMT+05:30) Asia/Kolkata'],
        #     'event_start_date': ['12/12/2023','12/12/2023','12/12/2023','12/12/2023'],
        #     'event_start_time': ['12122','12122','12122','12122'] ,
        #     'event_end_date': ['10/10/2023','10/10/2023','10/10/2023','10/10/2023'],
        #     'event_end_time' : ['10101','10101','10101','10101'],
        #     'registration_status':['Active','Active','Active','Active'],
        #     'registration_start_date':['12/12/2023','12/12/2023','12/12/2023','12/12/2023'],
        #     'registration_start_time':['12122','12122','12122','12122'],
        #     'registration_end_date':['10/10/2023','10/10/2023','10/10/2023','10/10/2023'],
        #     'registration_end_time':['10101','10101','10101','10101'],
        #     'registration_capacity':['20','21','22','23'],
        #     'address_line1':['asdfg','dfghg','srdty','sdfgf'],
        #     'address_line2':['ytrsd','rtfgh','tryt','yrter'],
        #     'street':['ertfhgdf','245rt','yyhfgdf','sfdfhg'],
        #     'area':['ewrdfhfg','sdgf','re5w4e','sdfg'],
        #     'state':['dfgh','hfgdf','sdfg','sdfg'],
        #     'zipcode':['1232434','523443','345234','456776'],
        #     'meetinglink':['2345sdfgfgdfg','sdfyhtt324354','dxfdghgdfs345','sfdgfghg345t'],
        #     'section_s1201339205248106497_standard_f1003_type_text':['sdfgf','qwret','gfds','dsvg'],
        #     'section_s1201339205248106497_standard_f1004_type_text':['345tgwe','frewter','trg4534r','vfds'],
        #     'section_s1201339205248106497_standard_f1005_type_number':['234','435','6543','345'],
        #     'section_s1201339205248106497_standard_f1006_type_number':['1','2','3','4'],
        #     'section_s1201339205248106497_standard_f1008_type_text':['wertrg','frgterf','frerwsd','645terf'],
        #     'section_s1201339205248106497_custom_f7_type_dropdown':['USA','USA','USA','USA'],
        #     'section_s1201339205248106497_custom_f92_type_text':['A','O','B','AB'],
        #     }

        for i in range(len(data_dict['event_title'])):

            await page.goto("https://gotest.gridlex.com/a/716/ep/1004/en/15/events/new/")
            await page.wait_for_load_state('networkidle')
            await page.select_option('#event_template_id', data_dict['event_template'][i])
            await page.wait_for_load_state('networkidle')
            await page.fill('input[id="event_title"]', data_dict['event_title'][i])
            await page.fill('textarea[id="event_description"]' ,data_dict['event_description'][i])
            await page.select_option('#event_format', data_dict['event_format'][i])
            await page.select_option('#event_type', data_dict['event_type'][i])
            await page.select_option('#event_category', data_dict['event_category'][i])
            await page.select_option('#event_sub_category', data_dict['event_sub_category'][i])
            await page.select_option('#event_timezone', data_dict['event_timezone'][i])
            await page.type('input[id="event_start_date"]', data_dict['event_start_date'][i])
            await page.type('input[id="event_start_time"]', data_dict['event_start_time'][i])
            await page.type('input[id="event_end_date"]', data_dict['event_end_date'][i])
            await page.type('input[id="event_end_time"]', data_dict['event_end_time'][i])
            await page.select_option('#registration_status', data_dict['registration_status'][i])
            await page.type('input[id="registration_start_date"]', data_dict['registration_start_date'][i])
            await page.type('input[id="registration_start_time"]', data_dict['registration_start_time'][i])
            await page.type('input[id="registration_end_date"]', data_dict['registration_end_date'][i])
            await page.type('input[id="registration_end_time"]', data_dict['registration_end_time'][i])
            await page.fill('input[id="registration_capacity"]', data_dict['registration_capacity'][i])
            await page.fill('input[id="address_line1"]', data_dict['address_line1'][i])
            await page.fill('input[id="address_line2"]', data_dict['address_line2'][i])
            await page.fill('input[id="street"]', data_dict['street'][i])
            await page.fill('input[id="area"]', data_dict['area'][i])
            await page.fill('input[id="state"]',data_dict['state'][i])
            await page.fill('input[id="zipcode"]', data_dict['zipcode'][i])
            await page.fill('input[id="meetinglink"]', data_dict['meetinglink'][i])

            await page.fill('input[id="section_s1201339205248106497_standard_f1003_type_text"]', data_dict['section_s1201339205248106497_standard_f1003_type_text'][i])
            await page.fill('input[id="section_s1201339205248106497_standard_f1004_type_text"]', data_dict['section_s1201339205248106497_standard_f1004_type_text'][i])
            await page.fill('input[id="section_s1201339205248106497_standard_f1005_type_number"]', data_dict['section_s1201339205248106497_standard_f1005_type_number'][i])
            await page.fill('input[id="section_s1201339205248106497_standard_f1006_type_number"]', data_dict['section_s1201339205248106497_standard_f1006_type_number'][i])
            await page.fill('input[id="section_s1201339205248106497_standard_f1008_type_text"]', data_dict['section_s1201339205248106497_standard_f1008_type_text'][i])

            await page.select_option('#section_s1201339205248106497_custom_f7_type_dropdown', data_dict['section_s1201339205248106497_custom_f7_type_dropdown'][i])
            await page.fill('input[id="section_s1201339205248106497_custom_f92_type_text"]', data_dict['section_s1201339205248106497_custom_f92_type_text'][i])

            await page.click('text=Next')
            await page.wait_for_url("contact/upload/")
            await page.wait_for_load_state('networkidle')


        await browser.close()

asyncio.run(main())