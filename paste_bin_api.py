
import requests as req
import sys

def post_new_paste(title, body_text, expiration='N', listed=True):
    """
    Uses PasteBin APi to create a new PasteBin past

    :param title: Paste title
    :param body_text: Paste body text
    :param expiration: Expiration date of paste (N = never, 10M = Minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
    :param listed: Whether paste is publically listed (True) or not (False)
    :returns: URL of new paste, if successful. Otherwise None.
    """
    # Change listed to work with API
    if listed:
        listed = '0'
    else:
        listed = '2'
    # Post URL
    url = 'https://pastebin.com/api/api_post.php'
    # Post request parameters
    post_params = {
            'api_dev_key': '',
            'api_option': 'paste',
            'api_paste_name': f'{title}',
            'api_paste_code': f'{body_text}',
            'api_paste_expiry_date': f'{listed}',
            }
    # Print process information to user
    print('Posting new paste to PasteBin...', end='')
    # Make the post request
    post_url = req.post(url, data=post_params)
    # Check that it was succesful and if it was return the post URL
    if post_url:
        print('Success')
        return post_url.text
    else:
        print('Failure')
        print(f'Status code: {post_url.status_code} ({post_url.reason})')
        print(post_url.text)
        sys.exit()


