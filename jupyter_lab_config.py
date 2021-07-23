# Configuration file for jupyter-notebook.

c.Application.log_level = 'INFO'
c.NotebookApp.open_browser = False
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_remote_access = True
c.ServerApp.allow_root = True
c.ServerApp.disable_check_xsrf = True
c.ServerApp.ip = '*'
c.ServerApp.port = 8888
c.ServerApp.token = ''
c.ServerApp.tornado_settings = {
    'headers': {
         'Content-Security-Policy': "frame-ancestors 'self' http://localhost:* https://localhost:* ;"
    },
    'cookie_options': {
        'SameSite': 'None',
        'Secure': True
    }
}
