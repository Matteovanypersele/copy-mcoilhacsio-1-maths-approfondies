from pyodide_mkdocs_theme.pyodide_macros import PyodideMacrosPlugin, TestsToken

def define_env(env:PyodideMacrosPlugin):

    custom = {
                "tests": TestsToken("\n# Tests"),
                }
                