'''
dependencies for this project
'''

def populate(d):
    d.requirements3=[
        'lxml',
        'requests',
        'browser-cookie3',
    ]

def getdeps():
    return [
        __file__, # myself
    ]