import datetime as dt
import random
import string
import time

from eth_typing import HexStr
import requests
from web3 import Web3
from web3.eth import Eth
from web3.types import TxReceipt

from logger import logger


def random_string(min_len: int, max_len: int):
    return ''.join(random.choices(string.ascii_lowercase, k=random.randint(min_len, max_len)))


def wait_for_transaction_receipt(
    web3: Eth,
    txn_hash: HexStr,
    timeout: int = 300
) -> TxReceipt:
    try:
        receipt = web3.wait_for_transaction_receipt(
            transaction_hash=txn_hash,
            timeout=timeout
        )
    except Exception as e:
        answer = input(f'Failed to get transaction receipt. Press Enter when transaction will be processed')
        try:
            receipt = web3.wait_for_transaction_receipt(
                transaction_hash=txn_hash,
                timeout=5
            )
        except Exception as e:
            logger.error(f'Failed to get transaction receipt: {e}')
            return None

    return receipt


def load_accounts() -> list[str]:
    with open('accounts.txt') as file:
        return [line.strip() for line in file.readlines()]


def sleep(sleep_time: float):
    logger.info(f'Sleeping for {round(sleep_time, 2)} seconds. If you want to skip this, press Ctrl+C')
    try:
        time.sleep(sleep_time)
    except KeyboardInterrupt:
        logger.info('Skipping sleep')


def random_sleep(min_sleep_time: float, max_sleep_time: float):
    sleep_time = round(random.uniform(min_sleep_time, max_sleep_time), 2)
    sleep(sleep_time)


def suggest_gas_fees(
    chain_id: int
):
    last_update = getattr(suggest_gas_fees, 'last_update', dt.datetime.fromtimestamp(0))
    last_chain_id = getattr(suggest_gas_fees, 'chain_id', None)
    if dt.datetime.now() - last_update > dt.timedelta(seconds=10) or last_chain_id != chain_id:
        try:
            response = requests.get(
                url=f'https://gas-api.metaswap.codefi.network/networks/{chain_id}/suggestedGasFees'
            )
        except Exception:
            logger.error(f'[Gas] Failed to get gas price for chain with ID {chain_id}')
            return None
        else:
            if response.status_code != 200:
                logger.error(f'[Gas] Failed to get gas price for chain with ID {chain_id}: {response.text}')
                return None
            gas_json = response.json()
            medium_gas = gas_json['medium']
            gas_price = {
                'maxFeePerGas': Web3.to_wei(medium_gas['suggestedMaxFeePerGas'], 'gwei'),
                'maxPriorityFeePerGas': Web3.to_wei(medium_gas['suggestedMaxPriorityFeePerGas'], 'gwei')
            }
            suggest_gas_fees.gas_price = gas_price
            suggest_gas_fees.last_update = dt.datetime.now()
            suggest_gas_fees.chain_id = chain_id
            return gas_price
    else:
        return getattr(suggest_gas_fees, 'gas_price', None)
