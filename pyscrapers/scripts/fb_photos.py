import requests
from lxml import etree
import logging
import argparse
import browser_cookie3
import pyscrapers.utils


def main():
    logger = logging.getLogger(__name__)
    # command line parsing
    parser = argparse.ArgumentParser(
            description='''download photos from facebook'''
    )
    parser.add_argument(
            '-i',
            '--id', 
            help='''id of the user to download the albums of
            For instance if you see a url like this:
                https://www.facebook.com/profile.php?id=[user_id]&fref=ts
            then the id for this script will be:
                [user_id]
            If the url is this way:
                https://www.facebook.com/[user_id]
            then the id for this script will be:
                [user_id]
            '''
    )
    args = parser.parse_args()
    if args.id is None:
        parser.error('-i/--id must be given')

    # load cookies from browser
    cookies = browser_cookie3.firefox()

    # start a session
    s = requests.Session()
    s.cookies = cookies

    url = 'https://www.facebook.com/{id}/photos'.format(id=args.id)
    logger.debug('url is [%s]', url)
    r = s.get(url)
    root = pyscrapers.utils.get_real_content(r)
    # print(etree.tostring(root, pretty_print=True))
    # sys.exit(1)

    urls = []
    e_a = root.xpath('//img')
    for x in e_a:
        print(etree.tostring(x, pretty_print=True))

    pyscrapers.utils.download_urls(urls)

if __name__ == '__main__':
    main()
