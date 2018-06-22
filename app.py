from testrail import *
from issue import *
import pprint

client = APIClient('')
client.user = ''
client.password = 'openebs'
 
result = client.send_post(
	'add_run/1',
	{ 'suite_id': 795, 'name': 'openebs-test-run2' }
)
run_id = result['id']
arg = 'add_results_for_cases/' + str(run_id)
playbookResult = {
"results":[
  {
    "case_id": 166292,
    "status_id": 1,
    "comment": "This test failed(api testing)",
    "defects": "TR-7"
  },
  {
    "case_id": 166291,
    "status_id": 1,
    "comment": "This test passed(api testing)"
  }
]
}
update = client.send_post(arg, playbookResult)
pprint.pprint(update)
length = len(playbookResult['results'])
x = playbookResult['results'][0]['comment']
# print(length)
for i in range(0, length):
    if playbookResult['results'][i]['status_id'] == 5:
        print(playbookResult['results'][i]['defects'])
        make_github_issue(playbookResult['results'][i]['defects'],playbookResult['results'][i]['comment'] , ['e2e'])
