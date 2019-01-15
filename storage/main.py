import argparse
import asyncio


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='verbose output',
                        action='store_true', default=False)
    parser.add_argument('-H', '--host', help='hostname or IP',
                        default='127.0.0.1')
    parser.add_argument('-P', '--port', type=int, help='port',
                        default=8666)
    params = parser.parse_args()

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if params.verbose:
        print('Server started on {}:{}'.format(params.host, params.port))

    # todo run application
    application = None
    raise NotImplementedError


if __name__ == '__main__':
    main()
