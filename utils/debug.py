def disableFaulthandler():
    try:
        import faulthandler
        # necessary to disable first or else new threads may not be handled.
        faulthandler.disable()
        return True
    except ImportError:
        return False
