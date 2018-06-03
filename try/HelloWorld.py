#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import symphony

# to enable loggers... try something like this
logging.getLogger("symphony").setLevel(logging.DEBUG)
# logging.basicConfig(filename='bot.log', level=logging.DEBUG, format='%(asctime)s %(message)s')


def main():
    ''' main program loop '''
    conn = symphony.Config('example-bot.cfg')
    # connect to pod
    agent, pod, symphony_sid = conn.connect()
    agent.test_echo('test')
    # main loop
    msgFormat = 'MESSAGEML'
    message = '<messageML> hello world. </messageML>'
    # send message
    agent.send_message(symphony_sid, msgFormat, message)


if __name__ == "__main__":
    main()
