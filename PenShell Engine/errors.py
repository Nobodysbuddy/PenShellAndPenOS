class PenShellAppError():
    def __init__(self, content, app_name):
        self.content = content
        self.app_name = app_name
        
    def throw(self):
        print('At run of', self.app_name, '-> Fatal Error:')
        print("PenShellAppError:", self.content, "in app", self.app_name)