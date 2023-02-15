

def post_new_paste(title, body_text, expiration='N', listed=True):
    """
    Uses PasteBin APi to create a new PasteBin past

    :param title: Paste title
    :param body_text: Paste body text
    :param expiration: Expiration date of paste (N = never, 10M = Minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
    :param listed: Whether paste is publically listed (True) or not (False)
    :returns: URL of new paste, if successful. Otherwise None.
    """


    # If the paste was succesful return the url of the new paste
    if new_paste_url:
        return new_paste_url
    return None




