import sys
from workflow import Workflow, ICON_WEB, web


def main(wf):
    url = 'http://api.cdnjs.com/libraries?'
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None
    params = dict(search=query)
    r = web.get(url, params)

    r.raise_for_status()
    results = r.json()['results']

    for result in results:
        wf.add_item(title=result['name'],
            subtitle=result['latest'],
            valid=True,
            icon='./cdnjs.jpeg',
            arg=result['latest'])

    wf.send_feedback()

if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
