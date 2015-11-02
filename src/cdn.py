import sys
from workflow import Workflow, ICON_WEB, web

UPDATE_SETTINGS = {'github_slug' : 'azai91/alfred-cdn-workflow'}
HELP_URL = 'https://github.com/azai91/alfred-cdn-workflow/issues'

wf = Workflow(update_settings=UPDATE_SETTINGS, help_url=HELP_URL)

URL = 'http://api.cdnjs.com/libraries?'


def main(_):

  if wf.update_available:
    wf.add_item(
      'An update is available!',
      autocomplete='workflow:update',
      valid=False)

  if len(wf.args):
    query = wf.args[0]
  else:
    query = None
  params = dict(search=query, fields='version,description')
  r = web.get(URL, params)

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
