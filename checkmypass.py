import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char

    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(
            f'Error Raised: {response.status_code}, check the API and try again')
    return response


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':')for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pawned_api_check(password):
    hash_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = hash_password[:5], hash_password[5:]
    res = request_api_data(first5_char)
    return get_password_leak_count(res, tail)


def main(args):
    for password in args:
        count = pawned_api_check(password)
        if count:
            print(f'{password} was found {
                count} times ... you should change your password')
        else:
            print(f'{password} was NOT found. Carry on!')


if __name__ == '__main__':

    sys.exit(main(sys.argv[1:]))
