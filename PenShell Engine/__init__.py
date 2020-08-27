from errors import PenShellAppError

def error(content, type, app_name, *args, **kwargs):
    if type == "PenShellAppError" or "PSAE":
        err = PenShellAppError(content, app_name)
        err.throw()
        
error('TEST', 'PenShellAppError', 'PenShell')