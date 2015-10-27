import sys
from workflow import Workflow, ICON_WEB, web

wf = Workflow()

def main(_):
  url = 'http://api.cdnjs.com/libraries?'
  if len(wf.args):
    query = wf.args[0]
  else:
    query = None
  params = dict(search=query, fields='version,description')
  r = web.get(url, params)

  r.raise_for_status()
  results = r.json()['results']

  for result in results:
    wf.add_item(title=result['name'],
      subtitle=result['latest'],
      valid=True,
      icon='./icons/cdnjs.png',
      arg=result['latest'])

  wf.send_feedback()
  return 0

if __name__ == "__main__":
  wf.run(main)
