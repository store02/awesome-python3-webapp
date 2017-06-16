#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio, logging
import aiomysql

@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global.__pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
    )