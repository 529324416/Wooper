from Prate.prate import Prate, PrateWindowAppearanceConfigure

__default_prate = None
__prate_configures = {}

def __ensure_default_configure():
    '''Ensure that the default configure is set up.'''

    global __default_prate
    if __default_prate is None:
        __default_prate = Prate(PrateWindowAppearanceConfigure.white())

def show_messagebox(message, title = None, configure:str = None):
    '''show messagebox with title and message'''

    if configure is None or not isinstance(configure, str):
        '''Use default configure if no configure is provided.'''
        __ensure_default_configure()
        __default_prate.ring(title=title, content=message)
        return
    
    if configure in __prate_configures:
        '''Use the loaded configure to show the messagebox.'''
        __prate_configures[configure].ring(title=title, content=message)

    else:
        _new_prate = Prate.create_prate(configure, as_sub_module=True, debug=False)
        if _new_prate != None: 
            __prate_configures[configure] = _new_prate
            __prate_configures[configure].ring(title=title, content=message)
        else:
            __ensure_default_configure()
            __default_prate.ring(title=title, content=message)
            print(f"Warning: The configure '{configure}' does not exist. Using default configure instead.")