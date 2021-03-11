import requests
proxy = {"https":"http://35.244.23.205:3128"}
vaccineDashboardNation = requests.request("get", "https://api.cowin.gov.in/api/v1/reports/getPublicReports?state_id=&district_id=&date=2021-03-01", proxies=proxy).json
print(vaccineDashboardNation)
