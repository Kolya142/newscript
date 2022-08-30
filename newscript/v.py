class newscript_error(Exception):
    def __init__(self, f, w, *args):
        self.f = f
        self.w = w
    def __str__(self):
        s = "new_script_error:\n"
        s += f'error: "{self.w}: {self.f}"'
        return s