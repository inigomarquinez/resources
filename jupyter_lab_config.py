# Configuration file for jupyter-notebook.

c.Application.log_level = 'INFO'
c.NotebookApp.allow_origin = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.allow_root = True
c.NotebookApp.disable_check_xsrf = True
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.token = ''
c.NotebookApp.tornado_settings = {
    'headers': {
         'Content-Security-Policy': 'frame-ancestors self http://localhost:3000',
    },
    'cookie_options': {
        'SameSite': 'None',
        'Secure': True
    }
}