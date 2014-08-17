import sublime, sublime_plugin
import urllib.request, json

def load_last_version(gem):
  url = "https://rubygems.org/api/v1/versions/%s.json" % gem
  response = urllib.request.urlopen(url)
  content = response.read()
  data = json.loads(content.decode('utf8'))
  return "gem '%s', '~> %s'" % (gem, data[0]['number'])

def run_on_selections(view, edit, func, no_lower=False):
  for s in view.sel():
    region = s if s else view.word(s)
    text = view.substr(region)
    # load_last_version(text)
    # text = strip_wrapping_underscores(text)
    view.replace(edit, region, func(text))

class ExampleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, 0, "Hello, World!")

class LoadGem(sublime_plugin.TextCommand):
  def run(self, edit, attribute=None, **kw):
    print("here")
    run_on_selections(self.view, edit, load_last_version)
