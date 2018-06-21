from testrail import *
import pprint

client = APIClient('https://xxxxxxxxx.testrail.com/')
client.user = 'xxxxxxx'
client.password = 'xxxxxx'
 
result = client.send_post(
	'add_run/1',
	{ 'suite_id': 795, 'name': 'openebs-test-run2' }
)
run_id = result['id']
arg = 'add_results_for_cases/' + str(run_id)
update = client.send_post(
    arg,
    {
	"results": [
		{
			"case_id": 166292,
            "status_id": 5,
			"comment": "This test failed(api testing)",
			"defects": "TR-7"
        },
        {
			"case_id": 166291,
            "status_id": 1,
			"comment": "This test passed(api testing)",
        }
    ]
    }
    )
pprint.pprint(update)
